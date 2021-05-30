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
</script>

<svelte:head>
  <title>event page</title>
</svelte:head>
{#await $promise}
{:then {
  id, name, description, location_lon,
  location_lat, location, sponsors, tags,
  image, start_date, end_date
}}
  <h1>{id}</h1>
  <h1>name: {name}</h1>
  <h1>start_date: {start_date}</h1>
  <h1>end_date: {end_date}</h1>
  <h1>address: {location}</h1>
{/await}
