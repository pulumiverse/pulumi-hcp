// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The HVN peering connection data source provides information about an existing peering connection between HVNs.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-hcp/sdk/go/hcp"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := hcp.LookupHvnPeeringConnection(ctx, &GetHvnPeeringConnectionArgs{
//				PeeringId: _var.Peering_id,
//				Hvn1:      _var.Hvn_1,
//				Hvn2:      _var.Hvn_2,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupHvnPeeringConnection(ctx *pulumi.Context, args *LookupHvnPeeringConnectionArgs, opts ...pulumi.InvokeOption) (*LookupHvnPeeringConnectionResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupHvnPeeringConnectionResult
	err := ctx.Invoke("hcp:index/getHvnPeeringConnection:getHvnPeeringConnection", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getHvnPeeringConnection.
type LookupHvnPeeringConnectionArgs struct {
	// The unique URL of one of the HVNs being peered.
	Hvn1 string `pulumi:"hvn1"`
	// The unique URL of one of the HVNs being peered.
	Hvn2 string `pulumi:"hvn2"`
	// The ID of the peering connection.
	PeeringId string `pulumi:"peeringId"`
}

// A collection of values returned by getHvnPeeringConnection.
type LookupHvnPeeringConnectionResult struct {
	// The time that the peering connection was created.
	CreatedAt string `pulumi:"createdAt"`
	// The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
	ExpiresAt string `pulumi:"expiresAt"`
	// The unique URL of one of the HVNs being peered.
	Hvn1 string `pulumi:"hvn1"`
	// The unique URL of one of the HVNs being peered.
	Hvn2 string `pulumi:"hvn2"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The ID of the HCP organization where the peering connection is located. Always matches the HVNs' organization.
	OrganizationId string `pulumi:"organizationId"`
	// The ID of the peering connection.
	PeeringId string `pulumi:"peeringId"`
	// The ID of the HCP project where the peering connection is located. Always matches the HVNs' project.
	ProjectId string `pulumi:"projectId"`
	// A unique URL identifying the peering connection
	SelfLink string `pulumi:"selfLink"`
	// The state of the HVN peering connection.
	State string `pulumi:"state"`
}

func LookupHvnPeeringConnectionOutput(ctx *pulumi.Context, args LookupHvnPeeringConnectionOutputArgs, opts ...pulumi.InvokeOption) LookupHvnPeeringConnectionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupHvnPeeringConnectionResult, error) {
			args := v.(LookupHvnPeeringConnectionArgs)
			r, err := LookupHvnPeeringConnection(ctx, &args, opts...)
			var s LookupHvnPeeringConnectionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupHvnPeeringConnectionResultOutput)
}

// A collection of arguments for invoking getHvnPeeringConnection.
type LookupHvnPeeringConnectionOutputArgs struct {
	// The unique URL of one of the HVNs being peered.
	Hvn1 pulumi.StringInput `pulumi:"hvn1"`
	// The unique URL of one of the HVNs being peered.
	Hvn2 pulumi.StringInput `pulumi:"hvn2"`
	// The ID of the peering connection.
	PeeringId pulumi.StringInput `pulumi:"peeringId"`
}

func (LookupHvnPeeringConnectionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupHvnPeeringConnectionArgs)(nil)).Elem()
}

// A collection of values returned by getHvnPeeringConnection.
type LookupHvnPeeringConnectionResultOutput struct{ *pulumi.OutputState }

func (LookupHvnPeeringConnectionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupHvnPeeringConnectionResult)(nil)).Elem()
}

func (o LookupHvnPeeringConnectionResultOutput) ToLookupHvnPeeringConnectionResultOutput() LookupHvnPeeringConnectionResultOutput {
	return o
}

func (o LookupHvnPeeringConnectionResultOutput) ToLookupHvnPeeringConnectionResultOutputWithContext(ctx context.Context) LookupHvnPeeringConnectionResultOutput {
	return o
}

// The time that the peering connection was created.
func (o LookupHvnPeeringConnectionResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHvnPeeringConnectionResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
func (o LookupHvnPeeringConnectionResultOutput) ExpiresAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHvnPeeringConnectionResult) string { return v.ExpiresAt }).(pulumi.StringOutput)
}

// The unique URL of one of the HVNs being peered.
func (o LookupHvnPeeringConnectionResultOutput) Hvn1() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHvnPeeringConnectionResult) string { return v.Hvn1 }).(pulumi.StringOutput)
}

// The unique URL of one of the HVNs being peered.
func (o LookupHvnPeeringConnectionResultOutput) Hvn2() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHvnPeeringConnectionResult) string { return v.Hvn2 }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupHvnPeeringConnectionResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHvnPeeringConnectionResult) string { return v.Id }).(pulumi.StringOutput)
}

// The ID of the HCP organization where the peering connection is located. Always matches the HVNs' organization.
func (o LookupHvnPeeringConnectionResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHvnPeeringConnectionResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

// The ID of the peering connection.
func (o LookupHvnPeeringConnectionResultOutput) PeeringId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHvnPeeringConnectionResult) string { return v.PeeringId }).(pulumi.StringOutput)
}

// The ID of the HCP project where the peering connection is located. Always matches the HVNs' project.
func (o LookupHvnPeeringConnectionResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHvnPeeringConnectionResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

// A unique URL identifying the peering connection
func (o LookupHvnPeeringConnectionResultOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHvnPeeringConnectionResult) string { return v.SelfLink }).(pulumi.StringOutput)
}

// The state of the HVN peering connection.
func (o LookupHvnPeeringConnectionResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupHvnPeeringConnectionResult) string { return v.State }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupHvnPeeringConnectionResultOutput{})
}
