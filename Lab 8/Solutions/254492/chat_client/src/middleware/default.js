/** @module default */
// Auto-generated, edits will be overwritten
import * as gateway from './gateway'

/**
 * Sends table of all users besides requesting user
 * 
 * @param {string} userID 
 * @return {Promise<object>} All OK
 */
export function getUsersUserID(userID) {
  const parameters = {
    path: {
      userID
    }
  }
  return gateway.request(getUsersUserIDOperation, parameters)
}

/**
 * Registers an user
 * 
 * @param {string} userID 
 * @return {Promise<object>} All OK
 */
export function postUsersUserID(userID) {
  const parameters = {
    path: {
      userID
    }
  }
  return gateway.request(postUsersUserIDOperation, parameters)
}

/**
 * Deletes an user
 * 
 * @param {string} userID 
 * @return {Promise<object>} All OK
 */
export function deleteUsersUserID(userID) {
  const parameters = {
    path: {
      userID
    }
  }
  return gateway.request(deleteUsersUserIDOperation, parameters)
}

/**
 * Login
 * 
 * @param {string} userID 
 * @return {Promise<object>} All OK
 */
export function getLoginUserID(userID) {
  const parameters = {
    path: {
      userID
    }
  }
  return gateway.request(getLoginUserIDOperation, parameters)
}

/**
 * Gets the table of messages
 * 
 * @param {string} userID 
 * @return {Promise<object>} All OK
 */
export function getMessagePanelUserID(userID) {
  const parameters = {
    path: {
      userID
    }
  }
  return gateway.request(getMessagePanelUserIDOperation, parameters)
}

/**
 * Send a message
 * 
 * @param {string} userID 
 * @return {Promise<object>} All OK
 */
export function postMessagePanelUserID(userID, sender, content) {
  const parameters = {
    path: {
      userID
    },
    body: {data: {
       sender, content
    }}

  }
  return gateway.request(postMessagePanelUserIDOperation, parameters)
}

const getUsersUserIDOperation = {
  path: '/users/{userID}',
  method: 'get'
}

const postUsersUserIDOperation = {
  path: '/users/{userID}',
  method: 'post'
}

const deleteUsersUserIDOperation = {
  path: '/users/{userID}',
  method: 'delete'
}

const getLoginUserIDOperation = {
  path: '/login/{userID}',
  method: 'get'
}

const getMessagePanelUserIDOperation = {
  path: '/messagePanel/{userID}',
  method: 'get'
}

const postMessagePanelUserIDOperation = {
  path: '/messagePanel/{userID}',
  method: 'post'
}
