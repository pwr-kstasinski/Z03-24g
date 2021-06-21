import io from 'socket.io-client'
import { ref, computed } from 'vue';

let socket

const isLogged = ref(false)
const logError = ref("")
const registerMessage = ref("")
const userList = ref([])
const privateMessages = ref([])
const generalMessages = ref([])

const addOnEvents = () => {
  socket.on('message', msg => {
    console.log(msg)
    privateMessages.value.push(msg)
  })
  socket.on('general', msg => {
    console.log(msg)
    generalMessages.value.push(msg)
  })
  socket.on('login', data =>{
    registerMessage.value = ""
    if (data[0] == "Login successful"){
      isLogged.value = true
      logError.value = ""
      console.log(data[2])
      privateMessages.value = data[1]
      generalMessages.value = data[2]
    }
    else {
      logError.value = data 
    }
    console.log(logError.value)
    console.log(data)
  })
  socket.on('logout', data =>{
    registerMessage.value = ""
    if (data == "Logout_successful"){
      isLogged.value = false
      console.log(isLogged.value)
    }
    //console.log(isLogged.value)
    console.log(data)
  })
  socket.on('register', data =>{
    logError.value = ""
    registerMessage.value = data
  })
  socket.on('users', data => {
    userList.value = []
    if(!data){
      userList.value = ["Error while getting users"]
    }
    else {
      userList.value = data
    }
    console.log(userList.value)
  })
}
export const connectToServer = () => {
  socket = io('http://127.0.0.1:5000')
  addOnEvents()
}

export const sendMessage = (data) => {
  socket.emit('message', data)
}

export const generalMessage = (data) => {
  socket.emit('general', data)
}

export const login = (data) => {
  socket.emit('login', {username: data.username, password: data.password})
}

export const logout = (data) =>{
  socket.emit('logout', {username: data.username, password: data.password})
}

export const register = (data) =>{
  socket.emit('register', {username: data.username, password: data.password})
}



export const getLogged = computed (() => isLogged.value)

export const getLogError = computed(() => logError.value)

export const getRegisterMessage = computed(() => registerMessage.value)

export const getUserList = computed(() => userList.value)

export const getPrivateMessages = computed(() => privateMessages.value)

export const getGeneralMessages = computed(() => generalMessages.value)