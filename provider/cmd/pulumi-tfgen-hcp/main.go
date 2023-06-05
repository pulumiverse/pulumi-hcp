package main

import (
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfgen"
	hcp "github.com/pulumiverse/pulumi-hcp/provider"
	"github.com/pulumiverse/pulumi-hcp/provider/pkg/version"
)

func main() {
	// Modify the path to point to the new provider
	tfgen.Main("hcp", version.Version, hcp.Provider())
}
