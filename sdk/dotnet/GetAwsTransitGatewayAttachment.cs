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
    public static class GetAwsTransitGatewayAttachment
    {
        /// <summary>
        /// The AWS transit gateway attachment data source provides information about an existing transit gateway attachment.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Hcp = Pulumi.Hcp;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var test = Hcp.GetAwsTransitGatewayAttachment.Invoke(new()
        ///     {
        ///         HvnId = @var.Hvn_id,
        ///         TransitGatewayAttachmentId = @var.Transit_gateway_attachment_id,
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetAwsTransitGatewayAttachmentResult> InvokeAsync(GetAwsTransitGatewayAttachmentArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAwsTransitGatewayAttachmentResult>("hcp:index/getAwsTransitGatewayAttachment:getAwsTransitGatewayAttachment", args ?? new GetAwsTransitGatewayAttachmentArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS transit gateway attachment data source provides information about an existing transit gateway attachment.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Hcp = Pulumi.Hcp;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var test = Hcp.GetAwsTransitGatewayAttachment.Invoke(new()
        ///     {
        ///         HvnId = @var.Hvn_id,
        ///         TransitGatewayAttachmentId = @var.Transit_gateway_attachment_id,
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetAwsTransitGatewayAttachmentResult> Invoke(GetAwsTransitGatewayAttachmentInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAwsTransitGatewayAttachmentResult>("hcp:index/getAwsTransitGatewayAttachment:getAwsTransitGatewayAttachment", args ?? new GetAwsTransitGatewayAttachmentInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAwsTransitGatewayAttachmentArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnId", required: true)]
        public string HvnId { get; set; } = null!;

        /// <summary>
        /// The user-settable name of the transit gateway attachment in HCP.
        /// </summary>
        [Input("transitGatewayAttachmentId", required: true)]
        public string TransitGatewayAttachmentId { get; set; } = null!;

        [Input("waitForActiveState")]
        public bool? WaitForActiveState { get; set; }

        public GetAwsTransitGatewayAttachmentArgs()
        {
        }
        public static new GetAwsTransitGatewayAttachmentArgs Empty => new GetAwsTransitGatewayAttachmentArgs();
    }

    public sealed class GetAwsTransitGatewayAttachmentInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnId", required: true)]
        public Input<string> HvnId { get; set; } = null!;

        /// <summary>
        /// The user-settable name of the transit gateway attachment in HCP.
        /// </summary>
        [Input("transitGatewayAttachmentId", required: true)]
        public Input<string> TransitGatewayAttachmentId { get; set; } = null!;

        [Input("waitForActiveState")]
        public Input<bool>? WaitForActiveState { get; set; }

        public GetAwsTransitGatewayAttachmentInvokeArgs()
        {
        }
        public static new GetAwsTransitGatewayAttachmentInvokeArgs Empty => new GetAwsTransitGatewayAttachmentInvokeArgs();
    }


    [OutputType]
    public sealed class GetAwsTransitGatewayAttachmentResult
    {
        /// <summary>
        /// The time that the transit gateway attachment was created.
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// The time after which the transit gateway attachment will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        /// </summary>
        public readonly string ExpiresAt;
        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        public readonly string HvnId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The ID of the HCP organization where the transit gateway attachment is located. Always matches the HVN's organization.
        /// </summary>
        public readonly string OrganizationId;
        /// <summary>
        /// The ID of the HCP project where the transit gateway attachment is located. Always matches the HVN's project.
        /// </summary>
        public readonly string ProjectId;
        /// <summary>
        /// The transit gateway attachment ID used by AWS.
        /// </summary>
        public readonly string ProviderTransitGatewayAttachmentId;
        /// <summary>
        /// A unique URL identifying the transit gateway attachment.
        /// </summary>
        public readonly string SelfLink;
        /// <summary>
        /// The state of the transit gateway attachment.
        /// </summary>
        public readonly string State;
        /// <summary>
        /// The user-settable name of the transit gateway attachment in HCP.
        /// </summary>
        public readonly string TransitGatewayAttachmentId;
        /// <summary>
        /// The ID of the user-owned transit gateway in AWS.
        /// </summary>
        public readonly string TransitGatewayId;
        public readonly bool? WaitForActiveState;

        [OutputConstructor]
        private GetAwsTransitGatewayAttachmentResult(
            string createdAt,

            string expiresAt,

            string hvnId,

            string id,

            string organizationId,

            string projectId,

            string providerTransitGatewayAttachmentId,

            string selfLink,

            string state,

            string transitGatewayAttachmentId,

            string transitGatewayId,

            bool? waitForActiveState)
        {
            CreatedAt = createdAt;
            ExpiresAt = expiresAt;
            HvnId = hvnId;
            Id = id;
            OrganizationId = organizationId;
            ProjectId = projectId;
            ProviderTransitGatewayAttachmentId = providerTransitGatewayAttachmentId;
            SelfLink = selfLink;
            State = state;
            TransitGatewayAttachmentId = transitGatewayAttachmentId;
            TransitGatewayId = transitGatewayId;
            WaitForActiveState = waitForActiveState;
        }
    }
}
