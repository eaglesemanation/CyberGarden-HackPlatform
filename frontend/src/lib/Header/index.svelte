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
	<div class="header-left"><a sveltekit:prefetch href="/" class="logo-brand">Garden<span class="green">Masters</span></a></div>
    <div class="header-center">
        <ul>
            <li><a sveltekit:prefetch href="/poster">Афиша</a></li>
            <li><a sveltekit:prefetch href="/teaming">Команда</a></li>
			{#if (Status==="organizer")||(Status==="admin")}
				<li><a sveltekit:prefetch href="/eventRegistration">Новое мероприятие</a></li>
			{/if}
        </ul>
    </div>
	{#if Token === null}
    	<a sveltekit:prefetch href="/authorization" class="main-button">Авторизация</a>
	{:else}
		<a sveltekit:prefetch href="/account" class="main-button">Профиль</a>
	{/if}
</header>

<style>

	@import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@700&family=Ubuntu:wght@400;500;700&display=swap');

	header {
		display: flex; 
		justify-content: space-between;
		align-items: center;
		padding: 2em;
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

	a {
		font-family: 'Ubuntu';
		display: flex;
		height: 100%;
		align-items: center;
		padding-right: 1em;
		color: var(--heading-color);
		font-weight: 500;
		font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
		text-decoration: none;
		transition: color 0.2s linear;
	}

	.logo-brand {
		color: #00160A;
		font-family: 'Ubuntu';
		text-decoration: none;
		font-size: calc(24px + (30 - 24) * ((100vw - 300px) / (1440 - 300)));
		font-weight: 700;
	}

	.logo-brand:hover {
		color: #00160A;
	}

	.green {
		color: #43DFA8;
	}

	.main-button {
		background-color: #00160A;
		color: #fff;
		font-family: 'Ubuntu';
		font-weight: 500;
		border-color: #00160A;
		border-radius: 30px;
		padding: 0.75em 2em;
		font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
	}
	
	@media (max-width: 1000px){
   		header	{
			flex-direction: column;
			align-items: flex-start;
    	}
	}

</style>
