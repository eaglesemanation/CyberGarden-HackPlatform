<script context="module">
  export const prerender = true;
</script>

<script>
  import MainButton from '$lib/MainButton/index.svelte';
</script>

<svelte:head>
  <title>Главная</title>
</svelte:head>

<div class="main">
  <img src="https://static.tildacdn.com/tild3866-6533-4062-a461-663039383531/Done.svg" alt=""/>
  <div class="text">
    <h1>Garden<span class="green">Masters</span></h1>
    <h3>Платформа для проведения мероприятий с упором на социальное взаимодействие и умную работу с данными</h3>
    <MainButton btntext="Что за чудо-инструмент?"></MainButton>
  </div>
</div>


<style>
  .main {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 5em;
  }

  img {
    max-width: 100%;
  }

  h1 {
    font-family: 'Ubuntu';
    font-weight: 700;
    font-size: calc(18px + (26 - 18) * ((100vw - 300px) / (1440 - 300)));
  }

  .green {
    color: #43DFA8;
  }

  .text {
    max-width: 400px;
    margin-left: 3em;
  }

  h3 {
    font-family: 'Ubuntu';
    color: #00160A;
    font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
    font-weight: 400;
  }

  @media (max-width: 850px) {
    .main {
      flex-direction: column;
    }

    .text {
      margin-left: 0;
    }
  }
</style>