# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api.models.base_model_ import Model
from api.models.api_response import ApiResponse  # noqa: F401,E501
from api import util


class AllAgents(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, error: int=None, message: str=None, data: object=None):  # noqa: E501
        """AllAgents - a model defined in Swagger

        :param error: The error of this AllAgents.  # noqa: E501
        :type error: int
        :param message: The message of this AllAgents.  # noqa: E501
        :type message: str
        :param data: The data of this AllAgents.  # noqa: E501
        :type data: object
        """
        self.swagger_types = {
            'error': int,
            'message': str,
            'data': object
        }

        self.attribute_map = {
            'error': 'error',
            'message': 'message',
            'data': 'data'
        }

        self._error = error
        self._message = message
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'AllAgents':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllAgents of this AllAgents.  # noqa: E501
        :rtype: AllAgents
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self) -> int:
        """Gets the error of this AllAgents.


        :return: The error of this AllAgents.
        :rtype: int
        """
        return self._error

    @error.setter
    def error(self, error: int):
        """Sets the error of this AllAgents.


        :param error: The error of this AllAgents.
        :type error: int
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def message(self) -> str:
        """Gets the message of this AllAgents.


        :return: The message of this AllAgents.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this AllAgents.


        :param message: The message of this AllAgents.
        :type message: str
        """

        self._message = message

    @property
    def data(self) -> object:
        """Gets the data of this AllAgents.


        :return: The data of this AllAgents.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data: object):
        """Sets the data of this AllAgents.


        :param data: The data of this AllAgents.
        :type data: object
        """

        self._data = data