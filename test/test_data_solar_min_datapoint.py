# coding: utf-8

"""
    Solar0 REST Interface for adapters

    REST Interface for communication with adapters

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from solar0_python_sdk.models.data_solar_min_datapoint import DataSolarMinDatapoint

class TestDataSolarMinDatapoint(unittest.TestCase):
    """DataSolarMinDatapoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataSolarMinDatapoint:
        """Test DataSolarMinDatapoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataSolarMinDatapoint`
        """
        model = DataSolarMinDatapoint()
        if include_optional:
            return DataSolarMinDatapoint(
                inverter = solar0_python_sdk.models.data/solar_inverter.data.SolarInverter(
                    group = '', 
                    id = '', 
                    name = '', 
                    power = 1.337, ),
                pac = 1.337,
                pdc = 1.337,
                temperature = 1.337,
                time = ''
            )
        else:
            return DataSolarMinDatapoint(
                inverter = solar0_python_sdk.models.data/solar_inverter.data.SolarInverter(
                    group = '', 
                    id = '', 
                    name = '', 
                    power = 1.337, ),
                pac = 1.337,
                pdc = 1.337,
                time = '',
        )
        """

    def testDataSolarMinDatapoint(self):
        """Test DataSolarMinDatapoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
