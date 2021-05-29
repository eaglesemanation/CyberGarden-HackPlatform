<script>
	import Post from '$lib/Post/index.svelte';
	// import { element } from 'svelte/internal';
	let searchLine = "";
	let selectedCity = "";
	const cityMass = [
		 "All", "Таганрог", "Луна", "Москва"
	]
	const postsMassFronServer = [
		{
			name: "CyberGarden Hack",
			location: "Таганрог",
			date: "28.05.2021",
			about: "Хакатон под пальмами для самых крутых людей. Хакатон под пальмами для самых крутых людей. Хакатон под пальмами для самых крутых людей. Хакатон под пальмами для самых крутых людей",
			likes: 56
		},
		{
			name: "hack moon",
			location: "Луна",
			date: "33.06.2022",
			about: "супер пупер дупер хак номер 2",
			likes: 4
		}
	];//для примера, заполнять будем после
	let postsMass = postsMassFronServer;//его строем после поиска 

	function funcSearch(){
		postsMass = [].concat();
		if(selectedCity==="All")selectedCity="";
		if(searchLine==="" && selectedCity===""){
			postsMass = postsMassFronServer.concat();
			return;
		} else if (selectedCity!==""){
			postsMassFronServer.forEach(element => {
				console.log(element.name);
				let hackCity = element.location.toLowerCase(); 
				if(hackCity.indexOf(selectedCity.toLowerCase()) !== -1){
					postsMass = postsMass.concat(element);
				}
			});
			if(searchLine!==""){
				postsMass = [].concat();
				postsMassFronServer.forEach(element => {
				console.log(element.name);
				let hackCity = element.location.toLowerCase(); 
				let hackName = element.name.toLowerCase(); 
				if((hackName.indexOf(searchLine.toLowerCase()) !== -1)&&(hackCity.indexOf(selectedCity.toLowerCase())!== -1)){
					postsMass = postsMass.concat(element);
				}	
			});	
			}
		} else {
			postsMassFronServer.forEach(element => {
				console.log(element.name);
				let hackName = element.name.toLowerCase(); 
				if(hackName.indexOf(searchLine.toLowerCase()) !== -1){
					postsMass = postsMass.concat(element);
				}	
			});	
		}
		
	}
	function handleKeydown(event) {
		if(event.key === "Enter"){
			funcSearch();
		}
	}
</script>

<svelte:head>
	<title>poster</title>
</svelte:head>


<svelte:window on:keydown={handleKeydown}/>

<input bind:value={searchLine} type="text">

<select bind:value={selectedCity} on:change="{() => answer = ''}">
	{#each cityMass as question}
		<option value={question}>
			{question}
		</option>
	{/each}
</select>



<button on:click={funcSearch}>Поиск</button>
<div class="events-block">
	{#each postsMass as post}
		<Post {...post}/>
	{/each}
</div>

<style>
	.events-block {
		display: flex;
		align-self: center;
	}
</style>