<script context="module">
  import {fetches} from "$lib/api";
  export async function load({session}) {
    let {token, role} = session;
    if (!token && !role && role === 'organizer') {
      return {redirect: "/users/signin", status: 301};
    }
    return {};
  }
</script>

<script>
  import MainButton from '$lib/MainButton/index.svelte';
  import {session} from "$app/stores";

  let name = "";
  let description = "";

  let start_date;
  let end_date;
  let organizer = [];
  let sponsor = [];

  // TODO add organizer, sponsor
  function create() {
    fetches.post('/hacks/create',
      {name, description, start_date, end_date},
      $session.token)
  }
</script>


<svelte:head>
  <title>Создать мероприятие</title>
</svelte:head>

<div class="main-block">
  <h1>Создать <span class="green">мероприятие</span></h1>
  <div class="input-wrapper">
    <input bind:value={name} type="text" placeholder="Название">
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label>Дата начала хакатона:</label>
    <input bind:value={start_date} type="date" placeholder="Дата начала хакатона">
    <label>Дата окончания хакатона:</label>
    <input bind:value={end_date} type="date" placeholder="Дата окончания хакатона">
    <textarea class="description" bind:value={description} placeholder="Описание"></textarea>
    <input bind:value={sponsor} type="text" placeholder="Спонсоры">
    <input bind:value={organizer} type="text" placeholder="Организаторы">
  </div>
  <MainButton on:click={create} btntext="Создать"/>
</div>

<style>

  h1 {
    font-size: 'Ubuntu';
    font-size: calc(18px + (26 - 18) * ((100vw - 300px) / (1440 - 300)));
    font-weight: 700;
  }

  .main-block {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    place-items: center;
    height: 100%;
    margin: 1em;
  }

  label {
    font-family: 'Ubuntu';
    font-weight: 400;
    margin-bottom: 3%;
    margin-left: 2em;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  .input-wrapper {
    display: flex;
    flex-direction: column;
  }

  .green {
    color: #43DFA8;
  }

  input {
    max-width: 600px;
    height: 48px;
    margin-bottom: 0.5em;
    border-radius: 8px;
    padding-left: 2em;
    padding-right: 2em;
    border: 1px solid #E1E3E6;
    font-family: 'Ubuntu';
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  textarea {
    max-width: 600px;
    height: 200px;
    margin-bottom: 0.5em;
    border-radius: 8px;
    padding-right: 2em;
    padding-top: 1em;
    padding-left: 2em;
    border: 1px solid #E1E3E6;
    font-family: 'Ubuntu';
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  input[type="date"] {
    color: #757575;
  }

  input[type="date"]:focus {
    outline: none;
    border: 1px solid #43DFA8;
    box-shadow: 0 0 10px rgba(67, 223, 168, 0.5);
  }

  textarea:focus {
    outline: none;
    border: 1px solid #43DFA8;
    box-shadow: 0 0 10px rgba(67, 223, 168, 0.5);
  }

  input:focus {
    outline: none;
    border: 1px solid #43DFA8;
    box-shadow: 0 0 10px rgba(67, 223, 168, 0.5);
  }

</style>
