<script>
	let mail = "";
	let password1 = "";
	let password2 = "";

	function submit(){
		console.log("registration");
	}
</script>

<h1>registration</h1>
<div class="regBox">
	<input bind:value={mail} placeholder="Mail" type="email">
	<input bind:value={password1} placeholder="Пароль" type="password">
	<input bind:value={password2} placeholder="Подтверждение пароля" type="password">
	<button on:click={submit}>Зарегистрировать</button>
</div>

<style>
	.regBox{
		display: flex;
		flex-direction: column;
	}
	.regBox *{
		width: 200px;
	}
</style>