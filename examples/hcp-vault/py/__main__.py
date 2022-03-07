import pulumi
import pulumi_hcp as hcp

def main() -> None:
    hvn = hcp.Hvn(
        "hvn-py",
        hvn_id="testing-hvn-py",
        cloud_provider="aws",
        region="us-east-1",
    )

    hcp.VaultCluster(
        "vault-py",
        hvn_id=hvn.hvn_id,
        cluster_id="vault-testing-cluster-py",
        tier="dev",
    )


if __name__ == "__main__":
    main()
