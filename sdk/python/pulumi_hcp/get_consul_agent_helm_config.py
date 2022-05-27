# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetConsulAgentHelmConfigResult',
    'AwaitableGetConsulAgentHelmConfigResult',
    'get_consul_agent_helm_config',
    'get_consul_agent_helm_config_output',
]

@pulumi.output_type
class GetConsulAgentHelmConfigResult:
    """
    A collection of values returned by getConsulAgentHelmConfig.
    """
    def __init__(__self__, cluster_id=None, config=None, expose_gossip_ports=None, id=None, kubernetes_endpoint=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if config and not isinstance(config, str):
            raise TypeError("Expected argument 'config' to be a str")
        pulumi.set(__self__, "config", config)
        if expose_gossip_ports and not isinstance(expose_gossip_ports, bool):
            raise TypeError("Expected argument 'expose_gossip_ports' to be a bool")
        pulumi.set(__self__, "expose_gossip_ports", expose_gossip_ports)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kubernetes_endpoint and not isinstance(kubernetes_endpoint, str):
            raise TypeError("Expected argument 'kubernetes_endpoint' to be a str")
        pulumi.set(__self__, "kubernetes_endpoint", kubernetes_endpoint)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def config(self) -> str:
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="exposeGossipPorts")
    def expose_gossip_ports(self) -> Optional[bool]:
        return pulumi.get(self, "expose_gossip_ports")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubernetesEndpoint")
    def kubernetes_endpoint(self) -> str:
        return pulumi.get(self, "kubernetes_endpoint")


class AwaitableGetConsulAgentHelmConfigResult(GetConsulAgentHelmConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConsulAgentHelmConfigResult(
            cluster_id=self.cluster_id,
            config=self.config,
            expose_gossip_ports=self.expose_gossip_ports,
            id=self.id,
            kubernetes_endpoint=self.kubernetes_endpoint)


def get_consul_agent_helm_config(cluster_id: Optional[str] = None,
                                 expose_gossip_ports: Optional[bool] = None,
                                 kubernetes_endpoint: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConsulAgentHelmConfigResult:
    """
    The Consul agent Helm config data source provides Helm values for a Consul agent running in Kubernetes.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    example = hcp.get_consul_agent_helm_config(cluster_id=var["cluster_id"],
        kubernetes_endpoint=var["kubernetes_endpoint"])
    ```
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['exposeGossipPorts'] = expose_gossip_ports
    __args__['kubernetesEndpoint'] = kubernetes_endpoint
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('hcp:index/getConsulAgentHelmConfig:getConsulAgentHelmConfig', __args__, opts=opts, typ=GetConsulAgentHelmConfigResult).value

    return AwaitableGetConsulAgentHelmConfigResult(
        cluster_id=__ret__.cluster_id,
        config=__ret__.config,
        expose_gossip_ports=__ret__.expose_gossip_ports,
        id=__ret__.id,
        kubernetes_endpoint=__ret__.kubernetes_endpoint)


@_utilities.lift_output_func(get_consul_agent_helm_config)
def get_consul_agent_helm_config_output(cluster_id: Optional[pulumi.Input[str]] = None,
                                        expose_gossip_ports: Optional[pulumi.Input[Optional[bool]]] = None,
                                        kubernetes_endpoint: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConsulAgentHelmConfigResult]:
    """
    The Consul agent Helm config data source provides Helm values for a Consul agent running in Kubernetes.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    example = hcp.get_consul_agent_helm_config(cluster_id=var["cluster_id"],
        kubernetes_endpoint=var["kubernetes_endpoint"])
    ```
    """
    ...
