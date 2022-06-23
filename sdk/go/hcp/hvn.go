// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The HVN resource allows you to manage a HashiCorp Virtual Network in HCP.
//
// We recommend the following when selecting the CIDR block of an HVN:
//
// - The CIDR block value must be a private IPv4 CIDR block within the [RFC1918](https://datatracker.ietf.org/doc/html/rfc1918) address space (10.*.*.*, 192.168.*.*, 172.[16-31].*.*).
//
// - The CIDR block value must be the first IP address of the desired CIDR block. The helper `cidrsubnet("172.16.1.1/24", 0, 0)` will specify the first address of the CIDR block in the first argument.
//
// - The CIDR block value must end between /16 and /25.
//
// - If the CIDR block values for your HVN and VPCs overlap, then you will not be able to establish a connection. Ensure that any VPCs you plan to connect do not have overlapping values.
//
// - The default HVN CIDR block value does not overlap with the default CIDR block value for AWS VPCs (172.31.0.0/16). However, if you are planning to use this HVN in production, we recommend adding a custom value instead of using the default.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/grapl-security/pulumi-hcp/sdk/go/hcp"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := hcp.NewHvn(ctx, "example", &hcp.HvnArgs{
// 			CidrBlock:     pulumi.String("172.25.16.0/20"),
// 			CloudProvider: pulumi.String("aws"),
// 			HvnId:         pulumi.String("main-hvn"),
// 			Region:        pulumi.String("us-west-2"),
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
// # The import ID is {hvn_id}
//
// ```sh
//  $ pulumi import hcp:index/hvn:Hvn example main-hvn
// ```
type Hvn struct {
	pulumi.CustomResourceState

	// The CIDR range of the HVN. If this is not provided, the service will provide a default value.
	CidrBlock pulumi.StringOutput `pulumi:"cidrBlock"`
	// The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
	CloudProvider pulumi.StringOutput `pulumi:"cloudProvider"`
	// The time that the HVN was created.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The ID of the HashiCorp Virtual Network (HVN).
	HvnId pulumi.StringOutput `pulumi:"hvnId"`
	// The ID of the HCP organization where the HVN is located.
	OrganizationId pulumi.StringOutput `pulumi:"organizationId"`
	// The ID of the HCP project where the HVN is located.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// The provider account ID where the HVN is located.
	ProviderAccountId pulumi.StringOutput `pulumi:"providerAccountId"`
	// The region where the HVN is located.
	Region pulumi.StringOutput `pulumi:"region"`
	// A unique URL identifying the HVN.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
}

