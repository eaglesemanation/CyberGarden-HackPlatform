<script>
  export let id = "";
  export let name = "";
  export let date = "";
  export let location = "";
  export let about = "";
  export let likes = 0;
  export let url = "";
  export let image;
  export let start_date;
  function showFunc(){
    console.log(date);
  }
</script>

<div class="postBox">
  <div class="info">
    <h2>{name}</h2>
    <h3>{start_date}</h3>
    <div class="locationBox">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
            d="M12 2C8.14 2 5 5.14 5 9C5 14.25 12 22 12 22C12 22 19 14.25 19 9C19 5.14 15.86 2 12 2ZM16 10H13V13H11V10H8V8H11V5H13V8H16V10Z"
            fill="#43DFA8"/>
      </svg>
      <h3 class="location">{location.city}</h3>
    </div>
    <p>{about}</p>
  </div>


  <!-- <button on:click={showFunc}>show</button> -->

  <!-- <img src={image} alt=""> -->
  
  <div class="bottom">
    <div class="leftBox">
      <a class="main-button" sveltekit:prefetch href="/events/{id}">Регистрация</a>
      <a class="learn" href={url}>Узнать больше</a>
    </div>
    <h3>{likes}</h3>
  </div>

</div>

<style>
  img{
    margin-right: 0px;
    height: 40%;
    width: 40%;
  }
  .postBox {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-top: 30px;
    background-color: #ffffff;
    border: 3px solid #E1E3E6;
    box-sizing: border-box;
    border-radius: 30px;
    width: 600px;
    margin-left: auto;
    margin-right: auto;
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
    /* padding-top: -100px; */
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
  .learn{
    margin-left: 10px;
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
