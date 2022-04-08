import pulumi
import pulumi_hcp as hcp
import pulumi_aws as aws

def main() -> None:

    aws_tags = {
        "pulumi:project": pulumi.get_project(),
        "pulumi:stack": pulumi.get_stack()
    }

    # Create the HVN (Hashicorp Virtual Network)
    hvn = hcp.Hvn(
        f"{pulumi.get_project()}-hvn",
        hvn_id=f"{pulumi.get_project()}-hvn",
        cloud_provider="aws",
        region="us-east-1",
        cidr_block="172.25.16.0/20",
    )

    # Create an AWS VPC to peer with the HVN
    peer_vpc = aws.ec2.Vpc(
        f"{pulumi.get_project()}-vpc",
        cidr_block="172.31.0.0/16",
        tags={
            "Name": f"{pulumi.get_project()}-vpc",
            **aws_tags,
        },
    )

    # Initiate the peering connection from HCP
    peering_connection = hcp.AwsNetworkPeering(
        f"{pulumi.get_project()}-peering",
        hvn_id=hvn.hvn_id,
        peering_id=f"{pulumi.get_project()}-peering",
        peer_vpc_id=peer_vpc.id,
        peer_account_id=peer_vpc.owner_id,
        peer_vpc_region="us-east-1",
        opts=pulumi.ResourceOptions(custom_timeouts=pulumi.CustomTimeouts(create='10m'))
    )

    # Accept the peering connection in AWS
    connection_accepter = aws.ec2.VpcPeeringConnectionAccepter(
        f"{pulumi.get_project()}-connection-accepter",
        vpc_peering_connection_id=peering_connection.provider_peering_id,
        auto_accept=True,
        tags=aws_tags,
    )

    # Create a route in the HVN to resources in the VPC
    hcp.HvnRoute(
        f"{pulumi.get_project()}-route-to-vpc",
        hvn_link=hvn.self_link,
        hvn_route_id=f"{pulumi.get_project()}-route-to-vpc",
        destination_cidr=peer_vpc.cidr_block,
        target_link=peering_connection.self_link
    )

    # Create a route in one of the VPCs routing tables (here, we'll
    # just use the main route table, but any routing table is fair
    # game) to the HVN.
    aws.ec2.Route(
        f"{pulumi.get_project()}-route-to-hvn",
        route_table_id=peer_vpc.main_route_table_id,
        destination_cidr_block=hvn.cidr_block,
        # Depend on the accepter, for proper sequencing
        vpc_peering_connection_id=connection_accepter.vpc_peering_connection_id,
    )

if __name__ == "__main__":
    main()
