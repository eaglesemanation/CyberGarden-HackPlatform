<script>
	let name = "";
	let date = "";
	let organizator = [];
	let sponsor = [];
	let location = "";
	let information = "";
	
	function funcCreate(){
		console.log("Create"+information);
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
	<textarea class="information" bind:value={information} placeholder="information"></textarea>
	<input bind:value={sponsor} type="text" placeholder="sponsor">
	<input bind:value={organizator} type="text" placeholder="organizator">
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
