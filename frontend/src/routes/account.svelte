<script>
	import { onMount } from "svelte";
	let Token;
	let Status;
	let accountInfo = {mail:"vadim@zhopa.com", fio:"Vadim Kandratov", avatar:"http://sun9-39.userapi.com/s/v1/ig2/8aqATIMGN_0ucbrpPT2w9-Od9s4_R-28vuF1rs263b_AnT8lBidXi9Tp1qazfob7TONkocJPt4t4cK1Z6ZOpdx3e.jpg?size=200x0&quality=96&crop=35,35,1002,1009&ava=1", status:"capitan"};
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