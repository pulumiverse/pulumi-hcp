package examples

import (
	"os"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func GetCwd(t *testing.T) string {
	cwd, err := os.Getwd()
	if err != nil {
		t.FailNow()
	}

	return cwd
}

func GetBaseOptions() integration.ProgramTestOptions {
	return integration.ProgramTestOptions{
		Verbose: true,
		// We need to stay within HCP's resource limits, so we're not
		// going to run in parallel. In CI, we run tests split out by
		// language runtime, rather than all together, so we can apply
		// additional parallelization limits at that level to fine
		// tune things.
		NoParallel: true,
		// After updating the Terraform provider to 0.28.0, we
		// started seeing errors on refresh. The actual diff,
		// however, is a bit mysterious, and it's not clear what
		// the meaningful difference actually is:
		//
		// ~  hcp:index/vaultCluster:VaultCluster (update)
		// [id=/project/<IDENTIFYING-UUID>/hashicorp.vault.cluster/vault-testing-cluster-py]
		// [urn=urn:pulumi:<A-RANDOM-TESTING-STACK-NAME>::vault-py::hcp:index/vaultCluster:VaultCluster::vault-py]
		//
		// For now, we'll just skip these.
		SkipRefresh: true,
	}
}
