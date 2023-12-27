# DataSolarInverter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**power** | **float** |  | [optional] 

## Example

```python
from solar0_python_sdk.models.data_solar_inverter import DataSolarInverter

# TODO update the JSON string below
json = "{}"
# create an instance of DataSolarInverter from a JSON string
data_solar_inverter_instance = DataSolarInverter.from_json(json)
# print the JSON string representation of the object
print DataSolarInverter.to_json()

# convert the object into a dict
data_solar_inverter_dict = data_solar_inverter_instance.to_dict()
# create an instance of DataSolarInverter from a dict
data_solar_inverter_form_dict = data_solar_inverter.from_dict(data_solar_inverter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


