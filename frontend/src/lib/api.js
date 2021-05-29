import {writable, get} from 'svelte/store'
import cookie from 'cookie';

export const apiUrl = 'https://b.cybergarden.hackmasters.tech';
export const selfUrl = 'https://cybergarden.hackmasters.tech';


export function deleteCookie(name) {
  setCookie(name, "", {
    'max-age': -1
  })
}

export function setCookie(name, value, options = {}) {
  options = {
    path: '/',
    ...options
  };
  if (options.expires instanceof Date) {
    options.expires = options.expires.toUTCString();
  }
  let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);
  for (let optionKey in options) {
    updatedCookie += "; " + optionKey;
    let optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += "=" + optionValue;
    }
  }
  document.cookie = updatedCookie;
}

export async function sendForm(isLogin, username, password) {
  let json_response = await fetch(
    apiUrl + (isLogin ? '/users/token' : '/users/create'),
    {
      method: 'POST',
      credentials: 'omit',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `username=${username}&password=${password}`
    },
  ).then(res => res.json());
  if (json_response.detail) {
    return isLogin ? "Неправильная почта или пароль" : "Такая почта уже используется"
  }
  let {access_token, token_type, user_id, role} = json_response;

  setCookie('token', access_token);
  setCookie('role', role);
}


// API part
export const cache = new Map();
export let dataStore = writable({});

// TODO добавить контроль над сроком действия токена

export const fetches = {
  get: (apiPart, token) => {
    return storeFetch(apiUrl + apiPart, 'get', {}, token)
  },
  post: (apiPart, data, token) => {
    return storeFetch(apiUrl + apiPart, 'post', data, token)
  },
  delete: (apiPart, token) => {
    return storeFetch(apiUrl + apiPart, 'delete', {}, token)
  },
}


export function storeFetch(url, method, data = null, token = null) {
  const store = writable(new Promise(() => {
  }));
  if (cache.has(url)) {
    store.set(Promise.resolve(cache.get(url)));
  }
  const load = async () => {
    let request = {
      method,
      headers: new Headers({
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token,
      })
    };
    if (method !== 'get') {
      request.body = JSON.stringify(data)
    }
    const response = await fetch(url, request);
    const rsp = await response.json();
    console.log(JSON.stringify(rsp))
    cache.set(url, rsp);
    store.set(Promise.resolve(rsp));
    dataStore.set(rsp);
  };
  load();
  return store;
}