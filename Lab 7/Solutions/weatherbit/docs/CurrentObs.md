# CurrentObs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city_name** | **str** | City name (closest) | [optional] 
**state_code** | **str** | State abbreviation | [optional] 
**country_code** | **str** | Country abbreviation | [optional] 
**timezone** | **str** | Local IANA time zone | [optional] 
**lat** | **float** | Latitude | [optional] 
**lon** | **float** | Longitude | [optional] 
**station** | **str** | Source Station ID | [optional] 
**vis** | **int** | Visibility - default (M) | [optional] 
**rh** | **int** | Relative humidity (%) | [optional] 
**dewpt** | **float** | Dew point temperature - default (C) | [optional] 
**wind_dir** | **int** | Wind direction (degrees) | [optional] 
**wind_cdir** | **str** | Cardinal wind direction | [optional] 
**wind_cdir_full** | **str** | Cardinal wind direction (text) | [optional] 
**wind_speed** | **float** | Wind speed - Default (m/s) | [optional] 
**temp** | **float** | Temperature - Default (C) | [optional] 
**app_temp** | **float** | Apparent temperature - Default (C) | [optional] 
**clouds** | **int** | Cloud cover (%) | [optional] 
**weather** | [**CurrentObsWeather**](CurrentObsWeather.md) |  | [optional] 
**datetime** | **str** | Cycle Hour (UTC) of observation | [optional] 
**ob_time** | **str** | Full time (UTC) of observation (YYYY-MM-DD HH:MM) | [optional] 
**ts** | **float** | Unix Timestamp | [optional] 
**sunrise** | **str** | Time (UTC) of Sunrise (HH:MM) | [optional] 
**sunset** | **str** | Time (UTC) of Sunset (HH:MM) | [optional] 
**slp** | **float** | Mean sea level pressure in millibars (mb) | [optional] 
**pres** | **float** | Pressure (mb) | [optional] 
**aqi** | **float** | Air quality index (US EPA standard 0 to +500) | [optional] 
**uv** | **float** | UV Index | [optional] 
**solar_rad** | **float** | Estimated solar radiation (W/m^2) | [optional] 
**ghi** | **float** | Global horizontal irradiance (W/m^2) | [optional] 
**dni** | **float** | Direct normal irradiance (W/m^2) | [optional] 
**dhi** | **float** | Diffuse horizontal irradiance (W/m^2) | [optional] 
**elev_angle** | **float** | Current solar elevation angle (Degrees) | [optional] 
**hour_angle** | **float** | Current solar hour angle (Degrees) | [optional] 
**pod** | **str** | Part of the day (d &#x3D; day, n &#x3D; night) | [optional] 
**precip** | **float** | Precipitation in last hour - Default (mm) | [optional] 
**snow** | **float** | Snowfall in last hour - Default (mm) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


