/** @module types */
// Auto-generated, edits will be overwritten

/**
 * @typedef ForecastHour
 * @memberof module:types
 * 
 * @property {number} ts Unix Timestamp
 * @property {string} timestamp_local Timestamp in local time
 * @property {string} timestamp_utc Timestamp UTC
 * @property {string} datetime Date in format "YYYY-MM-DD:HH". All datetime is in (UTC)
 * @property {number} snow Accumulated snowfall since last forecast point - Default (mm)
 * @property {number} snow_depth Snow depth - Default (mm)
 * @property {number} snow6h 6 hour accumulated snowfall. Default (mm)
 * @property {number} precip Accumulated precipitation since last forecast point. Default (mm)
 * @property {number} temp Temperature - Default (C)
 * @property {number} dewpt Dewpoint - Default (C)
 * @property {number} app_temp Apparent Temperature - Default (C)
 * @property {number} rh Relative Humidity as a percentage (%)
 * @property {number} clouds Cloud cover as a percentage (%)
 * @property {object} weather 
 * @property {number} slp Mean Sea level pressure (mb)
 * @property {number} pres Pressure (mb)
 * @property {number} uv UV Index
 * @property {number} solar_rad Estimated solar radiation (W/m^2)
 * @property {number} ghi Global horizontal solar irradiance (W/m^2)
 * @property {number} dhi Diffuse normal solar irradiance (W/m^2)
 * @property {number} dni Direct normal solar irradiance (W/m^2)
 * @property {number} vis Visibility - Default (KM)
 * @property {string} pod Part of day (d = day, n = night)
 * @property {number} pop Chance of Precipitation as a percentage (%)
 * @property {number} wind_spd Wind Speed - Default (m/s)
 * @property {number} wind_dir Wind direction
 * @property {string} wind_cdir Cardinal wind direction
 * @property {string} wind_cdir_full Cardinal wind direction (text)
 */

/**
 * @typedef Forecast
 * @memberof module:types
 * 
 * @property {number} ts Unix Timestamp
 * @property {string} timestamp_local Timestamp in local time
 * @property {string} timestamp_utc Timestamp UTC
 * @property {string} datetime Date in format "YYYY-MM-DD:HH". All datetime is in (UTC)
 * @property {number} snow Accumulated snowfall since last forecast point - default (mm)
 * @property {number} snow_depth Snow Depth - default (mm)
 * @property {number} precip Accumulated precipitation since last forecast point - default (mm)
 * @property {number} temp Temperature (Average) - default (C)
 * @property {number} dewpt Dewpoint (Average) - default (C)
 * @property {number} max_temp Maximum daily Temperature - default (C)
 * @property {number} min_temp Minimum daily Temperature - default (C)
 * @property {number} app_max_temp Apparent Maximum daily Temperature - default (C)
 * @property {number} app_min_temp Apparent Minimum daily Temperature - default (C)
 * @property {number} rh Relative Humidity as a percentage (%)
 * @property {number} clouds Cloud cover as a percentage (%)
 * @property {object} weather 
 * @property {number} slp Mean Sea level pressure (mb)
 * @property {number} pres Pressure (mb)
 * @property {number} uv UV Index
 * @property {number} max_dhi [Deprecated] Max direct component of solar insolation (W/m^2)
 * @property {number} vis Average Visibility default (KM)
 * @property {number} pop Chance of Precipitation as a percentage (%)
 * @property {number} moon_phase Moon phase
 * @property {number} sunrise_ts Sunrise unix timestamp
 * @property {number} sunset_ts Sunset unix timestamp
 * @property {number} moonrise_ts Moonrise unix timestamp
 * @property {number} moonset_ts Moonset unix timestamp
 * @property {string} pod Part of the day (d = day, n = night)
 * @property {number} wind_spd Wind Speed (default m/s)
 * @property {number} wind_dir Wind direction
 * @property {string} wind_cdir Cardinal wind direction
 * @property {string} wind_cdir_full Cardinal wind direction (text)
 */

/**
 * @typedef ForecastDay
 * @memberof module:types
 * 
 * @property {string} city_name City Name
 * @property {string} state_code State Abbreviation
 * @property {string} country_code Country Abbreviation
 * @property {string} lat Latitude
 * @property {string} lon Longitude
 * @property {string} timezone Local IANA time zone
 * @property {module:types.Forecast[]} data 
 */

/**
 * @typedef ForecastHourly
 * @memberof module:types
 * 
 * @property {string} city_name City Name
 * @property {string} state_code State Abbreviation
 * @property {string} country_code Country Abbreviation
 * @property {string} lat Latitude
 * @property {string} lon Longitude
 * @property {string} timezone Local IANA time zone
 * @property {module:types.ForecastHour[]} data 
 */

/**
 * @typedef Error
 * @memberof module:types
 * 
 * @property {number} code 
 * @property {string} message 
 */
