/**
 * Weatherbit.io - Swagger UI Weather API documentation
 * This is the documentation for the Weatherbit Weather API.  The base URL for the API is [http://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/) or [https://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/). Below is the Swagger UI documentation for the API. All API requests require the `key` parameter.        An Example for a 5 day forecast for London, UK would be `http://api.weatherbit.io/v2.0/forecast/3hourly?city=London`&`country=UK`. See our [Weather API description page](https://www.weatherbit.io/api) for additional documentation.
 *
 * The version of the OpenAPI document: 2.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
/* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent, HttpParameterCodec }       from '@angular/common/http';
import { CustomHttpParameterCodec }                          from '../encoder';
import { Observable }                                        from 'rxjs';

import { ForecastHourly } from '../model/models';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';
import {
    Class120HourHourlyForecastServiceInterface
} from './class120HourHourlyForecast.serviceInterface';



@Injectable({
  providedIn: 'root'
})
export class Class120HourHourlyForecastService implements Class120HourHourlyForecastServiceInterface {

    protected basePath = 'https://api.weatherbit.io/v2.0';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();
    public encoder: HttpParameterCodec;

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (configuration) {
            this.configuration = configuration;
        }
        if (typeof this.configuration.basePath !== 'string') {
            if (typeof basePath !== 'string') {
                basePath = this.basePath;
            }
            this.configuration.basePath = basePath;
        }
        this.encoder = this.configuration.encoder || new CustomHttpParameterCodec();
    }


    private addToHttpParams(httpParams: HttpParams, value: any, key?: string): HttpParams {
        if (typeof value === "object" && value instanceof Date === false) {
            httpParams = this.addToHttpParamsRecursive(httpParams, value);
        } else {
            httpParams = this.addToHttpParamsRecursive(httpParams, value, key);
        }
        return httpParams;
    }

    private addToHttpParamsRecursive(httpParams: HttpParams, value?: any, key?: string): HttpParams {
        if (value == null) {
            return httpParams;
        }

        if (typeof value === "object") {
            if (Array.isArray(value)) {
                (value as any[]).forEach( elem => httpParams = this.addToHttpParamsRecursive(httpParams, elem, key));
            } else if (value instanceof Date) {
                if (key != null) {
                    httpParams = httpParams.append(key,
                        (value as Date).toISOString().substr(0, 10));
                } else {
                   throw Error("key may not be null if value is Date");
                }
            } else {
                Object.keys(value).forEach( k => httpParams = this.addToHttpParamsRecursive(
                    httpParams, value[k], key != null ? `${key}.${k}` : k));
            }
        } else if (key != null) {
            httpParams = httpParams.append(key, value);
        } else {
            throw Error("key may not be null if value is not object or array");
        }
        return httpParams;
    }

    /**
     * Returns an 120 hour (hourly forecast) - Given City and/or State, Country.
     *  Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. 
     * @param city City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR
     * @param key Your registered API key.
     * @param state Full name of state.
     * @param country Country Code (2 letter).
     * @param units Convert to units. Default Metric See &lt;a target&#x3D;\&#39;blank\&#39; href&#x3D;\&#39;/api/requests\&#39;&gt;units field description&lt;/a&gt;
     * @param lang Language (Default: English) See &lt;a target&#x3D;\&#39;blank\&#39; href&#x3D;\&#39;/api/requests\&#39;&gt;language field description&lt;/a&gt;
     * @param callback Wraps return in jsonp callback. Example: callback&#x3D;func
     * @param hours Number of hours to return.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public forecastHourlyGet(city: string, key: string, state?: string, country?: string, units?: 'S' | 'I', lang?: 'ar' | 'az' | 'be' | 'bg' | 'bs' | 'ca' | 'cs' | 'de' | 'fi' | 'fr' | 'el' | 'es' | 'et' | 'hr' | 'hu' | 'id' | 'it' | 'is' | 'kw' | 'nb' | 'nl' | 'pl' | 'pt' | 'ro' | 'ru' | 'sk' | 'sl' | 'sr' | 'sv' | 'tr' | 'uk' | 'zh' | 'zh-tw', callback?: string, hours?: number, observe?: 'body', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json'}): Observable<ForecastHourly>;
    public forecastHourlyGet(city: string, key: string, state?: string, country?: string, units?: 'S' | 'I', lang?: 'ar' | 'az' | 'be' | 'bg' | 'bs' | 'ca' | 'cs' | 'de' | 'fi' | 'fr' | 'el' | 'es' | 'et' | 'hr' | 'hu' | 'id' | 'it' | 'is' | 'kw' | 'nb' | 'nl' | 'pl' | 'pt' | 'ro' | 'ru' | 'sk' | 'sl' | 'sr' | 'sv' | 'tr' | 'uk' | 'zh' | 'zh-tw', callback?: string, hours?: number, observe?: 'response', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json'}): Observable<HttpResponse<ForecastHourly>>;
    public forecastHourlyGet(city: string, key: string, state?: string, country?: string, units?: 'S' | 'I', lang?: 'ar' | 'az' | 'be' | 'bg' | 'bs' | 'ca' | 'cs' | 'de' | 'fi' | 'fr' | 'el' | 'es' | 'et' | 'hr' | 'hu' | 'id' | 'it' | 'is' | 'kw' | 'nb' | 'nl' | 'pl' | 'pt' | 'ro' | 'ru' | 'sk' | 'sl' | 'sr' | 'sv' | 'tr' | 'uk' | 'zh' | 'zh-tw', callback?: string, hours?: number, observe?: 'events', reportProgress?: boolean, options?: {httpHeaderAccept?: 'application/json'}): Observable<HttpEvent<ForecastHourly>>;
    public forecastHourlyGet(city: string, key: string, state?: string, country?: string, units?: 'S' | 'I', lang?: 'ar' | 'az' | 'be' | 'bg' | 'bs' | 'ca' | 'cs' | 'de' | 'fi' | 'fr' | 'el' | 'es' | 'et' | 'hr' | 'hu' | 'id' | 'it' | 'is' | 'kw' | 'nb' | 'nl' | 'pl' | 'pt' | 'ro' | 'ru' | 'sk' | 'sl' | 'sr' | 'sv' | 'tr' | 'uk' | 'zh' | 'zh-tw', callback?: string, hours?: number, observe: any = 'body', reportProgress: boolean = false, options?: {httpHeaderAccept?: 'application/json'}): Observable<any> {
        if (city === null || city === undefined) {
            throw new Error('Required parameter city was null or undefined when calling forecastHourlyGet.');
        }
        if (key === null || key === undefined) {
            throw new Error('Required parameter key was null or undefined when calling forecastHourlyGet.');
        }

        let queryParameters = new HttpParams({encoder: this.encoder});
        if (city !== undefined && city !== null) {
          queryParameters = this.addToHttpParams(queryParameters,
            <any>city, 'city');
        }
        if (state !== undefined && state !== null) {
          queryParameters = this.addToHttpParams(queryParameters,
            <any>state, 'state');
        }
        if (country !== undefined && country !== null) {
          queryParameters = this.addToHttpParams(queryParameters,
            <any>country, 'country');
        }
        if (units !== undefined && units !== null) {
          queryParameters = this.addToHttpParams(queryParameters,
            <any>units, 'units');
        }
        if (lang !== undefined && lang !== null) {
          queryParameters = this.addToHttpParams(queryParameters,
            <any>lang, 'lang');
        }
        if (callback !== undefined && callback !== null) {
          queryParameters = this.addToHttpParams(queryParameters,
            <any>callback, 'callback');
        }
        if (hours !== undefined && hours !== null) {
          queryParameters = this.addToHttpParams(queryParameters,
            <any>hours, 'hours');
        }
        if (key !== undefined && key !== null) {
          queryParameters = this.addToHttpParams(queryParameters,
            <any>key, 'key');
        }

        let headers = this.defaultHeaders;

        let httpHeaderAcceptSelected: string | undefined = options && options.httpHeaderAccept;
        if (httpHeaderAcceptSelected === undefined) {
            // to determine the Accept header
            const httpHeaderAccepts: string[] = [
                'application/json'
            ];
            httpHeaderAcceptSelected = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        }
        if (httpHeaderAcceptSelected !== undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }


        let responseType: 'text' | 'json' = 'json';
        if(httpHeaderAcceptSelected && httpHeaderAcceptSelected.startsWith('text')) {
            responseType = 'text';
        }

        return this.httpClient.get<ForecastHourly>(`${this.configuration.basePath}/forecast/hourly`,
            {
                params: queryParameters,
                responseType: <any>responseType,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
