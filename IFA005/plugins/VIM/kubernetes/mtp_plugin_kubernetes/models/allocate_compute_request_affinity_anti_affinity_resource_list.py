# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mtp_plugin_kubernetes.models.base_model_ import Model
from mtp_plugin_kubernetes import util


class AllocateComputeRequestAffinityAntiAffinityResourceList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, resource: List[str]=None):  # noqa: E501
        """AllocateComputeRequestAffinityAntiAffinityResourceList - a model defined in Swagger

        :param resource: The resource of this AllocateComputeRequestAffinityAntiAffinityResourceList.  # noqa: E501
        :type resource: List[str]
        """
        self.swagger_types = {
            'resource': List[str]
        }

        self.attribute_map = {
            'resource': 'resource'
        }

        self._resource = resource

    @classmethod
    def from_dict(cls, dikt) -> 'AllocateComputeRequestAffinityAntiAffinityResourceList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllocateComputeRequest_affinityAntiAffinityResourceList of this AllocateComputeRequestAffinityAntiAffinityResourceList.  # noqa: E501
        :rtype: AllocateComputeRequestAffinityAntiAffinityResourceList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource(self) -> List[str]:
        """Gets the resource of this AllocateComputeRequestAffinityAntiAffinityResourceList.

        List of identifiers of virtualised resources.  # noqa: E501

        :return: The resource of this AllocateComputeRequestAffinityAntiAffinityResourceList.
        :rtype: List[str]
        """
        return self._resource

    @resource.setter
    def resource(self, resource: List[str]):
        """Sets the resource of this AllocateComputeRequestAffinityAntiAffinityResourceList.

        List of identifiers of virtualised resources.  # noqa: E501

        :param resource: The resource of this AllocateComputeRequestAffinityAntiAffinityResourceList.
        :type resource: List[str]
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource