<template>
  <input :disabled="getLogged" type="text" v-model="username" />
  <input :disabled="getLogged" type="password" v-model="password" />
  <button v-if="!getLogged" @click="handleLogin">Login</button>
  <button v-if="getLogged" @click="handleLogout">Logout</button>
  <button v-if="!getLogged" @click="handleRegister">Register</button>
  <div v-if="getRegisterMessage"> {{getRegisterMessage}} </div> 
  <div v-if="getLogError"> {{getLogError}} </div>
  <div v-if="getLogged">
  <!-- <ul>
    <li v-for="(message, index) in getFilteredMessages" :key="index">
      {{message.sender}} to {{message.receiver}}: {{message.content}} | {{message.datetime}} -- {{message}}
    </li>
  </ul> -->
      <div
        class="container"
        style="
          height: 600px;
          overflow-y: scroll;
          background-color: #444;
          text-align: left;
        "
      >
        <div v-for="message in getFilteredMessages"
          :key="message"
          class = "container"
          style = "margin: 5px 0px; width:100%"
          :style="[message.sender == username ? 'display:flex; flex-direction:column; align-items: flex-end' : '']"
          >
        <div
          style="color: white; text-align: right; background-color:black; max-width: fit-content; padding: 5px"
          :style="[
            message.sender == username ? 'text-align: right; background-color:#081063' : 'text-align: left',
          ]"
        >
          <div class="message_header" style="font-size:25px">{{ message.sender }}:</div>
          <div class="h2" >{{ message.content }}</div>
          <div class="message_details">{{ message.datetime }}<span v-if="chosenUser!='general'"> - {{ message.is_read ? 'Seen' : 'Sent' }}</span></div>
        </div>
        </div>
      </div>
  
  <input type="text" v-model="msgText" />
  <button @click="handleSendingMessage">Send message</button>
  <div v-if="messageError">
    {{messageError}}
  </div>
  <div>
    <button style="background-color: Transparent;
    background-repeat:no-repeat;
    border: none;
    cursor:pointer;
    overflow: hidden;
    outline:none" @click="chosenUser='general'">General</button>
  </div>
  <ul style="list-style-type:none">
    <li v-for="(user, index) in getSortedUserListActivity" :key="index">
      <button style="background-color: Transparent;
    background-repeat:no-repeat;
    border: none;
    cursor:pointer;
    overflow: hidden;
    outline:none" @click="chosenUser=user.username">{{user.username}} - {{user.online ? 'online' : 'offline' }}</button>
    </li>
  </ul>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

import { computed, defineComponent, ref } from "vue";
import {
  connectToServer,
  sendMessage,
  login,
  getLogged,
  logout,
  getLogError,
  getRegisterMessage,
  register,
  getUserList,
  getPrivateMessages,
  getGeneralMessages,
  generalMessage
} from "./middleware/socketConection";

export default defineComponent({
  name: "App",
  setup() {
    const messageError = ref("")
    const chosenUser = ref("")
    const password = ref("")
    const username = ref("")
    const msgText = ref("");
    const handleSendingMessage = () => {
      if(!chosenUser.value){
        messageError.value = "You have to choose a recipient"
      }
      else if (!msgText.value){
        messageError.value = "Message can't be empty"
      }
      else {
        messageError.value = ""
        if(chosenUser.value == 'general'){
          generalMessage({sender: username.value, content: msgText.value, datetime: currentDateTime()})
        }
        else sendMessage({receiver: chosenUser.value, sender: username.value, content: msgText.value, datetime: currentDateTime()});
        msgText.value = "";
      }
    };
    const handleLogin = () => {
      login({username: username.value, password: password.value})
      
    };
    const handleLogout = () => {
      logout({username: username.value, password: password.value})
      username.value=""
      password.value=""
    };
    const handleRegister = () => {
      register({username: username.value, password: password.value})
      username.value=""
      password.value=""
      messageError.value = ""
    };
    const currentDateTime = () => {
      const current = new Date();
      const date = current.getFullYear()+ '-' +(current.getMonth()+1)+ '-'+ current.getDate();
      const time = current.getHours() + ":" + current.getMinutes() + ":" + current.getSeconds();
      const dateTime = date +' '+ time;
      
      return dateTime;
    };

    const getFilteredMessages = computed(() =>{
      if (chosenUser.value == 'general'){
        return getGeneralMessages.value
      }
      return getPrivateMessages.value.filter((message) => (message.sender == chosenUser.value || message.receiver == chosenUser.value))
          }
    )
    // 1. 
    const getSortedUserList = computed(() => {
      let messages = [...getPrivateMessages.value]
      let userList = []
      for (const message of messages.reverse()){
        console.log(message)
        console.log(message.sender)
        if (!userList.includes(message.sender)) userList.push(message.sender)
        if (!userList.includes(message.receiver)) userList.push(message.receiver)
      }
      let additionalUserList = [...getUserList.value]
      for (const user of additionalUserList.sort(function(a,b){return b.online-a.online})){
        if (!userList.includes(user.username)) userList.push(user.username)
      }
      return userList.filter((user) => (user != username.value))
    }
    )

    const getSortedUserListActivity = computed(() =>{
      return getUserList.value.filter(user => (getSortedUserList.value.includes(user.username))).sort((a,b) => getSortedUserList.value.indexOf(a.username) -getSortedUserList.value.indexOf(b.username) )
    }
    )


    return {
      handleSendingMessage,
      msgText,
      username,
      password,
      handleLogin,
      getLogged,
      getLogError,
      handleLogout,
      getRegisterMessage,
      handleRegister,
      getUserList,
      chosenUser,
      messageError,
      getPrivateMessages,
      getSortedUserList,
      getFilteredMessages,
      getSortedUserListActivity
    };
  },
  created() {
    connectToServer();
  },
  // components: {
  //   HelloWorld
  // }
  computed(){}
}); 
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.message_details {
  font-size: 15px;
}
</style>
