// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The Consul versions data source provides the Consul versions supported by HCP.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcp from "@pulumi/hcp";
 *
 * const defaultConsulVersions = pulumi.output(hcp.getConsulVersions());
 * ```
 */
export function getConsulVersions(opts?: pulumi.InvokeOptions): Promise<GetConsulVersionsResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("hcp:index/getConsulVersions:getConsulVersions", {
    }, opts);
}

/**
 * A collection of values returned by getConsulVersions.
 */
export interface GetConsulVersionsResult {
    /**
     * The Consul versions available on HCP.
     */
    readonly availables: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The preview versions of Consul available on HCP.
     */
    readonly previews: string[];
    /**
     * The recommended Consul version for HCP clusters.
     */
    readonly recommended: string;
}
