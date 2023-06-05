// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Hcp.Outputs
{

    [OutputType]
    public sealed class GetVaultClusterMetricsConfigResult
    {
        /// <summary>
        /// Datadog region for streaming metrics
        /// </summary>
        public readonly string DatadogRegion;
        /// <summary>
        /// Grafana endpoint for streaming metrics
        /// </summary>
        public readonly string GrafanaEndpoint;
        /// <summary>
        /// Grafana user for streaming metrics
        /// </summary>
        public readonly string GrafanaUser;
        /// <summary>
        /// Splunk endpoint for streaming metrics
        /// </summary>
        public readonly string SplunkHecendpoint;

        [OutputConstructor]
        private GetVaultClusterMetricsConfigResult(
            string datadogRegion,

            string grafanaEndpoint,

            string grafanaUser,

            string splunkHecendpoint)
        {
            DatadogRegion = datadogRegion;
            GrafanaEndpoint = grafanaEndpoint;
            GrafanaUser = grafanaUser;
            SplunkHecendpoint = splunkHecendpoint;
        }
    }
}
