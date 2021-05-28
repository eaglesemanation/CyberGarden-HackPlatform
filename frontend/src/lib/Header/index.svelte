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
	<div class="wrapper">
		<a href="/" class="logo-brand">Garden<span class="green">Masters</span></a>
		<nav>
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
	</div>
</header>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@700&family=Ubuntu:wght@400;500;700&display=swap');

	.wrapper {
		display: flex;
		justify-content: space-between;
		align-items: center;
		align-self: center;
		margin: auto;
		margin-top: 2%;
	}

	header {
		display: flex;
		justify-content: space-between;
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

	.logo-brand {
		color: #00160A;
		font-family: 'Ubuntu';
		text-decoration: none;
		font-size: 30px;
		font-weight: 700;
		padding-left: 5%;
	}

	.logo-brand:hover {
		color: #00160A;
	}

	.green {
		color: #43DFA8;
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
