<template>
  <div>
    <span class="h2" style="color: #2fb543"> Login: </span>
    <input type="text" class="h2" v-model="login" :disabled="logged" />
    <button class="h2" v-if="!logged" @click="log_in">Zaloguj</button>
    <button class="h2" v-if="!logged" @click="registerUser">Zarejestruj</button>
    <button class="h2" v-if="logged" @click="log_out">Wyloguj</button>
    <button class="h2" v-if="logged" @click="deleteUser">Usun uzytkownika</button>
    <div v-if="logged">
      <div
        class="container"
        style="
          height: 600px;
          overflow-y: scroll;
          background-color: #444;
          text-align: left;
        "
      >
        <div
          v-for="message in received_messages"
          :key="message"
          style="color: white; text-align: right"
          :style="[message.sender.slice(0,3) == 'you' ? 'text-align: right' : 'text-align: left']"
        >
          <div class="message_header">{{ message.sender }}:</div>
          <div class="h2">{{ message.content }}</div>
        </div>
      </div>
      <div class="flex container ml-0" style="display: flex;
  align-items: top;
  justify-content: center" >
        <!-- <input type="text" class="h2" v-model="destination" /> -->
        <select class="ml-0" style="font-size: 1.7rem" v-model="chosenUser">
          <option disabled value="">Please select user:</option>
          <option v-for="otheruser in otherusers" :key="otheruser" :value="otheruser">{{otheruser}}</option>
        </select>
        <textarea  type="text" style="width:100%"  v-model="messageToSend" />
      </div>
      <button :disabled="!chosenUser" class="h2" @click="postMessage">Wyslij</button>
      <!-- <button class="h2" @click="getMessages">Odswiez</button> -->
    </div>
    <div class="h3" style="color: red">{{ errorMessage }}</div>
  </div>
</template>

<script>
import {
  getLoginUserID,
  postMessagePanelUserID,
  getMessagePanelUserID,
  getUsersUserID,
  deleteUsersUserID,
  postUsersUserID
} from "../middleware/default.js";
export default {
  name: "Chat",
  props: {
    msg: String,
  },
  data() {
    return {
      login: "",
      logged: false,
      loginError: false,
      messageToSend: "",
      received_messages: [],
      interval: [],
      errorMessage: "",
      otherusers: [],
      chosenUser: ""
    };
  },
  methods: {
    async log_in() {
      try {
        const received = await getLoginUserID(this.login);
        if (received.data.code == 200) {
          this.loginError = false;
          this.logged = true;
          this.errorMessage = "";
          this.getUsernames();
          this.interval = [setInterval(this.getMessages, 1500) , setInterval(this.getUsernames(), 1500)];
        } else {
          this.loginError = true;
          this.logged = false;
          this.errorMessage = "Blad logowania";
        }
      } catch (err) {
        console.log(err);
      }
    },
    async postMessage() {
      const received = await postMessagePanelUserID(
        this.chosenUser,
        this.login,
        this.messageToSend
      );
      if (received.data.code != 200) {
        this.errorMessage = "Taki uzytkownik nie istnieje";
      } else {
        this.errorMessage = "";
        this.received_messages.push({
          sender: "you to " + this.chosenUser,
          content: this.messageToSend,
        });
      }
    },
    async getMessages() {
      try {
        const received = await getMessagePanelUserID(this.login);
        console.log(received);
        if (received.data.code == 200) {
          this.received_messages = [
            ...this.received_messages,
            ...received.data.contents,
          ];
          console.log(this.received_messages);
        }
      } catch (error) {
        console.log(error);
      }
    },
    async getUsernames() {
      const received = await getUsersUserID(this.login);
      if (received.data.code == 200) {
        this.otherusers = received.data.contents;
      }
    },
    log_out() {
      this.received_messages = []
      this.logged = false;
      this.loginError = false;
      this.login = "";
      this.errorMessage = "";
      clearInterval(...this.interval);
    },
    async deleteUser(){
      const received = await deleteUsersUserID(this.login)
      if(received.data.code == 200){
        this.log_out()
        this.errorMessage="Usunieto uzytkownika"
        }
      else{
        this.errorMessage="EROR"
      }
    },
    async registerUser(){
      try {
        const received = await postUsersUserID(this.login);
        if (received.data.code == 200) {
          this.loginError = false;
          this.logged = true;
          this.errorMessage = "";
          this.getUsernames();
          this.interval = [setInterval(this.getMessages, 1500) , setInterval(this.getUsernames(), 1500)];
        } else {
          this.loginError = true;
          this.logged = false;
          this.errorMessage = "Uzytkownik juz istnieje";
        }
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
message_header {
  color: white;
  font-size: 10px;
}
#wgtmsr{
 width:3000px;   
}
</style>


