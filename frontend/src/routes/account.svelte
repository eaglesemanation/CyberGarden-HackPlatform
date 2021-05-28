<script>
	import { onMount } from "svelte";
	let Token;
	let Status;
    onMount(() => {
        Token = localStorage.getItem("token");
		Status = localStorage.getItem("status");
    })
	function funcOut(){
		localStorage.clear();
		window.location.replace("/");
	}
</script>
<svelte:head>
	<title>account</title>
</svelte:head>

<h1>Token = {Token}, Status = {Status}</h1>
<button on:click={funcOut}>OUT</button>