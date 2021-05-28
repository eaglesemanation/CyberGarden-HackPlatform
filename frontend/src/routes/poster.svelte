<script>
	import Post from '$lib/Post/index.svelte';
	const postsMass = [
		{
			name: "Cyber Garden",
			date: "28.05.2021",
			about: "супер пупер дупер хак"
		},
		{
			name: "hack moon",
			date: "33.06.2022",
			about: "супер пупер дупер хак номер 2"
		}
	];//для примера, заполнять будем после
</script>

<svelte:head>
	<title>poster</title>
</svelte:head>
{#each postsMass as post}
	<Post {...post}/>
{/each}
<!-- <Post {...forExample[1]}/> -->