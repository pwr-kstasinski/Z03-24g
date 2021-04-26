<template>
  <div>
    <span class="h2" style="color: #2fb543"> Miejscowość: </span>
    <input
      type="text"
      class="h2"
      v-model="city"
      @keyup.enter="getDailyForecast"
    />
    <button class="h2" @click="getDailyForecast">Szukaj</button>
    <p class="h2" v-if="forecastDaily && forecastDaily.length">
      Temperatura dla {{ city_stable }}
    </p>
    <p class="h2" v-if="!isCityCorrect" style="color: #cf0000">
      Niepoprawna nazwa miasta
    </p>
    <ul class="d-flex justify-content-center">
      <li
        style="list-style: none"
        v-for="(weather, index) in dailyForecast"
        :key="index"
      >
        <div
          class="card mx-3"
          style="width: 10rem"
          @click="getHourlyForecast(weather.datetime)"
        >
          <img
            :src="imagePicker(weather.weather.icon)"
            class="card-img-top"
            alt="..."
          />
          <div class="card-body">
            <p class="card-text">{{ weather.datetime }}</p>
            <h1 class="card-text">{{ weather.max_temp }}°C</h1>
            <p class="card-text">
              {{ weather.min_temp }}°C <br />
              Opad: {{ weather.pop }}%
            </p>
          </div>
        </div>
      </li>
    </ul>
    <p
      v-if="forecastHourly && forecastHourly.length"
      style="font-size: 25px; text-align: center"
    >
      Godzinowa prognoza pogody na dzień: {{ actDate }}
    </p>
    <div style="display: flex; align-items: center; justify-content: center">
      <TempChart
        v-if="hourlyForecast.length"
        :data="hourlyForecastTemp"
        :labels="hourlyForecastHour"
        :key="key"
      />
    </div>
  </div>
</template>

<script>
import { getForecastDaily } from "../service/daydailyForecast.js";
import { getForecastHourly } from "../service/hourhourlyForecast.js";
import TempChart from "./chart.vue";

export default {
  name: "Weather",
  components: {
    TempChart,
  },
  data() {
    return {
      forecastHourly: null,
      forecastDaily: null,
      city: "",
      city_stable: "",
      howManyDays: 3,
      actDate: "",
      isCityCorrect: true,
    };
  },

  computed: {
    dailyForecast() {
      if (this.forecastDaily) {
        return this.forecastDaily.slice(0, this.howManyDays);
      }
      return [];
    },
    hourlyForecast() {
      if (this.forecastHourly) {
        return this.forecastHourly;
      }
      return [];
    },
    hourlyForecastTemp() {
      return this.hourlyForecast.map((x) => {
        return x.temp;
      });
    },
    hourlyForecastHour() {
      return this.hourlyForecast.map((x) => {
        return x.hour;
      });
    },
  },

  methods: {
    imagePicker(iconCode) {
      return "https://www.weatherbit.io/static/img/icons/" + iconCode + ".png";
    },
    async getDailyForecast() {
      this.isCityCorrect = true;
      this.forecastDaily = [];
      this.forecastHourly = [];
      try {
        const dataDaily = await getForecastDaily(
          this.city,
          "aadaae20db4e40b682a9b0144dabb9d8"
        );
        this.city_stable = this.city;
        const weatherInfo = dataDaily.data.data;
        return (this.forecastDaily = weatherInfo.map((weather) => {
          return {
            max_temp: weather.max_temp,
            min_temp: weather.min_temp,
            pop: weather.pop,
            weather: weather.weather,
            datetime: weather.datetime,
          };
        }));
      } catch (err) {
        console.log(err);
        this.isCityCorrect = false;
      }
    },
    async getHourlyForecast(datetime) {
      this.actDate = "";
      this.forecastHourly = [];
      try {
        const dataHourly = await getForecastHourly(
          this.city_stable,
          "aadaae20db4e40b682a9b0144dabb9d8"
        );
        const weatherInfo = dataHourly.data.data;
        this.actDate = datetime;
        const currentDateForecast = weatherInfo
          .filter((weather) => {
            return weather.datetime.slice(0, -3) == datetime;
          })
          .map((weather) => {
            return {
              hour: weather.datetime.slice(weather.datetime.length - 2),
              temp: weather.temp,
            };
          });
        this.forecastHourly = currentDateForecast;
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style>
h1 {
  color: blue;
  font-family: verdana;
  font-size: 25px;
  text-align: center;
}
</style>