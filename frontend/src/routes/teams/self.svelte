<script context="module">
  import {fetches} from "$lib/api";

  export async function load({page}) {
    let id = page.params.teamId;
    let promise = fetches.get(`/teams/${id}`)
    return {props: {promise}}
  }

</script>

<script>
  import Team from '$lib/TeamCard/index.svelte';
  // let teams = null;
  let teams = ["GardenMasters", "intSpirit"];
</script>

<svelte:head>
  <title>teaming</title>
</svelte:head>
<div class="main">
  {#if teams === null}
    <div class="a-box">
      <a class="main-button" sveltekit:prefetch href="/teamCreator">join team</a>
    </div>
  {:else}
    {#each teams as team}
      <Team name={team}/>
    {/each}
  {/if}
</div>


<style>
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