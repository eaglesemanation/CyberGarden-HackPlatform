<script context="module">
	export const prerender = true;
</script>

<svelte:head>
	<title>Главная</title>
</svelte:head>

<div class="main"> 
	<div class="text">
		<h1 class="black">Garden<span class="green">Masters</span></h1>
		<h3>Платформа для проведения мероприятий с упором на социальное взаимодействие и умную работу с данными</h3>
		<a href="/" class="main-button">Что за чудо инструмент?</a>
	</div>
</div>


<style>
	.main{
		display: flex;
		justify-content: space-around;
		margin-top: 100px;
	}
	.green{
		color: #43DFA8;
	}
	.black{
		color: #00160A;
		font-family: 'Ubuntu';
		text-decoration: none;
		font-size: calc(24px + (30 - 24) * ((100vw - 300px) / (1440 - 300)));
		font-weight: 1000;
	}
	.text{
		margin-top: 100px;
	}
	h3{
		font-style: normal;
		font-weight: 500;
		font-size: 24px;
		line-height: 29px;
		color: rgba(0, 22, 10, 0.7);
		width: 40vw;
		max-width: 500px;
		margin-bottom: 30px;
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
	@media (max-width: 850px){
		.main{
			flex-direction: column;
			align-items: flex-start;
    	}
		img{
			margin-left: auto;
			margin-right: auto;
		}
		.text{
			margin-left: auto;
			margin-right: auto;
		}
	}
</style>