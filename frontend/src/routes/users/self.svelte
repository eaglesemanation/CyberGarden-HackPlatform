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
    <!-- <div class="lds-dual-ring"></div> -->
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
    <div class="achive-block">
      <div class="container">
        <div class="row">
          <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <div class="our-team">
              <div class="picture">
                <img class="img-fluid" src="https://picsum.photos/130/130?image=1027">
              </div>
              <div class="team-content">
                <h3 class="name">Michele Miller</h3>
                <h4 class="title">Web Developer</h4>
              </div>
              <ul class="social">
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-facebook" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-twitter" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-google-plus" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-linkedin" aria-hidden="true"></a></li>
              </ul>
            </div>
          </div>
              <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <div class="our-team">
              <div class="picture">
                <img class="img-fluid" src="https://picsum.photos/130/130?image=839">
              </div>
              <div class="team-content">
                <h3 class="name">Patricia Knott</h3>
                <h4 class="title">Web Developer</h4>
              </div>
              <ul class="social">
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-facebook" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-twitter" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-google-plus" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-linkedin" aria-hidden="true"></a></li>
              </ul>
            </div>
          </div>
              <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <div class="our-team">
              <div class="picture">
                <img class="img-fluid" src="https://picsum.photos/130/130?image=856">
              </div>
              <div class="team-content">
                <h3 class="name">Justin Ramos</h3>
                <h4 class="title">Web Developer</h4>
              </div>
              <ul class="social">
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-facebook" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-twitter" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-google-plus" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-linkedin" aria-hidden="true"></a></li>
              </ul>
            </div>
          </div>
              <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <div class="our-team">
              <div class="picture">
                <img class="img-fluid" src="https://picsum.photos/130/130?image=836">
              </div>
              <div class="team-content">
                <h3 class="name">Mary Huntley</h3>
                <h4 class="title">Web Developer</h4>
              </div>
              <ul class="social">
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-facebook" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-twitter" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-google-plus" aria-hidden="true"></a></li>
                <li><a href="https://codepen.io/collection/XdWJOQ/" class="fa fa-linkedin" aria-hidden="true"></a></li>
              </ul>
            </div>
          </div>
        </div>
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

  h1 {
    font-family: 'Ubuntu';
    font-size: calc(18px + (26 - 18) * ((100vw - 300px) / (1440 - 300)));
    color: #00160A;
    margin-bottom: 0;
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

  .achive-block {
      height: 100vh;
      background-image: url(https://picsum.photos/g/3000/2000);
      background-size: cover;
      background-position: center;
      display: flex;
      align-items: center;
  }

  .our-team {
  padding: 30px 0 40px;
  margin-bottom: 30px;
  background-color: #f7f5ec;
  text-align: center;
  overflow: hidden;
  position: relative;
}

.our-team .picture {
  display: inline-block;
  height: 130px;
  width: 130px;
  margin-bottom: 50px;
  z-index: 1;
  position: relative;
}

.our-team .picture::before {
  content: "";
  width: 100%;
  height: 0;
  border-radius: 50%;
  background-color: #1369ce;
  position: absolute;
  bottom: 135%;
  right: 0;
  left: 0;
  opacity: 0.9;
  transform: scale(3);
  transition: all 0.3s linear 0s;
}

.our-team:hover .picture::before {
  height: 100%;
}

.our-team .picture::after {
  content: "";
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #1369ce;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}

.our-team .picture img {
  width: 100%;
  height: auto;
  border-radius: 50%;
  transform: scale(1);
  transition: all 0.9s ease 0s;
}

.our-team:hover .picture img {
  box-shadow: 0 0 0 14px #f7f5ec;
  transform: scale(0.7);
}

.our-team .title {
  display: block;
  font-size: 15px;
  color: #4e5052;
  text-transform: capitalize;
}

.our-team .social {
  width: 100%;
  padding: 0;
  margin: 0;
  background-color: #1369ce;
  position: absolute;
  bottom: -100px;
  left: 0;
  transition: all 0.5s ease 0s;
}

.our-team:hover .social {
  bottom: 0;
}

.our-team .social li {
  display: inline-block;
}

.our-team .social li a {
  display: block;
  padding: 10px;
  font-size: 17px;
  color: white;
  transition: all 0.3s ease 0s;
  text-decoration: none;
}

.our-team .social li a:hover {
  color: #1369ce;
  background-color: #f7f5ec;
}

</style>