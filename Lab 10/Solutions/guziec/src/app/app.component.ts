import { WebsocketService } from './websocket.service';
import { HttpParameterCodec } from '@angular/common/http';
import { MessageCreate } from './../../apiclient/model/messageCreate';
import { BodyCreateMessageUserMessagesPost } from './../../apiclient/model/bodyCreateMessageUserMessagesPost';
import { UserCreate } from './../../apiclient/model/userCreate';
import { User } from './../../apiclient/model/user';
import { bubble } from './bubble.model';
import { Component, OnDestroy, OnInit } from '@angular/core';
import { DefaultService, Message, UserBase} from '../../apiclient';
import { FormControl } from '@angular/forms';
import { Subscription } from 'rxjs';
import { DateTime } from 'luxon'


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  Viewpoint = Viewpoint;

  showit:boolean = false;
  
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
  
  sorter =new Map<Number, string>()

  map = new Map<Number, string>()

  newMessage:BodyCreateMessageUserMessagesPost ={ message:{content:'',author_id: 0}, reciver:{login:''}}

  dataarr = []
  dupa: any ={}
  currentViewpoint: Viewpoint;
  currentChat: any
  messageFromBelow: string;
  wsSimpscription: Subscription;
  client_id: any;

  kfc = new Map<Number, Number>()


constructor(private api: DefaultService, private wsService: WebsocketService) {}
ngOnInit(): void {
  this.currentViewpoint = Viewpoint.Neutral;
}
show(){
    this.showit= true; 
  }
