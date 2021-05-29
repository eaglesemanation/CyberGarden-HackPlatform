<script context="module">
  export async function load({page}){
    let {path} = page
    console.log(path);
    return {}
  }

</script>

<script>
  export let name;
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
<h1>{hackId}</h1>
<h1>name: {eventExample.name}</h1>
<h1>date: {eventExample.date}</h1>
<h1>addres: {eventExample.addres}</h1>