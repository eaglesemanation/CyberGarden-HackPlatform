<script>
    export let name = "";
</script>


<div class="teamBox">
    <h2>Team: {name}</h2>
    <button> <a href="/{name}">Перейти</a> </button>
</div>

<style>
    .teamBox{
        border: 3px solid black;
        height: 100px;
        width: 300px;
        margin-top: 50px;
    }
</style>