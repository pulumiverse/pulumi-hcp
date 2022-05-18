// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/grapl-security/pulumi-hcp/sdk/go/hcp"
// 	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/ec2"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		main, err := hcp.NewHvn(ctx, "main", &hcp.HvnArgs{
// 			HvnId:         pulumi.String("main-hvn"),
// 			CloudProvider: pulumi.String("aws"),
// 			Region:        pulumi.String("us-west-2"),
// 			CidrBlock:     pulumi.String("172.25.16.0/20"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		peerVpc, err := ec2.NewVpc(ctx, "peerVpc", &ec2.VpcArgs{
// 			CidrBlock: pulumi.String("192.168.0.0/20"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		example, err := hcp.NewAwsNetworkPeering(ctx, "example", &hcp.AwsNetworkPeeringArgs{
// 			PeeringId:     pulumi.String("peer-example"),
// 			HvnId:         main.HvnId,
// 			PeerVpcId:     peerVpc.ID(),
// 			PeerAccountId: peerVpc.OwnerId,
// 			PeerVpcRegion: pulumi.String("us-west-2"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ec2.NewVpcPeeringConnectionAccepter(ctx, "peerVpcPeeringConnectionAccepter", &ec2.VpcPeeringConnectionAccepterArgs{
// 			VpcPeeringConnectionId: example.ProviderPeeringId,
// 			AutoAccept:             pulumi.Bool(true),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hcp.NewHvnRoute(ctx, "example-peering-route", &hcp.HvnRouteArgs{
// 			HvnLink:         main.SelfLink,
// 			HvnRouteId:      pulumi.String("peering-route"),
// 			DestinationCidr: peerVpc.CidrBlock,
// 			TargetLink:      example.SelfLink,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// # The import ID is {hvn_id}:{hvn_route_id}
//
// ```sh
//  $ pulumi import hcp:index/hvnRoute:HvnRoute example main-hvn:example-hvn-route
// ```
type HvnRoute struct {
	pulumi.CustomResourceState

	// The time that the HVN route was created.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The destination CIDR of the HVN route.
	DestinationCidr pulumi.StringOutput `pulumi:"destinationCidr"`
	// The `self_link` of the HashiCorp Virtual Network (HVN).
	HvnLink pulumi.StringOutput `pulumi:"hvnLink"`
	// The ID of the HVN route.
	HvnRouteId pulumi.StringOutput `pulumi:"hvnRouteId"`
	// A unique URL identifying the HVN route.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// The state of the HVN route.
	State pulumi.StringOutput `pulumi:"state"`
	// A unique URL identifying the target of the HVN route. Examples of the target:
	// [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
	TargetLink pulumi.StringOutput `pulumi:"targetLink"`
}

