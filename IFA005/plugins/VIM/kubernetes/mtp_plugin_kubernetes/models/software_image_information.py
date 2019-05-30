# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mtp_plugin_kubernetes.models.base_model_ import Model
from mtp_plugin_kubernetes import util


class SoftwareImageInformation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, checksum: str=None, container_format: str=None, created_at: str=None, disk_format: str=None, id: str=None, min_disk: str=None, min_ram: str=None, name: str=None, provider: str=None, size: str=None, status: str=None, updated_at: str=None, version: str=None):  # noqa: E501
        """SoftwareImageInformation - a model defined in Swagger

        :param checksum: The checksum of this SoftwareImageInformation.  # noqa: E501
        :type checksum: str
        :param container_format: The container_format of this SoftwareImageInformation.  # noqa: E501
        :type container_format: str
        :param created_at: The created_at of this SoftwareImageInformation.  # noqa: E501
        :type created_at: str
        :param disk_format: The disk_format of this SoftwareImageInformation.  # noqa: E501
        :type disk_format: str
        :param id: The id of this SoftwareImageInformation.  # noqa: E501
        :type id: str
        :param min_disk: The min_disk of this SoftwareImageInformation.  # noqa: E501
        :type min_disk: str
        :param min_ram: The min_ram of this SoftwareImageInformation.  # noqa: E501
        :type min_ram: str
        :param name: The name of this SoftwareImageInformation.  # noqa: E501
        :type name: str
        :param provider: The provider of this SoftwareImageInformation.  # noqa: E501
        :type provider: str
        :param size: The size of this SoftwareImageInformation.  # noqa: E501
        :type size: str
        :param status: The status of this SoftwareImageInformation.  # noqa: E501
        :type status: str
        :param updated_at: The updated_at of this SoftwareImageInformation.  # noqa: E501
        :type updated_at: str
        :param version: The version of this SoftwareImageInformation.  # noqa: E501
        :type version: str
        """
        self.swagger_types = {
            'checksum': str,
            'container_format': str,
            'created_at': str,
            'disk_format': str,
            'id': str,
            'min_disk': str,
            'min_ram': str,
            'name': str,
            'provider': str,
            'size': str,
            'status': str,
            'updated_at': str,
            'version': str
        }

        self.attribute_map = {
            'checksum': 'checksum',
            'container_format': 'containerFormat',
            'created_at': 'createdAt',
            'disk_format': 'diskFormat',
            'id': 'id',
            'min_disk': 'minDisk',
            'min_ram': 'minRam',
            'name': 'name',
            'provider': 'provider',
            'size': 'size',
            'status': 'status',
            'updated_at': 'updatedAt',
            'version': 'version'
        }

        self._checksum = checksum
        self._container_format = container_format
        self._created_at = created_at
        self._disk_format = disk_format
        self._id = id
        self._min_disk = min_disk
        self._min_ram = min_ram
        self._name = name
        self._provider = provider
        self._size = size
        self._status = status
        self._updated_at = updated_at
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'SoftwareImageInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SoftwareImageInformation of this SoftwareImageInformation.  # noqa: E501
        :rtype: SoftwareImageInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def checksum(self) -> str:
        """Gets the checksum of this SoftwareImageInformation.

        The checksum of the software image file.  # noqa: E501

        :return: The checksum of this SoftwareImageInformation.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum: str):
        """Sets the checksum of this SoftwareImageInformation.

        The checksum of the software image file.  # noqa: E501

        :param checksum: The checksum of this SoftwareImageInformation.
        :type checksum: str
        """
        if checksum is None:
            raise ValueError("Invalid value for `checksum`, must not be `None`")  # noqa: E501

        self._checksum = checksum

    @property
    def container_format(self) -> str:
        """Gets the container_format of this SoftwareImageInformation.

        The container format indicates whether the software image is in a file format that also contains metadata about the actual software.  # noqa: E501

        :return: The container_format of this SoftwareImageInformation.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format: str):
        """Sets the container_format of this SoftwareImageInformation.

        The container format indicates whether the software image is in a file format that also contains metadata about the actual software.  # noqa: E501

        :param container_format: The container_format of this SoftwareImageInformation.
        :type container_format: str
        """
        if container_format is None:
            raise ValueError("Invalid value for `container_format`, must not be `None`")  # noqa: E501

        self._container_format = container_format

    @property
    def created_at(self) -> str:
        """Gets the created_at of this SoftwareImageInformation.

        The created time of this software image.  # noqa: E501

        :return: The created_at of this SoftwareImageInformation.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this SoftwareImageInformation.

        The created time of this software image.  # noqa: E501

        :param created_at: The created_at of this SoftwareImageInformation.
        :type created_at: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def disk_format(self) -> str:
        """Gets the disk_format of this SoftwareImageInformation.

        The disk format of a software image is the format of the underlying disk image.  # noqa: E501

        :return: The disk_format of this SoftwareImageInformation.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format: str):
        """Sets the disk_format of this SoftwareImageInformation.

        The disk format of a software image is the format of the underlying disk image.  # noqa: E501

        :param disk_format: The disk_format of this SoftwareImageInformation.
        :type disk_format: str
        """
        if disk_format is None:
            raise ValueError("Invalid value for `disk_format`, must not be `None`")  # noqa: E501

        self._disk_format = disk_format

    @property
    def id(self) -> str:
        """Gets the id of this SoftwareImageInformation.

        The identifier of this software image.  # noqa: E501

        :return: The id of this SoftwareImageInformation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SoftwareImageInformation.

        The identifier of this software image.  # noqa: E501

        :param id: The id of this SoftwareImageInformation.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def min_disk(self) -> str:
        """Gets the min_disk of this SoftwareImageInformation.

        The minimal Disk for this software image.  # noqa: E501

        :return: The min_disk of this SoftwareImageInformation.
        :rtype: str
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk: str):
        """Sets the min_disk of this SoftwareImageInformation.

        The minimal Disk for this software image.  # noqa: E501

        :param min_disk: The min_disk of this SoftwareImageInformation.
        :type min_disk: str
        """
        if min_disk is None:
            raise ValueError("Invalid value for `min_disk`, must not be `None`")  # noqa: E501

        self._min_disk = min_disk

    @property
    def min_ram(self) -> str:
        """Gets the min_ram of this SoftwareImageInformation.

        The minimal RAM for this software image.  # noqa: E501

        :return: The min_ram of this SoftwareImageInformation.
        :rtype: str
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram: str):
        """Sets the min_ram of this SoftwareImageInformation.

        The minimal RAM for this software image.  # noqa: E501

        :param min_ram: The min_ram of this SoftwareImageInformation.
        :type min_ram: str
        """
        if min_ram is None:
            raise ValueError("Invalid value for `min_ram`, must not be `None`")  # noqa: E501

        self._min_ram = min_ram

    @property
    def name(self) -> str:
        """Gets the name of this SoftwareImageInformation.

        The name of this software image.  # noqa: E501

        :return: The name of this SoftwareImageInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SoftwareImageInformation.

        The name of this software image.  # noqa: E501

        :param name: The name of this SoftwareImageInformation.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider(self) -> str:
        """Gets the provider of this SoftwareImageInformation.

        The provider of this software image.  # noqa: E501

        :return: The provider of this SoftwareImageInformation.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider: str):
        """Sets the provider of this SoftwareImageInformation.

        The provider of this software image.  # noqa: E501

        :param provider: The provider of this SoftwareImageInformation.
        :type provider: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def size(self) -> str:
        """Gets the size of this SoftwareImageInformation.

        The size of this software image.  # noqa: E501

        :return: The size of this SoftwareImageInformation.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size: str):
        """Sets the size of this SoftwareImageInformation.

        The size of this software image.  # noqa: E501

        :param size: The size of this SoftwareImageInformation.
        :type size: str
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def status(self) -> str:
        """Gets the status of this SoftwareImageInformation.

        The status of this software image.  # noqa: E501

        :return: The status of this SoftwareImageInformation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this SoftwareImageInformation.

        The status of this software image.  # noqa: E501

        :param status: The status of this SoftwareImageInformation.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def updated_at(self) -> str:
        """Gets the updated_at of this SoftwareImageInformation.

        The updated time of this software image.  # noqa: E501

        :return: The updated_at of this SoftwareImageInformation.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: str):
        """Sets the updated_at of this SoftwareImageInformation.

        The updated time of this software image.  # noqa: E501

        :param updated_at: The updated_at of this SoftwareImageInformation.
        :type updated_at: str
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def version(self) -> str:
        """Gets the version of this SoftwareImageInformation.

        The version of this software image.  # noqa: E501

        :return: The version of this SoftwareImageInformation.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this SoftwareImageInformation.

        The version of this software image.  # noqa: E501

        :param version: The version of this SoftwareImageInformation.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version
