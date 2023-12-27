# DataSolarDayDatapoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverter** | [**DataSolarInverter**](DataSolarInverter.md) |  | 
**pac** | **float** |  | 
**pdc** | **float** |  | 
**time** | **str** |  | 

## Example

```python
from solar0_python_sdk.models.data_solar_day_datapoint import DataSolarDayDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of DataSolarDayDatapoint from a JSON string
data_solar_day_datapoint_instance = DataSolarDayDatapoint.from_json(json)
# print the JSON string representation of the object
print DataSolarDayDatapoint.to_json()

# convert the object into a dict
data_solar_day_datapoint_dict = data_solar_day_datapoint_instance.to_dict()
# create an instance of DataSolarDayDatapoint from a dict
data_solar_day_datapoint_form_dict = data_solar_day_datapoint.from_dict(data_solar_day_datapoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


