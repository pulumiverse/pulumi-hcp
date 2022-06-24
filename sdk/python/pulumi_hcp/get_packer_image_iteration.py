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

__all__ = [
    'GetPackerImageIterationResult',
    'AwaitableGetPackerImageIterationResult',
    'get_packer_image_iteration',
    'get_packer_image_iteration_output',
]

@pulumi.output_type
class GetPackerImageIterationResult:
    """
    A collection of values returned by getPackerImageIteration.
    """
    def __init__(__self__, bucket_name=None, builds=None, channel=None, created_at=None, id=None, incremental_version=None, organization_id=None, project_id=None, revoke_at=None):
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("Expected argument 'bucket_name' to be a str")
        pulumi.set(__self__, "bucket_name", bucket_name)
        if builds and not isinstance(builds, list):
            raise TypeError("Expected argument 'builds' to be a list")
        pulumi.set(__self__, "builds", builds)
        if channel and not isinstance(channel, str):
            raise TypeError("Expected argument 'channel' to be a str")
        pulumi.set(__self__, "channel", channel)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if incremental_version and not isinstance(incremental_version, int):
            raise TypeError("Expected argument 'incremental_version' to be a int")
        pulumi.set(__self__, "incremental_version", incremental_version)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if revoke_at and not isinstance(revoke_at, str):
            raise TypeError("Expected argument 'revoke_at' to be a str")
        pulumi.set(__self__, "revoke_at", revoke_at)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        """
        The slug of the HCP Packer Registry image bucket to pull from.
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter
    def builds(self) -> Sequence['outputs.GetPackerImageIterationBuildResult']:
        """
        Builds for this iteration. An iteration can have more than one build if it took more than one go to build all images.
        """
        return pulumi.get(self, "builds")

    @property
    @pulumi.getter
    def channel(self) -> str:
        """
        The channel that points to the version of the image you want.
        """
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Creation time of this iteration
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="incrementalVersion")
    def incremental_version(self) -> int:
        """
        Incremental version of this iteration
        """
        return pulumi.get(self, "incremental_version")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The ID of the organization this HCP Packer registry is located in.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The ID of the project this HCP Packer registry is located in.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="revokeAt")
    def revoke_at(self) -> str:
        return pulumi.get(self, "revoke_at")


class AwaitableGetPackerImageIterationResult(GetPackerImageIterationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPackerImageIterationResult(
            bucket_name=self.bucket_name,
            builds=self.builds,
            channel=self.channel,
            created_at=self.created_at,
            id=self.id,
            incremental_version=self.incremental_version,
            organization_id=self.organization_id,
            project_id=self.project_id,
            revoke_at=self.revoke_at)


def get_packer_image_iteration(bucket_name: Optional[str] = None,
                               channel: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPackerImageIterationResult:
    """
    The Packer Image data source iteration gets the most recent iteration (or build) of an image, given a channel.


    :param str bucket_name: The slug of the HCP Packer Registry image bucket to pull from.
    :param str channel: The channel that points to the version of the image you want.
    """
    __args__ = dict()
    __args__['bucketName'] = bucket_name
    __args__['channel'] = channel
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('hcp:index/getPackerImageIteration:getPackerImageIteration', __args__, opts=opts, typ=GetPackerImageIterationResult).value

    return AwaitableGetPackerImageIterationResult(
        bucket_name=__ret__.bucket_name,
        builds=__ret__.builds,
        channel=__ret__.channel,
        created_at=__ret__.created_at,
        id=__ret__.id,
        incremental_version=__ret__.incremental_version,
        organization_id=__ret__.organization_id,
        project_id=__ret__.project_id,
        revoke_at=__ret__.revoke_at)


@_utilities.lift_output_func(get_packer_image_iteration)
def get_packer_image_iteration_output(bucket_name: Optional[pulumi.Input[str]] = None,
                                      channel: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPackerImageIterationResult]:
    """
    The Packer Image data source iteration gets the most recent iteration (or build) of an image, given a channel.


    :param str bucket_name: The slug of the HCP Packer Registry image bucket to pull from.
    :param str channel: The channel that points to the version of the image you want.
    """
    ...
