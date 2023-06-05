// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Hcp.Inputs
{

    public sealed class GetVaultClusterMetricsConfigInputArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Datadog region for streaming metrics
        /// </summary>
        [Input("datadogRegion", required: true)]
        public Input<string> DatadogRegion { get; set; } = null!;

        /// <summary>
        /// Grafana endpoint for streaming metrics
        /// </summary>
        [Input("grafanaEndpoint", required: true)]
        public Input<string> GrafanaEndpoint { get; set; } = null!;

        /// <summary>
        /// Grafana user for streaming metrics
        /// </summary>
        [Input("grafanaUser", required: true)]
        public Input<string> GrafanaUser { get; set; } = null!;

        /// <summary>
        /// Splunk endpoint for streaming metrics
        /// </summary>
        [Input("splunkHecendpoint", required: true)]
        public Input<string> SplunkHecendpoint { get; set; } = null!;

        public GetVaultClusterMetricsConfigInputArgs()
        {
        }
        public static new GetVaultClusterMetricsConfigInputArgs Empty => new GetVaultClusterMetricsConfigInputArgs();
    }
}