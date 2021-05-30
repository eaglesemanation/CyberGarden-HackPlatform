<script context="module">
  import {fetches} from "$lib/api";

  export async function load({session}) {
    let {token, role} = session;
    if (!token || !role) {
      return {redirect: "/users/signin", status: 301};
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
  import MainButton from '$lib/MainButton/index.svelte';

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

  let cards = [
    {
      name: "Первая встреча с командой",
      src: "https://s3.gifyu.com/images/DIZAIN-BEZ-NAZVANIY85964548c320716c.gif"
    },
    {
      name: "Гуру виртуальных миров",
      src: "https://s3.gifyu.com/images/DIZAIN-BEZ-NAZVANIY-2fa88de9df81eaa20.gif"
    },
    {
      name: "Все ограничения сняты",
      src: "https://s3.gifyu.com/images/DIZAIN-BEZ-NAZVANIY-4711a1c889ce162b2.gif"
    },
    {
      name: "Три метра до деплоя",
      src: "https://s3.gifyu.com/images/DIZAIN-BEZ-NAZVANIY-5.gif"
    },
    {
      name: "Звонок правительству",
      src: "https://s3.gifyu.com/images/DIZAIN-BEZ-NAZVANIY-6.gif"
    }
  ]

  onMount(async () => {
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
    <!-- <div class="lds-dual-ring"></div> -->

    <!-- main block -->
    <div class="info-block">
      <img src={accountInfo.avatar} alt="error">
      <h1>{accountInfo.fio}</h1>
      <h3>{accountInfo.role}</h3>
      {#if state}
        <div class="skills">
          {#each accountInfo.skills as skill}
            <h3>{skill}</h3>
          {/each}
        </div>
        <h3>Education: {accountInfo.education}</h3>
        <MainButton on:click={funcEdit} btntext="Редактировать"></MainButton>
      {:else}
        <div class="inputs">
          <input bind:value={accountInfo.skills} type="text" placeholder="Skills">
          <input bind:value={accountInfo.role} type="text" placeholder="Role in the team">
          <input bind:value={accountInfo.education} type="text" placeholder="Education">
        </div>
        <button on:click={funcSave}>save</button>
        <button on:click={funcDelete}>DELETE ACCOUNT</button>
      {/if}
    </div>
    <h1 class="naming">Будет, что <span class="green">рассказать маме</span></h1>
    <!-- achive block -->
    <div class="achive">
      <div class="cards-list">
        {#each cards as card}
        <div class="card">
          <div class="card_image"> <img src={card.src} class="image-card" alt="error"/> </div>
          <div class="card_title title-white">
            <p class="card_title">{card.name}</p>
          </div>
        </div>
        {/each}
      </div>
    </div>
</div>


<style>

  .main-block {
    display: flex;
    flex-direction: column;
  }

  .info-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    place-items: center;
    height: 80vh;
    margin: 1em;
  }

  .green {
    color: #43DFA8;
  }

  h1 {
    font-family: 'Ubuntu';
    font-size: calc(18px + (26 - 18) * ((100vw - 300px) / (1440 - 300)));
    color: #00160A;
    margin-bottom: 0;
    font-weight: 700;
  }

  .naming {
    margin-bottom: 2%;
    text-align: center;
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
    border-radius: 200px;
    width: 200px;
    height: 200px;
  }

  /* preloader */

  .lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
  }

  .lds-dual-ring:after {
    content: " ";
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #000;
    border-color: #000 transparent #000 transparent;
    animation: lds-dual-ring 1.2s linear infinite;
  }

  @keyframes lds-dual-ring {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  /* card example */

  .cards-list {
    z-index: 0;
    width: 100%;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin-bottom: 10%;
  }

  .card {
    margin: 10px auto;
    width: 200px;
    height: 200px;
    border-radius: 40px;
    border: 3px solid #E1E3E6;
    cursor: pointer;
    transition: 0.4s;
    margin-bottom: 15%;
  }

  .card .card_image {
    width: inherit;
    height: inherit;
    border-radius: 40px;
  }

  .card .card_image img {
    width: inherit;
    height: inherit;
    border-radius: 40px;
    object-fit: cover;
  }

  .card .card_title {
    text-align: center;
    font-family: 'Ubuntu';
    font-weight: 700;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  .card:hover {
    transform: scale(0.9, 0.9);
    box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
  }

  .title-white {
    color: white;
  }

  @media all and (max-width: 500px) {
    .card-list {
      /* On small screens, we are no longer using row direction but column */
      flex-direction: column;
    }
  }


</style>