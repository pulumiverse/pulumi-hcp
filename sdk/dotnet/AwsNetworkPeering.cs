// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Hcp
{
    /// <summary>
    /// The AWS network peering resource allows you to manage a network peering between an HVN and a peer AWS VPC.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// using Hcp = Pulumiverse.Hcp;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var main = new Hcp.Hvn("main", new()
    ///     {
    ///         HvnId = "main-hvn",
    ///         CloudProvider = "aws",
    ///         Region = "us-west-2",
    ///         CidrBlock = "172.25.16.0/20",
    ///     });
    /// 
    ///     var peerVpc = new Aws.Ec2.Vpc("peerVpc", new()
    ///     {
    ///         CidrBlock = "172.31.0.0/16",
    ///     });
    /// 
    ///     var peerArn = Aws.GetArn.Invoke(new()
    ///     {
    ///         Arn = peerVpc.Arn,
    ///     });
    /// 
    ///     var dev = new Hcp.AwsNetworkPeering("dev", new()
    ///     {
    ///         HvnId = main.HvnId,
    ///         PeeringId = "dev",
    ///         PeerVpcId = peerVpc.Id,
    ///         PeerAccountId = peerVpc.OwnerId,
    ///         PeerVpcRegion = peerArn.Apply(getArnResult =&gt; getArnResult.Region),
    ///     });
    /// 
    ///     var main_to_dev = new Hcp.HvnRoute("main-to-dev", new()
    ///     {
    ///         HvnLink = main.SelfLink,
    ///         HvnRouteId = "main-to-dev",
    ///         DestinationCidr = "172.31.0.0/16",
    ///         TargetLink = dev.SelfLink,
    ///     });
    /// 
    ///     var peerVpcPeeringConnectionAccepter = new Aws.Ec2.VpcPeeringConnectionAccepter("peerVpcPeeringConnectionAccepter", new()
    ///     {
    ///         VpcPeeringConnectionId = dev.ProviderPeeringId,
    ///         AutoAccept = true,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// # The import ID is {hvn_id}:{peering_id}
    /// 
    /// ```sh
    ///  $ pulumi import hcp:index/awsNetworkPeering:AwsNetworkPeering peer main-hvn:11eb60b3-d4ec-5eed-aacc-0242ac120015
    /// ```
    /// </summary>
    [HcpResourceType("hcp:index/awsNetworkPeering:AwsNetworkPeering")]
    public partial class AwsNetworkPeering : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The time that the network peering was created.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The time after which the network peering will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        /// </summary>
        [Output("expiresAt")]
        public Output<string> ExpiresAt { get; private set; } = null!;

        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Output("hvnId")]
        public Output<string> HvnId { get; private set; } = null!;

        /// <summary>
        /// The ID of the HCP organization where the network peering is located. Always matches the HVN's organization.
        /// </summary>
        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// The account ID of the peer VPC in AWS.
        /// </summary>
        [Output("peerAccountId")]
        public Output<string> PeerAccountId { get; private set; } = null!;

        /// <summary>
        /// The ID of the peer VPC in AWS.
        /// </summary>
        [Output("peerVpcId")]
        public Output<string> PeerVpcId { get; private set; } = null!;

        /// <summary>
        /// The region of the peer VPC in AWS.
        /// </summary>
        [Output("peerVpcRegion")]
        public Output<string> PeerVpcRegion { get; private set; } = null!;

        /// <summary>
        /// The ID of the network peering.
        /// </summary>
        [Output("peeringId")]
        public Output<string> PeeringId { get; private set; } = null!;

        /// <summary>
        /// The ID of the HCP project where the network peering is located. Always matches the HVN's project.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// The peering connection ID used by AWS.
        /// </summary>
        [Output("providerPeeringId")]
        public Output<string> ProviderPeeringId { get; private set; } = null!;

        /// <summary>
        /// A unique URL identifying the network peering.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        /// <summary>
        /// The state of the network peering.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;


        /// <summary>
        /// Create a AwsNetworkPeering resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AwsNetworkPeering(string name, AwsNetworkPeeringArgs args, CustomResourceOptions? options = null)
            : base("hcp:index/awsNetworkPeering:AwsNetworkPeering", name, args ?? new AwsNetworkPeeringArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AwsNetworkPeering(string name, Input<string> id, AwsNetworkPeeringState? state = null, CustomResourceOptions? options = null)
            : base("hcp:index/awsNetworkPeering:AwsNetworkPeering", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse/",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AwsNetworkPeering resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AwsNetworkPeering Get(string name, Input<string> id, AwsNetworkPeeringState? state = null, CustomResourceOptions? options = null)
        {
            return new AwsNetworkPeering(name, id, state, options);
        }
    }

    public sealed class AwsNetworkPeeringArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnId", required: true)]
        public Input<string> HvnId { get; set; } = null!;

        /// <summary>
        /// The account ID of the peer VPC in AWS.
        /// </summary>
        [Input("peerAccountId", required: true)]
        public Input<string> PeerAccountId { get; set; } = null!;

        /// <summary>
        /// The ID of the peer VPC in AWS.
        /// </summary>
        [Input("peerVpcId", required: true)]
        public Input<string> PeerVpcId { get; set; } = null!;

        /// <summary>
        /// The region of the peer VPC in AWS.
        /// </summary>
        [Input("peerVpcRegion", required: true)]
        public Input<string> PeerVpcRegion { get; set; } = null!;

        /// <summary>
        /// The ID of the network peering.
        /// </summary>
        [Input("peeringId", required: true)]
        public Input<string> PeeringId { get; set; } = null!;

        public AwsNetworkPeeringArgs()
        {
        }
        public static new AwsNetworkPeeringArgs Empty => new AwsNetworkPeeringArgs();
    }

    public sealed class AwsNetworkPeeringState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The time that the network peering was created.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The time after which the network peering will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        /// </summary>
        [Input("expiresAt")]
        public Input<string>? ExpiresAt { get; set; }

        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnId")]
        public Input<string>? HvnId { get; set; }

        /// <summary>
        /// The ID of the HCP organization where the network peering is located. Always matches the HVN's organization.
        /// </summary>
        [Input("organizationId")]
        public Input<string>? OrganizationId { get; set; }

        /// <summary>
        /// The account ID of the peer VPC in AWS.
        /// </summary>
        [Input("peerAccountId")]
        public Input<string>? PeerAccountId { get; set; }

        /// <summary>
        /// The ID of the peer VPC in AWS.
        /// </summary>
        [Input("peerVpcId")]
        public Input<string>? PeerVpcId { get; set; }

        /// <summary>
        /// The region of the peer VPC in AWS.
        /// </summary>
        [Input("peerVpcRegion")]
        public Input<string>? PeerVpcRegion { get; set; }

        /// <summary>
        /// The ID of the network peering.
        /// </summary>
        [Input("peeringId")]
        public Input<string>? PeeringId { get; set; }

        /// <summary>
        /// The ID of the HCP project where the network peering is located. Always matches the HVN's project.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// The peering connection ID used by AWS.
        /// </summary>
        [Input("providerPeeringId")]
        public Input<string>? ProviderPeeringId { get; set; }

        /// <summary>
        /// A unique URL identifying the network peering.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        /// <summary>
        /// The state of the network peering.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        public AwsNetworkPeeringState()
        {
        }
        public static new AwsNetworkPeeringState Empty => new AwsNetworkPeeringState();
    }
}
