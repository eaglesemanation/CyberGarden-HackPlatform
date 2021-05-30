<script>
    export let id;
    export let name;
</script>
 

<div class="teamBox">
    <h2>Team: {name}</h2>
    <a class="main-button" href="/teams/{id}">Перейти</a>
</div>

<style>
    .teamBox {
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
        margin-left: auto;
        margin-right: auto;
        padding: 2%;
        height: 200px;
    }
    .main-button {
		background-color: #00160A;
		color: #fff;
		font-family: 'Ubuntu';
		font-weight: 500;
        width: 200px;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
		border-color: #00160A;
		border-radius: 30px;
		padding: 0.75em 2em;
		font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
	}
</style>