// NewHvnRoute registers a new resource with the given unique name, arguments, and options.
func NewHvnRoute(ctx *pulumi.Context,
	name string, args *HvnRouteArgs, opts ...pulumi.ResourceOption) (*HvnRoute, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DestinationCidr == nil {
		return nil, errors.New("invalid value for required argument 'DestinationCidr'")
	}
	if args.HvnLink == nil {
		return nil, errors.New("invalid value for required argument 'HvnLink'")
	}
	if args.HvnRouteId == nil {
		return nil, errors.New("invalid value for required argument 'HvnRouteId'")
	}
	if args.TargetLink == nil {
		return nil, errors.New("invalid value for required argument 'TargetLink'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource HvnRoute
	err := ctx.RegisterResource("hcp:index/hvnRoute:HvnRoute", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHvnRoute gets an existing HvnRoute resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHvnRoute(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HvnRouteState, opts ...pulumi.ResourceOption) (*HvnRoute, error) {
	var resource HvnRoute
	err := ctx.ReadResource("hcp:index/hvnRoute:HvnRoute", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HvnRoute resources.
type hvnRouteState struct {
	// The time that the HVN route was created.
	CreatedAt *string `pulumi:"createdAt"`
	// The destination CIDR of the HVN route.
	DestinationCidr *string `pulumi:"destinationCidr"`
	// The `self_link` of the HashiCorp Virtual Network (HVN).
	HvnLink *string `pulumi:"hvnLink"`
	// The ID of the HVN route.
	HvnRouteId *string `pulumi:"hvnRouteId"`
	// A unique URL identifying the HVN route.
	SelfLink *string `pulumi:"selfLink"`
	// The state of the HVN route.
	State *string `pulumi:"state"`
	// A unique URL identifying the target of the HVN route. Examples of the target:
	// [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
	TargetLink *string `pulumi:"targetLink"`
}

type HvnRouteState struct {
	// The time that the HVN route was created.
	CreatedAt pulumi.StringPtrInput
	// The destination CIDR of the HVN route.
	DestinationCidr pulumi.StringPtrInput
	// The `self_link` of the HashiCorp Virtual Network (HVN).
	HvnLink pulumi.StringPtrInput
	// The ID of the HVN route.
	HvnRouteId pulumi.StringPtrInput
	// A unique URL identifying the HVN route.
	SelfLink pulumi.StringPtrInput
	// The state of the HVN route.
	State pulumi.StringPtrInput
	// A unique URL identifying the target of the HVN route. Examples of the target:
	// [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
	TargetLink pulumi.StringPtrInput
}

func (HvnRouteState) ElementType() reflect.Type {
	return reflect.TypeOf((*hvnRouteState)(nil)).Elem()
}

type hvnRouteArgs struct {
	// The destination CIDR of the HVN route.
	DestinationCidr string `pulumi:"destinationCidr"`
	// The `self_link` of the HashiCorp Virtual Network (HVN).
	HvnLink string `pulumi:"hvnLink"`
	// The ID of the HVN route.
	HvnRouteId string `pulumi:"hvnRouteId"`
	// A unique URL identifying the target of the HVN route. Examples of the target:
	// [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
	TargetLink string `pulumi:"targetLink"`
}

// The set of arguments for constructing a HvnRoute resource.
type HvnRouteArgs struct {
	// The destination CIDR of the HVN route.
	DestinationCidr pulumi.StringInput
	// The `self_link` of the HashiCorp Virtual Network (HVN).
	HvnLink pulumi.StringInput
	// The ID of the HVN route.
	HvnRouteId pulumi.StringInput
	// A unique URL identifying the target of the HVN route. Examples of the target:
	// [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
	TargetLink pulumi.StringInput
}

func (HvnRouteArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hvnRouteArgs)(nil)).Elem()
}

type HvnRouteInput interface {
	pulumi.Input

	ToHvnRouteOutput() HvnRouteOutput
	ToHvnRouteOutputWithContext(ctx context.Context) HvnRouteOutput
}

func (*HvnRoute) ElementType() reflect.Type {
	return reflect.TypeOf((**HvnRoute)(nil)).Elem()
}

func (i *HvnRoute) ToHvnRouteOutput() HvnRouteOutput {
	return i.ToHvnRouteOutputWithContext(context.Background())
}

func (i *HvnRoute) ToHvnRouteOutputWithContext(ctx context.Context) HvnRouteOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HvnRouteOutput)
}

// HvnRouteArrayInput is an input type that accepts HvnRouteArray and HvnRouteArrayOutput values.
// You can construct a concrete instance of `HvnRouteArrayInput` via:
//
//          HvnRouteArray{ HvnRouteArgs{...} }
type HvnRouteArrayInput interface {
	pulumi.Input

	ToHvnRouteArrayOutput() HvnRouteArrayOutput
	ToHvnRouteArrayOutputWithContext(context.Context) HvnRouteArrayOutput
}

type HvnRouteArray []HvnRouteInput

func (HvnRouteArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*HvnRoute)(nil)).Elem()
}

func (i HvnRouteArray) ToHvnRouteArrayOutput() HvnRouteArrayOutput {
	return i.ToHvnRouteArrayOutputWithContext(context.Background())
}

func (i HvnRouteArray) ToHvnRouteArrayOutputWithContext(ctx context.Context) HvnRouteArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HvnRouteArrayOutput)
}

// HvnRouteMapInput is an input type that accepts HvnRouteMap and HvnRouteMapOutput values.
// You can construct a concrete instance of `HvnRouteMapInput` via:
//
//          HvnRouteMap{ "key": HvnRouteArgs{...} }
type HvnRouteMapInput interface {
	pulumi.Input

	ToHvnRouteMapOutput() HvnRouteMapOutput
	ToHvnRouteMapOutputWithContext(context.Context) HvnRouteMapOutput
}

