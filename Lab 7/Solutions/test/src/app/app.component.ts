import { Component, OnInit } from '@angular/core';
import { Class16DayDailyForecastService, Class120HourHourlyForecastService, ForecastDay, ForecastHourly, ForecastHour} from '../../../apiclient';
import { FormControl } from '@angular/forms';
import { environment } from '../environments/environment';
import { BehaviorSubject } from 'rxjs';
import { debounceTime } from 'rxjs/operators';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  Viewpoint = Viewpoint;
  city = new FormControl('');

  daily: ForecastDay;
  hourly: ForecastHourly;
  currentViewpoint: Viewpoint;

  selectedDay: Date;

  constructor(private dailySerwajs: Class16DayDailyForecastService,
              private hourlySerwajs: Class120HourHourlyForecastService) {
  }

  ngOnInit(): void {
    this.currentViewpoint = Viewpoint.Neutral;
  }


  search(): void {
    this.dailySerwajs.forecastDailyGet(this.city.value, environment.API_KEY).subscribe((data) => {
      if (data !== null) {
        this.daily = data;
        this.daily.data = this.daily.data.slice(0, 3);
        this.city.setValue(this.daily.city_name);
        this.currentViewpoint = Viewpoint.Daily;
      } else {
        this.currentViewpoint = Viewpoint.Neutral;
        window.alert(`The city was not found: ${this.city.value}`);
      }
    });
  }

  getDate(str: string): Date {
    return new Date(str);
  }

  async temperatures(dateString: string): Promise<void> {
    if (!this.hourly || this.hourly.country_code !== this.daily.country_code) {
      this.hourly = await new Promise((res, rej) => {
        this.hourlySerwajs.forecastHourlyGet(this.daily.city_name, environment.API_KEY).subscribe(
          (data) => res(data),
          err => res(null),
        );
      });
    }

    if (this.hourly !== null) {
      this.selectedDay = new Date(dateString);
      this.currentViewpoint = Viewpoint.Hourly;
    } else {
      window.alert('We were unable to download hourly temperature');
    }
  }

  Hourtemp(): Array<ForecastHour> {
    return this.hourly.data.filter(({ timestamp_local }) => this.selectedDay.getTime() === new Date(timestamp_local.slice(0, 10)).getTime());
  }

  TempBars(temp: number): { 'height': string, 'background-position': string } {
    return {
      'height': Math.trunc(temp) + 30 + 'px',
      'background-position': Math.trunc(temp) + 10 + '%',
    };
  }

}

enum Viewpoint {
  Neutral,
  Daily,
  Hourly
}