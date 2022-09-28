// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * > **Note:** This data source is currently in public beta.
 *
 * The Azure peering connection resource allows you to manage a peering connection between an HVN and a peer Azure VNet.
 *
 * ## Import
 *
 * # The import ID is {hvn_id}:{peering_id}
 *
 * ```sh
 *  $ pulumi import hcp:index/azurePeeringConnection:AzurePeeringConnection peer main-hvn:199e7e96-4d5f-4456-91f3-b6cc71f1e561
 * ```
 */
export class AzurePeeringConnection extends pulumi.CustomResource {
    /**
     * Get an existing AzurePeeringConnection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AzurePeeringConnectionState, opts?: pulumi.CustomResourceOptions): AzurePeeringConnection {
        return new AzurePeeringConnection(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcp:index/azurePeeringConnection:AzurePeeringConnection';

    /**
     * Returns true if the given object is an instance of AzurePeeringConnection.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AzurePeeringConnection {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AzurePeeringConnection.__pulumiType;
    }

    /**
     * The ID of the Azure application whose credentials are used to peer the HCP HVN's underlying VNet with the customer VNet.
     */
    public /*out*/ readonly applicationId!: pulumi.Output<string>;
    /**
     * The peering connection ID used by Azure.
     */
    public /*out*/ readonly azurePeeringId!: pulumi.Output<string>;
    /**
     * The time that the peering connection was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
     */
    public /*out*/ readonly expiresAt!: pulumi.Output<string>;
    /**
     * The `selfLink` of the HashiCorp Virtual Network (HVN).
     */
    public readonly hvnLink!: pulumi.Output<string>;
    /**
     * The ID of the HCP organization where the peering connection is located. Always matches the HVN's organization.
     */
    public /*out*/ readonly organizationId!: pulumi.Output<string>;
    /**
     * The resource group name of the peer VNet in Azure.
     */
    public readonly peerResourceGroupName!: pulumi.Output<string>;
    /**
     * The subscription ID of the peer VNet in Azure.
     */
    public readonly peerSubscriptionId!: pulumi.Output<string>;
    /**
     * The tenant ID of the peer VNet in Azure.
     */
    public readonly peerTenantId!: pulumi.Output<string>;
    /**
     * The name of the peer VNet in Azure.
     */
    public readonly peerVnetName!: pulumi.Output<string>;
    /**
     * The region of the peer VNet in Azure.
     */
    public readonly peerVnetRegion!: pulumi.Output<string>;
    /**
     * The ID of the peering connection.
     */
    public readonly peeringId!: pulumi.Output<string>;
    /**
     * The ID of the HCP project where the peering connection is located. Always matches the HVN's project.
     */
    public /*out*/ readonly projectId!: pulumi.Output<string>;
    /**
     * A unique URL identifying the peering connection.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;
    /**
     * The state of the Azure peering connection.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;

    /**
     * Create a AzurePeeringConnection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AzurePeeringConnectionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AzurePeeringConnectionArgs | AzurePeeringConnectionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AzurePeeringConnectionState | undefined;
            resourceInputs["applicationId"] = state ? state.applicationId : undefined;
            resourceInputs["azurePeeringId"] = state ? state.azurePeeringId : undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["expiresAt"] = state ? state.expiresAt : undefined;
            resourceInputs["hvnLink"] = state ? state.hvnLink : undefined;
            resourceInputs["organizationId"] = state ? state.organizationId : undefined;
            resourceInputs["peerResourceGroupName"] = state ? state.peerResourceGroupName : undefined;
            resourceInputs["peerSubscriptionId"] = state ? state.peerSubscriptionId : undefined;
            resourceInputs["peerTenantId"] = state ? state.peerTenantId : undefined;
            resourceInputs["peerVnetName"] = state ? state.peerVnetName : undefined;
            resourceInputs["peerVnetRegion"] = state ? state.peerVnetRegion : undefined;
            resourceInputs["peeringId"] = state ? state.peeringId : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["selfLink"] = state ? state.selfLink : undefined;
            resourceInputs["state"] = state ? state.state : undefined;
        } else {
            const args = argsOrState as AzurePeeringConnectionArgs | undefined;
            if ((!args || args.hvnLink === undefined) && !opts.urn) {
                throw new Error("Missing required property 'hvnLink'");
            }
            if ((!args || args.peerResourceGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerResourceGroupName'");
            }
            if ((!args || args.peerSubscriptionId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerSubscriptionId'");
            }
            if ((!args || args.peerTenantId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerTenantId'");
            }
            if ((!args || args.peerVnetName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerVnetName'");
            }
            if ((!args || args.peerVnetRegion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerVnetRegion'");
            }
            if ((!args || args.peeringId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peeringId'");
            }
            resourceInputs["hvnLink"] = args ? args.hvnLink : undefined;
            resourceInputs["peerResourceGroupName"] = args ? args.peerResourceGroupName : undefined;
            resourceInputs["peerSubscriptionId"] = args ? args.peerSubscriptionId : undefined;
            resourceInputs["peerTenantId"] = args ? args.peerTenantId : undefined;
            resourceInputs["peerVnetName"] = args ? args.peerVnetName : undefined;
            resourceInputs["peerVnetRegion"] = args ? args.peerVnetRegion : undefined;
            resourceInputs["peeringId"] = args ? args.peeringId : undefined;
            resourceInputs["applicationId"] = undefined /*out*/;
            resourceInputs["azurePeeringId"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["expiresAt"] = undefined /*out*/;
            resourceInputs["organizationId"] = undefined /*out*/;
            resourceInputs["projectId"] = undefined /*out*/;
            resourceInputs["selfLink"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AzurePeeringConnection.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AzurePeeringConnection resources.
 */
export interface AzurePeeringConnectionState {
    /**
     * The ID of the Azure application whose credentials are used to peer the HCP HVN's underlying VNet with the customer VNet.
     */
    applicationId?: pulumi.Input<string>;
    /**
     * The peering connection ID used by Azure.
     */
    azurePeeringId?: pulumi.Input<string>;
    /**
     * The time that the peering connection was created.
     */
    createdAt?: pulumi.Input<string>;
    /**
     * The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
     */
    expiresAt?: pulumi.Input<string>;
    /**
     * The `selfLink` of the HashiCorp Virtual Network (HVN).
     */
    hvnLink?: pulumi.Input<string>;
    /**
     * The ID of the HCP organization where the peering connection is located. Always matches the HVN's organization.
     */
    organizationId?: pulumi.Input<string>;
    /**
     * The resource group name of the peer VNet in Azure.
     */
    peerResourceGroupName?: pulumi.Input<string>;
    /**
     * The subscription ID of the peer VNet in Azure.
     */
    peerSubscriptionId?: pulumi.Input<string>;
    /**
     * The tenant ID of the peer VNet in Azure.
     */
    peerTenantId?: pulumi.Input<string>;
    /**
     * The name of the peer VNet in Azure.
     */
    peerVnetName?: pulumi.Input<string>;
    /**
     * The region of the peer VNet in Azure.
     */
    peerVnetRegion?: pulumi.Input<string>;
    /**
     * The ID of the peering connection.
     */
    peeringId?: pulumi.Input<string>;
    /**
     * The ID of the HCP project where the peering connection is located. Always matches the HVN's project.
     */
    projectId?: pulumi.Input<string>;
    /**
     * A unique URL identifying the peering connection.
     */
    selfLink?: pulumi.Input<string>;
    /**
     * The state of the Azure peering connection.
     */
    state?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AzurePeeringConnection resource.
 */
export interface AzurePeeringConnectionArgs {
    /**
     * The `selfLink` of the HashiCorp Virtual Network (HVN).
     */
    hvnLink: pulumi.Input<string>;
    /**
     * The resource group name of the peer VNet in Azure.
     */
    peerResourceGroupName: pulumi.Input<string>;
    /**
     * The subscription ID of the peer VNet in Azure.
     */
    peerSubscriptionId: pulumi.Input<string>;
    /**
     * The tenant ID of the peer VNet in Azure.
     */
    peerTenantId: pulumi.Input<string>;
    /**
     * The name of the peer VNet in Azure.
     */
    peerVnetName: pulumi.Input<string>;
    /**
     * The region of the peer VNet in Azure.
     */
    peerVnetRegion: pulumi.Input<string>;
    /**
     * The ID of the peering connection.
     */
    peeringId: pulumi.Input<string>;
}
