# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['BoundaryClusterArgs', 'BoundaryCluster']

@pulumi.input_type
class BoundaryClusterArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        The set of arguments for constructing a BoundaryCluster resource.
        :param pulumi.Input[str] cluster_id: The ID of the Boundary cluster
        :param pulumi.Input[str] password: The password of the initial admin user. This must be at least 8 characters in length. Note that this may show up in logs, and it will be stored in the state file.
        :param pulumi.Input[str] username: The username of the initial admin user. This must be at least 3 characters in length, alphanumeric, hyphen, or period.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the Boundary cluster
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password of the initial admin user. This must be at least 8 characters in length. Note that this may show up in logs, and it will be stored in the state file.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The username of the initial admin user. This must be at least 3 characters in length, alphanumeric, hyphen, or period.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class _BoundaryClusterState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cluster_url: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BoundaryCluster resources.
        :param pulumi.Input[str] cluster_id: The ID of the Boundary cluster
        :param pulumi.Input[str] cluster_url: A unique URL identifying the Boundary cluster.
        :param pulumi.Input[str] created_at: The time that the Boundary cluster was created.
        :param pulumi.Input[str] password: The password of the initial admin user. This must be at least 8 characters in length. Note that this may show up in logs, and it will be stored in the state file.
        :param pulumi.Input[str] state: The state of the Boundary cluster.
        :param pulumi.Input[str] username: The username of the initial admin user. This must be at least 3 characters in length, alphanumeric, hyphen, or period.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if cluster_url is not None:
            pulumi.set(__self__, "cluster_url", cluster_url)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Boundary cluster
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="clusterUrl")
    def cluster_url(self) -> Optional[pulumi.Input[str]]:
        """
        A unique URL identifying the Boundary cluster.
        """
        return pulumi.get(self, "cluster_url")

    @cluster_url.setter
    def cluster_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_url", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time that the Boundary cluster was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the initial admin user. This must be at least 8 characters in length. Note that this may show up in logs, and it will be stored in the state file.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the Boundary cluster.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The username of the initial admin user. This must be at least 3 characters in length, alphanumeric, hyphen, or period.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class BoundaryCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to manage an HCP Boundary cluster

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcp as hcp

        example = hcp.BoundaryCluster("example",
            cluster_id="boundary-cluster",
            password="Password123!",
            username="test-user")
        ```

        ## Import

        # The import ID is {cluster_id}

        ```sh
         $ pulumi import hcp:index/boundaryCluster:BoundaryCluster example boundary-cluster
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the Boundary cluster
        :param pulumi.Input[str] password: The password of the initial admin user. This must be at least 8 characters in length. Note that this may show up in logs, and it will be stored in the state file.
        :param pulumi.Input[str] username: The username of the initial admin user. This must be at least 3 characters in length, alphanumeric, hyphen, or period.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BoundaryClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to manage an HCP Boundary cluster

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcp as hcp

        example = hcp.BoundaryCluster("example",
            cluster_id="boundary-cluster",
            password="Password123!",
            username="test-user")
        ```

        ## Import

        # The import ID is {cluster_id}

        ```sh
         $ pulumi import hcp:index/boundaryCluster:BoundaryCluster example boundary-cluster
        ```

        :param str resource_name: The name of the resource.
        :param BoundaryClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BoundaryClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BoundaryClusterArgs.__new__(BoundaryClusterArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = password
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
            __props__.__dict__["cluster_url"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["state"] = None
        super(BoundaryCluster, __self__).__init__(
            'hcp:index/boundaryCluster:BoundaryCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            cluster_url: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'BoundaryCluster':
        """
        Get an existing BoundaryCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the Boundary cluster
        :param pulumi.Input[str] cluster_url: A unique URL identifying the Boundary cluster.
        :param pulumi.Input[str] created_at: The time that the Boundary cluster was created.
        :param pulumi.Input[str] password: The password of the initial admin user. This must be at least 8 characters in length. Note that this may show up in logs, and it will be stored in the state file.
        :param pulumi.Input[str] state: The state of the Boundary cluster.
        :param pulumi.Input[str] username: The username of the initial admin user. This must be at least 3 characters in length, alphanumeric, hyphen, or period.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BoundaryClusterState.__new__(_BoundaryClusterState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["cluster_url"] = cluster_url
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["password"] = password
        __props__.__dict__["state"] = state
        __props__.__dict__["username"] = username
        return BoundaryCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the Boundary cluster
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="clusterUrl")
    def cluster_url(self) -> pulumi.Output[str]:
        """
        A unique URL identifying the Boundary cluster.
        """
        return pulumi.get(self, "cluster_url")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time that the Boundary cluster was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        The password of the initial admin user. This must be at least 8 characters in length. Note that this may show up in logs, and it will be stored in the state file.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the Boundary cluster.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The username of the initial admin user. This must be at least 3 characters in length, alphanumeric, hyphen, or period.
        """
        return pulumi.get(self, "username")

