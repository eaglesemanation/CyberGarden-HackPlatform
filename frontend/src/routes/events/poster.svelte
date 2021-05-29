<script>
  import Post from '$lib/Post/index.svelte';
  // import { element } from 'svelte/internal';
  let searchLine = "";
  let answer;
  let selectedCity = "";
  const cityMass = [
    "All", "Таганрог", "Луна", "Москва"
  ]
  const postsMassFronServer = [
    {
      name: "CyberGarden Hack",
      location: "Таганрог",
      date: "28.05.2021 - 30.05.2021",
      about: "Хакатон под пальмами для самых крутых людей. Хакатон под пальмами для самых крутых людей. Хакатон под пальмами для самых крутых людей. Хакатон под пальмами для самых крутых людей",
      likes: 56
    },
    {
      name: "hack moon",
      location: "Луна",
      date: "33.06.2022 - 32.06.2022",
      about: "супер пупер дупер хак номер 2",
      likes: 4
    }
  ];

  //для примера, заполнять будем после
  let postsMass = postsMassFronServer;

  //его строем после поиска
  function funcSearch() {
    postsMass = [].concat();
    if (selectedCity === "All") selectedCity = "";
    if (searchLine === "" && selectedCity === "") {
      postsMass = postsMassFronServer.concat();
      return;
    } else if (selectedCity !== "") {
      postsMassFronServer.forEach(element => {
        console.log(element.name);
        let hackCity = element.location.toLowerCase();
        if (hackCity.indexOf(selectedCity.toLowerCase()) !== -1) {
          postsMass = postsMass.concat(element);
        }
      });
      if (searchLine !== "") {
        postsMass = [].concat();
        postsMassFronServer.forEach(element => {
          console.log(element.name);
          let hackCity = element.location.toLowerCase();
          let hackName = element.name.toLowerCase();
          if ((hackName.indexOf(searchLine.toLowerCase()) !== -1) && (hackCity.indexOf(selectedCity.toLowerCase()) !== -1)) {
            postsMass = postsMass.concat(element);
          }
        });
      }
    } else {
      postsMassFronServer.forEach(element => {
        console.log(element.name);
        let hackName = element.name.toLowerCase();
        if (hackName.indexOf(searchLine.toLowerCase()) !== -1) {
          postsMass = postsMass.concat(element);
        }
      });
    }

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


<svelte:window on:keydown={handleKeydown}/>
<div class="main">

  <div class="search">
    <input bind:value={searchLine} type="text">
    <div class="a-box">
      <button on:click={funcSearch}>
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd"
                d="M2 8C2 4.691 4.691 2 8 2C11.309 2 14 4.691 14 8C14 11.309 11.309 14 8 14C4.691 14 2 11.309 2 8ZM17.707 16.293L14.312 12.897C15.365 11.543 16 9.846 16 8C16 3.589 12.411 0 8 0C3.589 0 0 3.589 0 8C0 12.411 3.589 16 8 16C9.846 16 11.543 15.365 12.897 14.312L16.293 17.707C16.488 17.902 16.744 18 17 18C17.256 18 17.512 17.902 17.707 17.707C18.098 17.316 18.098 16.684 17.707 16.293Z"
                fill="#757D8A"/>
        </svg>
      </button>
    </div>
  </div>


  <!-- svelte-ignore a11y-no-onchange -->
  <!-- svelte-ignore missing-declaration -->
  <select class="cities" bind:value={selectedCity} on:change="{() => answer = ''}">
    {#each cityMass as question}
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
    margin-left: 10px;
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
</style>