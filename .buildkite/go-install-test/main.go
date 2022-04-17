package main

import (
	hcp "github.com/grapl-security/pulumi-hcp/sdk/go/hcp"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This minimal program is solely designed to exercise the plugin
// binary installation. We must use *something* from the HCP SDK, so
// we'll just try to lookup a non-existent HVN; we don't care about
// the result, either.
//
// We'll also just be previewing this stack, as that is sufficient to
// trigger the plugin download. Note that we don't even need to
// provide HCP credentials for this to work (given this program, at
// least).
func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		hcp.LookupHvn(ctx, &hcp.LookupHvnArgs{
			HvnId: "not-really-there",
		})

		return nil
	})
}
