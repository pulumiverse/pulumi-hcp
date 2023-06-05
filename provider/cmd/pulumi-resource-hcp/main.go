//go:generate go run ./generate.go

package main

import (
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	hcp "github.com/pulumiverse/pulumi-hcp/provider"
	"github.com/pulumiverse/pulumi-hcp/provider/pkg/version"
)

func main() {
	// Modify the path to point to the new provider
	tfbridge.Main("hcp", version.Version, hcp.Provider(), pulumiSchema)
}
