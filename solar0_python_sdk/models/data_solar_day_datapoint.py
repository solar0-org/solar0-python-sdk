# coding: utf-8

"""
    Solar0 REST Interface for adapters

    REST Interface for communication with adapters

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from solar0_python_sdk.models.data_solar_inverter import DataSolarInverter
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DataSolarDayDatapoint(BaseModel):
    """
    DataSolarDayDatapoint
    """ # noqa: E501
    inverter: DataSolarInverter
    pac: Optional[Union[StrictFloat, StrictInt]] = None
    pdc: Optional[Union[StrictFloat, StrictInt]] = None
    time: StrictStr
    __properties: ClassVar[List[str]] = ["inverter", "pac", "pdc", "time"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DataSolarDayDatapoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of inverter
        if self.inverter:
            _dict['inverter'] = self.inverter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DataSolarDayDatapoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "inverter": DataSolarInverter.from_dict(obj.get("inverter")) if obj.get("inverter") is not None else None,
            "pac": obj.get("pac"),
            "pdc": obj.get("pdc"),
            "time": obj.get("time")
        })
        return _obj


