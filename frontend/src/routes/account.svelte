<script>
	import { onMount } from "svelte";
	let Token;
	let Status;
	let accountInfo = {mail:"vadim@zhopa.com", fio:"Vadim Kandratov", avatar:"https://images.app.goo.gl/XfutCMxgtQ6DV6BH6", status:"capitan"};
    onMount(() => {
        Token = localStorage.getItem("token");
		Status = localStorage.getItem("status");
    })
	function funcOut(){
		localStorage.clear();
		window.location.replace("/");
	}
	function funcDelete(){
		if(confirm("exactly?")){
			alert("Deleting...")
		}
	}
</script>
<svelte:head>
	<title>account</title>
</svelte:head>

<img src={accountInfo.avatar} alt="error">
<h2>FIO: {accountInfo.fio}</h2>
<h2>Status: {accountInfo.status}</h2>
<h1>Token = {Token}, Status = {Status}</h1>
<button on:click={funcOut}>OUT</button>
<button on:click={funcDelete}>DELETE ACCOUNT</button>

<style>
	img{
		width: 300px;
		height: 300px;
	}
</style>