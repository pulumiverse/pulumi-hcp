//go:build go || all
// +build go all

package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getGoBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := GetBaseOptions()
	baseGo := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"github.com/pulumiverse/pulumi-hcp/sdk",
		},
	})

	return baseGo
}

func TestVaultGo(t *testing.T) {
	test := getGoBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(GetCwd(t), "hcp-vault", "go"),
		})

	integration.ProgramTest(t, &test)
}

func TestHvnPeeringGo(t *testing.T) {
	test := getGoBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir:    filepath.Join(GetCwd(t), "hvn-peering", "go"),
			Config: map[string]string{"aws:region": "us-east-1"},
			// Sometimes (but not always!) refreshes will pick up a
			// change of the peering accepter's status, which aren't
			// interesting, and cause unnecessary spurious failures.
			SkipRefresh: true,
		})
	integration.ProgramTest(t, &test)
}
