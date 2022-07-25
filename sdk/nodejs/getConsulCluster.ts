// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The cluster data source provides information about an existing HCP Consul cluster.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcp from "@pulumi/hcp";
 *
 * const example = hcp.getConsulCluster({
 *     clusterId: _var.cluster_id,
 * });
 * ```
 */
export function getConsulCluster(args: GetConsulClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetConsulClusterResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("hcp:index/getConsulCluster:getConsulCluster", {
        "clusterId": args.clusterId,
    }, opts);
}

/**
 * A collection of arguments for invoking getConsulCluster.
 */
export interface GetConsulClusterArgs {
    clusterId: string;
}

/**
 * A collection of values returned by getConsulCluster.
 */
export interface GetConsulClusterResult {
    readonly autoHvnToHvnPeering: boolean;
    readonly cloudProvider: string;
    readonly clusterId: string;
    readonly connectEnabled: boolean;
    readonly consulAutomaticUpgrades: boolean;
    readonly consulCaFile: string;
    readonly consulConfigFile: string;
    readonly consulPrivateEndpointUrl: string;
    readonly consulPublicEndpointUrl: string;
    readonly consulSnapshotInterval: string;
    readonly consulSnapshotRetention: string;
    readonly consulVersion: string;
    readonly datacenter: string;
    readonly hvnId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly organizationId: string;
    readonly primaryLink: string;
    readonly projectId: string;
    readonly publicEndpoint: boolean;
    readonly region: string;
    readonly scale: number;
    readonly selfLink: string;
    readonly size: string;
    readonly state: string;
    readonly tier: string;
}

export function getConsulClusterOutput(args: GetConsulClusterOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetConsulClusterResult> {
    return pulumi.output(args).apply(a => getConsulCluster(a, opts))
}

/**
 * A collection of arguments for invoking getConsulCluster.
 */
export interface GetConsulClusterOutputArgs {
    clusterId: pulumi.Input<string>;
}
