<script>
	let name = "";
	let date = "";
	let organizator = [];
	let sponsor = [];
	let location = "";
	let information = "";
	
	function funcCreate(){
		console.log("Create");
	}
</script>


<svelte:head>
	<title>event registration</title>
</svelte:head>

<h1>event registration</h1>
<div class="inputBox">
	<input bind:value={name} type="text" placeholder="name">
	<input bind:value={date} type="text" placeholder="date">
	<input bind:value={location} type="text" placeholder="location">
	<input class="information" bind:value={information} type="text" placeholder="information">
</div>
<button on:click={funcCreate}>create</button>
<style>
	.inputBox{
		display: flex;
		flex-direction: column;
	}
	.inputBox *{
		width: 300px;
	}
	.inputBox .information{
		height: 200px;
	}
</style>
