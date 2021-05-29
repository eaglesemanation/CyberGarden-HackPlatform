<script>
	import Team from '$lib/LittleTeam/index.svelte';
	// let teams = null;
	let teams = ["GardenMasters", "intSpirit"];
</script>

<svelte:head>
	<title>teaming</title>
</svelte:head>

{#if teams === null}
	<button>join team</button>
{:else}
	{#each teams as team}
		<Team name = {team}/>
	{/each}
{/if}