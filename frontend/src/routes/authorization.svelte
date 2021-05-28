<script>
	let mail = "";
	let password = "";

	function submit(){
		console.log("start");
	}
</script>

<h1>authorization</h1>
<input bind:value={mail} type="email">
<input bind:value={password} type="password">
<button on:click={submit}>Вход</button>
<button><a sveltekit:prefetch href="/registration">Регистрация</a></button>