<script context="module">
  import {fetches} from "$lib/api";

  export async function load({page, session}) {
    let id = page.params.teamId;
    let promise = fetches.get(`/teams/my`, session.token)
    return {props: {promise}}
  }

</script>

<script>
  import Team from '$lib/TeamCard/index.svelte';
  // let teams = null;
  // let teams = ["GardenMasters", "intSpirit"];
  export let promise;
  let teamToken;
</script>

<svelte:head>
  <title>teaming</title>
</svelte:head>
<div class="main">

  <div class="join-block">
    <input placeholder="Токен команды" bind:value={teamToken}>
    <a class="main-button" sveltekit:prefetch href="/teams/enter-{teamToken}">Присоедниться</a>
  </div>
  <a class="main-button" sveltekit:prefetch href="/teams/create">Создать команду</a>
  {#await $promise}
  {:then {as_captain, as_participant}}
    {#each as_captain || [] as team}
      <Team name={team}/>
    {/each}
  {/await}
</div>


<style>
  .join-block {
    width: 400px;
    height: 90px;
  }
  .a-box {
    margin-left: 45vw;
    margin-top: 50px;
  }

  .main-button {
    background-color: #00160A;
    color: #fff;
    font-family: 'Ubuntu';
    font-weight: 500;
    border-color: #00160A;
    border-radius: 30px;
    padding: 0.75em 2em;
    /* margin-left: auto;
    margin-right: auto; */
    width: 15vw;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }
</style>