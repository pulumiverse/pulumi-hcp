//go:build python || all
// +build python all

package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getPythonBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := GetBaseOptions()
	basePython := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			filepath.Join("..", "sdk", "python", "bin"),
		},
	})

	return basePython
}

func TestVaultPy(t *testing.T) {
	test := getPythonBaseOptions(t).
		With(integration.ProgramTestOptions{
			// TODO: Why does this need getCwd(t), but the
			// Dependencies above doesn't?
			Dir: filepath.Join(GetCwd(t), "hcp-vault", "py"),
		})
	integration.ProgramTest(t, &test)
}

func TestHvnPeeringPy(t *testing.T) {
	test := getPythonBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir:    filepath.Join(GetCwd(t), "hvn-peering", "py"),
			Config: map[string]string{"aws:region": "us-east-1"},
			// Sometimes (but not always!) refreshes will pick up a
			// change of the peering accepter's status, which aren't
			// interesting, and cause unnecessary spurious failures.
			SkipRefresh: true,
		})
	integration.ProgramTest(t, &test)
}
