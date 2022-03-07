import * as pulumi from "@pulumi/pulumi";
import * as hcp from "@grapl/pulumi-hcp";
import * as aws from "@pulumi/aws";

const aws_tags = {
    "pulumi:project": pulumi.getProject(),
    "pulumi:stack": pulumi.getStack()
}

const hvn = new hcp.Hvn(
    `${ pulumi.getProject() }-hvn`,
    {
        hvnId: `${ pulumi.getProject() }-hvn`,
        cloudProvider: "aws",
        region: "us-east-1",
        cidrBlock: "172.25.16.0/20"
    }
);


// Create an AWS VPC to peer with the HVN
const peer_vpc = new aws.ec2.Vpc(
    `${pulumi.getProject()}-vpc`,
    {
        cidrBlock: "172.31.0.0/16",
        tags: {
            "Name": `${pulumi.getProject()}-vpc`,
            ...aws_tags,
        },
    }
);

// Initiate the peering connection from HCP
const peering_connection = new hcp.AwsNetworkPeering(
    `${pulumi.getProject()}-peering`,
    {
        hvnId: hvn.hvnId,
        peeringId: `${pulumi.getProject()}-peering`,
        peerVpcId: peer_vpc.id,
        peerAccountId: peer_vpc.ownerId,
        peerVpcRegion: "us-east-1",
    },
    {
        customTimeouts: { create: "10m" }
    }
);

// Accept the peering connection in AWS
const connection_accepter = new aws.ec2.VpcPeeringConnectionAccepter(
    `${pulumi.getProject()}-connection-accepter`,
    {
        vpcPeeringConnectionId: peering_connection.providerPeeringId,
        autoAccept: true,
        tags: aws_tags,
    }
);

// Create a route in the HVN to resources in the VPC
new hcp.HvnRoute(
    `${pulumi.getProject()}-route-to-vpc`,
    {
        hvnLink: hvn.selfLink,
        hvnRouteId: `${pulumi.getProject()}-route-to-vpc`,
        destinationCidr: peer_vpc.cidrBlock,
        targetLink: peering_connection.selfLink
    }
);

// Create a route in one of the VPCs routing tables (here, we'll
// just use the main route table, but any routing table is fair
// game) to the HVN.
new aws.ec2.Route(
    `${pulumi.getProject()}-route-to-hvn`,
    {
        routeTableId: peer_vpc.mainRouteTableId,
        destinationCidrBlock: hvn.cidrBlock,
        // Depend on the accepter, for proper sequencing
        vpcPeeringConnectionId: connection_accepter.vpcPeeringConnectionId,
    }
);
