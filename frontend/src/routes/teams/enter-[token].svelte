<script context="module">
  import {fetches} from "$lib/api"

  export async function load({page, session}) {
    let {token, role} = session;
    if (!token || !role) {
      return {redirect: "/users/signin", status: 301};
    }

    let invite = page.params.token;
    let promise = fetches.get(`/teams/enter/${invite}`, token);
    return {props: {promise}}
  }
</script>

<script>
  export let promise;
  const mass = {hack: "Cyber Garden", capitan: "Дмитрий Дин"};
  let state = 1;
  function funcState(){
    state = 0;
  }
</script>

<div>
  {#await $promise}
  {:then telo}
    <!-- <p>{JSON.stringify(telo)}</p> -->
    <div class="mainBox">
      <h1>{telo.name}</h1>
      <div class="bot">
        <div class="info">
          {#if state===1}
            <h2>Capitan: {mass.capitan}</h2>
            <h2>Hackathon: {mass.hack}</h2>
          {:else}
            <h2>Поздравляем, ваш запрос отправлен на рассмотрение командира команды!</h2>
          {/if}
          
        </div>
        <div class="a-box">
          <a on:click={funcState()}>
            <svg width="96" height="90" viewBox="0 0 96 90" fill="none" xmlns="http://www.w3.org/2000/svg">
              <line x1="0.797867" y1="44.3972" x2="34.7979" y2="89.3972" stroke="#909090" stroke-width="5"/>
              <line x1="33.1825" y1="89.424" x2="95.1825" y2="1.42405" stroke="#919191" stroke-width="5"/>
            </svg>
          </a>
        </div>
      </div>
      
    </div>
    
  {/await}
  
</div>

<style>
  .bot{
    display: flex;
    justify-content: space-between;
  }
  h1{
        font-family: 'Ubuntu';
        font-size: calc(34px + (26 - 18) * ((100vw - 300px) / (1440 - 300)));
        color: #00160A;
        margin-bottom: 20px;
        font-weight: 700;
  }
  h2{
    margin-top: 0px;
    margin-bottom: 0px;
  }
  .mainBox{
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
  }
  .a-box {
    height: 60px;
    background-color: #43dfb4;
    border: 1px solid #E1E3E6;
    width: 60px;
    /* margin-left: -5px; */
  }
  svg{
    margin-left: 5px;
    margin-top: 3px;
    width: 50px;
    height: 50px;
  }
  .a-box:hover {
    background-color: rgb(228, 225, 225);
    transition: 0.7s;
  }
  .a-box:active {
    background-color: rgb(199, 199, 199);
    transition: 0.1s;
  }
</style>