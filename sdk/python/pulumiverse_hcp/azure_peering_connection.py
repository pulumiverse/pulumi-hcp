# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AzurePeeringConnectionArgs', 'AzurePeeringConnection']

@pulumi.input_type
class AzurePeeringConnectionArgs:
    def __init__(__self__, *,
                 hvn_link: pulumi.Input[str],
                 peer_resource_group_name: pulumi.Input[str],
                 peer_subscription_id: pulumi.Input[str],
                 peer_tenant_id: pulumi.Input[str],
                 peer_vnet_name: pulumi.Input[str],
                 peer_vnet_region: pulumi.Input[str],
                 peering_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a AzurePeeringConnection resource.
        :param pulumi.Input[str] hvn_link: The `self_link` of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] peer_resource_group_name: The resource group name of the peer VNet in Azure.
        :param pulumi.Input[str] peer_subscription_id: The subscription ID of the peer VNet in Azure.
        :param pulumi.Input[str] peer_tenant_id: The tenant ID of the peer VNet in Azure.
        :param pulumi.Input[str] peer_vnet_name: The name of the peer VNet in Azure.
        :param pulumi.Input[str] peer_vnet_region: The region of the peer VNet in Azure.
        :param pulumi.Input[str] peering_id: The ID of the peering connection.
        """
        pulumi.set(__self__, "hvn_link", hvn_link)
        pulumi.set(__self__, "peer_resource_group_name", peer_resource_group_name)
        pulumi.set(__self__, "peer_subscription_id", peer_subscription_id)
        pulumi.set(__self__, "peer_tenant_id", peer_tenant_id)
        pulumi.set(__self__, "peer_vnet_name", peer_vnet_name)
        pulumi.set(__self__, "peer_vnet_region", peer_vnet_region)
        pulumi.set(__self__, "peering_id", peering_id)

    @property
    @pulumi.getter(name="hvnLink")
    def hvn_link(self) -> pulumi.Input[str]:
        """
        The `self_link` of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_link")

    @hvn_link.setter
    def hvn_link(self, value: pulumi.Input[str]):
        pulumi.set(self, "hvn_link", value)

    @property
    @pulumi.getter(name="peerResourceGroupName")
    def peer_resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_resource_group_name")

    @peer_resource_group_name.setter
    def peer_resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_resource_group_name", value)

    @property
    @pulumi.getter(name="peerSubscriptionId")
    def peer_subscription_id(self) -> pulumi.Input[str]:
        """
        The subscription ID of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_subscription_id")

    @peer_subscription_id.setter
    def peer_subscription_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_subscription_id", value)

    @property
    @pulumi.getter(name="peerTenantId")
    def peer_tenant_id(self) -> pulumi.Input[str]:
        """
        The tenant ID of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_tenant_id")

    @peer_tenant_id.setter
    def peer_tenant_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_tenant_id", value)

    @property
    @pulumi.getter(name="peerVnetName")
    def peer_vnet_name(self) -> pulumi.Input[str]:
        """
        The name of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_vnet_name")

    @peer_vnet_name.setter
    def peer_vnet_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_vnet_name", value)

    @property
    @pulumi.getter(name="peerVnetRegion")
    def peer_vnet_region(self) -> pulumi.Input[str]:
        """
        The region of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_vnet_region")

    @peer_vnet_region.setter
    def peer_vnet_region(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_vnet_region", value)

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> pulumi.Input[str]:
        """
        The ID of the peering connection.
        """
        return pulumi.get(self, "peering_id")

    @peering_id.setter
    def peering_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "peering_id", value)


