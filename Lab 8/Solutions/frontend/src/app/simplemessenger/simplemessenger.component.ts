import { Component, OnInit } from '@angular/core';
import {ApiModule, LoginService, MessengerService} from "../../../build/lab8client";
import {PartialObserver} from "rxjs";
import {HttpResponse} from "@angular/common/http";
import {toNumbers} from "@angular/compiler-cli/src/diagnostics/typescript_version";

@Component({
  selector: 'app-simplemessenger',
  templateUrl: './simplemessenger.component.html',
  styleUrls: ['./simplemessenger.component.css']
})
export class SimplemessengerComponent implements OnInit {

  loginForRegister:string = ""
  registerSuccess: string = ""
  registerError: string = ""
  loginForLogin:string = ""
  loginSuccess: string = ""
  loginError: string = ""
  sendSuccess: string = ""
  sendError: string = ""
  sendMessage: string = ""
  sendReceiver: string = ""

  actualToken: number = NaN

  messageList: any[] = []

  constructor(private loginService: LoginService, private messengerService: MessengerService) {

  }

  ngOnInit(): void {

  }

  register(login: string): void {
    this.loginService.registerPost(login, 'response').subscribe(
      (response) => {
        this.registerSuccess = "Pomyślnie zarejestrowano! Teraz proszę się zalogować"
      },
      (err) => {
        this.registerSuccess = "Nie udało się zarejestrować. Czy podano prawidłowy, unikalny login?"
      },
      () => {
        console.log("completed")
      }
    )
  }

  login(login: string): void {
    this.loginService.loginPost(login, 'response').subscribe(
      (response) => {
        this.loginSuccess = "Pomyślnie zalogowano! Możesz już korzystać z chatu"
        console.log(response)
        console.log(response.body)
        this.actualToken = toNumbers(response.body)[0]
        console.log(this.actualToken)
      },
      (err) => {
        this.loginSuccess = "Nie udało się zalogować. Czy podano prawidłowy, wcześniej zarejestrowany login?"
      },
      () => {
        console.log("completed")
      }
    )
  }

  refresh(): void {
    this.messengerService.receiveGet(this.actualToken).subscribe(
      (response) => {
        console.log(response)
        let list: Array<string> = JSON.parse(response)
        console.log(list)
        list.forEach((value: any) => {
          this.messageList.push(value)
        })

      },
      (err) => {
        console.log(err)
      },
      () => {
        console.log("completed")
      }
    )
  }

  send(message: string, receiverLogin: string): void {
    console.log("message = " + message)
    console.log("receiverLogin = " + receiverLogin)
    if (receiverLogin == "")
    {
      this.messengerService.sendPost(this.actualToken, message).subscribe(
        (response) => {

          this.sendSuccess = "Wiadomość wysłano"
        },
        (err) => {
          this.sendError = "Błąd wysłania wiadomości"
        },
        () => {
          console.log("completed")
        }
      )
    }
    else
    {
      this.messengerService.sendPost(this.actualToken, message, receiverLogin).subscribe(
        (response) => {

          this.sendSuccess = "Wiadomość wysłano"
        },
        (err) => {
          this.sendError = "Błąd wysłania wiadomości"
        },
        () => {
          console.log("completed")
        }
      )
    }
  }



}
