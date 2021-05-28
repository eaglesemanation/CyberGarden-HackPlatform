<script>
    export let name="";
    export let date=""; 
    export let about="";
</script>

<div class="postBox">
    <h2>{name}</h2>
    <h3>{date}</h3>
    <p>{about}</p>
    <a sveltekit:prefetch href="/eventPage">more info...</a>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@700&family=Ubuntu:wght@400;500;700&display=swap');

    .postBox{
        margin-top: 30px;
        background-color: #ffffff;
        border: 3px solid #E1E3E6;
        box-sizing: border-box;
        border-radius: 30px;
        max-width: 30%;
        padding-top: 0;
        margin-left: 5%;
        margin-right: 5%;
        padding: 2%;
    }

    h2, h3, p {
        font-family: 'Ubuntu';
        color: #00160A;
        line-height: 0.5;
    }

    h2 {
        font-weight: 700;
        font-size: 30px;
    }

    h3 {
        font-size: 20px;
        font-weight: 500;
    }

    p {
        font-weight: 400;
        line-height: 1.5;
    }
</style>