@pulumi.input_type
class _AzurePeeringConnectionState:
    def __init__(__self__, *,
                 application_id: Optional[pulumi.Input[str]] = None,
                 azure_peering_id: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 hvn_link: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 peer_resource_group_name: Optional[pulumi.Input[str]] = None,
                 peer_subscription_id: Optional[pulumi.Input[str]] = None,
                 peer_tenant_id: Optional[pulumi.Input[str]] = None,
                 peer_vnet_name: Optional[pulumi.Input[str]] = None,
                 peer_vnet_region: Optional[pulumi.Input[str]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AzurePeeringConnection resources.
        :param pulumi.Input[str] application_id: The ID of the Azure application whose credentials are used to peer the HCP HVN's underlying VNet with the customer VNet.
        :param pulumi.Input[str] azure_peering_id: The peering connection ID used by Azure.
        :param pulumi.Input[str] created_at: The time that the peering connection was created.
        :param pulumi.Input[str] expires_at: The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        :param pulumi.Input[str] hvn_link: The `self_link` of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the peering connection is located. Always matches the HVN's organization.
        :param pulumi.Input[str] peer_resource_group_name: The resource group name of the peer VNet in Azure.
        :param pulumi.Input[str] peer_subscription_id: The subscription ID of the peer VNet in Azure.
        :param pulumi.Input[str] peer_tenant_id: The tenant ID of the peer VNet in Azure.
        :param pulumi.Input[str] peer_vnet_name: The name of the peer VNet in Azure.
        :param pulumi.Input[str] peer_vnet_region: The region of the peer VNet in Azure.
        :param pulumi.Input[str] peering_id: The ID of the peering connection.
        :param pulumi.Input[str] project_id: The ID of the HCP project where the peering connection is located. Always matches the HVN's project.
        :param pulumi.Input[str] self_link: A unique URL identifying the peering connection.
        :param pulumi.Input[str] state: The state of the Azure peering connection.
        """
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if azure_peering_id is not None:
            pulumi.set(__self__, "azure_peering_id", azure_peering_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)
        if hvn_link is not None:
            pulumi.set(__self__, "hvn_link", hvn_link)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if peer_resource_group_name is not None:
            pulumi.set(__self__, "peer_resource_group_name", peer_resource_group_name)
        if peer_subscription_id is not None:
            pulumi.set(__self__, "peer_subscription_id", peer_subscription_id)
        if peer_tenant_id is not None:
            pulumi.set(__self__, "peer_tenant_id", peer_tenant_id)
        if peer_vnet_name is not None:
            pulumi.set(__self__, "peer_vnet_name", peer_vnet_name)
        if peer_vnet_region is not None:
            pulumi.set(__self__, "peer_vnet_region", peer_vnet_region)
        if peering_id is not None:
            pulumi.set(__self__, "peering_id", peering_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Azure application whose credentials are used to peer the HCP HVN's underlying VNet with the customer VNet.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="azurePeeringId")
    def azure_peering_id(self) -> Optional[pulumi.Input[str]]:
        """
        The peering connection ID used by Azure.
        """
        return pulumi.get(self, "azure_peering_id")

    @azure_peering_id.setter
    def azure_peering_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_peering_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time that the peering connection was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_at", value)

    @property
    @pulumi.getter(name="hvnLink")
    def hvn_link(self) -> Optional[pulumi.Input[str]]:
        """
        The `self_link` of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_link")

    @hvn_link.setter
    def hvn_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hvn_link", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP organization where the peering connection is located. Always matches the HVN's organization.
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="peerResourceGroupName")
    def peer_resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource group name of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_resource_group_name")

    @peer_resource_group_name.setter
    def peer_resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_resource_group_name", value)

    @property
    @pulumi.getter(name="peerSubscriptionId")
    def peer_subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The subscription ID of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_subscription_id")

    @peer_subscription_id.setter
    def peer_subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_subscription_id", value)

    @property
    @pulumi.getter(name="peerTenantId")
    def peer_tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The tenant ID of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_tenant_id")

    @peer_tenant_id.setter
    def peer_tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_tenant_id", value)

    @property
    @pulumi.getter(name="peerVnetName")
    def peer_vnet_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_vnet_name")

    @peer_vnet_name.setter
    def peer_vnet_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_vnet_name", value)

    @property
    @pulumi.getter(name="peerVnetRegion")
    def peer_vnet_region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_vnet_region")

    @peer_vnet_region.setter
    def peer_vnet_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_vnet_region", value)

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the peering connection.
        """
        return pulumi.get(self, "peering_id")

    @peering_id.setter
    def peering_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peering_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP project where the peering connection is located. Always matches the HVN's project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        A unique URL identifying the peering connection.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the Azure peering connection.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class AzurePeeringConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hvn_link: Optional[pulumi.Input[str]] = None,
                 peer_resource_group_name: Optional[pulumi.Input[str]] = None,
                 peer_subscription_id: Optional[pulumi.Input[str]] = None,
                 peer_tenant_id: Optional[pulumi.Input[str]] = None,
                 peer_vnet_name: Optional[pulumi.Input[str]] = None,
                 peer_vnet_region: Optional[pulumi.Input[str]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        > **Note:** This data source is currently in public beta.

        The Azure peering connection resource allows you to manage a peering connection between an HVN and a peer Azure VNet.

        ## Import

        # The import ID is {hvn_id}:{peering_id}

        ```sh
         $ pulumi import hcp:index/azurePeeringConnection:AzurePeeringConnection peer main-hvn:199e7e96-4d5f-4456-91f3-b6cc71f1e561
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hvn_link: The `self_link` of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] peer_resource_group_name: The resource group name of the peer VNet in Azure.
        :param pulumi.Input[str] peer_subscription_id: The subscription ID of the peer VNet in Azure.
        :param pulumi.Input[str] peer_tenant_id: The tenant ID of the peer VNet in Azure.
        :param pulumi.Input[str] peer_vnet_name: The name of the peer VNet in Azure.
        :param pulumi.Input[str] peer_vnet_region: The region of the peer VNet in Azure.
        :param pulumi.Input[str] peering_id: The ID of the peering connection.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AzurePeeringConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **Note:** This data source is currently in public beta.

        The Azure peering connection resource allows you to manage a peering connection between an HVN and a peer Azure VNet.

        ## Import

        # The import ID is {hvn_id}:{peering_id}

        ```sh
         $ pulumi import hcp:index/azurePeeringConnection:AzurePeeringConnection peer main-hvn:199e7e96-4d5f-4456-91f3-b6cc71f1e561
        ```

        :param str resource_name: The name of the resource.
        :param AzurePeeringConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AzurePeeringConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hvn_link: Optional[pulumi.Input[str]] = None,
                 peer_resource_group_name: Optional[pulumi.Input[str]] = None,
                 peer_subscription_id: Optional[pulumi.Input[str]] = None,
                 peer_tenant_id: Optional[pulumi.Input[str]] = None,
                 peer_vnet_name: Optional[pulumi.Input[str]] = None,
                 peer_vnet_region: Optional[pulumi.Input[str]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AzurePeeringConnectionArgs.__new__(AzurePeeringConnectionArgs)

            if hvn_link is None and not opts.urn:
                raise TypeError("Missing required property 'hvn_link'")
            __props__.__dict__["hvn_link"] = hvn_link
            if peer_resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'peer_resource_group_name'")
            __props__.__dict__["peer_resource_group_name"] = peer_resource_group_name
            if peer_subscription_id is None and not opts.urn:
                raise TypeError("Missing required property 'peer_subscription_id'")
            __props__.__dict__["peer_subscription_id"] = peer_subscription_id
            if peer_tenant_id is None and not opts.urn:
                raise TypeError("Missing required property 'peer_tenant_id'")
            __props__.__dict__["peer_tenant_id"] = peer_tenant_id
            if peer_vnet_name is None and not opts.urn:
                raise TypeError("Missing required property 'peer_vnet_name'")
            __props__.__dict__["peer_vnet_name"] = peer_vnet_name
            if peer_vnet_region is None and not opts.urn:
                raise TypeError("Missing required property 'peer_vnet_region'")
            __props__.__dict__["peer_vnet_region"] = peer_vnet_region
            if peering_id is None and not opts.urn:
                raise TypeError("Missing required property 'peering_id'")
            __props__.__dict__["peering_id"] = peering_id
            __props__.__dict__["application_id"] = None
            __props__.__dict__["azure_peering_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["expires_at"] = None
            __props__.__dict__["organization_id"] = None
            __props__.__dict__["project_id"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["state"] = None
        super(AzurePeeringConnection, __self__).__init__(
            'hcp:index/azurePeeringConnection:AzurePeeringConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_id: Optional[pulumi.Input[str]] = None,
            azure_peering_id: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            expires_at: Optional[pulumi.Input[str]] = None,
            hvn_link: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            peer_resource_group_name: Optional[pulumi.Input[str]] = None,
            peer_subscription_id: Optional[pulumi.Input[str]] = None,
            peer_tenant_id: Optional[pulumi.Input[str]] = None,
            peer_vnet_name: Optional[pulumi.Input[str]] = None,
            peer_vnet_region: Optional[pulumi.Input[str]] = None,
            peering_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'AzurePeeringConnection':
        """
        Get an existing AzurePeeringConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The ID of the Azure application whose credentials are used to peer the HCP HVN's underlying VNet with the customer VNet.
        :param pulumi.Input[str] azure_peering_id: The peering connection ID used by Azure.
        :param pulumi.Input[str] created_at: The time that the peering connection was created.
        :param pulumi.Input[str] expires_at: The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        :param pulumi.Input[str] hvn_link: The `self_link` of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the peering connection is located. Always matches the HVN's organization.
        :param pulumi.Input[str] peer_resource_group_name: The resource group name of the peer VNet in Azure.
        :param pulumi.Input[str] peer_subscription_id: The subscription ID of the peer VNet in Azure.
        :param pulumi.Input[str] peer_tenant_id: The tenant ID of the peer VNet in Azure.
        :param pulumi.Input[str] peer_vnet_name: The name of the peer VNet in Azure.
        :param pulumi.Input[str] peer_vnet_region: The region of the peer VNet in Azure.
        :param pulumi.Input[str] peering_id: The ID of the peering connection.
        :param pulumi.Input[str] project_id: The ID of the HCP project where the peering connection is located. Always matches the HVN's project.
        :param pulumi.Input[str] self_link: A unique URL identifying the peering connection.
        :param pulumi.Input[str] state: The state of the Azure peering connection.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AzurePeeringConnectionState.__new__(_AzurePeeringConnectionState)

        __props__.__dict__["application_id"] = application_id
        __props__.__dict__["azure_peering_id"] = azure_peering_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["expires_at"] = expires_at
        __props__.__dict__["hvn_link"] = hvn_link
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["peer_resource_group_name"] = peer_resource_group_name
        __props__.__dict__["peer_subscription_id"] = peer_subscription_id
        __props__.__dict__["peer_tenant_id"] = peer_tenant_id
        __props__.__dict__["peer_vnet_name"] = peer_vnet_name
        __props__.__dict__["peer_vnet_region"] = peer_vnet_region
        __props__.__dict__["peering_id"] = peering_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["self_link"] = self_link
        __props__.__dict__["state"] = state
        return AzurePeeringConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The ID of the Azure application whose credentials are used to peer the HCP HVN's underlying VNet with the customer VNet.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="azurePeeringId")
    def azure_peering_id(self) -> pulumi.Output[str]:
        """
        The peering connection ID used by Azure.
        """
        return pulumi.get(self, "azure_peering_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time that the peering connection was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[str]:
        """
        The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter(name="hvnLink")
    def hvn_link(self) -> pulumi.Output[str]:
        """
        The `self_link` of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_link")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP organization where the peering connection is located. Always matches the HVN's organization.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="peerResourceGroupName")
    def peer_resource_group_name(self) -> pulumi.Output[str]:
        """
        The resource group name of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_resource_group_name")

    @property
    @pulumi.getter(name="peerSubscriptionId")
    def peer_subscription_id(self) -> pulumi.Output[str]:
        """
        The subscription ID of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_subscription_id")

    @property
    @pulumi.getter(name="peerTenantId")
    def peer_tenant_id(self) -> pulumi.Output[str]:
        """
        The tenant ID of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_tenant_id")

    @property
    @pulumi.getter(name="peerVnetName")
    def peer_vnet_name(self) -> pulumi.Output[str]:
        """
        The name of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_vnet_name")

    @property
    @pulumi.getter(name="peerVnetRegion")
    def peer_vnet_region(self) -> pulumi.Output[str]:
        """
        The region of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_vnet_region")

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> pulumi.Output[str]:
        """
        The ID of the peering connection.
        """
        return pulumi.get(self, "peering_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP project where the peering connection is located. Always matches the HVN's project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        A unique URL identifying the peering connection.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the Azure peering connection.
        """
        return pulumi.get(self, "state")
