# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mtp_plugin_kubernetes.models.base_model_ import Model
from mtp_plugin_kubernetes.models.reserved_virtual_compute_compute_pool_reserved_compute_attributes import ReservedVirtualComputeComputePoolReservedComputeAttributes  # noqa: F401,E501
from mtp_plugin_kubernetes import util


class ReservedVirtualComputeVirtualisationContainerReservedFlavourId(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, compute_attributes: ReservedVirtualComputeComputePoolReservedComputeAttributes=None, num_cpu_cores: int=None, num_vc_instances: int=None, virtual_mem_size: float=None, zone_id: str=None):  # noqa: E501
        """ReservedVirtualComputeVirtualisationContainerReservedFlavourId - a model defined in Swagger

        :param compute_attributes: The compute_attributes of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.  # noqa: E501
        :type compute_attributes: ReservedVirtualComputeComputePoolReservedComputeAttributes
        :param num_cpu_cores: The num_cpu_cores of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.  # noqa: E501
        :type num_cpu_cores: int
        :param num_vc_instances: The num_vc_instances of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.  # noqa: E501
        :type num_vc_instances: int
        :param virtual_mem_size: The virtual_mem_size of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.  # noqa: E501
        :type virtual_mem_size: float
        :param zone_id: The zone_id of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.  # noqa: E501
        :type zone_id: str
        """
        self.swagger_types = {
            'compute_attributes': ReservedVirtualComputeComputePoolReservedComputeAttributes,
            'num_cpu_cores': int,
            'num_vc_instances': int,
            'virtual_mem_size': float,
            'zone_id': str
        }

        self.attribute_map = {
            'compute_attributes': 'computeAttributes',
            'num_cpu_cores': 'numCpuCores',
            'num_vc_instances': 'numVcInstances',
            'virtual_mem_size': 'virtualMemSize',
            'zone_id': 'zoneId'
        }

        self._compute_attributes = compute_attributes
        self._num_cpu_cores = num_cpu_cores
        self._num_vc_instances = num_vc_instances
        self._virtual_mem_size = virtual_mem_size
        self._zone_id = zone_id

    @classmethod
    def from_dict(cls, dikt) -> 'ReservedVirtualComputeVirtualisationContainerReservedFlavourId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReservedVirtualCompute_virtualisationContainerReserved_flavourId of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.  # noqa: E501
        :rtype: ReservedVirtualComputeVirtualisationContainerReservedFlavourId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def compute_attributes(self) -> ReservedVirtualComputeComputePoolReservedComputeAttributes:
        """Gets the compute_attributes of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.


        :return: The compute_attributes of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.
        :rtype: ReservedVirtualComputeComputePoolReservedComputeAttributes
        """
        return self._compute_attributes

    @compute_attributes.setter
    def compute_attributes(self, compute_attributes: ReservedVirtualComputeComputePoolReservedComputeAttributes):
        """Sets the compute_attributes of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.


        :param compute_attributes: The compute_attributes of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.
        :type compute_attributes: ReservedVirtualComputeComputePoolReservedComputeAttributes
        """
        if compute_attributes is None:
            raise ValueError("Invalid value for `compute_attributes`, must not be `None`")  # noqa: E501

        self._compute_attributes = compute_attributes

    @property
    def num_cpu_cores(self) -> int:
        """Gets the num_cpu_cores of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.

        Number of CPU cores that have been reserved.  # noqa: E501

        :return: The num_cpu_cores of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.
        :rtype: int
        """
        return self._num_cpu_cores

    @num_cpu_cores.setter
    def num_cpu_cores(self, num_cpu_cores: int):
        """Sets the num_cpu_cores of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.

        Number of CPU cores that have been reserved.  # noqa: E501

        :param num_cpu_cores: The num_cpu_cores of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.
        :type num_cpu_cores: int
        """
        if num_cpu_cores is None:
            raise ValueError("Invalid value for `num_cpu_cores`, must not be `None`")  # noqa: E501

        self._num_cpu_cores = num_cpu_cores

    @property
    def num_vc_instances(self) -> int:
        """Gets the num_vc_instances of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.

        Number of virtual container instances that have been reserved.  # noqa: E501

        :return: The num_vc_instances of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.
        :rtype: int
        """
        return self._num_vc_instances

    @num_vc_instances.setter
    def num_vc_instances(self, num_vc_instances: int):
        """Sets the num_vc_instances of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.

        Number of virtual container instances that have been reserved.  # noqa: E501

        :param num_vc_instances: The num_vc_instances of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.
        :type num_vc_instances: int
        """
        if num_vc_instances is None:
            raise ValueError("Invalid value for `num_vc_instances`, must not be `None`")  # noqa: E501

        self._num_vc_instances = num_vc_instances

    @property
    def virtual_mem_size(self) -> float:
        """Gets the virtual_mem_size of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.

        Size of virtual memory that has been reserved.  # noqa: E501

        :return: The virtual_mem_size of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.
        :rtype: float
        """
        return self._virtual_mem_size

    @virtual_mem_size.setter
    def virtual_mem_size(self, virtual_mem_size: float):
        """Sets the virtual_mem_size of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.

        Size of virtual memory that has been reserved.  # noqa: E501

        :param virtual_mem_size: The virtual_mem_size of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.
        :type virtual_mem_size: float
        """
        if virtual_mem_size is None:
            raise ValueError("Invalid value for `virtual_mem_size`, must not be `None`")  # noqa: E501

        self._virtual_mem_size = virtual_mem_size

    @property
    def zone_id(self) -> str:
        """Gets the zone_id of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.

        References the resource zone where the virtual compute resources have been reserved. Cardinality can be 0 to cover the case where reserved compute resources are not bound to a specific resource zone.  # noqa: E501

        :return: The zone_id of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id: str):
        """Sets the zone_id of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.

        References the resource zone where the virtual compute resources have been reserved. Cardinality can be 0 to cover the case where reserved compute resources are not bound to a specific resource zone.  # noqa: E501

        :param zone_id: The zone_id of this ReservedVirtualComputeVirtualisationContainerReservedFlavourId.
        :type zone_id: str
        """
        if zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

        self._zone_id = zone_id
