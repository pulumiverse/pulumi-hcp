# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AwsTransitGatewayAttachmentArgs', 'AwsTransitGatewayAttachment']

@pulumi.input_type
class AwsTransitGatewayAttachmentArgs:
    def __init__(__self__, *,
                 hvn_id: pulumi.Input[str],
                 resource_share_arn: pulumi.Input[str],
                 transit_gateway_attachment_id: pulumi.Input[str],
                 transit_gateway_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a AwsTransitGatewayAttachment resource.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] resource_share_arn: The Amazon Resource Name (ARN) of the Resource Share that is needed to grant HCP access to the transit gateway in AWS.
               The Resource Share should be associated with the HCP AWS account principal (see
               [aws_ram_principal_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_principal_association))
               and the transit gateway resource (see
               [aws_ram_resource_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_resource_association))
        :param pulumi.Input[str] transit_gateway_attachment_id: The user-settable name of the transit gateway attachment in HCP.
        :param pulumi.Input[str] transit_gateway_id: The ID of the user-owned transit gateway in AWS. The AWS region of the transit gateway must match the HVN.
        """
        pulumi.set(__self__, "hvn_id", hvn_id)
        pulumi.set(__self__, "resource_share_arn", resource_share_arn)
        pulumi.set(__self__, "transit_gateway_attachment_id", transit_gateway_attachment_id)
        pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)

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
    @pulumi.getter(name="resourceShareArn")
    def resource_share_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the Resource Share that is needed to grant HCP access to the transit gateway in AWS.
        The Resource Share should be associated with the HCP AWS account principal (see
        [aws_ram_principal_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_principal_association))
        and the transit gateway resource (see
        [aws_ram_resource_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_resource_association))
        """
        return pulumi.get(self, "resource_share_arn")

    @resource_share_arn.setter
    def resource_share_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_share_arn", value)

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Input[str]:
        """
        The user-settable name of the transit gateway attachment in HCP.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "transit_gateway_attachment_id", value)

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Input[str]:
        """
        The ID of the user-owned transit gateway in AWS. The AWS region of the transit gateway must match the HVN.
        """
        return pulumi.get(self, "transit_gateway_id")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "transit_gateway_id", value)


@pulumi.input_type
class _AwsTransitGatewayAttachmentState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 hvn_id: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 provider_transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                 resource_share_arn: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AwsTransitGatewayAttachment resources.
        :param pulumi.Input[str] created_at: The time that the transit gateway attachment was created.
        :param pulumi.Input[str] expires_at: The time after which the transit gateway attachment will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the transit gateway attachment is located. Always matches the HVN's organization.
        :param pulumi.Input[str] project_id: The ID of the HCP project where the transit gateway attachment is located. Always matches the HVN's project.
        :param pulumi.Input[str] provider_transit_gateway_attachment_id: The transit gateway attachment ID used by AWS.
        :param pulumi.Input[str] resource_share_arn: The Amazon Resource Name (ARN) of the Resource Share that is needed to grant HCP access to the transit gateway in AWS.
               The Resource Share should be associated with the HCP AWS account principal (see
               [aws_ram_principal_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_principal_association))
               and the transit gateway resource (see
               [aws_ram_resource_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_resource_association))
        :param pulumi.Input[str] self_link: A unique URL identifying the transit gateway attachment.
        :param pulumi.Input[str] state: The state of the transit gateway attachment.
        :param pulumi.Input[str] transit_gateway_attachment_id: The user-settable name of the transit gateway attachment in HCP.
        :param pulumi.Input[str] transit_gateway_id: The ID of the user-owned transit gateway in AWS. The AWS region of the transit gateway must match the HVN.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)
        if hvn_id is not None:
            pulumi.set(__self__, "hvn_id", hvn_id)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if provider_transit_gateway_attachment_id is not None:
            pulumi.set(__self__, "provider_transit_gateway_attachment_id", provider_transit_gateway_attachment_id)
        if resource_share_arn is not None:
            pulumi.set(__self__, "resource_share_arn", resource_share_arn)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if transit_gateway_attachment_id is not None:
            pulumi.set(__self__, "transit_gateway_attachment_id", transit_gateway_attachment_id)
        if transit_gateway_id is not None:
            pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time that the transit gateway attachment was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time after which the transit gateway attachment will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_at", value)

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
        The ID of the HCP organization where the transit gateway attachment is located. Always matches the HVN's organization.
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP project where the transit gateway attachment is located. Always matches the HVN's project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="providerTransitGatewayAttachmentId")
    def provider_transit_gateway_attachment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The transit gateway attachment ID used by AWS.
        """
        return pulumi.get(self, "provider_transit_gateway_attachment_id")

    @provider_transit_gateway_attachment_id.setter
    def provider_transit_gateway_attachment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_transit_gateway_attachment_id", value)

    @property
    @pulumi.getter(name="resourceShareArn")
    def resource_share_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the Resource Share that is needed to grant HCP access to the transit gateway in AWS.
        The Resource Share should be associated with the HCP AWS account principal (see
        [aws_ram_principal_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_principal_association))
        and the transit gateway resource (see
        [aws_ram_resource_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_resource_association))
        """
        return pulumi.get(self, "resource_share_arn")

    @resource_share_arn.setter
    def resource_share_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_share_arn", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        A unique URL identifying the transit gateway attachment.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the transit gateway attachment.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The user-settable name of the transit gateway attachment in HCP.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_gateway_attachment_id", value)

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the user-owned transit gateway in AWS. The AWS region of the transit gateway must match the HVN.
        """
        return pulumi.get(self, "transit_gateway_id")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_gateway_id", value)


class AwsTransitGatewayAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hvn_id: Optional[pulumi.Input[str]] = None,
                 resource_share_arn: Optional[pulumi.Input[str]] = None,
                 transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_hcp as hcp

        main = hcp.Hvn("main",
            hvn_id="main-hvn",
            cloud_provider="aws",
            region="us-west-2",
            cidr_block="172.25.16.0/20")
        example_vpc = aws.ec2.Vpc("exampleVpc", cidr_block="172.31.0.0/16")
        example_transit_gateway = aws.ec2transitgateway.TransitGateway("exampleTransitGateway", tags={
            "Name": "example-tgw",
        })
        example_resource_share = aws.ram.ResourceShare("exampleResourceShare", allow_external_principals=True)
        example_principal_association = aws.ram.PrincipalAssociation("examplePrincipalAssociation",
            resource_share_arn=example_resource_share.arn,
            principal=main.provider_account_id)
        example_resource_association = aws.ram.ResourceAssociation("exampleResourceAssociation",
            resource_share_arn=example_resource_share.arn,
            resource_arn=example_transit_gateway.arn)
        example_aws_transit_gateway_attachment = hcp.AwsTransitGatewayAttachment("exampleAwsTransitGatewayAttachment",
            hvn_id=main.hvn_id,
            transit_gateway_attachment_id="example-tgw-attachment",
            transit_gateway_id=example_transit_gateway.id,
            resource_share_arn=example_resource_share.arn,
            opts=pulumi.ResourceOptions(depends_on=[
                    example_principal_association,
                    example_resource_association,
                ]))
        route = hcp.HvnRoute("route",
            hvn_link=main.self_link,
            hvn_route_id="hvn-to-tgw-attachment",
            destination_cidr=example_vpc.cidr_block,
            target_link=example_aws_transit_gateway_attachment.self_link)
        example_vpc_attachment_accepter = aws.ec2transitgateway.VpcAttachmentAccepter("exampleVpcAttachmentAccepter", transit_gateway_attachment_id=example_aws_transit_gateway_attachment.provider_transit_gateway_attachment_id)
        ```

        ## Import

        # The import ID is {hvn_id}:{transit_gateway_attachment_id}

        ```sh
         $ pulumi import hcp:index/awsTransitGatewayAttachment:AwsTransitGatewayAttachment example main-hvn:example-tgw-attachment
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] resource_share_arn: The Amazon Resource Name (ARN) of the Resource Share that is needed to grant HCP access to the transit gateway in AWS.
               The Resource Share should be associated with the HCP AWS account principal (see
               [aws_ram_principal_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_principal_association))
               and the transit gateway resource (see
               [aws_ram_resource_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_resource_association))
        :param pulumi.Input[str] transit_gateway_attachment_id: The user-settable name of the transit gateway attachment in HCP.
        :param pulumi.Input[str] transit_gateway_id: The ID of the user-owned transit gateway in AWS. The AWS region of the transit gateway must match the HVN.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AwsTransitGatewayAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_hcp as hcp

        main = hcp.Hvn("main",
            hvn_id="main-hvn",
            cloud_provider="aws",
            region="us-west-2",
            cidr_block="172.25.16.0/20")
        example_vpc = aws.ec2.Vpc("exampleVpc", cidr_block="172.31.0.0/16")
        example_transit_gateway = aws.ec2transitgateway.TransitGateway("exampleTransitGateway", tags={
            "Name": "example-tgw",
        })
        example_resource_share = aws.ram.ResourceShare("exampleResourceShare", allow_external_principals=True)
        example_principal_association = aws.ram.PrincipalAssociation("examplePrincipalAssociation",
            resource_share_arn=example_resource_share.arn,
            principal=main.provider_account_id)
        example_resource_association = aws.ram.ResourceAssociation("exampleResourceAssociation",
            resource_share_arn=example_resource_share.arn,
            resource_arn=example_transit_gateway.arn)
        example_aws_transit_gateway_attachment = hcp.AwsTransitGatewayAttachment("exampleAwsTransitGatewayAttachment",
            hvn_id=main.hvn_id,
            transit_gateway_attachment_id="example-tgw-attachment",
            transit_gateway_id=example_transit_gateway.id,
            resource_share_arn=example_resource_share.arn,
            opts=pulumi.ResourceOptions(depends_on=[
                    example_principal_association,
                    example_resource_association,
                ]))
        route = hcp.HvnRoute("route",
            hvn_link=main.self_link,
            hvn_route_id="hvn-to-tgw-attachment",
            destination_cidr=example_vpc.cidr_block,
            target_link=example_aws_transit_gateway_attachment.self_link)
        example_vpc_attachment_accepter = aws.ec2transitgateway.VpcAttachmentAccepter("exampleVpcAttachmentAccepter", transit_gateway_attachment_id=example_aws_transit_gateway_attachment.provider_transit_gateway_attachment_id)
        ```

        ## Import

        # The import ID is {hvn_id}:{transit_gateway_attachment_id}

        ```sh
         $ pulumi import hcp:index/awsTransitGatewayAttachment:AwsTransitGatewayAttachment example main-hvn:example-tgw-attachment
        ```

        :param str resource_name: The name of the resource.
        :param AwsTransitGatewayAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AwsTransitGatewayAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hvn_id: Optional[pulumi.Input[str]] = None,
                 resource_share_arn: Optional[pulumi.Input[str]] = None,
                 transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AwsTransitGatewayAttachmentArgs.__new__(AwsTransitGatewayAttachmentArgs)

            if hvn_id is None and not opts.urn:
                raise TypeError("Missing required property 'hvn_id'")
            __props__.__dict__["hvn_id"] = hvn_id
            if resource_share_arn is None and not opts.urn:
                raise TypeError("Missing required property 'resource_share_arn'")
            __props__.__dict__["resource_share_arn"] = resource_share_arn
            if transit_gateway_attachment_id is None and not opts.urn:
                raise TypeError("Missing required property 'transit_gateway_attachment_id'")
            __props__.__dict__["transit_gateway_attachment_id"] = transit_gateway_attachment_id
            if transit_gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'transit_gateway_id'")
            __props__.__dict__["transit_gateway_id"] = transit_gateway_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["expires_at"] = None
            __props__.__dict__["organization_id"] = None
            __props__.__dict__["project_id"] = None
            __props__.__dict__["provider_transit_gateway_attachment_id"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["state"] = None
        super(AwsTransitGatewayAttachment, __self__).__init__(
            'hcp:index/awsTransitGatewayAttachment:AwsTransitGatewayAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            expires_at: Optional[pulumi.Input[str]] = None,
            hvn_id: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            provider_transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
            resource_share_arn: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
            transit_gateway_id: Optional[pulumi.Input[str]] = None) -> 'AwsTransitGatewayAttachment':
        """
        Get an existing AwsTransitGatewayAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: The time that the transit gateway attachment was created.
        :param pulumi.Input[str] expires_at: The time after which the transit gateway attachment will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        :param pulumi.Input[str] hvn_id: The ID of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the transit gateway attachment is located. Always matches the HVN's organization.
        :param pulumi.Input[str] project_id: The ID of the HCP project where the transit gateway attachment is located. Always matches the HVN's project.
        :param pulumi.Input[str] provider_transit_gateway_attachment_id: The transit gateway attachment ID used by AWS.
        :param pulumi.Input[str] resource_share_arn: The Amazon Resource Name (ARN) of the Resource Share that is needed to grant HCP access to the transit gateway in AWS.
               The Resource Share should be associated with the HCP AWS account principal (see
               [aws_ram_principal_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_principal_association))
               and the transit gateway resource (see
               [aws_ram_resource_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_resource_association))
        :param pulumi.Input[str] self_link: A unique URL identifying the transit gateway attachment.
        :param pulumi.Input[str] state: The state of the transit gateway attachment.
        :param pulumi.Input[str] transit_gateway_attachment_id: The user-settable name of the transit gateway attachment in HCP.
        :param pulumi.Input[str] transit_gateway_id: The ID of the user-owned transit gateway in AWS. The AWS region of the transit gateway must match the HVN.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AwsTransitGatewayAttachmentState.__new__(_AwsTransitGatewayAttachmentState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["expires_at"] = expires_at
        __props__.__dict__["hvn_id"] = hvn_id
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["provider_transit_gateway_attachment_id"] = provider_transit_gateway_attachment_id
        __props__.__dict__["resource_share_arn"] = resource_share_arn
        __props__.__dict__["self_link"] = self_link
        __props__.__dict__["state"] = state
        __props__.__dict__["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        __props__.__dict__["transit_gateway_id"] = transit_gateway_id
        return AwsTransitGatewayAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time that the transit gateway attachment was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[str]:
        """
        The time after which the transit gateway attachment will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

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
        The ID of the HCP organization where the transit gateway attachment is located. Always matches the HVN's organization.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP project where the transit gateway attachment is located. Always matches the HVN's project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="providerTransitGatewayAttachmentId")
    def provider_transit_gateway_attachment_id(self) -> pulumi.Output[str]:
        """
        The transit gateway attachment ID used by AWS.
        """
        return pulumi.get(self, "provider_transit_gateway_attachment_id")

    @property
    @pulumi.getter(name="resourceShareArn")
    def resource_share_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Resource Share that is needed to grant HCP access to the transit gateway in AWS.
        The Resource Share should be associated with the HCP AWS account principal (see
        [aws_ram_principal_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_principal_association))
        and the transit gateway resource (see
        [aws_ram_resource_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_resource_association))
        """
        return pulumi.get(self, "resource_share_arn")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        A unique URL identifying the transit gateway attachment.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the transit gateway attachment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[str]:
        """
        The user-settable name of the transit gateway attachment in HCP.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[str]:
        """
        The ID of the user-owned transit gateway in AWS. The AWS region of the transit gateway must match the HVN.
        """
        return pulumi.get(self, "transit_gateway_id")