type HvnRouteMap map[string]HvnRouteInput

func (HvnRouteMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*HvnRoute)(nil)).Elem()
}

func (i HvnRouteMap) ToHvnRouteMapOutput() HvnRouteMapOutput {
	return i.ToHvnRouteMapOutputWithContext(context.Background())
}

func (i HvnRouteMap) ToHvnRouteMapOutputWithContext(ctx context.Context) HvnRouteMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HvnRouteMapOutput)
}

type HvnRouteOutput struct{ *pulumi.OutputState }

func (HvnRouteOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**HvnRoute)(nil)).Elem()
}

func (o HvnRouteOutput) ToHvnRouteOutput() HvnRouteOutput {
	return o
}

func (o HvnRouteOutput) ToHvnRouteOutputWithContext(ctx context.Context) HvnRouteOutput {
	return o
}

// The time that the HVN route was created.
func (o HvnRouteOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *HvnRoute) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The destination CIDR of the HVN route.
func (o HvnRouteOutput) DestinationCidr() pulumi.StringOutput {
	return o.ApplyT(func(v *HvnRoute) pulumi.StringOutput { return v.DestinationCidr }).(pulumi.StringOutput)
}

// The `self_link` of the HashiCorp Virtual Network (HVN).
func (o HvnRouteOutput) HvnLink() pulumi.StringOutput {
	return o.ApplyT(func(v *HvnRoute) pulumi.StringOutput { return v.HvnLink }).(pulumi.StringOutput)
}

// The ID of the HVN route.
func (o HvnRouteOutput) HvnRouteId() pulumi.StringOutput {
	return o.ApplyT(func(v *HvnRoute) pulumi.StringOutput { return v.HvnRouteId }).(pulumi.StringOutput)
}

// A unique URL identifying the HVN route.
func (o HvnRouteOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v *HvnRoute) pulumi.StringOutput { return v.SelfLink }).(pulumi.StringOutput)
}

// The state of the HVN route.
func (o HvnRouteOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *HvnRoute) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// A unique URL identifying the target of the HVN route. Examples of the target:
// [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
func (o HvnRouteOutput) TargetLink() pulumi.StringOutput {
	return o.ApplyT(func(v *HvnRoute) pulumi.StringOutput { return v.TargetLink }).(pulumi.StringOutput)
}

type HvnRouteArrayOutput struct{ *pulumi.OutputState }

func (HvnRouteArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*HvnRoute)(nil)).Elem()
}

func (o HvnRouteArrayOutput) ToHvnRouteArrayOutput() HvnRouteArrayOutput {
	return o
}

func (o HvnRouteArrayOutput) ToHvnRouteArrayOutputWithContext(ctx context.Context) HvnRouteArrayOutput {
	return o
}

func (o HvnRouteArrayOutput) Index(i pulumi.IntInput) HvnRouteOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *HvnRoute {
		return vs[0].([]*HvnRoute)[vs[1].(int)]
	}).(HvnRouteOutput)
}

type HvnRouteMapOutput struct{ *pulumi.OutputState }

func (HvnRouteMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*HvnRoute)(nil)).Elem()
}

func (o HvnRouteMapOutput) ToHvnRouteMapOutput() HvnRouteMapOutput {
	return o
}

func (o HvnRouteMapOutput) ToHvnRouteMapOutputWithContext(ctx context.Context) HvnRouteMapOutput {
	return o
}

func (o HvnRouteMapOutput) MapIndex(k pulumi.StringInput) HvnRouteOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *HvnRoute {
		return vs[0].(map[string]*HvnRoute)[vs[1].(string)]
	}).(HvnRouteOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*HvnRouteInput)(nil)).Elem(), &HvnRoute{})
	pulumi.RegisterInputType(reflect.TypeOf((*HvnRouteArrayInput)(nil)).Elem(), HvnRouteArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*HvnRouteMapInput)(nil)).Elem(), HvnRouteMap{})
	pulumi.RegisterOutputType(HvnRouteOutput{})
	pulumi.RegisterOutputType(HvnRouteArrayOutput{})
	pulumi.RegisterOutputType(HvnRouteMapOutput{})
}
