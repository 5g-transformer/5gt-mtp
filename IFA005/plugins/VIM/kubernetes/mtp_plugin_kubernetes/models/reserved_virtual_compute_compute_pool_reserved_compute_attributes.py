# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mtp_plugin_kubernetes.models.base_model_ import Model
from mtp_plugin_kubernetes import util


class ReservedVirtualComputeComputePoolReservedComputeAttributes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, acceleration_capability: str=None, cpu_architecture: str=None, virtual_cpu_oversubscription_policy: str=None):  # noqa: E501
        """ReservedVirtualComputeComputePoolReservedComputeAttributes - a model defined in Swagger

        :param acceleration_capability: The acceleration_capability of this ReservedVirtualComputeComputePoolReservedComputeAttributes.  # noqa: E501
        :type acceleration_capability: str
        :param cpu_architecture: The cpu_architecture of this ReservedVirtualComputeComputePoolReservedComputeAttributes.  # noqa: E501
        :type cpu_architecture: str
        :param virtual_cpu_oversubscription_policy: The virtual_cpu_oversubscription_policy of this ReservedVirtualComputeComputePoolReservedComputeAttributes.  # noqa: E501
        :type virtual_cpu_oversubscription_policy: str
        """
        self.swagger_types = {
            'acceleration_capability': str,
            'cpu_architecture': str,
            'virtual_cpu_oversubscription_policy': str
        }

        self.attribute_map = {
            'acceleration_capability': 'accelerationCapability',
            'cpu_architecture': 'cpuArchitecture',
            'virtual_cpu_oversubscription_policy': 'virtualCpuOversubscriptionPolicy'
        }

        self._acceleration_capability = acceleration_capability
        self._cpu_architecture = cpu_architecture
        self._virtual_cpu_oversubscription_policy = virtual_cpu_oversubscription_policy

    @classmethod
    def from_dict(cls, dikt) -> 'ReservedVirtualComputeComputePoolReservedComputeAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReservedVirtualCompute_computePoolReserved_computeAttributes of this ReservedVirtualComputeComputePoolReservedComputeAttributes.  # noqa: E501
        :rtype: ReservedVirtualComputeComputePoolReservedComputeAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def acceleration_capability(self) -> str:
        """Gets the acceleration_capability of this ReservedVirtualComputeComputePoolReservedComputeAttributes.

        Selected acceleration capabilities (e.g. crypto, GPU) from the set of capabilities offered by the compute node acceleration resources. The cardinality can be 0, if no particular acceleration capability is provided.  # noqa: E501

        :return: The acceleration_capability of this ReservedVirtualComputeComputePoolReservedComputeAttributes.
        :rtype: str
        """
        return self._acceleration_capability

    @acceleration_capability.setter
    def acceleration_capability(self, acceleration_capability: str):
        """Sets the acceleration_capability of this ReservedVirtualComputeComputePoolReservedComputeAttributes.

        Selected acceleration capabilities (e.g. crypto, GPU) from the set of capabilities offered by the compute node acceleration resources. The cardinality can be 0, if no particular acceleration capability is provided.  # noqa: E501

        :param acceleration_capability: The acceleration_capability of this ReservedVirtualComputeComputePoolReservedComputeAttributes.
        :type acceleration_capability: str
        """
        if acceleration_capability is None:
            raise ValueError("Invalid value for `acceleration_capability`, must not be `None`")  # noqa: E501

        self._acceleration_capability = acceleration_capability

    @property
    def cpu_architecture(self) -> str:
        """Gets the cpu_architecture of this ReservedVirtualComputeComputePoolReservedComputeAttributes.

        CPU architecture type. Examples are \"x86\", \"ARM\". The cardinality can be 0, if no particular CPU architecture type is provided.  # noqa: E501

        :return: The cpu_architecture of this ReservedVirtualComputeComputePoolReservedComputeAttributes.
        :rtype: str
        """
        return self._cpu_architecture

    @cpu_architecture.setter
    def cpu_architecture(self, cpu_architecture: str):
        """Sets the cpu_architecture of this ReservedVirtualComputeComputePoolReservedComputeAttributes.

        CPU architecture type. Examples are \"x86\", \"ARM\". The cardinality can be 0, if no particular CPU architecture type is provided.  # noqa: E501

        :param cpu_architecture: The cpu_architecture of this ReservedVirtualComputeComputePoolReservedComputeAttributes.
        :type cpu_architecture: str
        """
        if cpu_architecture is None:
            raise ValueError("Invalid value for `cpu_architecture`, must not be `None`")  # noqa: E501

        self._cpu_architecture = cpu_architecture

    @property
    def virtual_cpu_oversubscription_policy(self) -> str:
        """Gets the virtual_cpu_oversubscription_policy of this ReservedVirtualComputeComputePoolReservedComputeAttributes.

        The CPU core oversubscription policy in terms of virtual CPU cores to physical CPU cores/threads on the platform. The cardinality can be 0, if no particular value is provided.  # noqa: E501

        :return: The virtual_cpu_oversubscription_policy of this ReservedVirtualComputeComputePoolReservedComputeAttributes.
        :rtype: str
        """
        return self._virtual_cpu_oversubscription_policy

    @virtual_cpu_oversubscription_policy.setter
    def virtual_cpu_oversubscription_policy(self, virtual_cpu_oversubscription_policy: str):
        """Sets the virtual_cpu_oversubscription_policy of this ReservedVirtualComputeComputePoolReservedComputeAttributes.

        The CPU core oversubscription policy in terms of virtual CPU cores to physical CPU cores/threads on the platform. The cardinality can be 0, if no particular value is provided.  # noqa: E501

        :param virtual_cpu_oversubscription_policy: The virtual_cpu_oversubscription_policy of this ReservedVirtualComputeComputePoolReservedComputeAttributes.
        :type virtual_cpu_oversubscription_policy: str
        """
        if virtual_cpu_oversubscription_policy is None:
            raise ValueError("Invalid value for `virtual_cpu_oversubscription_policy`, must not be `None`")  # noqa: E501

        self._virtual_cpu_oversubscription_policy = virtual_cpu_oversubscription_policy
