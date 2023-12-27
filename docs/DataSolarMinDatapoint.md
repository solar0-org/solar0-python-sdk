# DataSolarMinDatapoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverter** | [**DataSolarInverter**](DataSolarInverter.md) |  | 
**pac** | **float** |  | 
**pdc** | **float** |  | 
**temperature** | **float** |  | [optional] 
**time** | **str** |  | 

## Example

```python
from solar0_python_sdk.models.data_solar_min_datapoint import DataSolarMinDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of DataSolarMinDatapoint from a JSON string
data_solar_min_datapoint_instance = DataSolarMinDatapoint.from_json(json)
# print the JSON string representation of the object
print DataSolarMinDatapoint.to_json()

# convert the object into a dict
data_solar_min_datapoint_dict = data_solar_min_datapoint_instance.to_dict()
# create an instance of DataSolarMinDatapoint from a dict
data_solar_min_datapoint_form_dict = data_solar_min_datapoint.from_dict(data_solar_min_datapoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


