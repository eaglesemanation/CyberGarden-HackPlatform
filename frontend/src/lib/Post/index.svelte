<script>
    export let name="";
    export let date=""; 
    export let location="";
    export let about="";
    export let likes=0;
</script>

<div class="postBox">
    <div class="info">
        <h2>{name}</h2>
        <h3>{location}</h3>
        <h3>{date}</h3>
        <p>{about}</p>
    </div>
    <div class="bottom">
        <a sveltekit:prefetch href="/eventPage-{name}">more info...</a>
        <h3>{likes}</h3>
    </div>
    
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@700&family=Ubuntu:wght@400;500;700&display=swap');

    .postBox {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-top: 30px;
        background-color: #ffffff;
        border: 3px solid #E1E3E6;
        box-sizing: border-box;
        border-radius: 30px;
        width: 681px;
        padding-top: 0;
        margin-left: 2%;
        margin-right: 2%;
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
    .bottom{
        display: flex;
        justify-content: space-between;
    }
</style>