// NewHvn registers a new resource with the given unique name, arguments, and options.
func NewHvn(ctx *pulumi.Context,
	name string, args *HvnArgs, opts ...pulumi.ResourceOption) (*Hvn, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CloudProvider == nil {
		return nil, errors.New("invalid value for required argument 'CloudProvider'")
	}
	if args.HvnId == nil {
		return nil, errors.New("invalid value for required argument 'HvnId'")
	}
	if args.Region == nil {
		return nil, errors.New("invalid value for required argument 'Region'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource Hvn
	err := ctx.RegisterResource("hcp:index/hvn:Hvn", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHvn gets an existing Hvn resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHvn(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HvnState, opts ...pulumi.ResourceOption) (*Hvn, error) {
	var resource Hvn
	err := ctx.ReadResource("hcp:index/hvn:Hvn", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Hvn resources.
type hvnState struct {
	// The CIDR range of the HVN. If this is not provided, the service will provide a default value.
	CidrBlock *string `pulumi:"cidrBlock"`
	// The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
	CloudProvider *string `pulumi:"cloudProvider"`
	// The time that the HVN was created.
	CreatedAt *string `pulumi:"createdAt"`
	// The ID of the HashiCorp Virtual Network (HVN).
	HvnId *string `pulumi:"hvnId"`
	// The ID of the HCP organization where the HVN is located.
	OrganizationId *string `pulumi:"organizationId"`
	// The ID of the HCP project where the HVN is located.
	ProjectId *string `pulumi:"projectId"`
	// The provider account ID where the HVN is located.
	ProviderAccountId *string `pulumi:"providerAccountId"`
	// The region where the HVN is located.
	Region *string `pulumi:"region"`
	// A unique URL identifying the HVN.
	SelfLink *string `pulumi:"selfLink"`
}

type HvnState struct {
	// The CIDR range of the HVN. If this is not provided, the service will provide a default value.
	CidrBlock pulumi.StringPtrInput
	// The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
	CloudProvider pulumi.StringPtrInput
	// The time that the HVN was created.
	CreatedAt pulumi.StringPtrInput
	// The ID of the HashiCorp Virtual Network (HVN).
	HvnId pulumi.StringPtrInput
	// The ID of the HCP organization where the HVN is located.
	OrganizationId pulumi.StringPtrInput
	// The ID of the HCP project where the HVN is located.
	ProjectId pulumi.StringPtrInput
	// The provider account ID where the HVN is located.
	ProviderAccountId pulumi.StringPtrInput
	// The region where the HVN is located.
	Region pulumi.StringPtrInput
	// A unique URL identifying the HVN.
	SelfLink pulumi.StringPtrInput
}

func (HvnState) ElementType() reflect.Type {
	return reflect.TypeOf((*hvnState)(nil)).Elem()
}

type hvnArgs struct {
	// The CIDR range of the HVN. If this is not provided, the service will provide a default value.
	CidrBlock *string `pulumi:"cidrBlock"`
	// The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
	CloudProvider string `pulumi:"cloudProvider"`
	// The ID of the HashiCorp Virtual Network (HVN).
	HvnId string `pulumi:"hvnId"`
	// The region where the HVN is located.
	Region string `pulumi:"region"`
}

// The set of arguments for constructing a Hvn resource.
type HvnArgs struct {
	// The CIDR range of the HVN. If this is not provided, the service will provide a default value.
	CidrBlock pulumi.StringPtrInput
	// The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
	CloudProvider pulumi.StringInput
	// The ID of the HashiCorp Virtual Network (HVN).
	HvnId pulumi.StringInput
	// The region where the HVN is located.
	Region pulumi.StringInput
}

func (HvnArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hvnArgs)(nil)).Elem()
}

type HvnInput interface {
	pulumi.Input

	ToHvnOutput() HvnOutput
	ToHvnOutputWithContext(ctx context.Context) HvnOutput
}

func (*Hvn) ElementType() reflect.Type {
	return reflect.TypeOf((**Hvn)(nil)).Elem()
}

func (i *Hvn) ToHvnOutput() HvnOutput {
	return i.ToHvnOutputWithContext(context.Background())
}

func (i *Hvn) ToHvnOutputWithContext(ctx context.Context) HvnOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HvnOutput)
}

// HvnArrayInput is an input type that accepts HvnArray and HvnArrayOutput values.
// You can construct a concrete instance of `HvnArrayInput` via:
//
//          HvnArray{ HvnArgs{...} }
type HvnArrayInput interface {
	pulumi.Input

	ToHvnArrayOutput() HvnArrayOutput
	ToHvnArrayOutputWithContext(context.Context) HvnArrayOutput
}

type HvnArray []HvnInput

func (HvnArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Hvn)(nil)).Elem()
}

func (i HvnArray) ToHvnArrayOutput() HvnArrayOutput {
	return i.ToHvnArrayOutputWithContext(context.Background())
}

func (i HvnArray) ToHvnArrayOutputWithContext(ctx context.Context) HvnArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HvnArrayOutput)
}

// HvnMapInput is an input type that accepts HvnMap and HvnMapOutput values.
// You can construct a concrete instance of `HvnMapInput` via:
//
//          HvnMap{ "key": HvnArgs{...} }
type HvnMapInput interface {
	pulumi.Input

	ToHvnMapOutput() HvnMapOutput
	ToHvnMapOutputWithContext(context.Context) HvnMapOutput
}

