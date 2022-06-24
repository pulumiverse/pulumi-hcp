// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// > **Note:** This data source is currently in public beta.
//
// The Azure peering connection data source provides information about a peering connection between an HVN and a peer Azure VNet.
func LookupAzurePeeringConnection(ctx *pulumi.Context, args *LookupAzurePeeringConnectionArgs, opts ...pulumi.InvokeOption) (*LookupAzurePeeringConnectionResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupAzurePeeringConnectionResult
	err := ctx.Invoke("hcp:index/getAzurePeeringConnection:getAzurePeeringConnection", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAzurePeeringConnection.
type LookupAzurePeeringConnectionArgs struct {
	HvnLink            string `pulumi:"hvnLink"`
	PeeringId          string `pulumi:"peeringId"`
	WaitForActiveState *bool  `pulumi:"waitForActiveState"`
}

// A collection of values returned by getAzurePeeringConnection.
type LookupAzurePeeringConnectionResult struct {
	ApplicationId  string `pulumi:"applicationId"`
	AzurePeeringId string `pulumi:"azurePeeringId"`
	CreatedAt      string `pulumi:"createdAt"`
	ExpiresAt      string `pulumi:"expiresAt"`
	HvnLink        string `pulumi:"hvnLink"`
	// The provider-assigned unique ID for this managed resource.
	Id                    string `pulumi:"id"`
	OrganizationId        string `pulumi:"organizationId"`
	PeerResourceGroupName string `pulumi:"peerResourceGroupName"`
	PeerSubscriptionId    string `pulumi:"peerSubscriptionId"`
	PeerTenantId          string `pulumi:"peerTenantId"`
	PeerVnetName          string `pulumi:"peerVnetName"`
	PeerVnetRegion        string `pulumi:"peerVnetRegion"`
	PeeringId             string `pulumi:"peeringId"`
	ProjectId             string `pulumi:"projectId"`
	SelfLink              string `pulumi:"selfLink"`
	WaitForActiveState    *bool  `pulumi:"waitForActiveState"`
}

func LookupAzurePeeringConnectionOutput(ctx *pulumi.Context, args LookupAzurePeeringConnectionOutputArgs, opts ...pulumi.InvokeOption) LookupAzurePeeringConnectionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAzurePeeringConnectionResult, error) {
			args := v.(LookupAzurePeeringConnectionArgs)
			r, err := LookupAzurePeeringConnection(ctx, &args, opts...)
			var s LookupAzurePeeringConnectionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAzurePeeringConnectionResultOutput)
}

// A collection of arguments for invoking getAzurePeeringConnection.
type LookupAzurePeeringConnectionOutputArgs struct {
	HvnLink            pulumi.StringInput  `pulumi:"hvnLink"`
	PeeringId          pulumi.StringInput  `pulumi:"peeringId"`
	WaitForActiveState pulumi.BoolPtrInput `pulumi:"waitForActiveState"`
}

func (LookupAzurePeeringConnectionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAzurePeeringConnectionArgs)(nil)).Elem()
}

// A collection of values returned by getAzurePeeringConnection.
type LookupAzurePeeringConnectionResultOutput struct{ *pulumi.OutputState }

func (LookupAzurePeeringConnectionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAzurePeeringConnectionResult)(nil)).Elem()
}

func (o LookupAzurePeeringConnectionResultOutput) ToLookupAzurePeeringConnectionResultOutput() LookupAzurePeeringConnectionResultOutput {
	return o
}

func (o LookupAzurePeeringConnectionResultOutput) ToLookupAzurePeeringConnectionResultOutputWithContext(ctx context.Context) LookupAzurePeeringConnectionResultOutput {
	return o
}

func (o LookupAzurePeeringConnectionResultOutput) ApplicationId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.ApplicationId }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) AzurePeeringId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.AzurePeeringId }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) ExpiresAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.ExpiresAt }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) HvnLink() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.HvnLink }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupAzurePeeringConnectionResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) PeerResourceGroupName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.PeerResourceGroupName }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) PeerSubscriptionId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.PeerSubscriptionId }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) PeerTenantId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.PeerTenantId }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) PeerVnetName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.PeerVnetName }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) PeerVnetRegion() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.PeerVnetRegion }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) PeeringId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.PeeringId }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) string { return v.SelfLink }).(pulumi.StringOutput)
}

func (o LookupAzurePeeringConnectionResultOutput) WaitForActiveState() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupAzurePeeringConnectionResult) *bool { return v.WaitForActiveState }).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAzurePeeringConnectionResultOutput{})
}
