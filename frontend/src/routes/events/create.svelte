<script context="module">
  import {fetches} from "$lib/api";
  export async function load({session}) {
    let {token, role} = session;
    if (!token || !role) {
      return {redirect: "/users/signin", status: 301};
    }
    return {};
  }
</script>

<script>
  import MainButton from '$lib/MainButton/index.svelte';

  let name = "";
  let description = "";

  let date = "";
  let organizer = [];
  let sponsor = [];
  let location_lon = 0.0;
  let location_lat = 0.0;

  function create() {
    fetches.post()
  }
</script>


<svelte:head>
  <title>Создать мероприятие</title>
</svelte:head>

<div class="main-block">
  <h1>event registration</h1>
  <div class="input-wrapper">
    <input bind:value={name} type="text" placeholder="name">
    <label>Дата <span class="green">начала</span> хакатона</label>
    <input bind:value={date} type="date" placeholder="Время начала хакатона">
    <input bind:value={date} type="date" placeholder="Время окончания хакатона">
    <textarea class="description" bind:value={description} placeholder="Описание"></textarea>
    <input bind:value={sponsor} type="text" placeholder="Спонсоры">
    <input bind:value={organizer} type="text" placeholder="Организаторы">
  </div>
  <MainButton on:click={create} btntext="Создать"></MainButton>
</div>

<style>

  .main-block {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    place-items: center;
    height: 100%;
    margin: 1em;
  }

  .input-wrapper {
    display: flex;
    flex-direction: column;
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
