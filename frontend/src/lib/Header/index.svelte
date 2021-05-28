<script>
	import { page } from '$app/stores';
	import { onMount } from "svelte";
	let Token;
	let Status;
    onMount(() => {
        Token = localStorage.getItem("token");
		Status = localStorage.getItem("status");
    })
</script>

<header>
	<nav>
		<h1>GardenMasters</h1>
		<ul>
			<li><a sveltekit:prefetch href="/">main</a></li>
			{#if Token === null}
				<li><a sveltekit:prefetch href="/authorization">authorization</a></li>
			{:else}
			<li><a sveltekit:prefetch href="/account">account</a></li>
			{/if}
			
			<li><a sveltekit:prefetch href="/poster">Poster</a></li>
			{#if (Status==="organizer")||(Status==="admin")}
				<li><a sveltekit:prefetch href="/eventRegistration">event registration</a></li>
			{/if}
			<li><a sveltekit:prefetch href="/teaming">teaming</a></li>
		</ul>
	</nav>
</header>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@700&display=swap');

	header {
		display: flex;
		justify-content: space-between;
	}

	nav {
		display: flex;
		justify-content: center;
		--background: rgba(255, 255, 255, 0.7);
	}

	ul {
		position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		display: flex;
		justify-content: center;
		align-items: center;
		list-style: none;
		background: var(--background);
		background-size: contain;
	}

	li {
		position: relative;
		height: 100%;
	}

	h1 {
		font-family: 'Red Hat Display';
		font-size: 14px;
	}

	nav a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 1em;
		color: var(--heading-color);
		font-weight: 700;
		font-size: 0.8rem;
		text-transform: uppercase;
		letter-spacing: 10%;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	a:hover {
		color: var(--accent-color);
	}
</style>
