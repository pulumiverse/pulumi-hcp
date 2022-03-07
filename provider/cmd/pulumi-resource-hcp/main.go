//go:generate go run ./generate.go

package main

import (
	hcp "github.com/grapl-security/pulumi-hcp/provider"
	"github.com/grapl-security/pulumi-hcp/provider/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
)

func main() {
	// Modify the path to point to the new provider
	tfbridge.Main("hcp", version.Version, hcp.Provider(), pulumiSchema)
}
