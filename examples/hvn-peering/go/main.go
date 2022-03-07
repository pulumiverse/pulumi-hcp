package main

import (
	"fmt"
	hcp "github.com/grapl-security/pulumi-hcp/sdk/go/hcp"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Create the HVN (Hashicorp Virtual Network)
		hvn, err := hcp.NewHvn(ctx, "hvn-peering-go-hvn", &hcp.HvnArgs{
			HvnId:         pulumi.String("hvn-peering-go-hvn"),
			CloudProvider: pulumi.String("aws"),
			Region:        pulumi.String("us-east-1"),
			CidrBlock:     pulumi.String("172.25.16.0/20"),
		})
		if err != nil {
			return fmt.Errorf("error creating HVN: %v", err)
		}

		// Create an AWS VPC to peer with the HVN
		peer_vpc, err := ec2.NewVpc(ctx, "hvn-peering-go-vpc", &ec2.VpcArgs{
			CidrBlock: pulumi.String("172.31.0.0/16"),
			Tags: pulumi.StringMap{
				"Name":           pulumi.String("hvn-peering-go-vpc"),
				"pulumi:project": pulumi.String(ctx.Project()),
				"pulumi:stack":   pulumi.String(ctx.Stack()),
			},
		})
		if err != nil {
			return fmt.Errorf("error creating VPC: %v", err)
		}

		// Initiate the peering connection from HCP
		peering_connection, err := hcp.NewAwsNetworkPeering(ctx, "hvn-peering-go-peering", &hcp.AwsNetworkPeeringArgs{
			HvnId:         hvn.HvnId,
			PeeringId:     pulumi.String("hvn-peering-go-peering"),
			PeerVpcId:     peer_vpc.ID(),
			PeerAccountId: peer_vpc.OwnerId,
			PeerVpcRegion: pulumi.String("us-east-1"),
		},
			pulumi.Timeouts(&pulumi.CustomTimeouts{Create: "10m"}),
		)
		if err != nil {
			return fmt.Errorf("error creating peering connection: %v", err)
		}

		// Accept the peering connection in AWS
		connection_accepter, err := ec2.NewVpcPeeringConnectionAccepter(ctx, "hvn-peering-go-connection-accepter", &ec2.VpcPeeringConnectionAccepterArgs{
			VpcPeeringConnectionId: peering_connection.ProviderPeeringId,
			AutoAccept:             pulumi.Bool(true),
			Tags: pulumi.StringMap{
				"pulumi:project": pulumi.String(ctx.Project()),
				"pulumi:stack":   pulumi.String(ctx.Stack()),
			},
		})
		if err != nil {
			return fmt.Errorf("error creating connection accepter: %v", err)
		}

		// Create a route in the HVN to resources in the VPC
		_, err = hcp.NewHvnRoute(ctx, "hvn-peering-go-route-to-vpc", &hcp.HvnRouteArgs{
			HvnLink:         hvn.SelfLink,
			HvnRouteId:      pulumi.String("hvn-peering-go-route-to-vpc"),
			DestinationCidr: peer_vpc.CidrBlock,
			TargetLink:      peering_connection.SelfLink,
		})
		if err != nil {
			return fmt.Errorf("error creating HVN route: %v", err)
		}

		// Create a route in one of the VPCs routing tables (here, we'll
		// just use the main route table, but any routing table is fair
		// game) to the HVN.
		_, err = ec2.NewRoute(ctx, "hvn-peering-go-route-to-hvn", &ec2.RouteArgs{
			RouteTableId:         peer_vpc.MainRouteTableId,
			DestinationCidrBlock: hvn.CidrBlock,
			// Depend on the accepter, for proper sequencing
			VpcPeeringConnectionId: connection_accepter.VpcPeeringConnectionId,
		})
		if err != nil {
			return fmt.Errorf("error creating VPC route: %v", err)
		}

		return nil
	})
}
