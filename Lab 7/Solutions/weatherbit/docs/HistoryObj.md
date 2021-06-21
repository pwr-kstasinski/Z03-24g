# HistoryObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ts** | **float** | Unix Timestamp | [optional] 
**timestamp_local** | **str** | Timestamp in local time | [optional] 
**timestamp_utc** | **str** | Timestamp UTC | [optional] 
**datetime** | **str** | Date in format \&quot;YYYY-MM-DD:HH\&quot;. All datetime is in (UTC) | [optional] 
**slp** | **float** | Sea level pressure (mb) | [optional] 
**pres** | **float** | Pressure (mb) | [optional] 
**rh** | **int** | Relative Humidity as a percentage (%) | [optional] 
**dewpt** | **int** | Dew point (Default Celcius) | [optional] 
**temp** | **float** | Temperature (Default Celcius) | [optional] 
**wind_spd** | **float** | Wind Speed (Default m/s) | [optional] 
**wind_dir** | **int** | Wind direction (Degrees) | [optional] 
**uv** | **float** | UV Index (1-11+) | [optional] 
**solar_rad** | **float** | Estimated solar radiation (W/m^2) | [optional] 
**ghi** | **float** | Global horizontal solar irradiance (W/m^2) | [optional] 
**dhi** | **float** | Diffuse normal solar irradiance (W/m^2) | [optional] 
**dni** | **float** | Direct normal solar irradiance (W/m^2) | [optional] 
**h_angle** | **float** | Solar hour angle (Degrees) | [optional] 
**elev_angle** | **float** | Solar elevation angle (Degrees) | [optional] 
**pod** | **str** | Part of the day (d &#x3D; day, n &#x3D; night) | [optional] 
**weather** | [**HistoryObjWeather**](HistoryObjWeather.md) |  | [optional] 
**precip** | **float** | Liquid equivalent precipitation - Default (mm) | [optional] 
**snow** | **float** | Snowfall - Default (mm) | [optional] 
**snow6h** | **float** | Snowfall in last 6 hours - Default (mm) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


