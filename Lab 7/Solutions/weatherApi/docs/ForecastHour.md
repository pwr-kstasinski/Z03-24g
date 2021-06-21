# ForecastHour


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ts** | **float** | Unix Timestamp | [optional] 
**timestamp_local** | **str** | Timestamp in local time | [optional] 
**timestamp_utc** | **str** | Timestamp UTC | [optional] 
**datetime** | **str** | Date in format \&quot;YYYY-MM-DD:HH\&quot;. All datetime is in (UTC) | [optional] 
**snow** | **float** | Accumulated snowfall since last forecast point - Default (mm) | [optional] 
**snow_depth** | **float** | Snow depth - Default (mm) | [optional] 
**snow6h** | **float** | 6 hour accumulated snowfall. Default (mm) | [optional] 
**precip** | **float** | Accumulated precipitation since last forecast point. Default (mm) | [optional] 
**temp** | **float** | Temperature - Default (C) | [optional] 
**dewpt** | **float** | Dewpoint - Default (C) | [optional] 
**app_temp** | **float** | Apparent Temperature - Default (C) | [optional] 
**rh** | **int** | Relative Humidity as a percentage (%) | [optional] 
**clouds** | **int** | Cloud cover as a percentage (%) | [optional] 
**weather** | [**ForecastHourWeather**](ForecastHourWeather.md) |  | [optional] 
**slp** | **float** | Mean Sea level pressure (mb) | [optional] 
**pres** | **float** | Pressure (mb) | [optional] 
**uv** | **float** | UV Index | [optional] 
**solar_rad** | **float** | Estimated solar radiation (W/m^2) | [optional] 
**ghi** | **float** | Global horizontal solar irradiance (W/m^2) | [optional] 
**dhi** | **float** | Diffuse normal solar irradiance (W/m^2) | [optional] 
**dni** | **float** | Direct normal solar irradiance (W/m^2) | [optional] 
**vis** | **float** | Visibility - Default (KM) | [optional] 
**pod** | **str** | Part of day (d &#x3D; day, n &#x3D; night) | [optional] 
**pop** | **float** | Chance of Precipitation as a percentage (%) | [optional] 
**wind_spd** | **float** | Wind Speed - Default (m/s) | [optional] 
**wind_dir** | **int** | Wind direction | [optional] 
**wind_cdir** | **str** | Cardinal wind direction | [optional] 
**wind_cdir_full** | **str** | Cardinal wind direction (text) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


