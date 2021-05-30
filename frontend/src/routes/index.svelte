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
    <MainButton btntext="Что за чудо-инструмент?"/>
  </div>
</div>
<div class="about">
  <h1>✋ Можно <span class="green">познакомиться?</span></h1>
  <div class="cards">
    <div class="card">
        <img src="https://static.tildacdn.com/tild3635-6139-4532-b331-326666666563/Video_Call.svg" alt="developer-image">
        <h3>Cooбщество</h3>
        <p>Наш приоритет — удобное и веселое взаимодействие участников с организаторами и между собой. Ведь хакатоны в первую очередь сбор сообщества, а не просто работа над задачей</p>
    </div>
    <div class="card">
        <img src="https://static.tildacdn.com/tild3639-3462-4532-b466-366334663330/Group_14.svg" alt="new-analytics-image">
        <h3>Удобная работа с данными</h3>
        <p>Сбор обратной связи по результам мероприятия, подготовка отчетов с краткой сводкой по участникам, база резюме и много еще полезного</p>
    </div>
    <div class="card">
        <img src="https://static.tildacdn.com/tild3636-6230-4461-b039-336231653933/Group_2.svg" alt="not-it-image">
        <h3>Автоматизация</h3>
        <p>Больше не надо тратить свое время на такие рутинные задачи как распределение участников по трекам или подготовка сертификатов. Система все сделает за вас, наслаждайтесь общением с участниками</p>
    </div>
  </div>
</div>


<style>
  .main {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  .about {
    display: grid;
    justify-content: center;
    align-items: center;
    text-align: center;
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

  .cards {
    display: flex;
    justify-content: center;
    align-items: center;
    align-items: flex-start;
  }

  .card {
    background: #FFFFFF;
    width: 20%;
    margin: 2%;
    padding: 20px;
    height: auto;
    box-shadow: 0px 9.03px 27.09px rgba(176, 190, 197, 0.32), 0px 3.39px 5.64px rgba(176, 190, 197, 0.32);
    border-radius: 10px;
  }

  @media (max-width: 850px) {
    .main {
      flex-direction: column;
      padding: 2em;
    }

    .text {
      margin-left: 0;
      margin-top: 1em;
      text-align: center;
    }
  }
</style>