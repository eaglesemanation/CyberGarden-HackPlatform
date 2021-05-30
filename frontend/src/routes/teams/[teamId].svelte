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
      <h1 class="name">{name}</h1>
      <h2>Ссылка для пришлашения: </h2>
      <h1>{invite_link}</h1>
    {/if}
     <!-- <h1>{JSON.stringify(data)}</h1> -->
  {/await}
</div>
<style>
  .name{
      margin-top: 100px;
        font-family: 'Ubuntu';
        font-size: calc(34px + (26 - 18) * ((100vw - 300px) / (1440 - 300)));
        color: #00160A;
        margin-bottom: 0;
        font-weight: 700;
    }
  h2{
    margin-top: 5 0px;
  }
  h1{
    margin-top: -10px;
  }
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