/** @module default */
// Auto-generated, edits will be overwritten
import * as gateway from './gateway'

/**
 * Sends table of all users besides requesting user
 * 
 * @param {string} userID
 * @param {string} password
 * @return {Promise<object>} All OK
 */
export function getUsersUserID(userID, password) {
  const parameters = {
    path: {
      userID,
      password
    }
  }
  return gateway.request(getUsersUserIDOperation, parameters)
}

/**
 * Registers an user
 * 
 * @param {string} userID
 * @param {string} password  
 * @return {Promise<object>} All OK
 */
export function postUsersUserID(userID, password) {
  const parameters = {
    path: {
      userID,
      password
    }
  }
  return gateway.request(postUsersUserIDOperation, parameters)
}

/**
 * Deletes an user
 * 
 * @param {string} userID 
 * @param {string} password  
 * @return {Promise<object>} All OK
 */
export function deleteUsersUserID(userID, password) {
  const parameters = {
    path: {
      userID,
      password
    }
  }
  return gateway.request(deleteUsersUserIDOperation, parameters)
}

/**
 * Login
 * 
 * @param {string} userID 
 * @param {string} password  
 * @return {Promise<object>} All OK
 */
export function getLoginUserID(userID, password) {
  const parameters = {
    path: {
      userID,
      password
    }
  }
  return gateway.request(getLoginUserIDOperation, parameters)
}

/**
 * Logout
 * 
 * @param {string} userID 
 * @param {string} password  
 * @return {Promise<object>} All OK
 */
export function getLogoutUserID(userID, password) {
  const parameters = {
    path: {
      userID,
      password
    }
  }
  return gateway.request(getLogoutUserIDOperation, parameters)
}

/**
 * Gets the table of messages
 * 
 * @param {string} userID
 * @param {string} password  
 * @return {Promise<object>} All OK
 */
export function getMessagePanelUserID(userID, password) {
  const parameters = {
    path: {
      userID,
      password
    }
  }
  return gateway.request(getMessagePanelUserIDOperation, parameters)
}

/**
 * Send a message
 * 
 * @param {string} userID 
 * @param {string} password  
 * @return {Promise<object>} All OK
 */
export function postMessagePanelUserID(userID, password, sender, content) {
  const parameters = {
    path: {
      userID,
      password
    },
    body: {data: {
       sender, content
    }}

  }
  return gateway.request(postMessagePanelUserIDOperation, parameters)
}

const getUsersUserIDOperation = {
  path: '/users/{userID}/{password}',
  method: 'get'
}

const postUsersUserIDOperation = {
  path: '/users/{userID}/{password}',
  method: 'post'
}

const deleteUsersUserIDOperation = {
  path: '/users/{userID}/{password}',
  method: 'delete'
}

const getLoginUserIDOperation = {
  path: '/login/{userID}/{password}',
  method: 'get'
}

const getLogoutUserIDOperation = {
  path: '/logout/{userID}/{password}',
  method: 'get'
}

const getMessagePanelUserIDOperation = {
  path: '/messagePanel/{userID}/{password}',
  method: 'get'
}

const postMessagePanelUserIDOperation = {
  path: '/messagePanel/{userID}/{password}',
  method: 'post'
}
