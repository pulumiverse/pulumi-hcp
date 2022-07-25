// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The AWS transit gateway attachment data source provides information about an existing transit gateway attachment.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcp from "@pulumi/hcp";
 *
 * const test = hcp.getAwsTransitGatewayAttachment({
 *     hvnId: _var.hvn_id,
 *     transitGatewayAttachmentId: _var.transit_gateway_attachment_id,
 * });
 * ```
 */
export function getAwsTransitGatewayAttachment(args: GetAwsTransitGatewayAttachmentArgs, opts?: pulumi.InvokeOptions): Promise<GetAwsTransitGatewayAttachmentResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("hcp:index/getAwsTransitGatewayAttachment:getAwsTransitGatewayAttachment", {
        "hvnId": args.hvnId,
        "transitGatewayAttachmentId": args.transitGatewayAttachmentId,
        "waitForActiveState": args.waitForActiveState,
    }, opts);
}

/**
 * A collection of arguments for invoking getAwsTransitGatewayAttachment.
 */
export interface GetAwsTransitGatewayAttachmentArgs {
    hvnId: string;
    transitGatewayAttachmentId: string;
    waitForActiveState?: boolean;
}

/**
 * A collection of values returned by getAwsTransitGatewayAttachment.
 */
export interface GetAwsTransitGatewayAttachmentResult {
    readonly createdAt: string;
    readonly expiresAt: string;
    readonly hvnId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly organizationId: string;
    readonly projectId: string;
    readonly providerTransitGatewayAttachmentId: string;
    readonly selfLink: string;
    readonly state: string;
    readonly transitGatewayAttachmentId: string;
    readonly transitGatewayId: string;
    readonly waitForActiveState?: boolean;
}

export function getAwsTransitGatewayAttachmentOutput(args: GetAwsTransitGatewayAttachmentOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAwsTransitGatewayAttachmentResult> {
    return pulumi.output(args).apply(a => getAwsTransitGatewayAttachment(a, opts))
}

/**
 * A collection of arguments for invoking getAwsTransitGatewayAttachment.
 */
export interface GetAwsTransitGatewayAttachmentOutputArgs {
    hvnId: pulumi.Input<string>;
    transitGatewayAttachmentId: pulumi.Input<string>;
    waitForActiveState?: pulumi.Input<boolean>;
}