hide(){
      this.showit= false; 
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
      this.currentUser.is_active =true;
      this.api.updateUserStatusUsersStatusPut(this.currentUser).subscribe((data)=> {if (data===null) window.alert("Inplementation issue mate oi!")})
      this.wsSimpscription = this.wsService.createObservableSocket('ws://localhost:8000/ws/' + this.currentUser.id)
      .subscribe(
        mess => this.molestTheEvent(mess),
        err => console.log('err'),
        () => console.log("complete"),
      );
      this.api.readUsersUserGet().subscribe((data)=>{
        if (data !== null){
          this.users = data;
        }
      });
      this.users.forEach(record =>{
        this.map.set(record.id, record.login)
        this.api.unreadMessagesToUserFromMessageReciverAuthorUnreadPost(this.currentUser.id,record.id).subscribe((data)=>{
          if(data !==null && data !==0){
            this.kfc.set(record.id, data);
          }
        })
      })
      this.activeUsers = this.users.sort((a, b) =>{ if(a.is_active > b.is_active) return 1; if (a.is_active < b.is_active) return -1; else return 0}).reverse();
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
      this.currentUser = data;
      this.wsSimpscription = this.wsService.createObservableSocket('ws://localhost:8000/ws/' + this.currentUser.id)
      .subscribe(
        mess =>  this.molestTheEvent(mess), 
        err => console.log('err'),
        () => console.log("complete"),
      );
      this.api.readUsersUserGet().subscribe((data)=>{
        if (data !== null){
          this.users = data;
          this.users.forEach(record =>{
            this.map.set(record.id, record.login)
            this.api.unreadMessagesToUserFromMessageReciverAuthorUnreadPost(this.currentUser.id,record.id).subscribe((data)=>{
              if(data !==null && data !==0){
                this.kfc.set(record.id, data);
              }
            })
          })
          this.activeUsers = this.users.sort((a, b) =>{ if(a.is_active > b.is_active) return 1; if (a.is_active < b.is_active) return -1; else return 0}).reverse();
        }
      });
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
molestTheEvent(data: string) :void{
  this.messageFromBelow = data;
  console.log(this.messageFromBelow);
  switch(this.messageFromBelow){
    case "Jedna bestie mniej":{
      this.api.readUsersUserGet().subscribe((data)=>{
        if (data !== null){
          this.users = data;
          this.users.forEach(record =>{
            this.map.set(record.id, record.login)
          })
          this.activeUsers = this.users.sort((a, b) =>{ if(a.is_active > b.is_active) return 1; if (a.is_active < b.is_active) return -1; else return 0}).reverse();
        }
      });
      break;
    }
    case "status":{
      this.api.readUsersUserGet().subscribe((data)=>{
        if (data !== null){
          this.users = data;
          this.users.forEach(record =>{
            this.map.set(record.id, record.login)
            this.api.unreadMessagesToUserFromMessageReciverAuthorUnreadPost(this.currentUser.id,record.id).subscribe((data)=>{
              if(data !==null && data !==0){
                this.kfc.set(record.id, data);
              }
            })
          })
          this.activeUsers = this.users.sort((a, b) =>{ if(a.is_active > b.is_active) return 1; if (a.is_active < b.is_active) return -1; else return 0}).reverse();
        }
      });
      break;
    }
    case "new_message" :{
      if(this.currentChat !== 13){
      let today = DateTime.now().toString()
      console.log(today)
      let dupa:bubble = {sender: this.currentUser.login,content:this.newMessage.message.content,read:false, date:today.substring(0,16)}
      this.dataarr.push(dupa)
      }
      break;
    }
    case "general" :{
      if (this.currentChat === 13){
        var ideeki = []
        this.api.readMessagesGeneralGeneralGet().subscribe((data) =>{
          if (data !== null){
            data.forEach(record =>{
              if (record.is_recived===false){
                let dupa:bubble = {sender:this.map.get(record.author_id), content:record.content, read:true, date:record.date.substring(0,16)}
                this.dataarr.push(dupa);
                ideeki.push(record.id);
              }
            })
            this.api.updateMessageStatusMessageReciverReadPut(13,ideeki).subscribe((err) => {
              if(err===null) window.alert("Inplementation issue mate oi!")
            });
          } else {
            window.alert("Inplementation issue mate oi!")
          }
        })
      }
      break;
    }
    case "read" :{
      break;
    }
    case "complete":{
      break;
    }
    default:{
      var moeLester = this.messageFromBelow.split(" ");
      if (moeLester[0] === "read"){
        var temp
        this.api.unreadMessagesToUserFromMessageReciverAuthorUnreadPost(parseInt(moeLester[1]),this.currentUser.id).subscribe((data)=>{
          if(data !==null){
            temp = data
            if(temp===0){
              this.dataarr.forEach(buuble =>{
                buuble.read=true;
              })
            }
          }
          else window.alert("Inplementation issue mate oi!");
        })
      }else{
      var author = parseInt( moeLester[1]);
      if (author === this.currentChat){
      var ideeki = []
      this.api.getMessagesToUserUserMessagesReciverAuthorGet(this.currentUser.id,author).subscribe((data) =>{
        if (data !== null){
          data.forEach(record =>{
            if (record.is_recived === false){
            let dupa:bubble = {sender:this.map.get(record.author_id), content:record.content, read:true, date:record.date.substring(0,16)}
            this.dataarr.push(dupa);
            ideeki.push(record.id);
          }})
          this.api.updateMessageStatusMessageReciverReadPut(this.currentUser.id,ideeki).subscribe((err) => {
            if(err===null) window.alert("Inplementation issue mate oi!")
          });
        } else {
          window.alert("Inplementation issue mate oi!")
        }
      });
    } else{
      this.api.unreadMessagesToUserFromMessageReciverAuthorUnreadPost(this.currentUser.id,author).subscribe((data)=>{
        if(data !==null){
          this.kfc.set(author, data);
        }
        else window.alert("Inplementation issue mate oi!");
      })
    }
  }
      break;
    }
    }
}
sendThemNapalm() :void{
  this.newMessage.message.content=this.napalm.value
  this.newMessage.message.author_id=this.currentUser.id
  this.newMessage.reciver.login=this.vietcong.value
  this.api.createMessageUserMessagesPost(this.newMessage).subscribe((data)=>{
    if (data !== null){
      console.log(data.date)
    }else{
      window.alert("Inplementation issue mate oi!")
    }
  },(error) => {
    if (error !== null) {
      window.alert("Nawet prostej wiadomości nie potrafisz wysłać");
    }
  });
}
youAreGoingToBrazil(banished: Number) :void{
  this.currentChat = banished;
  this.dataarr =[]
  var ideeki = []
  this.kfc.set(banished, null)
  if (banished ==13){
    this.api.readMessagesGeneralGeneralGet().subscribe((data) =>{
      if (data !== null){
        data.forEach(record =>{
          let dupa:bubble = {sender:this.map.get(record.author_id), content:record.content, read:true, date:record.date.substring(0,16)}
          this.dataarr.push(dupa);
          if (record.is_recived===false){
            ideeki.push(record.id);
          }
        })
        this.api.updateMessageStatusMessageReciverReadPut(13,ideeki).subscribe((err) => {
          if(err===null) window.alert("Inplementation issue mate oi!")
        });
      } else {
        window.alert("Inplementation issue mate oi!")
      }
    })
  } else{
  this.api.readMessagesToUserFromMessageReceiverIdSenderIdGet(this.currentUser.id,this.currentChat).subscribe((data) =>{
    if (data !== null){
      data.forEach(record =>{
        let dupa:bubble = {sender:this.map.get(record.author_id), content:record.content, read:true, date:record.date.substring(0,16)}
        this.dataarr.push(dupa);
        if (record.is_recived===false){
          ideeki.push(record.id);
        }
      })
      this.api.updateMessageStatusMessageReciverReadPut(this.currentUser.id,ideeki).subscribe((err) => {
        if(err===null) window.alert("Inplementation issue mate oi!")
      });
    } else {
      window.alert("Inplementation issue mate oi!")
    }
  });}
}
punishMeDaddy() :void{
  let dezerter:UserBase = {login: this.currentUser.login}
  this.currentUser.is_active=false;
  this.api.updateUserStatusUsersStatusPut(this.currentUser).subscribe((data) => {
    if (data===null) window.alert("Inplementation issue mate oi!")
  });
  this.currentViewpoint = Viewpoint.Neutral
  this.wsSimpscription.unsubscribe();
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