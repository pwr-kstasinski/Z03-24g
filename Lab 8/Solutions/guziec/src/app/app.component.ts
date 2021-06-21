import { bubble } from './bubble.model';
import { Component, OnInit } from '@angular/core';
import { DefaultService, Message} from '../../apiclient';
import { FormControl } from '@angular/forms';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  Viewpoint = Viewpoint;
  login = new FormControl('')
  register = new FormControl('')
  napalm = new FormControl('')
  vietcong = new FormControl('')

  dataarr = []
  bubble= new bubble()

  prettySmell:Message = {sender:'',content:''}
  myuser: string =('')
  dupa: any ={}
  currentViewpoint: Viewpoint;



constructor(private api: DefaultService) {}
ngOnInit(): void {
  this.currentViewpoint = Viewpoint.Neutral;
}
logger(): void{
  this.currentViewpoint = Viewpoint.Prelogged;
}

hogger(): void{
  this.currentViewpoint = Viewpoint.Registerform;
}
legMeInLegMeIN(): void{
  this.api.getLoginLoginLoginGet(this.login.value,'body').subscribe((data) =>{
    if (data !== null){
      
      //window.alert(`printf: ${data[0].code}`);
      this.dupa = data[0].code;
      if(this.dupa === 200){
        this.currentViewpoint = Viewpoint.Logged;
        this.myuser=this.login.value;
      }else{
        window.alert('Tyle że takich użytkowników nie ma');
      }
    }
    else {
      window.alert('Się nic nie pobrało');
    }
  })
}

doYouWantFunnelCake(): void{
  this.api.postUserUserLoginPost(this.register.value, 'body').subscribe((data) =>{
    if (data !== null){
      
      //window.alert(`printf: ${data[0].code}`);
      this.dupa = data[0].code;
      if(this.dupa === 200){
        this.currentViewpoint = Viewpoint.Logged;
        this.myuser=this.register.value;
      }else{
        window.alert('Powiedzy sobie szczerze pszyszedłeś tu tylko po to by móc pocałować Gomeza');
      }
    }
    else {
      window.alert('Się nic nie pobrało');
    }
  });
}

sendThemNapalm() :void{
  this.prettySmell.content=this.napalm.value;
  this.prettySmell.sender=this.myuser;
  this.api.postMessageMessageLoginPost(this.vietcong.value, this.prettySmell, "body").subscribe((data)=>{
    if (data !== null){
    this.dupa = data[0].code;
      if(this.dupa === 200){
        let dupa:bubble = {sender:'me to:'+this.vietcong.value,content:this.prettySmell.content}
            this.dataarr.push(dupa)
      }else{
        window.alert('Nawet prostej wiadomości nie potrafisz wysłać');
      }
    }
    else {
      window.alert('Się nic nie pobrało');
    }
  });
}

showMeDeWay() :void{
  this.api.getMessageMessageLoginGet(this.myuser, 'body').subscribe((data) => {
    if (data !== null){
      this.dupa = data[0].code;
        if(this.dupa === 200){
          data[0].contents.forEach(record => {
            var json = JSON.parse(record)
            console.log('sender: ' + json.sender + ' centent: '+json.content)
            let dupa:bubble = {sender:json.sender,content:json.content}
            this.dataarr.push(dupa)
          });
        }else{
          window.alert('Już żeś wszystko zaciągnał');
        }
      }
      else {
        window.alert('Się nic nie pobrało');
      }
  });
}


}

enum Viewpoint{
  Neutral,
  Prelogged,
  Registerform,
  Logged
}