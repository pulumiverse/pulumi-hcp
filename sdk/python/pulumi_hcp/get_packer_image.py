# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetPackerImageResult',
    'AwaitableGetPackerImageResult',
    'get_packer_image',
    'get_packer_image_output',
]

@pulumi.output_type
class GetPackerImageResult:
    """
    A collection of values returned by getPackerImage.
    """
    def __init__(__self__, bucket_name=None, build_id=None, channel=None, cloud_image_id=None, cloud_provider=None, component_type=None, created_at=None, id=None, iteration_id=None, labels=None, organization_id=None, packer_run_uuid=None, project_id=None, region=None, revoke_at=None):
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("Expected argument 'bucket_name' to be a str")
        pulumi.set(__self__, "bucket_name", bucket_name)
        if build_id and not isinstance(build_id, str):
            raise TypeError("Expected argument 'build_id' to be a str")
        pulumi.set(__self__, "build_id", build_id)
        if channel and not isinstance(channel, str):
            raise TypeError("Expected argument 'channel' to be a str")
        pulumi.set(__self__, "channel", channel)
        if cloud_image_id and not isinstance(cloud_image_id, str):
            raise TypeError("Expected argument 'cloud_image_id' to be a str")
        pulumi.set(__self__, "cloud_image_id", cloud_image_id)
        if cloud_provider and not isinstance(cloud_provider, str):
            raise TypeError("Expected argument 'cloud_provider' to be a str")
        pulumi.set(__self__, "cloud_provider", cloud_provider)
        if component_type and not isinstance(component_type, str):
            raise TypeError("Expected argument 'component_type' to be a str")
        pulumi.set(__self__, "component_type", component_type)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if iteration_id and not isinstance(iteration_id, str):
            raise TypeError("Expected argument 'iteration_id' to be a str")
        pulumi.set(__self__, "iteration_id", iteration_id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if packer_run_uuid and not isinstance(packer_run_uuid, str):
            raise TypeError("Expected argument 'packer_run_uuid' to be a str")
        pulumi.set(__self__, "packer_run_uuid", packer_run_uuid)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
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
    @pulumi.getter(name="buildId")
    def build_id(self) -> str:
        """
        HCP ID of this build.
        """
        return pulumi.get(self, "build_id")

    @property
    @pulumi.getter
    def channel(self) -> Optional[str]:
        """
        The channel that points to the version of the image being retrieved. Either this or `iteration_id` must be specified. Note: will incur a billable request
        """
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter(name="cloudImageId")
    def cloud_image_id(self) -> str:
        """
        Cloud Image ID or URL string identifying this image for the builder that built it.
        """
        return pulumi.get(self, "cloud_image_id")

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> str:
        """
        Name of the cloud provider this image is stored-in.
        """
        return pulumi.get(self, "cloud_provider")

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> str:
        """
        Name of the builder that built this image. Ex: `amazon-ebs.example`.
        """
        return pulumi.get(self, "component_type")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Creation time of this build.
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
    @pulumi.getter(name="iterationId")
    def iteration_id(self) -> str:
        """
        The iteration from which to get the image. Either this or `channel` must be specified.
        """
        return pulumi.get(self, "iteration_id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, Any]:
        """
        Labels associated with this build.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The ID of the organization this HCP Packer registry is located in.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="packerRunUuid")
    def packer_run_uuid(self) -> str:
        """
        UUID of this build.
        """
        return pulumi.get(self, "packer_run_uuid")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The ID of the project this HCP Packer registry is located in.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        Region this image is stored in, if any.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="revokeAt")
    def revoke_at(self) -> str:
        """
        The revocation time of this build. This field will be null for any build that has not been revoked or scheduled for revocation.
        """
        return pulumi.get(self, "revoke_at")


class AwaitableGetPackerImageResult(GetPackerImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPackerImageResult(
            bucket_name=self.bucket_name,
            build_id=self.build_id,
            channel=self.channel,
            cloud_image_id=self.cloud_image_id,
            cloud_provider=self.cloud_provider,
            component_type=self.component_type,
            created_at=self.created_at,
            id=self.id,
            iteration_id=self.iteration_id,
            labels=self.labels,
            organization_id=self.organization_id,
            packer_run_uuid=self.packer_run_uuid,
            project_id=self.project_id,
            region=self.region,
            revoke_at=self.revoke_at)


def get_packer_image(bucket_name: Optional[str] = None,
                     channel: Optional[str] = None,
                     cloud_provider: Optional[str] = None,
                     component_type: Optional[str] = None,
                     iteration_id: Optional[str] = None,
                     region: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPackerImageResult:
    """
    The Packer Image data source iteration gets the most recent iteration (or build) of an image, given an iteration id or a channel.

    ## Example Usage
    ### Single image sourcing

    ```python
    import pulumi
    import pulumi_hcp as hcp

    baz = hcp.get_packer_image(bucket_name="hardened-ubuntu-16-04",
        cloud_provider="aws",
        channel="production",
        region="us-east-1")
    pulumi.export("packer-registry-ubuntu-east-1", baz.cloud_image_id)
    ```

    > **Note:** The `channel` attribute in this data source may incur a billable request to HCP Packer. This attribute is intended for convenience when using a single image. When sourcing multiple images from a single iteration, the `get_packer_iteration` data source is the alternative for querying a channel just once.
    ### Multiple image sourcing from a single iteration

    ```python
    import pulumi
    import pulumi_hcp as hcp

    hardened_source = hcp.get_packer_iteration(bucket_name="hardened-ubuntu-16-04",
        channel="production")
    foo = hcp.get_packer_image(bucket_name="hardened-ubuntu-16-04",
        cloud_provider="aws",
        iteration_id=hardened_source.ulid,
        region="us-east-1")
    bar = hcp.get_packer_image(bucket_name="hardened-ubuntu-16-04",
        cloud_provider="aws",
        iteration_id=hardened_source.ulid,
        region="us-west-1")
    pulumi.export("packer-registry-ubuntu-east-1", foo.cloud_image_id)
    pulumi.export("packer-registry-ubuntu-west-1", bar.cloud_image_id)
    ```

    > **Note:** This data source only returns the first found image's metadata filtered by the given arguments, from the returned list of images associated with the specified iteration. Therefore, if multiple images exist in the same region, it will only pick one of them. In this case, you can filter images by a source build name (Ex: `amazon-ebs.example`) using the `component_type` optional argument.


    :param str bucket_name: The slug of the HCP Packer Registry image bucket to pull from.
    :param str channel: The channel that points to the version of the image being retrieved. Either this or `iteration_id` must be specified. Note: will incur a billable request
    :param str cloud_provider: Name of the cloud provider this image is stored-in.
    :param str component_type: Name of the builder that built this image. Ex: `amazon-ebs.example`.
    :param str iteration_id: The iteration from which to get the image. Either this or `channel` must be specified.
    :param str region: Region this image is stored in, if any.
    """
    __args__ = dict()
    __args__['bucketName'] = bucket_name
    __args__['channel'] = channel
    __args__['cloudProvider'] = cloud_provider
    __args__['componentType'] = component_type
    __args__['iterationId'] = iteration_id
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('hcp:index/getPackerImage:getPackerImage', __args__, opts=opts, typ=GetPackerImageResult).value

    return AwaitableGetPackerImageResult(
        bucket_name=__ret__.bucket_name,
        build_id=__ret__.build_id,
        channel=__ret__.channel,
        cloud_image_id=__ret__.cloud_image_id,
        cloud_provider=__ret__.cloud_provider,
        component_type=__ret__.component_type,
        created_at=__ret__.created_at,
        id=__ret__.id,
        iteration_id=__ret__.iteration_id,
        labels=__ret__.labels,
        organization_id=__ret__.organization_id,
        packer_run_uuid=__ret__.packer_run_uuid,
        project_id=__ret__.project_id,
        region=__ret__.region,
        revoke_at=__ret__.revoke_at)


@_utilities.lift_output_func(get_packer_image)
def get_packer_image_output(bucket_name: Optional[pulumi.Input[str]] = None,
                            channel: Optional[pulumi.Input[Optional[str]]] = None,
                            cloud_provider: Optional[pulumi.Input[str]] = None,
                            component_type: Optional[pulumi.Input[Optional[str]]] = None,
                            iteration_id: Optional[pulumi.Input[Optional[str]]] = None,
                            region: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPackerImageResult]:
    """
    The Packer Image data source iteration gets the most recent iteration (or build) of an image, given an iteration id or a channel.

    ## Example Usage
    ### Single image sourcing

    ```python
    import pulumi
    import pulumi_hcp as hcp

    baz = hcp.get_packer_image(bucket_name="hardened-ubuntu-16-04",
        cloud_provider="aws",
        channel="production",
        region="us-east-1")
    pulumi.export("packer-registry-ubuntu-east-1", baz.cloud_image_id)
    ```

    > **Note:** The `channel` attribute in this data source may incur a billable request to HCP Packer. This attribute is intended for convenience when using a single image. When sourcing multiple images from a single iteration, the `get_packer_iteration` data source is the alternative for querying a channel just once.
    ### Multiple image sourcing from a single iteration

    ```python
    import pulumi
    import pulumi_hcp as hcp

    hardened_source = hcp.get_packer_iteration(bucket_name="hardened-ubuntu-16-04",
        channel="production")
    foo = hcp.get_packer_image(bucket_name="hardened-ubuntu-16-04",
        cloud_provider="aws",
        iteration_id=hardened_source.ulid,
        region="us-east-1")
    bar = hcp.get_packer_image(bucket_name="hardened-ubuntu-16-04",
        cloud_provider="aws",
        iteration_id=hardened_source.ulid,
        region="us-west-1")
    pulumi.export("packer-registry-ubuntu-east-1", foo.cloud_image_id)
    pulumi.export("packer-registry-ubuntu-west-1", bar.cloud_image_id)
    ```

    > **Note:** This data source only returns the first found image's metadata filtered by the given arguments, from the returned list of images associated with the specified iteration. Therefore, if multiple images exist in the same region, it will only pick one of them. In this case, you can filter images by a source build name (Ex: `amazon-ebs.example`) using the `component_type` optional argument.


    :param str bucket_name: The slug of the HCP Packer Registry image bucket to pull from.
    :param str channel: The channel that points to the version of the image being retrieved. Either this or `iteration_id` must be specified. Note: will incur a billable request
    :param str cloud_provider: Name of the cloud provider this image is stored-in.
    :param str component_type: Name of the builder that built this image. Ex: `amazon-ebs.example`.
    :param str iteration_id: The iteration from which to get the image. Either this or `channel` must be specified.
    :param str region: Region this image is stored in, if any.
    """
    ...
