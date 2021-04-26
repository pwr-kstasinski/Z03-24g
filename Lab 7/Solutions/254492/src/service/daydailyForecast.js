/** @module daydailyForecast */
// Auto-generated, edits will be overwritten
import * as gateway from './gateway'

/**
 * Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format "YYYY-MM-DD". One day begins at 00:00 UTC, and ends at 23:59 UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate.
 * 
 * @param {string} city City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
 * @param {string} key Your registered API key.
 * @param {object} options Optional options
 * @param {string} [options.state] Full name of state.
 * @param {string} [options.country] Country Code (2 letter).
 * @param {number} [options.days] Number of days to return. Default 16.
 * @param {string} [options.units] Enum: S, I. Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
 * @param {string} [options.lang] Enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw. Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
 * @param {string} [options.callback] Wraps return in jsonp callback. Example - callback=func
 * @return {Promise<module:types.ForecastDay>} A forecast object.
 */
export function getForecastDaily(city, key, options) {
  if (!options) options = {}
  const parameters = {
    query: {
      city,
      state: options.state,
      country: options.country,
      days: options.days,
      units: options.units,
      lang: options.lang,
      callback: options.callback,
      key
    }
  }
  return gateway.request(getForecastDailyOperation, parameters)
}

const getForecastDailyOperation = {
  path: '/forecast/daily',
  method: 'get'
}
