# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetVaultClusterResult',
    'AwaitableGetVaultClusterResult',
    'get_vault_cluster',
    'get_vault_cluster_output',
]

@pulumi.output_type
class GetVaultClusterResult:
    """
    A collection of values returned by getVaultCluster.
    """
    def __init__(__self__, audit_log_configs=None, cloud_provider=None, cluster_id=None, created_at=None, hvn_id=None, id=None, metrics_configs=None, min_vault_version=None, namespace=None, organization_id=None, paths_filters=None, primary_link=None, project_id=None, public_endpoint=None, region=None, self_link=None, state=None, tier=None, vault_private_endpoint_url=None, vault_public_endpoint_url=None, vault_version=None):
        if audit_log_configs and not isinstance(audit_log_configs, list):
            raise TypeError("Expected argument 'audit_log_configs' to be a list")
        pulumi.set(__self__, "audit_log_configs", audit_log_configs)
        if cloud_provider and not isinstance(cloud_provider, str):
            raise TypeError("Expected argument 'cloud_provider' to be a str")
        pulumi.set(__self__, "cloud_provider", cloud_provider)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if hvn_id and not isinstance(hvn_id, str):
            raise TypeError("Expected argument 'hvn_id' to be a str")
        pulumi.set(__self__, "hvn_id", hvn_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metrics_configs and not isinstance(metrics_configs, list):
            raise TypeError("Expected argument 'metrics_configs' to be a list")
        pulumi.set(__self__, "metrics_configs", metrics_configs)
        if min_vault_version and not isinstance(min_vault_version, str):
            raise TypeError("Expected argument 'min_vault_version' to be a str")
        pulumi.set(__self__, "min_vault_version", min_vault_version)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if paths_filters and not isinstance(paths_filters, list):
            raise TypeError("Expected argument 'paths_filters' to be a list")
        pulumi.set(__self__, "paths_filters", paths_filters)
        if primary_link and not isinstance(primary_link, str):
            raise TypeError("Expected argument 'primary_link' to be a str")
        pulumi.set(__self__, "primary_link", primary_link)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if public_endpoint and not isinstance(public_endpoint, bool):
            raise TypeError("Expected argument 'public_endpoint' to be a bool")
        pulumi.set(__self__, "public_endpoint", public_endpoint)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tier and not isinstance(tier, str):
            raise TypeError("Expected argument 'tier' to be a str")
        pulumi.set(__self__, "tier", tier)
        if vault_private_endpoint_url and not isinstance(vault_private_endpoint_url, str):
            raise TypeError("Expected argument 'vault_private_endpoint_url' to be a str")
        pulumi.set(__self__, "vault_private_endpoint_url", vault_private_endpoint_url)
        if vault_public_endpoint_url and not isinstance(vault_public_endpoint_url, str):
            raise TypeError("Expected argument 'vault_public_endpoint_url' to be a str")
        pulumi.set(__self__, "vault_public_endpoint_url", vault_public_endpoint_url)
        if vault_version and not isinstance(vault_version, str):
            raise TypeError("Expected argument 'vault_version' to be a str")
        pulumi.set(__self__, "vault_version", vault_version)

    @property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(self) -> Sequence['outputs.GetVaultClusterAuditLogConfigResult']:
        """
        The audit logs configuration for export. (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
        """
        return pulumi.get(self, "audit_log_configs")

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> str:
        """
        The provider where the HCP Vault cluster is located.
        """
        return pulumi.get(self, "cloud_provider")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The ID of the HCP Vault cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time that the Vault cluster was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="hvnId")
    def hvn_id(self) -> str:
        """
        The ID of the HVN this HCP Vault cluster is associated to.
        """
        return pulumi.get(self, "hvn_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="metricsConfigs")
    def metrics_configs(self) -> Sequence['outputs.GetVaultClusterMetricsConfigResult']:
        """
        The metrics configuration for export. (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
        """
        return pulumi.get(self, "metrics_configs")

    @property
    @pulumi.getter(name="minVaultVersion")
    def min_vault_version(self) -> str:
        """
        The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP.
        """
        return pulumi.get(self, "min_vault_version")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        The name of the customer namespace this HCP Vault cluster is located in.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The ID of the organization this HCP Vault cluster is located in.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="pathsFilters")
    def paths_filters(self) -> Sequence[str]:
        """
        The performance replication [paths filter](https://learn.hashicorp.com/tutorials/vault/paths-filter). Applies to performance replication secondaries only and operates in "deny" mode only.
        """
        return pulumi.get(self, "paths_filters")

    @property
    @pulumi.getter(name="primaryLink")
    def primary_link(self) -> str:
        """
        The `self_link` of the HCP Vault Plus tier cluster which is the primary in the performance replication setup with this HCP Vault Plus tier cluster. If not specified, it is a standalone Plus tier HCP Vault cluster.
        """
        return pulumi.get(self, "primary_link")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The ID of the project this HCP Vault cluster is located in.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> bool:
        """
        Denotes that the cluster has a public endpoint. Defaults to false.
        """
        return pulumi.get(self, "public_endpoint")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region where the HCP Vault cluster is located.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        A unique URL identifying the Vault cluster.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the Vault cluster.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tier(self) -> str:
        """
        The tier that the HCP Vault cluster will be provisioned as.  Only 'development' is available at this time.
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter(name="vaultPrivateEndpointUrl")
    def vault_private_endpoint_url(self) -> str:
        """
        The private URL for the Vault cluster.
        """
        return pulumi.get(self, "vault_private_endpoint_url")

    @property
    @pulumi.getter(name="vaultPublicEndpointUrl")
    def vault_public_endpoint_url(self) -> str:
        """
        The public URL for the Vault cluster. This will be empty if `public_endpoint` is `false`.
        """
        return pulumi.get(self, "vault_public_endpoint_url")

    @property
    @pulumi.getter(name="vaultVersion")
    def vault_version(self) -> str:
        """
        The Vault version of the cluster.
        """
        return pulumi.get(self, "vault_version")


class AwaitableGetVaultClusterResult(GetVaultClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVaultClusterResult(
            audit_log_configs=self.audit_log_configs,
            cloud_provider=self.cloud_provider,
            cluster_id=self.cluster_id,
            created_at=self.created_at,
            hvn_id=self.hvn_id,
            id=self.id,
            metrics_configs=self.metrics_configs,
            min_vault_version=self.min_vault_version,
            namespace=self.namespace,
            organization_id=self.organization_id,
            paths_filters=self.paths_filters,
            primary_link=self.primary_link,
            project_id=self.project_id,
            public_endpoint=self.public_endpoint,
            region=self.region,
            self_link=self.self_link,
            state=self.state,
            tier=self.tier,
            vault_private_endpoint_url=self.vault_private_endpoint_url,
            vault_public_endpoint_url=self.vault_public_endpoint_url,
            vault_version=self.vault_version)


def get_vault_cluster(audit_log_configs: Optional[Sequence[pulumi.InputType['GetVaultClusterAuditLogConfigArgs']]] = None,
                      cluster_id: Optional[str] = None,
                      metrics_configs: Optional[Sequence[pulumi.InputType['GetVaultClusterMetricsConfigArgs']]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVaultClusterResult:
    """
    The cluster data source provides information about an existing HCP Vault cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    example = hcp.get_vault_cluster(cluster_id=var["cluster_id"])
    ```


    :param Sequence[pulumi.InputType['GetVaultClusterAuditLogConfigArgs']] audit_log_configs: The audit logs configuration for export. (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
    :param str cluster_id: The ID of the HCP Vault cluster.
    :param Sequence[pulumi.InputType['GetVaultClusterMetricsConfigArgs']] metrics_configs: The metrics configuration for export. (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
    """
    __args__ = dict()
    __args__['auditLogConfigs'] = audit_log_configs
    __args__['clusterId'] = cluster_id
    __args__['metricsConfigs'] = metrics_configs
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('hcp:index/getVaultCluster:getVaultCluster', __args__, opts=opts, typ=GetVaultClusterResult).value

    return AwaitableGetVaultClusterResult(
        audit_log_configs=__ret__.audit_log_configs,
        cloud_provider=__ret__.cloud_provider,
        cluster_id=__ret__.cluster_id,
        created_at=__ret__.created_at,
        hvn_id=__ret__.hvn_id,
        id=__ret__.id,
        metrics_configs=__ret__.metrics_configs,
        min_vault_version=__ret__.min_vault_version,
        namespace=__ret__.namespace,
        organization_id=__ret__.organization_id,
        paths_filters=__ret__.paths_filters,
        primary_link=__ret__.primary_link,
        project_id=__ret__.project_id,
        public_endpoint=__ret__.public_endpoint,
        region=__ret__.region,
        self_link=__ret__.self_link,
        state=__ret__.state,
        tier=__ret__.tier,
        vault_private_endpoint_url=__ret__.vault_private_endpoint_url,
        vault_public_endpoint_url=__ret__.vault_public_endpoint_url,
        vault_version=__ret__.vault_version)


@_utilities.lift_output_func(get_vault_cluster)
def get_vault_cluster_output(audit_log_configs: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetVaultClusterAuditLogConfigArgs']]]]] = None,
                             cluster_id: Optional[pulumi.Input[str]] = None,
                             metrics_configs: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetVaultClusterMetricsConfigArgs']]]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVaultClusterResult]:
    """
    The cluster data source provides information about an existing HCP Vault cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    example = hcp.get_vault_cluster(cluster_id=var["cluster_id"])
    ```


    :param Sequence[pulumi.InputType['GetVaultClusterAuditLogConfigArgs']] audit_log_configs: The audit logs configuration for export. (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
    :param str cluster_id: The ID of the HCP Vault cluster.
    :param Sequence[pulumi.InputType['GetVaultClusterMetricsConfigArgs']] metrics_configs: The metrics configuration for export. (https://learn.hashicorp.com/tutorials/cloud/vault-metrics-guide#metrics-streaming-configuration)
    """
    ...
