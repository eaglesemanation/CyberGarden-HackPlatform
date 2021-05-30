<script context="module">
  import {fetches} from "$lib/api";

  export async function load({page}) {
    let id = page.params.hackId;
    let promise = fetches.get(`/hacks/${id}`);
    return {props: {promise}}
  }

</script>

<script>
  export let promise;

  const eventExample = {
    name: "Cyber garden",
    date: "28.05.2021",
    addres: "moscow",
    organizers: ["ooo 3 axes", "12edsa"],
    sponsor: ["12", "12e12"]
  }//запрос с сервера
  function show(a){
    alert(a);
  }
</script>

<svelte:head>
  <title>event page</title>
</svelte:head>
{#await $promise}
{:then {
  id, name, description, location_lon,
  location_lat, location, sponsors, tags,
  image, start_date, end_date, publications
}}
  <div class="main">
    <div class="info">
      <!-- <button on:click={show(tags)}>show</button> -->
      <img src={image} alt="">
      <h1>{name}</h1>
      <h2>{start_date} - {end_date}</h2>
    </div>

    <div class="locationBox">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
            d="M12 2C8.14 2 5 5.14 5 9C5 14.25 12 22 12 22C12 22 19 14.25 19 9C19 5.14 15.86 2 12 2ZM16 10H13V13H11V10H8V8H11V5H13V8H16V10Z"
            fill="#43DFA8"/>
      </svg>
      <h3 class="location">{location.city}</h3>
    </div>

    {#each publications as {title, text, date}}
    <div class="boxForNew">
      <p>{title}</p>
      <p style="font-size: 20px">{text}</p>
      <p style="text-align: right">{date.substr(0,10)}</p>
    </div>
    {/each}
    <a href="/events/newsCreator" class="main-button">Создать новость</a>
  </div>
{/await}

<style>
  .main{
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
  img{
    height: 60%;
    width: 60%;
    margin-left:20%;
    border: 6px solid #43DFA8;
  }
  .location {
    color: #43DFA8;
  }
  svg{
    margin-top: 17px;
  }
  .locationBox {
    display: flex;
    margin-left: auto;
    margin-right: auto;
  }
  h1, h2{
    text-align: center;
  }
  .boxForNew{
    border: 3px solid #E1E3E6;
    margin-bottom: 20px;
  }
  .boxForNew p{
    margin-left: 20px;
    margin-right: 10px;
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
