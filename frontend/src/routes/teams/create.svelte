<script>
  import {goto} from "$app/navigation";
  import {fetches} from "$lib/api";
  import {session} from "$app/stores";

  let name = "";
  let hack = "";

  function validate() {
    if (name === "") {
      alert("Введите название команды");
      return false;
    }
    if (hack === "") {
      alert("Введите название хакатона");
      return false;
    }
    return true;
  }

  function funcCreateTeam() {
    if (!validate()) return;
    fetches.post('/teams/create', {name}, $session.token)
    goto('/teams/self')
  }
</script>
<svelte:head>
  <title>Создать команду</title>
</svelte:head>


<div class="main">
  <div class="form">
    <h1>Создать <span class="green">команду</span></h1>
    <div class="box">
      <div class="inputs">
        <input bind:value={name} type="text" placeholder="Team name">
        <input bind:value={hack} type="text" placeholder="For hack">
      </div>
      <button class="main-button" on:click={funcCreateTeam}>Создать команду</button>
    </div>
  </div>

  <img src="/static/forTeamCreator.svg"/>
</div>


<style>
  .main {
    display: flex;
    align-items: center;
    justify-content: center;
    place-items: center;
    height: 80vh;
    margin: 1em;
  }

  h1 {
    color: #00160A;
    font-family: 'Ubuntu';
    text-decoration: none;
    font-size: calc(30px + (30 - 24) * ((100vw - 300px) / (1440 - 300)));
    font-weight: 700;
  }

  .box {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background-color: #ffffff;
    border: 3px solid #E1E3E6;
    box-sizing: border-box;
    border-radius: 30px;
    padding: 4em;
  }

  .green {
    color: #43DFA8;
  }

  .main-button {
    background-color: #00160A;
    color: #fff;
    font-family: 'Ubuntu';
    font-weight: 500;
    border-color: #00160A;
    border-radius: 30px;
    padding: 0.75em 2em;
    margin-left: auto;
    margin-right: auto;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  .inputs {
    display: flex;
    flex-direction: column;
    margin-top: auto;
    margin-left: auto;
    margin-right: auto;
  }

  input {
    padding: 1em;
    margin-bottom: 0.7em;
    border-radius: 8px;
    border: 1px solid #E1E3E6;
    font-family: 'Ubuntu';
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  input:focus {
    outline: none;
    border: 1px solid #43DFA8;
    box-shadow: 0 0 10px rgba(67, 223, 168, 0.5);
  }

  @media (max-width: 800px) {
    img {
      height: 0vw;
      width: 0vw;
    }

    .box {
      width: 90vw;
      margin-left: 7vw;
      /* margin-right: 50px; */
    }

    input {
      width: 80vw;
    }
  }

  @media (max-width: 1000px) {
    img {
      margin-top: -200px;
    }

    .main-button {
      width: 150px;
    }
  }
</style>