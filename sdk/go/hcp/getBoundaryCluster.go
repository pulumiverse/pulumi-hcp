// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The Boundary cluster data source provides information about an existing HCP Boundary cluster.
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
// 		_, err := hcp.LookupBoundaryCluster(ctx, &GetBoundaryClusterArgs{
// 			ClusterId: _var.Cluster_id,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupBoundaryCluster(ctx *pulumi.Context, args *LookupBoundaryClusterArgs, opts ...pulumi.InvokeOption) (*LookupBoundaryClusterResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupBoundaryClusterResult
	err := ctx.Invoke("hcp:index/getBoundaryCluster:getBoundaryCluster", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getBoundaryCluster.
type LookupBoundaryClusterArgs struct {
	// The ID of the Boundary cluster
	ClusterId string `pulumi:"clusterId"`
}

// A collection of values returned by getBoundaryCluster.
type LookupBoundaryClusterResult struct {
	// The ID of the Boundary cluster
	ClusterId string `pulumi:"clusterId"`
	// A unique URL identifying the Boundary cluster.
	ClusterUrl string `pulumi:"clusterUrl"`
	// The time that the Boundary cluster was created.
	CreatedAt string `pulumi:"createdAt"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The state of the Boundary cluster.
	State string `pulumi:"state"`
}

func LookupBoundaryClusterOutput(ctx *pulumi.Context, args LookupBoundaryClusterOutputArgs, opts ...pulumi.InvokeOption) LookupBoundaryClusterResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupBoundaryClusterResult, error) {
			args := v.(LookupBoundaryClusterArgs)
			r, err := LookupBoundaryCluster(ctx, &args, opts...)
			var s LookupBoundaryClusterResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupBoundaryClusterResultOutput)
}

// A collection of arguments for invoking getBoundaryCluster.
type LookupBoundaryClusterOutputArgs struct {
	// The ID of the Boundary cluster
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
}

func (LookupBoundaryClusterOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBoundaryClusterArgs)(nil)).Elem()
}

// A collection of values returned by getBoundaryCluster.
type LookupBoundaryClusterResultOutput struct{ *pulumi.OutputState }

func (LookupBoundaryClusterResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBoundaryClusterResult)(nil)).Elem()
}

func (o LookupBoundaryClusterResultOutput) ToLookupBoundaryClusterResultOutput() LookupBoundaryClusterResultOutput {
	return o
}

func (o LookupBoundaryClusterResultOutput) ToLookupBoundaryClusterResultOutputWithContext(ctx context.Context) LookupBoundaryClusterResultOutput {
	return o
}

// The ID of the Boundary cluster
func (o LookupBoundaryClusterResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBoundaryClusterResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// A unique URL identifying the Boundary cluster.
func (o LookupBoundaryClusterResultOutput) ClusterUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBoundaryClusterResult) string { return v.ClusterUrl }).(pulumi.StringOutput)
}

// The time that the Boundary cluster was created.
func (o LookupBoundaryClusterResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBoundaryClusterResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupBoundaryClusterResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBoundaryClusterResult) string { return v.Id }).(pulumi.StringOutput)
}

// The state of the Boundary cluster.
func (o LookupBoundaryClusterResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBoundaryClusterResult) string { return v.State }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBoundaryClusterResultOutput{})
}
