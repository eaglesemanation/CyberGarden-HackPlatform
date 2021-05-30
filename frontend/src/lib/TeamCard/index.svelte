<script>
    export let id;
    export let name;
</script>
 

<div class="teamBox">
    <h2>Team: {name}</h2>
    <div class="buttons">
        <a class="main-button" href="/teams/{id}">Перейти</a>
        <button class="main-button-red" href="/teams/{id}">Удалить</button>
    </div>
    
</div>

<style>
    h2{
        font-family: 'Ubuntu';
        font-size: calc(18px + (26 - 18) * ((100vw - 300px) / (1440 - 300)));
        color: #00160A;
        margin-bottom: 0;
        font-weight: 700;
    }
    .buttons{
        display: flex;
    }
    .buttons *{
        color: #fff;
		font-family: 'Ubuntu';
		font-weight: 500;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
        border-radius: 30px;
		padding: 0.75em 2em;
		font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
    }
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
        width: 200px;
		border-color: #00160A;
	}
    .main-button-red{
        background-color: red;
		border-color: red;
    }
</style>