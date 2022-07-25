# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['HvnArgs', 'Hvn']

@pulumi.input_type
class HvnArgs:
    def __init__(__self__, *,
                 cloud_provider: pulumi.Input[str],
                 hvn_id: pulumi.Input[str],
                 region: pulumi.Input[str],
                 cidr_block: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Hvn resource.
        :param pulumi.Input[str] cloud_provider: The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] region: The region where the HVN is located.
        :param pulumi.Input[str] cidr_block: The CIDR range of the HVN. If this is not provided, the service will provide a default value.
        """
        pulumi.set(__self__, "cloud_provider", cloud_provider)
        pulumi.set(__self__, "hvn_id", hvn_id)
        pulumi.set(__self__, "region", region)
        if cidr_block is not None:
            pulumi.set(__self__, "cidr_block", cidr_block)

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> pulumi.Input[str]:
        """
        The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
        """
        return pulumi.get(self, "cloud_provider")

    @cloud_provider.setter
    def cloud_provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "cloud_provider", value)

    @property
    @pulumi.getter(name="hvnId")
    def hvn_id(self) -> pulumi.Input[str]:
        """
        The ID of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_id")

    @hvn_id.setter
    def hvn_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hvn_id", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        The region where the HVN is located.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[str]]:
        """
        The CIDR range of the HVN. If this is not provided, the service will provide a default value.
        """
        return pulumi.get(self, "cidr_block")

    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_block", value)


