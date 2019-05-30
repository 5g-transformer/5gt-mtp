# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.transport_descriptor import TransportDescriptor  # noqa: F401,E501
from swagger_server import util


class TransportDependency(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, transport: TransportDescriptor=None, serializers: str=None, labels: List[str]=None):  # noqa: E501
        """TransportDependency - a model defined in Swagger

        :param transport: The transport of this TransportDependency.  # noqa: E501
        :type transport: TransportDescriptor
        :param serializers: The serializers of this TransportDependency.  # noqa: E501
        :type serializers: str
        :param labels: The labels of this TransportDependency.  # noqa: E501
        :type labels: List[str]
        """
        self.swagger_types = {
            'transport': TransportDescriptor,
            'serializers': str,
            'labels': List[str]
        }

        self.attribute_map = {
            'transport': 'transport',
            'serializers': 'serializers',
            'labels': 'labels'
        }

        self._transport = transport
        self._serializers = serializers
        self._labels = labels

    @classmethod
    def from_dict(cls, dikt) -> 'TransportDependency':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransportDependency of this TransportDependency.  # noqa: E501
        :rtype: TransportDependency
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transport(self) -> TransportDescriptor:
        """Gets the transport of this TransportDependency.


        :return: The transport of this TransportDependency.
        :rtype: TransportDescriptor
        """
        return self._transport

    @transport.setter
    def transport(self, transport: TransportDescriptor):
        """Sets the transport of this TransportDependency.


        :param transport: The transport of this TransportDependency.
        :type transport: TransportDescriptor
        """
        if transport is None:
            raise ValueError("Invalid value for `transport`, must not be `None`")  # noqa: E501

        self._transport = transport

    @property
    def serializers(self) -> str:
        """Gets the serializers of this TransportDependency.

        Information about the serializers in this transport binding, as defined in the SerializerTypes type in ETSI GS MEC 011. Support for at least one of the entries is required in conjunction with the transport.  # noqa: E501

        :return: The serializers of this TransportDependency.
        :rtype: str
        """
        return self._serializers

    @serializers.setter
    def serializers(self, serializers: str):
        """Sets the serializers of this TransportDependency.

        Information about the serializers in this transport binding, as defined in the SerializerTypes type in ETSI GS MEC 011. Support for at least one of the entries is required in conjunction with the transport.  # noqa: E501

        :param serializers: The serializers of this TransportDependency.
        :type serializers: str
        """
        allowed_values = ["JSON", "XML", "PROTOBUF3"]  # noqa: E501
        if serializers not in allowed_values:
            raise ValueError(
                "Invalid value for `serializers` ({0}), must be one of {1}"
                .format(serializers, allowed_values)
            )

        self._serializers = serializers

    @property
    def labels(self) -> List[str]:
        """Gets the labels of this TransportDependency.

        Set of labels that allow to define groups of transport bindings.  # noqa: E501

        :return: The labels of this TransportDependency.
        :rtype: List[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels: List[str]):
        """Sets the labels of this TransportDependency.

        Set of labels that allow to define groups of transport bindings.  # noqa: E501

        :param labels: The labels of this TransportDependency.
        :type labels: List[str]
        """
        if labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels
