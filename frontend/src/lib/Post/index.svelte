<script>
    export let name="";
    export let date=""; 
    export let about="";
</script>

<div class="postBox">
    <h1>Haccaton: {name}</h1>
    <h1>date: {date}</h1>
    <h1>about: {about}</h1>
    <a sveltekit:prefetch href="/eventPage">more info...</a>
</div>

<style>
    .postBox{
        margin-top: 30px;
        border: 4px double black;
        width: 50vw;
        margin-left: auto;
        margin-right: auto;
    }
</style>
