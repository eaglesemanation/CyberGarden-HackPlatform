<script context="module">
  import {fetches} from "$lib/api";

  export async function load({page}) {
    let id = page.params.teamId;
    let promise = fetches.get(`/teams/${id}`)
    return {props: {promise}}
  }
</script>

<script>
  export let promise;
</script>


<div class="page">
  {#await $promise}
    <!--{:then {name, participants, invite_link}}-->
  {:then {
    detail,
    id, name, invite_link, capitan, participants
  }}
    {#if detail}
      <img src="https://static.tildacdn.com/tild3935-3365-4465-b965-396661666130/img.svg" alt="404 not found">
    {:else}
      <h1>{invite_link}</h1>
    {/if}
    <!--  <h1>{JSON.stringify(data)}</h1>-->
    <!--  <h1>{name}</h1>-->
    <!--  <h1>{participants}</h1>-->
    <!--  <h1>{invite_link}</h1>-->
  {/await}
</div>
<style>
  img {
    width: 80%;
    max-width: 600px;
  }

  .page {
    width: 100%;
    height: 100%;
    display: grid;
    place-items: center;
  }
</style>