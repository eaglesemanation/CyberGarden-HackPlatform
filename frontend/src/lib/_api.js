import {writable, get} from 'svelte/store'
import {userToken} from '$lib/_store'
export const apiUrl = 'https://b.cybergarden.hackmasters.tech/';
export const selfUrl = 'https://cybergarden.hackmasters.tech/';

export let user = writable("");


export async function sendForm(isLogin, username, password) {
  let json_response = await fetch(
    apiUrl + (isLogin ? 'users/token' : 'users/create'),
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
  let {access_token, token_type, user_id} = json_response;
  console.log(access_token);
  userToken.updateInfo(access_token);

}


// API part
export const cache = new Map();
export let dataStore = writable({});
// TODO добавить контроль над сроком действия токена

export function storeFetch(url, method, data=null) {
  const store = writable(new Promise(() => {}));
  if (cache.has(url)) {
    store.set(Promise.resolve(cache.get(url)));
  }
  const load = async () => {
    console.log('Bearer ' + get(userToken))

    let request = {
        method, 
        headers: new Headers({
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + userToken,
    })};
    if (method !== 'get') {
      request.body = JSON.stringify(data)
    }

    const response = await fetch(url, );
    const rsp = await response.json();
    cache.set(url, rsp);
    store.set(Promise.resolve(rsp));
    dataStore.set(rsp);
  };

  load();
  return store;
}