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

<h1>team creator</h1>
<input bind:value={name} type="text" placeholder="Team name">
<input bind:value={hack} type="text" placeholder="For hack">
<button on:click={funcCreateTeam}>Create team</button>