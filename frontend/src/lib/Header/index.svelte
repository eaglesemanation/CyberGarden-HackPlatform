<script>
  import {page} from '$app/stores';
  import {onMount} from "svelte";
  import MainButton from "$lib/MainButton/index.svelte";
  import {session} from "$app/stores";
  import {goto} from "$app/navigation";
  import {deleteCookie} from "$lib/api";

  let token, role;
  session.subscribe(value => {
    token = value.token;
    role = value.role;
  })

  function exit() {
    $session = {token: null, role: null};
    deleteCookie("token");
    deleteCookie("role");
    goto('/');
  }

</script>

<header>
  <div class="header-left"><a sveltekit:prefetch href="/" class="logo-brand">Garden<span
      class="green">Masters</span></a></div>
  <div class="header-center">
    <ul>
      <li><a sveltekit:prefetch href="/events/poster">Афиша</a></li>
      <li><a sveltekit:prefetch href="/users/self">Профиль</a></li>
      <li><a sveltekit:prefetch href="/events/create">Новое мероприятие</a></li>
      {#if (role === "organizer") || (role === "admin")}
        <li><a sveltekit:prefetch href="/eventAdmin">Дашборд</a></li>
      {:else if (role === "participant") || (role === "capitan")}
        <li><a sveltekit:prefetch href="/teams/self">Команда</a></li>
      {/if}
    </ul>
  </div>
  {#if token === null}
    <a sveltekit:prefetch href="/users/signin" class="main-button">Авторизация</a>
  {:else}
    <MainButton on:click={exit} btntext="Выход"/>
  {/if}
</header>

<style>

  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1em;
  }

  ul {
    position: relative;
    padding: 0;
    margin: 0;
    height: 3em;
    display: flex;
    justify-content: center;
    align-items: center;
    list-style: none;
    background: var(--background);
    background-size: contain;
  }

  a {
    font-family: 'Ubuntu';
    display: flex;
    height: 100%;
    align-items: center;
    padding-right: 1em;
    color: var(--heading-color);
    font-weight: 500;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
    text-decoration: none;
    transition: color 0.2s linear;
    outline: none;
  }

  a:hover {
    outline: none;
  }

  .logo-brand {
    color: #00160A;
    font-family: 'Ubuntu';
    text-decoration: none;
    font-size: calc(24px + (30 - 24) * ((100vw - 300px) / (1440 - 300)));
    font-weight: 700;
  }

  .logo-brand:hover {
    color: #00160A;
  }

  .green {
    color: #43DFA8;
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
    header {
      flex-direction: column;
      align-items: flex-start;
    }
  }

</style>
