<script context="module">
  import {fetches} from "$lib/api";

  export async function load({}) {
    let promise = fetches.get('/hacks/all');
    return {props: {promise}};
  }
</script>

<script>
  import Post from '$lib/Post/index.svelte';
  // import { element } from 'svelte/internal';
  let searchLine = "";
  let answer;
  let selectedCity = "";
  const cities = [
    "All", "Таганрог", "Луна", "Москва"
  ]
  export let promise;

  //для примера, заполнять будем после
  let posts = [];
  let postsMass = posts;

  //его строем после поиска
  function funcSearch(massF) {
    console.log(massF);
    postsMass = [];
    if (selectedCity === "All") selectedCity = "";
    if (searchLine === "" && selectedCity === "") {
      postsMass = massF.concat();
      return;
    } else if (selectedCity !== "") {
      massF.forEach(element => {
        let hackCity = element.location.toLowerCase();
        if (hackCity.indexOf(selectedCity.toLowerCase()) !== -1) {
          postsMass = postsMass.concat(element);
        }
      });
      if (searchLine !== "") {
        postsMass = [].concat();
        massF.forEach(element => {
          let hackCity = element.location.toLowerCase();
          let hackName = element.name.toLowerCase();
          if ((hackName.indexOf(searchLine.toLowerCase()) !== -1) && (hackCity.indexOf(selectedCity.toLowerCase()) !== -1)) {
            postsMass = postsMass.concat(element);
          }
        });
      }
    } else {
      massF.forEach(element => {
        let hackName = element.name.toLowerCase();
        if (hackName.indexOf(searchLine.toLowerCase()) !== -1) {
          postsMass = postsMass.concat(element);
        }
      });
    }
    // console.log(postsMass);
    // posts = [];
    return;
  }

  function handleKeydown(event) {
    if (event.key === "Enter") {
      funcSearch();
    }
  }
</script>

<svelte:head>
  <title>poster</title>
</svelte:head>


<!-- <svelte:window on:keydown={handleKeydown}/> -->
{#await $promise}
  {:then posts}
<h1 style="font-size:0px">{funcSearch(posts)}</h1>
<div class="main">

  <div class="search">
    <input bind:value={searchLine} type="text">
    <div class="a-box">
      <a on:click={funcSearch(posts)}>
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd"
                d="M2 8C2 4.691 4.691 2 8 2C11.309 2 14 4.691 14 8C14 11.309 11.309 14 8 14C4.691 14 2 11.309 2 8ZM17.707 16.293L14.312 12.897C15.365 11.543 16 9.846 16 8C16 3.589 12.411 0 8 0C3.589 0 0 3.589 0 8C0 12.411 3.589 16 8 16C9.846 16 11.543 15.365 12.897 14.312L16.293 17.707C16.488 17.902 16.744 18 17 18C17.256 18 17.512 17.902 17.707 17.707C18.098 17.316 18.098 16.684 17.707 16.293Z"
                fill="#757D8A"/>
        </svg>
      </a>
    </div>
  </div>
  <select class="cities" bind:value={selectedCity} on:change="{() => answer = ''}">
    {#each cities as question}
      <option value={question}>
        {question}
      </option>
    {/each}
  </select>

</div>


<div class="events-block">
  
    {#each postsMass as post}
      <Post {...post}/>
    {/each}
  
</div>
{/await}
<style>
  .main {
    display: flex;
    /* justify-content: space-evenly; */
    /* flex-direction: row;
    background-color: yellow; */
  }

  .cities {
    width: 352px;
    border: 1px solid #E1E3E6;
    font-family: 'Ubuntu';
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  svg {
    margin-left: 28%;
  }

  .events-block {
    flex-wrap: wrap;
    display: flex;
    align-self: center;
  }

  .search {
    display: flex;

    width: 350px;
  }

  .search * {
    height: 50px;
  }

  input {
    width: 300px;
    /* margin-bottom: 0.7em; */
    border-radius: 8px 0px 0px 8px;
    border: 1px solid #E1E3E6;
    font-family: 'Ubuntu';
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
  }

  .a-box {
    height: 52px;
    background-color: whitesmoke;
    border: 1px solid #E1E3E6;
    width: 40px;
    /* margin-left: -5px; */
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