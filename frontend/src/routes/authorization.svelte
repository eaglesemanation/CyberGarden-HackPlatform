<script>
	let mail = "";
	let password = "";
    function validate(){

    }
	function submit(){
        if(!validate()) return;
		console.log("authorization");
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