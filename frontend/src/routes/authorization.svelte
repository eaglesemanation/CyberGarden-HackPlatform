<script>
    import { onMount } from "svelte";
	let mail = "";
	let password = "";
    let Token;
    onMount(() => {
        Token = localStorage.getItem("token");
        console.log(Token)
    })
    import { userToken, userStatus } from '$lib/_store';
    function validate(){
        if(mail === "") {
            alert("Введите mail")
            return false;   
        }
        if(password === "") {
            alert("Введите пароль")
            return false;
        }
        return true;
    }
	function submit(){
        if(!validate()) return;
        //тута запрос к серверу
        userToken.updateInfo("12:asd1:12w1e:1231");//заглушка, получим с бека
        userStatus.updateInfo("capitan");//заглушка, получим с бека
		window.location.replace("/");//если все прошло успешно
	}
</script>

<h1>token in storage (svelte) - {Token}</h1>
<div class="authBox">
    <input bind:value={mail} placeholder="Mail" type="email">
    <input bind:value={password} placeholder="Пароль" type="password">
    <div class="buttonsBox">
        <button on:click={submit}>Вход</button>
        <button><a sveltekit:prefetch href="/registration">Регистрация</a></button>
    </div>
</div>

<style>
	.authBox{
		display: flex;
		flex-direction: column;
	}
	.authBox input{
		width: 200px;
	}
    .authBox button{
		width: 100px;
	}
</style>