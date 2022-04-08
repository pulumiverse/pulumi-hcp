package main

import (
	hcp "github.com/grapl-security/pulumi-hcp/provider"
	"github.com/grapl-security/pulumi-hcp/provider/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfgen"
)

func main() {
	// Modify the path to point to the new provider
	tfgen.Main("hcp", version.Version, hcp.Provider())
}
