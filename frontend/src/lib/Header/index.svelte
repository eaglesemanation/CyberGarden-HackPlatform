<script>
	import { page } from '$app/stores';
</script>

<header>
	<nav>
		<ul>
			<li><a sveltekit:prefetch href="/">main</a></li>
			<li><a sveltekit:prefetch href="/authorization">authorization</a></li>
			<li><a sveltekit:prefetch href="/poster">Poster</a></li>
			<li><a sveltekit:prefetch href="/eventRegistration">event registration</a></li>
			<li><a sveltekit:prefetch href="/teaming">teaming</a></li>
		</ul>
	</nav>
</header>

<style>
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
