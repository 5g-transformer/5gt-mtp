# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mtp_plugin_kubernetes.models.base_model_ import Model
from mtp_plugin_kubernetes import util


class AllocateParameters(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, location_constraints: str=None, reservation_id: str=None, type_network_data: str=None, affinity_or_anti_affinity_constraints: str=None, type_network_port_data: str=None, resource_group_id: str=None, metadata: str=None, network_resource_type: str=None, network_resource_name: str=None, type_subnet_data: str=None, bandwidth: float=None, delay: str=None, network_type: str=None, segment_type: str=None, network_qo_s: str=None, is_shared: bool=None, sharing_criteria: str=None, layer3_attributes: str=None, port_type: str=None, network_id: str=None, segment_id: str=None, ingress_point_ip_address: str=None, ingress_point_port_address: str=None, egress_point_ip_address: str=None, egress_point_port_address: str=None, wan_link_id: str=None):  # noqa: E501
        """AllocateParameters - a model defined in Swagger

        :param location_constraints: The location_constraints of this AllocateParameters.  # noqa: E501
        :type location_constraints: str
        :param reservation_id: The reservation_id of this AllocateParameters.  # noqa: E501
        :type reservation_id: str
        :param type_network_data: The type_network_data of this AllocateParameters.  # noqa: E501
        :type type_network_data: str
        :param affinity_or_anti_affinity_constraints: The affinity_or_anti_affinity_constraints of this AllocateParameters.  # noqa: E501
        :type affinity_or_anti_affinity_constraints: str
        :param type_network_port_data: The type_network_port_data of this AllocateParameters.  # noqa: E501
        :type type_network_port_data: str
        :param resource_group_id: The resource_group_id of this AllocateParameters.  # noqa: E501
        :type resource_group_id: str
        :param metadata: The metadata of this AllocateParameters.  # noqa: E501
        :type metadata: str
        :param network_resource_type: The network_resource_type of this AllocateParameters.  # noqa: E501
        :type network_resource_type: str
        :param network_resource_name: The network_resource_name of this AllocateParameters.  # noqa: E501
        :type network_resource_name: str
        :param type_subnet_data: The type_subnet_data of this AllocateParameters.  # noqa: E501
        :type type_subnet_data: str
        :param bandwidth: The bandwidth of this AllocateParameters.  # noqa: E501
        :type bandwidth: float
        :param delay: The delay of this AllocateParameters.  # noqa: E501
        :type delay: str
        :param network_type: The network_type of this AllocateParameters.  # noqa: E501
        :type network_type: str
        :param segment_type: The segment_type of this AllocateParameters.  # noqa: E501
        :type segment_type: str
        :param network_qo_s: The network_qo_s of this AllocateParameters.  # noqa: E501
        :type network_qo_s: str
        :param is_shared: The is_shared of this AllocateParameters.  # noqa: E501
        :type is_shared: bool
        :param sharing_criteria: The sharing_criteria of this AllocateParameters.  # noqa: E501
        :type sharing_criteria: str
        :param layer3_attributes: The layer3_attributes of this AllocateParameters.  # noqa: E501
        :type layer3_attributes: str
        :param port_type: The port_type of this AllocateParameters.  # noqa: E501
        :type port_type: str
        :param network_id: The network_id of this AllocateParameters.  # noqa: E501
        :type network_id: str
        :param segment_id: The segment_id of this AllocateParameters.  # noqa: E501
        :type segment_id: str
        :param ingress_point_ip_address: The ingress_point_ip_address of this AllocateParameters.  # noqa: E501
        :type ingress_point_ip_address: str
        :param ingress_point_port_address: The ingress_point_port_address of this AllocateParameters.  # noqa: E501
        :type ingress_point_port_address: str
        :param egress_point_ip_address: The egress_point_ip_address of this AllocateParameters.  # noqa: E501
        :type egress_point_ip_address: str
        :param egress_point_port_address: The egress_point_port_address of this AllocateParameters.  # noqa: E501
        :type egress_point_port_address: str
        :param wan_link_id: The wan_link_id of this AllocateParameters.  # noqa: E501
        :type wan_link_id: str
        """
        self.swagger_types = {
            'location_constraints': str,
            'reservation_id': str,
            'type_network_data': str,
            'affinity_or_anti_affinity_constraints': str,
            'type_network_port_data': str,
            'resource_group_id': str,
            'metadata': str,
            'network_resource_type': str,
            'network_resource_name': str,
            'type_subnet_data': str,
            'bandwidth': float,
            'delay': str,
            'network_type': str,
            'segment_type': str,
            'network_qo_s': str,
            'is_shared': bool,
            'sharing_criteria': str,
            'layer3_attributes': str,
            'port_type': str,
            'network_id': str,
            'segment_id': str,
            'ingress_point_ip_address': str,
            'ingress_point_port_address': str,
            'egress_point_ip_address': str,
            'egress_point_port_address': str,
            'wan_link_id': str
        }

        self.attribute_map = {
            'location_constraints': 'locationConstraints',
            'reservation_id': 'reservationId',
            'type_network_data': 'typeNetworkData',
            'affinity_or_anti_affinity_constraints': 'affinityOrAntiAffinityConstraints',
            'type_network_port_data': 'typeNetworkPortData',
            'resource_group_id': 'resourceGroupId',
            'metadata': 'metadata',
            'network_resource_type': 'networkResourceType',
            'network_resource_name': 'networkResourceName',
            'type_subnet_data': 'typeSubnetData',
            'bandwidth': 'bandwidth',
            'delay': 'delay',
            'network_type': 'networkType',
            'segment_type': 'segmentType',
            'network_qo_s': 'networkQoS',
            'is_shared': 'isShared',
            'sharing_criteria': 'sharingCriteria',
            'layer3_attributes': 'layer3Attributes',
            'port_type': 'portType',
            'network_id': 'networkId',
            'segment_id': 'segmentId',
            'ingress_point_ip_address': 'ingressPointIPAddress',
            'ingress_point_port_address': 'ingressPointPortAddress',
            'egress_point_ip_address': 'egressPointIPAddress',
            'egress_point_port_address': 'egressPointPortAddress',
            'wan_link_id': 'wanLinkId'
        }

        self._location_constraints = location_constraints
        self._reservation_id = reservation_id
        self._type_network_data = type_network_data
        self._affinity_or_anti_affinity_constraints = affinity_or_anti_affinity_constraints
        self._type_network_port_data = type_network_port_data
        self._resource_group_id = resource_group_id
        self._metadata = metadata
        self._network_resource_type = network_resource_type
        self._network_resource_name = network_resource_name
        self._type_subnet_data = type_subnet_data
        self._bandwidth = bandwidth
        self._delay = delay
        self._network_type = network_type
        self._segment_type = segment_type
        self._network_qo_s = network_qo_s
        self._is_shared = is_shared
        self._sharing_criteria = sharing_criteria
        self._layer3_attributes = layer3_attributes
        self._port_type = port_type
        self._network_id = network_id
        self._segment_id = segment_id
        self._ingress_point_ip_address = ingress_point_ip_address
        self._ingress_point_port_address = ingress_point_port_address
        self._egress_point_ip_address = egress_point_ip_address
        self._egress_point_port_address = egress_point_port_address
        self._wan_link_id = wan_link_id

    @classmethod
    def from_dict(cls, dikt) -> 'AllocateParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllocateParameters of this AllocateParameters.  # noqa: E501
        :rtype: AllocateParameters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location_constraints(self) -> str:
        """Gets the location_constraints of this AllocateParameters.

        Controls the visibility of the image. In case of \"private\" value the image is available only for the tenant assigned to the provided resourceGroupId and the administrator tenants of the VIM while in case of \"public\" value, all tenants of the VIM can use the image.  # noqa: E501

        :return: The location_constraints of this AllocateParameters.
        :rtype: str
        """
        return self._location_constraints

    @location_constraints.setter
    def location_constraints(self, location_constraints: str):
        """Sets the location_constraints of this AllocateParameters.

        Controls the visibility of the image. In case of \"private\" value the image is available only for the tenant assigned to the provided resourceGroupId and the administrator tenants of the VIM while in case of \"public\" value, all tenants of the VIM can use the image.  # noqa: E501

        :param location_constraints: The location_constraints of this AllocateParameters.
        :type location_constraints: str
        """
        if location_constraints is None:
            raise ValueError("Invalid value for `location_constraints`, must not be `None`")  # noqa: E501

        self._location_constraints = location_constraints

    @property
    def reservation_id(self) -> str:
        """Gets the reservation_id of this AllocateParameters.

        Identifier of the resource reservation applicable to this virtualised resource management operation.  # noqa: E501

        :return: The reservation_id of this AllocateParameters.
        :rtype: str
        """
        return self._reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id: str):
        """Sets the reservation_id of this AllocateParameters.

        Identifier of the resource reservation applicable to this virtualised resource management operation.  # noqa: E501

        :param reservation_id: The reservation_id of this AllocateParameters.
        :type reservation_id: str
        """
        if reservation_id is None:
            raise ValueError("Invalid value for `reservation_id`, must not be `None`")  # noqa: E501

        self._reservation_id = reservation_id

    @property
    def type_network_data(self) -> str:
        """Gets the type_network_data of this AllocateParameters.

        The network data provides information about the particular virtual network resource to create. Cardinality can be \"0\" depending on the value of networkResourceType.  # noqa: E501

        :return: The type_network_data of this AllocateParameters.
        :rtype: str
        """
        return self._type_network_data

    @type_network_data.setter
    def type_network_data(self, type_network_data: str):
        """Sets the type_network_data of this AllocateParameters.

        The network data provides information about the particular virtual network resource to create. Cardinality can be \"0\" depending on the value of networkResourceType.  # noqa: E501

        :param type_network_data: The type_network_data of this AllocateParameters.
        :type type_network_data: str
        """
        if type_network_data is None:
            raise ValueError("Invalid value for `type_network_data`, must not be `None`")  # noqa: E501

        self._type_network_data = type_network_data

    @property
    def affinity_or_anti_affinity_constraints(self) -> str:
        """Gets the affinity_or_anti_affinity_constraints of this AllocateParameters.

        The binary software image file.  # noqa: E501

        :return: The affinity_or_anti_affinity_constraints of this AllocateParameters.
        :rtype: str
        """
        return self._affinity_or_anti_affinity_constraints

    @affinity_or_anti_affinity_constraints.setter
    def affinity_or_anti_affinity_constraints(self, affinity_or_anti_affinity_constraints: str):
        """Sets the affinity_or_anti_affinity_constraints of this AllocateParameters.

        The binary software image file.  # noqa: E501

        :param affinity_or_anti_affinity_constraints: The affinity_or_anti_affinity_constraints of this AllocateParameters.
        :type affinity_or_anti_affinity_constraints: str
        """
        if affinity_or_anti_affinity_constraints is None:
            raise ValueError("Invalid value for `affinity_or_anti_affinity_constraints`, must not be `None`")  # noqa: E501

        self._affinity_or_anti_affinity_constraints = affinity_or_anti_affinity_constraints

    @property
    def type_network_port_data(self) -> str:
        """Gets the type_network_port_data of this AllocateParameters.

        The binary software image file.  # noqa: E501

        :return: The type_network_port_data of this AllocateParameters.
        :rtype: str
        """
        return self._type_network_port_data

    @type_network_port_data.setter
    def type_network_port_data(self, type_network_port_data: str):
        """Sets the type_network_port_data of this AllocateParameters.

        The binary software image file.  # noqa: E501

        :param type_network_port_data: The type_network_port_data of this AllocateParameters.
        :type type_network_port_data: str
        """
        if type_network_port_data is None:
            raise ValueError("Invalid value for `type_network_port_data`, must not be `None`")  # noqa: E501

        self._type_network_port_data = type_network_port_data

    @property
    def resource_group_id(self) -> str:
        """Gets the resource_group_id of this AllocateParameters.

        Unique identifier of the \"infrastructure resource group\", logical grouping of virtual resources assigned to a tenant within an Infrastructure Domain.  # noqa: E501

        :return: The resource_group_id of this AllocateParameters.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id: str):
        """Sets the resource_group_id of this AllocateParameters.

        Unique identifier of the \"infrastructure resource group\", logical grouping of virtual resources assigned to a tenant within an Infrastructure Domain.  # noqa: E501

        :param resource_group_id: The resource_group_id of this AllocateParameters.
        :type resource_group_id: str
        """
        if resource_group_id is None:
            raise ValueError("Invalid value for `resource_group_id`, must not be `None`")  # noqa: E501

        self._resource_group_id = resource_group_id

    @property
    def metadata(self) -> str:
        """Gets the metadata of this AllocateParameters.

        The binary software image file.  # noqa: E501

        :return: The metadata of this AllocateParameters.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: str):
        """Sets the metadata of this AllocateParameters.

        The binary software image file.  # noqa: E501

        :param metadata: The metadata of this AllocateParameters.
        :type metadata: str
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def network_resource_type(self) -> str:
        """Gets the network_resource_type of this AllocateParameters.

        Type of virtualised network resource. Possible values are: \"network\", \"subnet\" or network-port.  # noqa: E501

        :return: The network_resource_type of this AllocateParameters.
        :rtype: str
        """
        return self._network_resource_type

    @network_resource_type.setter
    def network_resource_type(self, network_resource_type: str):
        """Sets the network_resource_type of this AllocateParameters.

        Type of virtualised network resource. Possible values are: \"network\", \"subnet\" or network-port.  # noqa: E501

        :param network_resource_type: The network_resource_type of this AllocateParameters.
        :type network_resource_type: str
        """
        if network_resource_type is None:
            raise ValueError("Invalid value for `network_resource_type`, must not be `None`")  # noqa: E501

        self._network_resource_type = network_resource_type

    @property
    def network_resource_name(self) -> str:
        """Gets the network_resource_name of this AllocateParameters.

        Name provided by the consumer for the virtualised network resource to allocate. It can be used for identifying resources from consumer side.  # noqa: E501

        :return: The network_resource_name of this AllocateParameters.
        :rtype: str
        """
        return self._network_resource_name

    @network_resource_name.setter
    def network_resource_name(self, network_resource_name: str):
        """Sets the network_resource_name of this AllocateParameters.

        Name provided by the consumer for the virtualised network resource to allocate. It can be used for identifying resources from consumer side.  # noqa: E501

        :param network_resource_name: The network_resource_name of this AllocateParameters.
        :type network_resource_name: str
        """
        if network_resource_name is None:
            raise ValueError("Invalid value for `network_resource_name`, must not be `None`")  # noqa: E501

        self._network_resource_name = network_resource_name

    @property
    def type_subnet_data(self) -> str:
        """Gets the type_subnet_data of this AllocateParameters.

        The subnet data provides information about the particular sub-network resource to create.  # noqa: E501

        :return: The type_subnet_data of this AllocateParameters.
        :rtype: str
        """
        return self._type_subnet_data

    @type_subnet_data.setter
    def type_subnet_data(self, type_subnet_data: str):
        """Sets the type_subnet_data of this AllocateParameters.

        The subnet data provides information about the particular sub-network resource to create.  # noqa: E501

        :param type_subnet_data: The type_subnet_data of this AllocateParameters.
        :type type_subnet_data: str
        """
        if type_subnet_data is None:
            raise ValueError("Invalid value for `type_subnet_data`, must not be `None`")  # noqa: E501

        self._type_subnet_data = type_subnet_data

    @property
    def bandwidth(self) -> float:
        """Gets the bandwidth of this AllocateParameters.

        The bandwidth of the virtual network interface (in Mbps).  # noqa: E501

        :return: The bandwidth of this AllocateParameters.
        :rtype: float
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth: float):
        """Sets the bandwidth of this AllocateParameters.

        The bandwidth of the virtual network interface (in Mbps).  # noqa: E501

        :param bandwidth: The bandwidth of this AllocateParameters.
        :type bandwidth: float
        """
        if bandwidth is None:
            raise ValueError("Invalid value for `bandwidth`, must not be `None`")  # noqa: E501

        self._bandwidth = bandwidth

    @property
    def delay(self) -> str:
        """Gets the delay of this AllocateParameters.

        Transmission delay.  # noqa: E501

        :return: The delay of this AllocateParameters.
        :rtype: str
        """
        return self._delay

    @delay.setter
    def delay(self, delay: str):
        """Sets the delay of this AllocateParameters.

        Transmission delay.  # noqa: E501

        :param delay: The delay of this AllocateParameters.
        :type delay: str
        """
        if delay is None:
            raise ValueError("Invalid value for `delay`, must not be `None`")  # noqa: E501

        self._delay = delay

    @property
    def network_type(self) -> str:
        """Gets the network_type of this AllocateParameters.

        The type of network that maps to the virtualised network.  # noqa: E501

        :return: The network_type of this AllocateParameters.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type: str):
        """Sets the network_type of this AllocateParameters.

        The type of network that maps to the virtualised network.  # noqa: E501

        :param network_type: The network_type of this AllocateParameters.
        :type network_type: str
        """
        if network_type is None:
            raise ValueError("Invalid value for `network_type`, must not be `None`")  # noqa: E501

        self._network_type = network_type

    @property
    def segment_type(self) -> str:
        """Gets the segment_type of this AllocateParameters.

        The isolated segment for the virtualised network.  # noqa: E501

        :return: The segment_type of this AllocateParameters.
        :rtype: str
        """
        return self._segment_type

    @segment_type.setter
    def segment_type(self, segment_type: str):
        """Sets the segment_type of this AllocateParameters.

        The isolated segment for the virtualised network.  # noqa: E501

        :param segment_type: The segment_type of this AllocateParameters.
        :type segment_type: str
        """
        if segment_type is None:
            raise ValueError("Invalid value for `segment_type`, must not be `None`")  # noqa: E501

        self._segment_type = segment_type

    @property
    def network_qo_s(self) -> str:
        """Gets the network_qo_s of this AllocateParameters.

        Element providing information about Quality of Service attributes that the network shall support.  # noqa: E501

        :return: The network_qo_s of this AllocateParameters.
        :rtype: str
        """
        return self._network_qo_s

    @network_qo_s.setter
    def network_qo_s(self, network_qo_s: str):
        """Sets the network_qo_s of this AllocateParameters.

        Element providing information about Quality of Service attributes that the network shall support.  # noqa: E501

        :param network_qo_s: The network_qo_s of this AllocateParameters.
        :type network_qo_s: str
        """
        if network_qo_s is None:
            raise ValueError("Invalid value for `network_qo_s`, must not be `None`")  # noqa: E501

        self._network_qo_s = network_qo_s

    @property
    def is_shared(self) -> bool:
        """Gets the is_shared of this AllocateParameters.

        It defines whether the virtualised network is shared among consumers.  # noqa: E501

        :return: The is_shared of this AllocateParameters.
        :rtype: bool
        """
        return self._is_shared

    @is_shared.setter
    def is_shared(self, is_shared: bool):
        """Sets the is_shared of this AllocateParameters.

        It defines whether the virtualised network is shared among consumers.  # noqa: E501

        :param is_shared: The is_shared of this AllocateParameters.
        :type is_shared: bool
        """
        if is_shared is None:
            raise ValueError("Invalid value for `is_shared`, must not be `None`")  # noqa: E501

        self._is_shared = is_shared

    @property
    def sharing_criteria(self) -> str:
        """Gets the sharing_criteria of this AllocateParameters.

        Only present for shared networks. Indicate the sharing criteria for this network. These criteria might be a list of authorized consumers.  # noqa: E501

        :return: The sharing_criteria of this AllocateParameters.
        :rtype: str
        """
        return self._sharing_criteria

    @sharing_criteria.setter
    def sharing_criteria(self, sharing_criteria: str):
        """Sets the sharing_criteria of this AllocateParameters.

        Only present for shared networks. Indicate the sharing criteria for this network. These criteria might be a list of authorized consumers.  # noqa: E501

        :param sharing_criteria: The sharing_criteria of this AllocateParameters.
        :type sharing_criteria: str
        """
        if sharing_criteria is None:
            raise ValueError("Invalid value for `sharing_criteria`, must not be `None`")  # noqa: E501

        self._sharing_criteria = sharing_criteria

    @property
    def layer3_attributes(self) -> str:
        """Gets the layer3_attributes of this AllocateParameters.

        The attribute allows setting up a network providing defined layer 3 connectivity.  # noqa: E501

        :return: The layer3_attributes of this AllocateParameters.
        :rtype: str
        """
        return self._layer3_attributes

    @layer3_attributes.setter
    def layer3_attributes(self, layer3_attributes: str):
        """Sets the layer3_attributes of this AllocateParameters.

        The attribute allows setting up a network providing defined layer 3 connectivity.  # noqa: E501

        :param layer3_attributes: The layer3_attributes of this AllocateParameters.
        :type layer3_attributes: str
        """
        if layer3_attributes is None:
            raise ValueError("Invalid value for `layer3_attributes`, must not be `None`")  # noqa: E501

        self._layer3_attributes = layer3_attributes

    @property
    def port_type(self) -> str:
        """Gets the port_type of this AllocateParameters.

        Type of network port.  # noqa: E501

        :return: The port_type of this AllocateParameters.
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type: str):
        """Sets the port_type of this AllocateParameters.

        Type of network port.  # noqa: E501

        :param port_type: The port_type of this AllocateParameters.
        :type port_type: str
        """
        if port_type is None:
            raise ValueError("Invalid value for `port_type`, must not be `None`")  # noqa: E501

        self._port_type = port_type

    @property
    def network_id(self) -> str:
        """Gets the network_id of this AllocateParameters.

        Identifier of the network that the port belongs to.  # noqa: E501

        :return: The network_id of this AllocateParameters.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id: str):
        """Sets the network_id of this AllocateParameters.

        Identifier of the network that the port belongs to.  # noqa: E501

        :param network_id: The network_id of this AllocateParameters.
        :type network_id: str
        """
        if network_id is None:
            raise ValueError("Invalid value for `network_id`, must not be `None`")  # noqa: E501

        self._network_id = network_id

    @property
    def segment_id(self) -> str:
        """Gets the segment_id of this AllocateParameters.

        The isolated segment the network port belongs to.  # noqa: E501

        :return: The segment_id of this AllocateParameters.
        :rtype: str
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id: str):
        """Sets the segment_id of this AllocateParameters.

        The isolated segment the network port belongs to.  # noqa: E501

        :param segment_id: The segment_id of this AllocateParameters.
        :type segment_id: str
        """
        if segment_id is None:
            raise ValueError("Invalid value for `segment_id`, must not be `None`")  # noqa: E501

        self._segment_id = segment_id

    @property
    def ingress_point_ip_address(self) -> str:
        """Gets the ingress_point_ip_address of this AllocateParameters.

        The ingress point IP Address.  # noqa: E501

        :return: The ingress_point_ip_address of this AllocateParameters.
        :rtype: str
        """
        return self._ingress_point_ip_address

    @ingress_point_ip_address.setter
    def ingress_point_ip_address(self, ingress_point_ip_address: str):
        """Sets the ingress_point_ip_address of this AllocateParameters.

        The ingress point IP Address.  # noqa: E501

        :param ingress_point_ip_address: The ingress_point_ip_address of this AllocateParameters.
        :type ingress_point_ip_address: str
        """
        if ingress_point_ip_address is None:
            raise ValueError("Invalid value for `ingress_point_ip_address`, must not be `None`")  # noqa: E501

        self._ingress_point_ip_address = ingress_point_ip_address

    @property
    def ingress_point_port_address(self) -> str:
        """Gets the ingress_point_port_address of this AllocateParameters.

        The ingress point Port(interface) Address.  # noqa: E501

        :return: The ingress_point_port_address of this AllocateParameters.
        :rtype: str
        """
        return self._ingress_point_port_address

    @ingress_point_port_address.setter
    def ingress_point_port_address(self, ingress_point_port_address: str):
        """Sets the ingress_point_port_address of this AllocateParameters.

        The ingress point Port(interface) Address.  # noqa: E501

        :param ingress_point_port_address: The ingress_point_port_address of this AllocateParameters.
        :type ingress_point_port_address: str
        """
        if ingress_point_port_address is None:
            raise ValueError("Invalid value for `ingress_point_port_address`, must not be `None`")  # noqa: E501

        self._ingress_point_port_address = ingress_point_port_address

    @property
    def egress_point_ip_address(self) -> str:
        """Gets the egress_point_ip_address of this AllocateParameters.

        The engress point IP Address.  # noqa: E501

        :return: The egress_point_ip_address of this AllocateParameters.
        :rtype: str
        """
        return self._egress_point_ip_address

    @egress_point_ip_address.setter
    def egress_point_ip_address(self, egress_point_ip_address: str):
        """Sets the egress_point_ip_address of this AllocateParameters.

        The engress point IP Address.  # noqa: E501

        :param egress_point_ip_address: The egress_point_ip_address of this AllocateParameters.
        :type egress_point_ip_address: str
        """

        self._egress_point_ip_address = egress_point_ip_address

    @property
    def egress_point_port_address(self) -> str:
        """Gets the egress_point_port_address of this AllocateParameters.

        The engress point Port(interface) Address.  # noqa: E501

        :return: The egress_point_port_address of this AllocateParameters.
        :rtype: str
        """
        return self._egress_point_port_address

    @egress_point_port_address.setter
    def egress_point_port_address(self, egress_point_port_address: str):
        """Sets the egress_point_port_address of this AllocateParameters.

        The engress point Port(interface) Address.  # noqa: E501

        :param egress_point_port_address: The egress_point_port_address of this AllocateParameters.
        :type egress_point_port_address: str
        """
        if egress_point_port_address is None:
            raise ValueError("Invalid value for `egress_point_port_address`, must not be `None`")  # noqa: E501

        self._egress_point_port_address = egress_point_port_address

    @property
    def wan_link_id(self) -> str:
        """Gets the wan_link_id of this AllocateParameters.

        The logical link ID between two nodes.  # noqa: E501

        :return: The wan_link_id of this AllocateParameters.
        :rtype: str
        """
        return self._wan_link_id

    @wan_link_id.setter
    def wan_link_id(self, wan_link_id: str):
        """Sets the wan_link_id of this AllocateParameters.

        The logical link ID between two nodes.  # noqa: E501

        :param wan_link_id: The wan_link_id of this AllocateParameters.
        :type wan_link_id: str
        """
        if wan_link_id is None:
            raise ValueError("Invalid value for `wan_link_id`, must not be `None`")  # noqa: E501

        self._wan_link_id = wan_link_id
