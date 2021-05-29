<script context="module">
  import {fetches} from "$lib/api";

  export async function load({session}) {
    let {token, role} = session;
    if (!token || !role) {
      return {redirect: "/authorization", status: 301};
    }
    let promise = fetches.get('/users/profile', token)
    return {
      props: {promise}
    };

  }
</script>

<script>
  import {onMount} from "svelte";
  import {deleteCookie} from '$lib/api.js';

  import {goto} from "$app/navigation";

  export let promise;
  let state = true;
  let Token;
  let Status;
  let accountInfo = {
    mail: "vadim@zhopa.com",
    fio: "Vadim Kandratov",
    avatar: "http://sun9-39.userapi.com/s/v1/ig2/8aqATIMGN_0ucbrpPT2w9-Od9s4_R-28vuF1rs263b_AnT8lBidXi9Tp1qazfob7TONkocJPt4t4cK1Z6ZOpdx3e.jpg?size=200x0&quality=96&crop=35,35,1002,1009&ava=1",
    status: "capitan",
    skills: ['svelte', 'js', 'python'],
    role: "frontend developer",
    education: "NUST MISiS"
  };
  onMount(async () => {
    // Token = localStorage.getItem("token");
    // Status = localStorage.getItem("status");
  })

  function exit() {
    deleteCookie("token");
    deleteCookie("role");
    goto("/");
  }

  function funcDelete() {
    if (confirm("exactly?")) {
      alert("Deleting...")
    }
  }

  function funcEdit() {
    state = !state;
  }

  function funcSave() {
    state = !state;
    //функция сохранение на бек
  }
</script>
<svelte:head>
  <title>account</title>
</svelte:head>

<div class="main-block">
  {#await $promise}
    <h1>Загрузка...</h1>
  {:then {fio, role, id}}
    <img src={accountInfo.avatar} alt="error">
    <h1>{accountInfo.fio}</h1>
    {#if state}
      <div class="skills">
        {#each accountInfo.skills as skill}
          <h3>{skill}</h3>
        {/each}
      </div>
      <h3>Role in the team: {accountInfo.role}</h3>
      <h3>Education: {accountInfo.education}</h3>
      <button on:click={funcEdit}>edit</button>
    {:else}
      <div class="inputs">
        <input bind:value={accountInfo.skills} type="text" placeholder="Skills">
        <input bind:value={accountInfo.role} type="text" placeholder="Role in the team">
        <input bind:value={accountInfo.education} type="text" placeholder="Education">
      </div>
      <button on:click={funcSave}>save</button>
      <button on:click={funcDelete}>DELETE ACCOUNT</button>
    {/if}
  {/await}
</div>


<style>

  .main-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    place-items: center;
    height: 80vh;
    margin: 1em;
  }

  h1 {
    font-family: 'Ubuntu';
    font-weight: 700;
  }
  
  .skills {
    display: flex;
    text-align: center;
    justify-content: center;
  }

  .skills h3 {
    background-color: rgba(222, 222, 222, 0.5);
    padding: 0.5em 1em;
    border-radius: 4px;
    margin: 2%;
    font-family: 'Ubuntu';
    font-weight: 400;
  }

  .inputs {
    display: flex;
    flex-direction: column;
  }

  input {
    width: 300px;
    margin-bottom: 10px;
  }

  img {
    border-radius: 300px;
    width: 300px;
    height: 300px;
  }
</style>