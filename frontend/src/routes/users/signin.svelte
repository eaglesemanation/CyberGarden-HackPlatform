<script context="module">
  export function load({session}) {
    if (session.token && session.role) {
      return {redirect: '/users/self', status: 301}
    }
    return {}
  }
</script>

<script>
  import MainButton from '$lib/MainButton/index.svelte';
  import {sendForm} from "$lib/api";
  import {goto} from "$app/navigation";

  let mail = "";
  let password = "";
  let Token;
  let errorMessage = null;
  $: showError = !!errorMessage;

  function validate() {
    if (mail === "") {
      errorMessage = "Введите e-mail";
      return false;
    }
    if (password === "") {
      errorMessage = "Введите пароль";
      return false;
    }
    return true;
  }

  async function submit() {

    // проверка на валидность указанных данных
    if (!validate()) return;

    // отправка запроса на авторизацию
    showError = false;
    let error = await sendForm(true, mail.value, password.value);
    if (error) {
      errorMessage = error;
      return;
    }

    // userStatus.updateInfo("capitan"); //заглушка, получим с бека
    // window.location.replace("/poster"); //если все прошло успешно
    goto("/events/poster"); //если все прошло успешно
  }

</script>

<div class="main-block">
  <!-- svelte-ignore a11y-missing-attribute -->
  <img src="/static/space.svg"/>
  <div class="auth-wrapper">
    <h1>Зайти в <span class="green">пространство</span></h1>
    <div class="authBox">
      <input bind:value={mail} placeholder="E-mail" type="email">
      <input bind:value={password} placeholder="Пароль" type="password">
      {#if (errorMessage != null)}
        <h3>{errorMessage}</h3>
      {/if}
      <div class="buttonsBox">
        <MainButton on:click={submit} btntext="Вход"></MainButton>
        <a sveltekit:prefetch href="/users/signup" class="reg-button">Регистрация</a>
      </div>
    </div>
  </div>
</div>

<style>
  .main-block {
    display: flex;
    align-items: center;
    justify-content: center;
    place-items: center;
    height: 80vh;
    margin: 1em;
  }

  img {
    max-width: 90%;
    height: auto;
  }

  .auth-wrapper {
    margin-left: 3em;
  }

  .authBox {
    display: flex;
    flex-direction: column;
  }

  h1 {
    font-family: 'Ubuntu';
    font-size: calc(18px + (26 - 18) * ((100vw - 300px) / (1440 - 300)));
    font-weight: 700;
  }

  h3 {
    font-family: 'Ubuntu';
    color: #E84855;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
    font-weight: 500;
  }

  .green {
    color: #43DFA8;
  }

  input {
    max-width: 400px;
    height: 48px;
    margin-bottom: 0.5em;
    border-radius: 8px;
    padding-left: 2em;
    border: 1px solid #E1E3E6;
    font-family: 'Ubuntu';
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  input:focus {
    outline: none;
    border: 1px solid #43DFA8;
    box-shadow: 0 0 10px rgba(67, 223, 168, 0.5);
  }

  .reg-button {
    background-color: transparent;
    color: #00160A;
    font-family: 'Ubuntu';
    font-weight: 500;
    border: 2px solid #00160A;
    border-radius: 30px;
    padding: 0.75em 2em;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  @media (max-width: 1000px) {
    .main-block {
      flex-direction: column;
    }

    .auth-wrapper {
      margin-left: 0;
    }

    h1 {
      text-align: center;
    }
  }

</style>