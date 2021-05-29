<script>
	import { onMount } from "svelte";
	import { storeFetch, user } from '$lib/_api.js';
	import { userToken } from '$lib/_store.js';

	const promise = storeFetch('https://b.cybergarden.hackmasters.tech/users/profile');

	let state = true;
	let Token;
	let Status;
	let accountInfo = {
						mail:"vadim@zhopa.com", 
						fio:"Vadim Kandratov", 
						avatar:"http://sun9-39.userapi.com/s/v1/ig2/8aqATIMGN_0ucbrpPT2w9-Od9s4_R-28vuF1rs263b_AnT8lBidXi9Tp1qazfob7TONkocJPt4t4cK1Z6ZOpdx3e.jpg?size=200x0&quality=96&crop=35,35,1002,1009&ava=1",
						status:"capitan",
						skills:"svelte, js, python",
						role: "frontend developer",
						education: "NITU MISiS"
					};
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
	function funcEdit(){
		state = !state;
	}
	function funcSave(){
		state = !state;
		//функция сохранение на бек
	}
</script>
<svelte:head>
	<title>account</title>
</svelte:head>

{#await $promise}
	<h1>Загрузка...</h1>
{:then {fio, role, id}}
	<p>{$promise.id}</p>
	<p>{$userToken}</p>
	<img src={accountInfo.avatar} alt="error">
	<h2>{accountInfo.fio}, {accountInfo.status}</h2>
	{#if state}
		<h3>Skills: {accountInfo.skills}</h3>
		<h3>Role in the team: {accountInfo.role}</h3>
		<h3>Education: {accountInfo.education}</h3>
		<button on:click={funcEdit}>edit</button>
	{:else}
		<div class="inputs">
			<input bind:value={accountInfo.skills} type="text" placeholder="Skills">
			<input bind:value={accountInfo.role} type="text" placeholder="Role in the team">
			<input bind:value={accountInfo.education} type="text" placeholder="Education">		
		</div>
		<button on:click={funcSave}>save</button>
	{/if}
{/await}



<button on:click={funcOut}>OUT</button>
<button on:click={funcDelete}>DELETE ACCOUNT</button>

<h1>Token = {Token}, Status = {Status}</h1>


<style>
	.inputs{
		display: flex;
		flex-direction: column;
	}
	input{
		width: 300px;
		margin-bottom: 10px;
	}
	img{
		border-radius: 300px;
		width: 300px;
		height: 300px;
	}
</style>