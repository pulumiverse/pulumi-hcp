// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS network peering data source provides information about an existing network peering between an HVN and a peer AWS VPC.
func LookupAwsNetworkPeering(ctx *pulumi.Context, args *LookupAwsNetworkPeeringArgs, opts ...pulumi.InvokeOption) (*LookupAwsNetworkPeeringResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupAwsNetworkPeeringResult
	err := ctx.Invoke("hcp:index/getAwsNetworkPeering:getAwsNetworkPeering", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAwsNetworkPeering.
type LookupAwsNetworkPeeringArgs struct {
	HvnId              string `pulumi:"hvnId"`
	PeeringId          string `pulumi:"peeringId"`
	WaitForActiveState *bool  `pulumi:"waitForActiveState"`
}

// A collection of values returned by getAwsNetworkPeering.
type LookupAwsNetworkPeeringResult struct {
	CreatedAt string `pulumi:"createdAt"`
	ExpiresAt string `pulumi:"expiresAt"`
	HvnId     string `pulumi:"hvnId"`
	// The provider-assigned unique ID for this managed resource.
	Id                 string `pulumi:"id"`
	OrganizationId     string `pulumi:"organizationId"`
	PeerAccountId      string `pulumi:"peerAccountId"`
	PeerVpcId          string `pulumi:"peerVpcId"`
	PeerVpcRegion      string `pulumi:"peerVpcRegion"`
	PeeringId          string `pulumi:"peeringId"`
	ProjectId          string `pulumi:"projectId"`
	ProviderPeeringId  string `pulumi:"providerPeeringId"`
	SelfLink           string `pulumi:"selfLink"`
	State              string `pulumi:"state"`
	WaitForActiveState *bool  `pulumi:"waitForActiveState"`
}

func LookupAwsNetworkPeeringOutput(ctx *pulumi.Context, args LookupAwsNetworkPeeringOutputArgs, opts ...pulumi.InvokeOption) LookupAwsNetworkPeeringResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAwsNetworkPeeringResult, error) {
			args := v.(LookupAwsNetworkPeeringArgs)
			r, err := LookupAwsNetworkPeering(ctx, &args, opts...)
			var s LookupAwsNetworkPeeringResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAwsNetworkPeeringResultOutput)
}

// A collection of arguments for invoking getAwsNetworkPeering.
type LookupAwsNetworkPeeringOutputArgs struct {
	HvnId              pulumi.StringInput  `pulumi:"hvnId"`
	PeeringId          pulumi.StringInput  `pulumi:"peeringId"`
	WaitForActiveState pulumi.BoolPtrInput `pulumi:"waitForActiveState"`
}

func (LookupAwsNetworkPeeringOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAwsNetworkPeeringArgs)(nil)).Elem()
}

// A collection of values returned by getAwsNetworkPeering.
type LookupAwsNetworkPeeringResultOutput struct{ *pulumi.OutputState }

func (LookupAwsNetworkPeeringResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAwsNetworkPeeringResult)(nil)).Elem()
}

func (o LookupAwsNetworkPeeringResultOutput) ToLookupAwsNetworkPeeringResultOutput() LookupAwsNetworkPeeringResultOutput {
	return o
}

func (o LookupAwsNetworkPeeringResultOutput) ToLookupAwsNetworkPeeringResultOutputWithContext(ctx context.Context) LookupAwsNetworkPeeringResultOutput {
	return o
}

func (o LookupAwsNetworkPeeringResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) ExpiresAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.ExpiresAt }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) HvnId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.HvnId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupAwsNetworkPeeringResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) PeerAccountId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.PeerAccountId }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) PeerVpcId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.PeerVpcId }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) PeerVpcRegion() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.PeerVpcRegion }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) PeeringId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.PeeringId }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) ProviderPeeringId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.ProviderPeeringId }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.SelfLink }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) string { return v.State }).(pulumi.StringOutput)
}

func (o LookupAwsNetworkPeeringResultOutput) WaitForActiveState() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupAwsNetworkPeeringResult) *bool { return v.WaitForActiveState }).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAwsNetworkPeeringResultOutput{})
}
