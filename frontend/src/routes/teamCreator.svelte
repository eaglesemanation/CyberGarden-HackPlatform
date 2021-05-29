<script>
    let name = "";
    let hack = "";
    function validate(){
        if(name===""){
            alert("Введите название команды");
            return false;
        }
        if(hack===""){
            alert("Введите название хакатона");
            return false;
        }
        return true;
    }
    function funcCreateTeam(){
        if(!validate())return;
        //отдаем серверу команду
        window.location.replace("/teaming");
    }
</script>
<svelte:head>
	<title>team creator</title>
</svelte:head>




<h1>Создать команду</h1>

<img src="./static/forTeamCreator.svg" />    

<div class="box">
    <div class="inputs">
        <input bind:value={name} type="text" placeholder="Team name">
        <input bind:value={hack} type="text" placeholder="For hack">
    </div>
    <button class="main-button" on:click={funcCreateTeam}>Создать команду</button>
</div>

<style>
    img{
        position: absolute;
        top: 0;
        right: 0;
        height: 40vw;
        width: 40vw;
        margin-right: 120px;
    }
    h1{
		color: #00160A;
		font-family: 'Ubuntu';
		text-decoration: none;
		font-size: calc(30px + (30 - 24) * ((100vw - 300px) / (1440 - 300)));
		font-weight: 1000;
        margin-left: 15px;
	}
    .box {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-top: 70px;
        background-color: #ffffff;
        border: 3px solid #E1E3E6;
        box-sizing: border-box;
        border-radius: 30px;
        width: 40vw;
        height: 25vw;
        padding-top: 0;
        margin-left: 2%;
        margin-right: 2%;
        padding: 2%;
        margin-left: auto;
        margin-right: auto;
        min-height: 300px;
    }
    .main-button {
		background-color: #00160A;
		color: #fff;
		font-family: 'Ubuntu';
		font-weight: 500;
		border-color: #00160A;
		border-radius: 30px;
		padding: 0.75em 2em;
        margin-left: auto;
        margin-right: auto;
        width: 15vw;
		font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
	}
    .inputs{
        display: flex;
        flex-direction: column;
        margin-top: auto;
        margin-left: auto;
        margin-right: auto;
    }
    input {
        /* margin-top: auto; */
        width: 30vw;
		/* max-width: 400px; */
        height: 48px;
        margin-bottom: 0.5em;
        border-radius: 8px;
        border: 1px solid #E1E3E6;
        font-family: 'Ubuntu';
        font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
	}

    input:focus {
        outline: none;
        border: 1px solid #43DFA8;
        box-shadow: 0 0 10px rgba(67, 223, 168, 0.5);
    }
    @media (max-width: 500px){ 
        .box{
            width: 90vw;
        }
        input{
            width: 80vw;
        }
    }
    @media (max-width: 1000px){ 
        img{
            height: 0vw;
            width: 0vw;
        }
        .main-button{
            width: 150px;
        }
    }
</style>