//go:build nodejs || all
// +build nodejs all

package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getJSBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := GetBaseOptions()
	baseJS := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"@grapl/pulumi-hcp",
		},
	})

	return baseJS
}

func TestVaultJS(t *testing.T) {
	test := getJSBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(GetCwd(t), "hcp-vault", "nodejs"),
		})
	integration.ProgramTest(t, &test)
}

func TestHvnPeeringJS(t *testing.T) {
	test := getJSBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir:    filepath.Join(GetCwd(t), "hvn-peering", "nodejs"),
			Config: map[string]string{"aws:region": "us-east-1"},
			// Sometimes (but not always!) refreshes will pick up a
			// change of the peering accepter's status, which aren't
			// interesting, and cause unnecessary spurious failures.
			SkipRefresh: true,
		})
	integration.ProgramTest(t, &test)
}
