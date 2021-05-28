<script>
	import Post from '$lib/Post/index.svelte';
	const forExample = {
		name: "Cyber Garden",
		date: "28.05.2021",
		about: "супер пупер дупер хак"
	};
</script>

<svelte:head>
	<title>poster</title>
</svelte:head>


<h1>poster</h1>
<Post {...forExample}/>