<script>
  export let id = "";
  export let name = "";
  export let date = "";
  export let location = "";
  export let about = "";
  export let likes = 0;
  export let link = "";
</script>

<div class="postBox">
  <div class="info">
    <h2>{name}</h2>
    <h3>{date}</h3>
    <div class="locationBox">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
            d="M12 2C8.14 2 5 5.14 5 9C5 14.25 12 22 12 22C12 22 19 14.25 19 9C19 5.14 15.86 2 12 2ZM16 10H13V13H11V10H8V8H11V5H13V8H16V10Z"
            fill="#43DFA8"/>
      </svg>
      <h3 class="location">{location}</h3>
    </div>
    <p>{about}</p>
  </div>

  <div class="bottom">
    <a class="main-button" sveltekit:prefetch href="/events/{id}">Регистрация</a>
    <h3>{likes}</h3>
  </div>

</div>

<style>

  .postBox {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-top: 30px;
    background-color: #ffffff;
    border: 3px solid #E1E3E6;
    box-sizing: border-box;
    border-radius: 30px;
    width: 681px;
    margin-left: 2%;
    margin-right: 2%;
    padding: 2%;
  }

  h2, h3, p {
    font-family: 'Ubuntu', serif;
    color: #00160A;
    line-height: 0.5;
  }

  h2 {
    line-height: 1;
    font-weight: 700;
    font-size: 30px;
    text-overflow: ellipsis;
    overflow: hidden;
  }

  h3 {
    font-size: 20px;
    font-weight: 500;
  }

  a {
    line-height: 2;
  }

  p {
    font-weight: 400;
    line-height: 1.5;
  }

  .bottom {
    display: flex;
    justify-content: space-between;
  }

  .location {
    color: #43DFA8;
  }

  .locationBox {
    display: flex;
  }

  .locationBox svg {
    margin-top: auto;
    margin-bottom: auto;
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
</style>