@pulumi.input_type
class _HvnState:
    def __init__(__self__, *,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 hvn_id: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 provider_account_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Hvn resources.
        :param pulumi.Input[str] cidr_block: The CIDR range of the HVN. If this is not provided, the service will provide a default value.
        :param pulumi.Input[str] cloud_provider: The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
        :param pulumi.Input[str] created_at: The time that the HVN was created.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the HVN is located.
        :param pulumi.Input[str] project_id: The ID of the HCP project where the HVN is located.
        :param pulumi.Input[str] provider_account_id: The provider account ID where the HVN is located.
        :param pulumi.Input[str] region: The region where the HVN is located.
        :param pulumi.Input[str] self_link: A unique URL identifying the HVN.
        :param pulumi.Input[str] state: The state of the HVN.
        """
        if cidr_block is not None:
            pulumi.set(__self__, "cidr_block", cidr_block)
        if cloud_provider is not None:
            pulumi.set(__self__, "cloud_provider", cloud_provider)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if hvn_id is not None:
            pulumi.set(__self__, "hvn_id", hvn_id)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if provider_account_id is not None:
            pulumi.set(__self__, "provider_account_id", provider_account_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[str]]:
        """
        The CIDR range of the HVN. If this is not provided, the service will provide a default value.
        """
        return pulumi.get(self, "cidr_block")

    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_block", value)

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> Optional[pulumi.Input[str]]:
        """
        The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
        """
        return pulumi.get(self, "cloud_provider")

    @cloud_provider.setter
    def cloud_provider(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_provider", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time that the HVN was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="hvnId")
    def hvn_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_id")

    @hvn_id.setter
    def hvn_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hvn_id", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP organization where the HVN is located.
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP project where the HVN is located.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="providerAccountId")
    def provider_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The provider account ID where the HVN is located.
        """
        return pulumi.get(self, "provider_account_id")

    @provider_account_id.setter
    def provider_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_account_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region where the HVN is located.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        A unique URL identifying the HVN.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the HVN.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class Hvn(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 hvn_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The HVN resource allows you to manage a HashiCorp Virtual Network in HCP.

        We recommend the following when selecting the CIDR block of an HVN:

        - The CIDR block value must be a private IPv4 CIDR block within the [RFC1918](https://datatracker.ietf.org/doc/html/rfc1918) address space (10.*.*.*, 192.168.*.*, 172.[16-31].*.*).

        - The CIDR block value must be the first IP address of the desired CIDR block. The helper `cidrsubnet("172.16.1.1/24", 0, 0)` will specify the first address of the CIDR block in the first argument.

        - The CIDR block value must end between /16 and /25.

        - If the CIDR block values for your HCP HVN and your cloud provider’s virtual network overlap you will not be able to establish a connection. The following are default CIDR block values to be aware of: HCP HVN (172.25.16.0/20), AWS VPC (172.31.0.0/16), and Azure VNet (172.29.0.0/24). Avoid creating overlapping networks.

        - If you’re creating a HVN for use in production it's recommended that you specify a CIDR block value that does not overlap with the other HVNs already created in your organization. You will not be able to connect two HVNs with overlapping CIDR block values.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcp as hcp

        example = hcp.Hvn("example",
            cidr_block="172.25.16.0/20",
            cloud_provider="aws",
            hvn_id="main-hvn",
            region="us-west-2")
        ```

        ## Import

        # The import ID is {hvn_id}

        ```sh
         $ pulumi import hcp:index/hvn:Hvn example main-hvn
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr_block: The CIDR range of the HVN. If this is not provided, the service will provide a default value.
        :param pulumi.Input[str] cloud_provider: The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] region: The region where the HVN is located.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HvnArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The HVN resource allows you to manage a HashiCorp Virtual Network in HCP.

        We recommend the following when selecting the CIDR block of an HVN:

        - The CIDR block value must be a private IPv4 CIDR block within the [RFC1918](https://datatracker.ietf.org/doc/html/rfc1918) address space (10.*.*.*, 192.168.*.*, 172.[16-31].*.*).

        - The CIDR block value must be the first IP address of the desired CIDR block. The helper `cidrsubnet("172.16.1.1/24", 0, 0)` will specify the first address of the CIDR block in the first argument.

        - The CIDR block value must end between /16 and /25.

        - If the CIDR block values for your HCP HVN and your cloud provider’s virtual network overlap you will not be able to establish a connection. The following are default CIDR block values to be aware of: HCP HVN (172.25.16.0/20), AWS VPC (172.31.0.0/16), and Azure VNet (172.29.0.0/24). Avoid creating overlapping networks.

        - If you’re creating a HVN for use in production it's recommended that you specify a CIDR block value that does not overlap with the other HVNs already created in your organization. You will not be able to connect two HVNs with overlapping CIDR block values.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcp as hcp

        example = hcp.Hvn("example",
            cidr_block="172.25.16.0/20",
            cloud_provider="aws",
            hvn_id="main-hvn",
            region="us-west-2")
        ```

        ## Import

        # The import ID is {hvn_id}

        ```sh
         $ pulumi import hcp:index/hvn:Hvn example main-hvn
        ```

        :param str resource_name: The name of the resource.
        :param HvnArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HvnArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 hvn_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HvnArgs.__new__(HvnArgs)

            __props__.__dict__["cidr_block"] = cidr_block
            if cloud_provider is None and not opts.urn:
                raise TypeError("Missing required property 'cloud_provider'")
            __props__.__dict__["cloud_provider"] = cloud_provider
            if hvn_id is None and not opts.urn:
                raise TypeError("Missing required property 'hvn_id'")
            __props__.__dict__["hvn_id"] = hvn_id
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["created_at"] = None
            __props__.__dict__["organization_id"] = None
            __props__.__dict__["project_id"] = None
            __props__.__dict__["provider_account_id"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["state"] = None
        super(Hvn, __self__).__init__(
            'hcp:index/hvn:Hvn',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cidr_block: Optional[pulumi.Input[str]] = None,
            cloud_provider: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            hvn_id: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            provider_account_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'Hvn':
        """
        Get an existing Hvn resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr_block: The CIDR range of the HVN. If this is not provided, the service will provide a default value.
        :param pulumi.Input[str] cloud_provider: The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
        :param pulumi.Input[str] created_at: The time that the HVN was created.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the HVN is located.
        :param pulumi.Input[str] project_id: The ID of the HCP project where the HVN is located.
        :param pulumi.Input[str] provider_account_id: The provider account ID where the HVN is located.
        :param pulumi.Input[str] region: The region where the HVN is located.
        :param pulumi.Input[str] self_link: A unique URL identifying the HVN.
        :param pulumi.Input[str] state: The state of the HVN.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HvnState.__new__(_HvnState)

        __props__.__dict__["cidr_block"] = cidr_block
        __props__.__dict__["cloud_provider"] = cloud_provider
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["hvn_id"] = hvn_id
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["provider_account_id"] = provider_account_id
        __props__.__dict__["region"] = region
        __props__.__dict__["self_link"] = self_link
        __props__.__dict__["state"] = state
        return Hvn(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[str]:
        """
        The CIDR range of the HVN. If this is not provided, the service will provide a default value.
        """
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> pulumi.Output[str]:
        """
        The provider where the HVN is located. The provider 'aws' is generally available and 'azure' is in public beta.
        """
        return pulumi.get(self, "cloud_provider")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time that the HVN was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="hvnId")
    def hvn_id(self) -> pulumi.Output[str]:
        """
        The ID of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_id")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP organization where the HVN is located.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP project where the HVN is located.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="providerAccountId")
    def provider_account_id(self) -> pulumi.Output[str]:
        """
        The provider account ID where the HVN is located.
        """
        return pulumi.get(self, "provider_account_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region where the HVN is located.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        A unique URL identifying the HVN.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the HVN.
        """
        return pulumi.get(self, "state")

