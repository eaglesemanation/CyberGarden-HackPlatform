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
    <div class="nameAndFriens">
      <h2>{name}</h2>
      {#if name === "Cyber Garden"}
      <div>
        <img class="friends" src="http://sun9-28.userapi.com/s/v1/ig2/T-4OZUw58MtUwNbXVctGitXohRT2pnd2-Jow_eLuq_ILb1JDHZYvxuqBqY4nuwSZnCpcqUmDC2lQ3fWxXlfP3iXQ.jpg?size=400x0&quality=96&crop=542,0,1705,1705&ava=1" alt="">
        <img class="friends" src="data:image/jpeg;base64,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" alt="">
      </div>
      {:else if name ==="VTBхMGNT Хакатон"}
      <img class="friends" src="http://sun9-28.userapi.com/s/v1/ig2/T-4OZUw58MtUwNbXVctGitXohRT2pnd2-Jow_eLuq_ILb1JDHZYvxuqBqY4nuwSZnCpcqUmDC2lQ3fWxXlfP3iXQ.jpg?size=400x0&quality=96&crop=542,0,1705,1705&ava=1" alt="">
      {/if}
    </div>
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
  .nameAndFriens{
    display: flex;
    justify-content: space-between;
  }
  .friends{
    width: 80px;
    height: 80px;
    border-radius: 100px;
  }
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
