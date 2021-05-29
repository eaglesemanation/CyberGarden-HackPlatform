<script>
    export let btntext;
</script>

<button on:click class="main-button">{btntext}</button>

<style>

    .main-button {
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