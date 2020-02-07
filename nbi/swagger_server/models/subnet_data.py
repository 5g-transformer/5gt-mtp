# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.meta_data import MetaData  # noqa: F401,E501
from swagger_server import util


class SubnetData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, resource_id: str=None, network_id: str=None, ip_version: str=None, gateway_ip: str=None, cidr: str=None, is_dhcp_enabled: bool=None, address_pool: List[int]=None, metadata: MetaData=None):  # noqa: E501
        """SubnetData - a model defined in Swagger

        :param resource_id: The resource_id of this SubnetData.  # noqa: E501
        :type resource_id: str
        :param network_id: The network_id of this SubnetData.  # noqa: E501
        :type network_id: str
        :param ip_version: The ip_version of this SubnetData.  # noqa: E501
        :type ip_version: str
        :param gateway_ip: The gateway_ip of this SubnetData.  # noqa: E501
        :type gateway_ip: str
        :param cidr: The cidr of this SubnetData.  # noqa: E501
        :type cidr: str
        :param is_dhcp_enabled: The is_dhcp_enabled of this SubnetData.  # noqa: E501
        :type is_dhcp_enabled: bool
        :param address_pool: The address_pool of this SubnetData.  # noqa: E501
        :type address_pool: List[int]
        :param metadata: The metadata of this SubnetData.  # noqa: E501
        :type metadata: MetaData
        """
        self.swagger_types = {
            'resource_id': str,
            'network_id': str,
            'ip_version': str,
            'gateway_ip': str,
            'cidr': str,
            'is_dhcp_enabled': bool,
            'address_pool': List[int],
            'metadata': MetaData
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'network_id': 'networkId',
            'ip_version': 'ipVersion',
            'gateway_ip': 'gatewayIp',
            'cidr': 'cidr',
            'is_dhcp_enabled': 'isDhcpEnabled',
            'address_pool': 'addressPool',
            'metadata': 'metadata'
        }

        self._resource_id = resource_id
        self._network_id = network_id
        self._ip_version = ip_version
        self._gateway_ip = gateway_ip
        self._cidr = cidr
        self._is_dhcp_enabled = is_dhcp_enabled
        self._address_pool = address_pool
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'SubnetData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubnetData of this SubnetData.  # noqa: E501
        :rtype: SubnetData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_id(self) -> str:
        """Gets the resource_id of this SubnetData.

        Identifiers of the network Resource  # noqa: E501

        :return: The resource_id of this SubnetData.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id: str):
        """Sets the resource_id of this SubnetData.

        Identifiers of the network Resource  # noqa: E501

        :param resource_id: The resource_id of this SubnetData.
        :type resource_id: str
        """
        if resource_id is None:
            raise ValueError("Invalid value for `resource_id`, must not be `None`")  # noqa: E501

        self._resource_id = resource_id

    @property
    def network_id(self) -> str:
        """Gets the network_id of this SubnetData.

        Network identifier the subnetwork Resource  # noqa: E501

        :return: The network_id of this SubnetData.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id: str):
        """Sets the network_id of this SubnetData.

        Network identifier the subnetwork Resource  # noqa: E501

        :param network_id: The network_id of this SubnetData.
        :type network_id: str
        """
        if network_id is None:
            raise ValueError("Invalid value for `network_id`, must not be `None`")  # noqa: E501

        self._network_id = network_id

    @property
    def ip_version(self) -> str:
        """Gets the ip_version of this SubnetData.

        IP version of the subnetwork Resource  # noqa: E501

        :return: The ip_version of this SubnetData.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version: str):
        """Sets the ip_version of this SubnetData.

        IP version of the subnetwork Resource  # noqa: E501

        :param ip_version: The ip_version of this SubnetData.
        :type ip_version: str
        """
        if ip_version is None:
            raise ValueError("Invalid value for `ip_version`, must not be `None`")  # noqa: E501

        self._ip_version = ip_version

    @property
    def gateway_ip(self) -> str:
        """Gets the gateway_ip of this SubnetData.

        gateway of the subnetwork Resource  # noqa: E501

        :return: The gateway_ip of this SubnetData.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip: str):
        """Sets the gateway_ip of this SubnetData.

        gateway of the subnetwork Resource  # noqa: E501

        :param gateway_ip: The gateway_ip of this SubnetData.
        :type gateway_ip: str
        """
        if gateway_ip is None:
            raise ValueError("Invalid value for `gateway_ip`, must not be `None`")  # noqa: E501

        self._gateway_ip = gateway_ip

    @property
    def cidr(self) -> str:
        """Gets the cidr of this SubnetData.

        cidr of the subnetwork Resource  # noqa: E501

        :return: The cidr of this SubnetData.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr: str):
        """Sets the cidr of this SubnetData.

        cidr of the subnetwork Resource  # noqa: E501

        :param cidr: The cidr of this SubnetData.
        :type cidr: str
        """
        if cidr is None:
            raise ValueError("Invalid value for `cidr`, must not be `None`")  # noqa: E501

        self._cidr = cidr

    @property
    def is_dhcp_enabled(self) -> bool:
        """Gets the is_dhcp_enabled of this SubnetData.

        enable if dhcp of the network Resource  # noqa: E501

        :return: The is_dhcp_enabled of this SubnetData.
        :rtype: bool
        """
        return self._is_dhcp_enabled

    @is_dhcp_enabled.setter
    def is_dhcp_enabled(self, is_dhcp_enabled: bool):
        """Sets the is_dhcp_enabled of this SubnetData.

        enable if dhcp of the network Resource  # noqa: E501

        :param is_dhcp_enabled: The is_dhcp_enabled of this SubnetData.
        :type is_dhcp_enabled: bool
        """
        if is_dhcp_enabled is None:
            raise ValueError("Invalid value for `is_dhcp_enabled`, must not be `None`")  # noqa: E501

        self._is_dhcp_enabled = is_dhcp_enabled

    @property
    def address_pool(self) -> List[int]:
        """Gets the address_pool of this SubnetData.

        Address Pool format as range of valid address  # noqa: E501

        :return: The address_pool of this SubnetData.
        :rtype: List[int]
        """
        return self._address_pool

    @address_pool.setter
    def address_pool(self, address_pool: List[int]):
        """Sets the address_pool of this SubnetData.

        Address Pool format as range of valid address  # noqa: E501

        :param address_pool: The address_pool of this SubnetData.
        :type address_pool: List[int]
        """
        if address_pool is None:
            raise ValueError("Invalid value for `address_pool`, must not be `None`")  # noqa: E501

        self._address_pool = address_pool

    @property
    def metadata(self) -> MetaData:
        """Gets the metadata of this SubnetData.


        :return: The metadata of this SubnetData.
        :rtype: MetaData
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: MetaData):
        """Sets the metadata of this SubnetData.


        :param metadata: The metadata of this SubnetData.
        :type metadata: MetaData
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata
