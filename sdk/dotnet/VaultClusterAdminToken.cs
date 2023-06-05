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
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Hcp = Pulumiverse.Hcp;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new Hcp.VaultClusterAdminToken("example", new()
    ///     {
    ///         ClusterId = "test-vault-cluster",
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [HcpResourceType("hcp:index/vaultClusterAdminToken:VaultClusterAdminToken")]
    public partial class VaultClusterAdminToken : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the HCP Vault cluster.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// The time that the admin token was created.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The admin token of this HCP Vault cluster.
        /// </summary>
        [Output("token")]
        public Output<string> Token { get; private set; } = null!;


        /// <summary>
        /// Create a VaultClusterAdminToken resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VaultClusterAdminToken(string name, VaultClusterAdminTokenArgs args, CustomResourceOptions? options = null)
            : base("hcp:index/vaultClusterAdminToken:VaultClusterAdminToken", name, args ?? new VaultClusterAdminTokenArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VaultClusterAdminToken(string name, Input<string> id, VaultClusterAdminTokenState? state = null, CustomResourceOptions? options = null)
            : base("hcp:index/vaultClusterAdminToken:VaultClusterAdminToken", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing VaultClusterAdminToken resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VaultClusterAdminToken Get(string name, Input<string> id, VaultClusterAdminTokenState? state = null, CustomResourceOptions? options = null)
        {
            return new VaultClusterAdminToken(name, id, state, options);
        }
    }

    public sealed class VaultClusterAdminTokenArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the HCP Vault cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        public VaultClusterAdminTokenArgs()
        {
        }
        public static new VaultClusterAdminTokenArgs Empty => new VaultClusterAdminTokenArgs();
    }

    public sealed class VaultClusterAdminTokenState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the HCP Vault cluster.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// The time that the admin token was created.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The admin token of this HCP Vault cluster.
        /// </summary>
        [Input("token")]
        public Input<string>? Token { get; set; }

        public VaultClusterAdminTokenState()
        {
        }
        public static new VaultClusterAdminTokenState Empty => new VaultClusterAdminTokenState();
    }
}
