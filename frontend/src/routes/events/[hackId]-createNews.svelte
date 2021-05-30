<script context="module">

  export async function load({page}) {
    let hackId = page.params.hackId;
    return {props: {hackId}}
  }
</script>
<script>
  import {fetches} from "$lib/api";
  import {session} from "$app/stores";
  import {goto} from "$app/navigation";
  export let hackId;

  let title = ""
  let text = "";
  function create() {
    fetches.post(`/hacks/${hackId}/publish`, {title, text}, session.token);
    goto(`/events/${hackId}`);
  }
</script>

<div class="box">
  <h1>Создание новости</h1>
  <input bind:value={title} placeholder="Название">
  <input bind:value={text} placeholder="Текст">
  <button class="main-button" on:click={create}>Создать</button>
</div>

<style>
  .box {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-top: 30px;
    background-color: #ffffff;
    border: 3px solid #E1E3E6;
    box-sizing: border-box;
    border-radius: 30px;
    width: 600px;
    margin-left: auto;
    margin-right: auto;
    padding: 2%;
    margin-left: auto;
    margin-right: auto;
    width: 50vw;
  }

  input {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    height: 50px;
    margin-bottom: 20px;
    border-radius: 8px 0px 0px 8px;
    border: 1px solid #E1E3E6;
    font-family: 'Ubuntu';
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  h1 {
    text-align: center;
  }

  .main-button {
    text-align: center;
    width: 200px;
    margin-left: auto;
    margin-right: auto;
    background-color: #00160A;
    color: #fff;
    font-family: 'Ubuntu';
    font-weight: 500;
    border-color: #00160A;
    border-radius: 30px;
    padding: 0.75em 2em;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }
</style>