type HvnMap map[string]HvnInput

func (HvnMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Hvn)(nil)).Elem()
}

func (i HvnMap) ToHvnMapOutput() HvnMapOutput {
	return i.ToHvnMapOutputWithContext(context.Background())
}

func (i HvnMap) ToHvnMapOutputWithContext(ctx context.Context) HvnMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HvnMapOutput)
}

type HvnOutput struct{ *pulumi.OutputState }

func (HvnOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Hvn)(nil)).Elem()
}

func (o HvnOutput) ToHvnOutput() HvnOutput {
	return o
}

func (o HvnOutput) ToHvnOutputWithContext(ctx context.Context) HvnOutput {
	return o
}

// The CIDR range of the HVN. If this is not provided, the service will provide a default value.
func (o HvnOutput) CidrBlock() pulumi.StringOutput {
	return o.ApplyT(func(v *Hvn) pulumi.StringOutput { return v.CidrBlock }).(pulumi.StringOutput)
}

// The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
func (o HvnOutput) CloudProvider() pulumi.StringOutput {
	return o.ApplyT(func(v *Hvn) pulumi.StringOutput { return v.CloudProvider }).(pulumi.StringOutput)
}

// The time that the HVN was created.
func (o HvnOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Hvn) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The ID of the HashiCorp Virtual Network (HVN).
func (o HvnOutput) HvnId() pulumi.StringOutput {
	return o.ApplyT(func(v *Hvn) pulumi.StringOutput { return v.HvnId }).(pulumi.StringOutput)
}

// The ID of the HCP organization where the HVN is located.
func (o HvnOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v *Hvn) pulumi.StringOutput { return v.OrganizationId }).(pulumi.StringOutput)
}

// The ID of the HCP project where the HVN is located.
func (o HvnOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *Hvn) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

// The provider account ID where the HVN is located.
func (o HvnOutput) ProviderAccountId() pulumi.StringOutput {
	return o.ApplyT(func(v *Hvn) pulumi.StringOutput { return v.ProviderAccountId }).(pulumi.StringOutput)
}

// The region where the HVN is located.
func (o HvnOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *Hvn) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// A unique URL identifying the HVN.
func (o HvnOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v *Hvn) pulumi.StringOutput { return v.SelfLink }).(pulumi.StringOutput)
}

type HvnArrayOutput struct{ *pulumi.OutputState }

func (HvnArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Hvn)(nil)).Elem()
}

func (o HvnArrayOutput) ToHvnArrayOutput() HvnArrayOutput {
	return o
}

func (o HvnArrayOutput) ToHvnArrayOutputWithContext(ctx context.Context) HvnArrayOutput {
	return o
}

func (o HvnArrayOutput) Index(i pulumi.IntInput) HvnOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Hvn {
		return vs[0].([]*Hvn)[vs[1].(int)]
	}).(HvnOutput)
}

type HvnMapOutput struct{ *pulumi.OutputState }

func (HvnMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Hvn)(nil)).Elem()
}

func (o HvnMapOutput) ToHvnMapOutput() HvnMapOutput {
	return o
}

func (o HvnMapOutput) ToHvnMapOutputWithContext(ctx context.Context) HvnMapOutput {
	return o
}

func (o HvnMapOutput) MapIndex(k pulumi.StringInput) HvnOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Hvn {
		return vs[0].(map[string]*Hvn)[vs[1].(string)]
	}).(HvnOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*HvnInput)(nil)).Elem(), &Hvn{})
	pulumi.RegisterInputType(reflect.TypeOf((*HvnArrayInput)(nil)).Elem(), HvnArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*HvnMapInput)(nil)).Elem(), HvnMap{})
	pulumi.RegisterOutputType(HvnOutput{})
	pulumi.RegisterOutputType(HvnArrayOutput{})
	pulumi.RegisterOutputType(HvnMapOutput{})
}
