# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['GoogleCloudFolderArgs', 'GoogleCloudFolder']

@pulumi.input_type
class GoogleCloudFolderArgs:
    def __init__(__self__, *,
                 bucket_name: pulumi.Input[str],
                 path: pulumi.Input[str],
                 managed_objects: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a GoogleCloudFolder resource.
        :param pulumi.Input[str] bucket_name: The name of the Google Cloud Storage bucket to sync to (e.g., `my-bucket` in `gs://my-bucket`). Required.
        :param pulumi.Input[str] path: The path (relative or fully-qualified) to the folder containing the files to be synced. Required.
        :param pulumi.Input[bool] managed_objects: Whether to have Pulumi manage files as individual cloud resources. Defaults to `true`.
        """
        pulumi.set(__self__, "bucket_name", bucket_name)
        pulumi.set(__self__, "path", path)
        if managed_objects is not None:
            pulumi.set(__self__, "managed_objects", managed_objects)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[str]:
        """
        The name of the Google Cloud Storage bucket to sync to (e.g., `my-bucket` in `gs://my-bucket`). Required.
        """
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        The path (relative or fully-qualified) to the folder containing the files to be synced. Required.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="managedObjects")
    def managed_objects(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to have Pulumi manage files as individual cloud resources. Defaults to `true`.
        """
        return pulumi.get(self, "managed_objects")

    @managed_objects.setter
    def managed_objects(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "managed_objects", value)


class GoogleCloudFolder(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 managed_objects: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a GoogleCloudFolder resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket_name: The name of the Google Cloud Storage bucket to sync to (e.g., `my-bucket` in `gs://my-bucket`). Required.
        :param pulumi.Input[bool] managed_objects: Whether to have Pulumi manage files as individual cloud resources. Defaults to `true`.
        :param pulumi.Input[str] path: The path (relative or fully-qualified) to the folder containing the files to be synced. Required.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GoogleCloudFolderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a GoogleCloudFolder resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param GoogleCloudFolderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GoogleCloudFolderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 managed_objects: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GoogleCloudFolderArgs.__new__(GoogleCloudFolderArgs)

            if bucket_name is None and not opts.urn:
                raise TypeError("Missing required property 'bucket_name'")
            __props__.__dict__["bucket_name"] = bucket_name
            __props__.__dict__["managed_objects"] = managed_objects
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
        super(GoogleCloudFolder, __self__).__init__(
            'synced-folder:index:GoogleCloudFolder',
            resource_name,
            __props__,
            opts,
            remote=True)

