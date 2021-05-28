<script>
	let mail = "";
	let password = "";
    function validate(){
        if(mail === "") {
            alert("Введите mail")
            return false;
        }
        if(password === "") {
            alert("Введите пароль")
            return false;
        }
        return true;
    }
	function submit(){
        console.log("start");
        if(!validate()) return;
        //тута запрос к серверу
		console.log("end");
	}
</script>

<h1>authorization</h1>
<div class="authBox">
    <input bind:value={mail} placeholder="Mail" type="email">
    <input bind:value={password} placeholder="Пароль" type="password">
    <div class="buttonsBox">
        <button on:click={submit}>Вход</button>
        <button><a sveltekit:prefetch href="/registration">Регистрация</a></button>
    </div>
</div>

<style>
	.authBox{
		display: flex;
		flex-direction: column;
	}
	.authBox input{
		width: 200px;
	}
    .authBox button{
		width: 100px;
	}
</style>