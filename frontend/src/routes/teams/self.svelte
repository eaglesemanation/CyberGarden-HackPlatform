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
  export let promise;
  let teamToken;
</script>

<svelte:head>
  <title>Мои команды</title>
</svelte:head>
<div class="main">
  <h1>Мои <span class="green">команды</span></h1>
  <div class="buttons">
    <div>
      <input placeholder="Добавить команду по токену" bind:value={teamToken}>
    </div>
    <div class="a-box">
     <a class="box" sveltekit:prefetch href="/teams/enter-{teamToken}">
        <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
        <line y1="14" x2="30" y2="14" stroke="#757D8A" stroke-width="2"/>
        <line x1="15" y1="30" x2="15" stroke="#757D8A" stroke-width="2"/>
        </svg>
      </a>
    </div>
    <a class="main-button" sveltekit:prefetch href="/teams/create">Создать новую команду</a>
  </div>
  


  {#await $promise}
  {:then {as_captain, as_participant}}
    {#each as_captain || [] as team}
      <Team {...team}/>
    {/each}
  {/await}
</div>


<style>

  h1 {
    font-family: 'Ubuntu';
    font-weight: 700;
    font-size: calc(18px + (26 - 18) * ((100vw - 300px) / (1440 - 300)));
  }

  .green {
    color: #43DFA8;
  }

  .main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    place-items: center;
    height: 80vh;
    margin: 1em;
  }

  .buttons{
    display: flex;
  }
  svg{
    margin-left: 15px;
    margin-top: 10px;
  }
  input{
    width: 300px;
    height: 3em;
    border-radius: 8px 0px 0px 8px;
    border: 1px solid #E1E3E6;
    font-family: 'Ubuntu';
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }
  .a-box {
    height: 3.472em;
    background-color: whitesmoke;
    border: 1px solid #E1E3E6;
    width: 60px;
  }
  .main-button {
    background-color: #00160A;
    color: #fff;
    font-family: 'Ubuntu';
    font-weight: 500;
    border-color: #00160A;
    border-radius: 30px;
    padding: 0.75em 2em;
    width: 15vw;
    margin-left: 20px;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }
</style>