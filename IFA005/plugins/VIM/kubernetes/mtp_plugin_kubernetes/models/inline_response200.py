# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mtp_plugin_kubernetes.models.base_model_ import Model
from mtp_plugin_kubernetes.models.gateways import Gateways  # noqa: F401,E501
from mtp_plugin_kubernetes.models.virtual_links import VirtualLinks  # noqa: F401,E501
from mtp_plugin_kubernetes import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, gateways: Gateways=None, virtual_links: VirtualLinks=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param gateways: The gateways of this InlineResponse200.  # noqa: E501
        :type gateways: Gateways
        :param virtual_links: The virtual_links of this InlineResponse200.  # noqa: E501
        :type virtual_links: VirtualLinks
        """
        self.swagger_types = {
            'gateways': Gateways,
            'virtual_links': VirtualLinks
        }

        self.attribute_map = {
            'gateways': 'Gateways',
            'virtual_links': 'virtualLinks'
        }

        self._gateways = gateways
        self._virtual_links = virtual_links

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gateways(self) -> Gateways:
        """Gets the gateways of this InlineResponse200.


        :return: The gateways of this InlineResponse200.
        :rtype: Gateways
        """
        return self._gateways

    @gateways.setter
    def gateways(self, gateways: Gateways):
        """Sets the gateways of this InlineResponse200.


        :param gateways: The gateways of this InlineResponse200.
        :type gateways: Gateways
        """

        self._gateways = gateways

    @property
    def virtual_links(self) -> VirtualLinks:
        """Gets the virtual_links of this InlineResponse200.


        :return: The virtual_links of this InlineResponse200.
        :rtype: VirtualLinks
        """
        return self._virtual_links

    @virtual_links.setter
    def virtual_links(self, virtual_links: VirtualLinks):
        """Sets the virtual_links of this InlineResponse200.


        :param virtual_links: The virtual_links of this InlineResponse200.
        :type virtual_links: VirtualLinks
        """

        self._virtual_links = virtual_links
