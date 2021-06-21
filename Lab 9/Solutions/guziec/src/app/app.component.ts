import { HttpParameterCodec } from '@angular/common/http';
import { MessageCreate } from './../../apiclient/model/messageCreate';
import { BodyCreateMessageUserMessagesPost } from './../../apiclient/model/bodyCreateMessageUserMessagesPost';
import { UserCreate } from './../../apiclient/model/userCreate';
import { User } from './../../apiclient/model/user';
import { bubble } from './bubble.model';
import { Component, OnInit } from '@angular/core';
import { DefaultService, Message, UserBase} from '../../apiclient';
import { FormControl } from '@angular/forms';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  Viewpoint = Viewpoint;

  loginlogin = new FormControl('')
  loginpassword = new FormControl('')

  registerlogin = new FormControl('')
  registerpassword = new FormControl('')

  napalm = new FormControl('')
  vietcong = new FormControl('')
  
  newUser:UserCreate ={login:'',password:''}
  currentUser:User
  users: User[] = []
  activeUsers = []
  
  map = new Map<Number, string>()

  newMessage:BodyCreateMessageUserMessagesPost ={ message:{content:'',author_id: 0}, reciver:{login:''}}

  dataarr = []
  dupa: any ={}
  currentViewpoint: Viewpoint;



constructor(private api: DefaultService) {}
ngOnInit(): void {
  this.api.readUsersUserGet().subscribe((data)=>{
    if (data !== null){
      this.users = data;
    }
  });
  this.users.forEach(user =>{
    this.map.set(user.id, user.login);
  });
  this.currentViewpoint = Viewpoint.Neutral;
}
logger(): void{
  this.currentViewpoint = Viewpoint.Prelogged;
}

hogger(): void{
  this.currentViewpoint = Viewpoint.Registerform;
}
legMeInLegMeIN(): void{
  this.newUser.login = this.loginlogin.value;
  this.newUser.password = this.loginpassword.value;
  this.api.loginUserUserLoginPost(this.newUser).subscribe((data) =>{
    if (data !== null) {
      this.currentUser = data;
      this.currentViewpoint = Viewpoint.Logged;
    } else {
      window.alert("Inplementation issue mate oi!");
    }
  },(error) => {
    if (error !== null) {
      window.alert("Tyle że takich użytkowników nie ma");
    }
  });
}

doYouWantFunnelCake(): void{
  this.newUser.login = this.registerlogin.value;
  this.newUser.password = this.registerpassword.value;
  this.api.createUserUserPost(this.newUser).subscribe((data) =>{
    if (data !== null) {
      window.alert(data);
      this.currentUser = data;
      this.currentViewpoint = Viewpoint.Logged;
    } else {
      window.alert("Inplementation issue mate oi!");
    }
  },(error) => {
    if (error !== null) {
      window.alert("Już masz tutaj konto czyżby początki Alzheimera?");
    }
  });
}

sendThemNapalm() :void{
  this.newMessage.message.content=this.napalm.value
  this.newMessage.message.author_id=this.currentUser.id
  this.newMessage.reciver.login=this.vietcong.value
  this.api.createMessageUserMessagesPost(this.newMessage).subscribe((data)=>{
    if (data !== null){
      let dupa:bubble = {sender: 'me to:'+this.vietcong.value,content:this.newMessage.message.content}
      this.dataarr.push(dupa)
    }else{
      window.alert("Inplementation issue mate oi!")
    }
  },(error) => {
    if (error !== null) {
      window.alert("Nawet prostej wiadomości nie potrafisz wysłać");
    }
  });
}

showMeDeWay() :void{
  this.api.getMessagesToUserUserMessagesReciverGet(this.currentUser.id).subscribe((data) =>{
    if (data !== null){
      data.forEach(record =>{
        let dupa:bubble = {sender:this.map.get(record.author_id), content:record.content}
        this.dataarr.push(dupa);
      })
    } else {
      window.alert("Inplementation issue mate oi!")
    }
  },(error) => {
    if (error !== null) {
      window.alert("Nie bądź chciwy Mikołaj już nie ma dla Ciebie wiadomości");
    }
  });
  this.api.readUsersUserGet().subscribe((data)=>{
    if (data !== null){
      this.users = data;
    }
  });
  this.users.forEach(user =>{
    this.map.set(user.id, user.login);
  });
  this.activeUsers = []
  this.users.forEach(user => {
    if (user.is_active && user.login !== this.currentUser.login){
    this.activeUsers.push(user);
    }
  })
}
punishMeDaddy() :void{
  let dezerter:UserBase = {login: this.currentUser.login}
  this.api.logoutUserUserLogoutPost(dezerter).subscribe((data)=>{
    if (data === null){
      window.alert("Inplementation issue mate oi!")
    }else{
      this.currentViewpoint = Viewpoint.Neutral
    }
  });
  this.activeUsers = [];
  this.dataarr = [];
  this.loginlogin.setValue('');
  this.loginpassword.setValue('');
  this.registerlogin.setValue('');
  this.registerpassword.setValue('');
  this.napalm.setValue('');
  this.vietcong.setValue('');
}

}

enum Viewpoint{
  Neutral,
  Prelogged,
  Registerform,
  Logged
}