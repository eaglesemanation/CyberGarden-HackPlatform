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
  <title>event registration</title>
</svelte:head>

<h1>event registration</h1>
<div class="inputBox">
  <input bind:value={name} type="text" placeholder="name">
  <input bind:value={date} type="text" placeholder="date">
  <input bind:value={location_lon} type="text" placeholder="location">
  <input bind:value={location_lat} type="text" placeholder="location">
  <textarea class="description" bind:value={description} placeholder="description"></textarea>
  <input bind:value={sponsor} type="text" placeholder="sponsor">
  <input bind:value={organizer} type="text" placeholder="organizator">
</div>
<button on:click={create}>create</button>
<style>
  .inputBox {
    display: flex;
    flex-direction: column;
  }

  .inputBox * {
    width: 300px;
  }

  .inputBox .information {
    height: 200px;
  }
</style>
