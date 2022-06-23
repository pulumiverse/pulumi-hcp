// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The Packer Image data source iteration gets the most recent iteration (or build) of an image, given a channel.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcp from "@pulumi/hcp";
 *
 * const hardened_source = pulumi.output(hcp.getPackerIteration({
 *     bucketName: "hardened-ubuntu-16-04",
 *     channel: "megan-test",
 * }));
 * ```
 */
export function getPackerIteration(args: GetPackerIterationArgs, opts?: pulumi.InvokeOptions): Promise<GetPackerIterationResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("hcp:index/getPackerIteration:getPackerIteration", {
        "bucketName": args.bucketName,
        "channel": args.channel,
    }, opts);
}

/**
 * A collection of arguments for invoking getPackerIteration.
 */
export interface GetPackerIterationArgs {
    bucketName: string;
    channel: string;
}

/**
 * A collection of values returned by getPackerIteration.
 */
export interface GetPackerIterationResult {
    readonly authorId: string;
    readonly bucketName: string;
    readonly channel: string;
    readonly createdAt: string;
    readonly fingerprint: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly incrementalVersion: number;
    readonly organizationId: string;
    readonly projectId: string;
    readonly revokeAt: string;
    readonly ulid: string;
    readonly updatedAt: string;
}

export function getPackerIterationOutput(args: GetPackerIterationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPackerIterationResult> {
    return pulumi.output(args).apply(a => getPackerIteration(a, opts))
}

/**
 * A collection of arguments for invoking getPackerIteration.
 */
export interface GetPackerIterationOutputArgs {
    bucketName: pulumi.Input<string>;
    channel: pulumi.Input<string>;
}
