import * as pulumi from "@pulumi/pulumi";
import * as hcp from "@grapl/pulumi-hcp";

const hvn = new hcp.Hvn(
    "hvn-ts",
    {
        hvnId: "testing-hvn-ts",
        cloudProvider: "aws",
        region: "us-east-1"
    }
);

new hcp.VaultCluster(
    "vault-ts",
    {
        hvnId: hvn.hvnId,
        clusterId: "vault-testing-cluster-ts",
        tier: "dev"
    }
);
