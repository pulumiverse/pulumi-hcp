package main

import (
	"fmt"
	hcp "github.com/grapl-security/pulumi-hcp/sdk/go/hcp"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		hvn, err := hcp.NewHvn(ctx, "hvn-go", &hcp.HvnArgs{
			HvnId:         pulumi.String("testing-hvn-go"),
			CloudProvider: pulumi.String("aws"),
			Region:        pulumi.String("us-east-1"),
		})
		if err != nil {
			return fmt.Errorf("error creating HVN: %v", err)
		}

		_, err = hcp.NewVaultCluster(ctx, "vault-go", &hcp.VaultClusterArgs{
			HvnId:     hvn.HvnId,
			ClusterId: pulumi.String("vault-testing-cluster-go"),
			Tier:      pulumi.String("dev"),
		})
		if err != nil {
			return fmt.Errorf("error creating Vault cluster: %v", err)
		}

		return nil
	})
}
