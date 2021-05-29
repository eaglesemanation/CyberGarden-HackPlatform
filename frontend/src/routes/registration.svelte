<script>
  import {sendForm} from "$lib/api.js";
  import {goto} from "$app/navigation";

  let mail = "";
  let password1 = "";
  let password2 = "";
  let errorMessage = null;
  $: showError = !!errorMessage;

  function validate() {
    if (mail === "") {
      errorMessage = "Введите e-mail";
      return false;
    }
    if (password1 === "") {
      errorMessage = "Введите пароль";
      return false;
    }
    if (password2 === "") {
      errorMessage = "Введите пароль для подтверждения";
      return false;
    }
    if (password1 !== password2) {
      errorMessage = "Пароли не совпадают";
      password1 = "";
      password2 = "";
      return false;
    }
    return true;
  }

  async function submit() {

    // проверка на валидность указанных данных
    if (!validate()) return;

    // отправка на сервер запроса на регистрацию
    showError = false;
    let error = await sendForm(false, mail.value, password1.value);
    if (error) {
      errorMessage = error;
      return;
    }
    goto("/account")
    // window.location.replace("/account");
  }

</script>

<div class="main-block">
  <!-- svelte-ignore a11y-missing-attribute -->
  <img src="./static/reg.svg"/>
  <div class="reg-wrapper">
    <h1>Исследуй мир <span class="green">хакатонов</span></h1>
    <div class="regBox">
      <input bind:value={mail} placeholder="E-mail" type="email">
      <input bind:value={password1} placeholder="Пароль" type="password">
      <input bind:value={password2} placeholder="Подтверждение пароля" type="password">
      {#if (errorMessage != null)}
        <h3>{errorMessage}</h3>
      {/if}
      <button on:click={submit} class="main-button">Зарегистрироваться</button>
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

  .reg-wrapper {
    margin-left: 3em;
  }

  .regBox {
    display: flex;
    flex-direction: column;
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

  .main-button {
    background-color: #00160A;
    color: #fff;
    font-family: 'Ubuntu';
    font-weight: 500;
    border-color: #00160A;
    border-radius: 30px;
    padding: 0.75em 2em;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  @media (max-width: 1000px) {
    .main-block {
      flex-direction: column;
    }
  }

</style>