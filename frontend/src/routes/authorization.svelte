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
    <input bind:value={mail} placeholder="E-mail" type="email">
    <input bind:value={password} placeholder="Пароль" type="password">
    <div class="buttonsBox">
        <button on:click={submit} class="auth-button">Вход</button>
        <a sveltekit:prefetch href="/registration" class="reg-button">Регистрация</a>
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@700&family=Ubuntu:wght@400;500;700&display=swap');

	.authBox{
		display: flex;
		flex-direction: column;
	}

	input {
		max-width: 400px;
        height: 48px;
        margin: 1em;
        margin-bottom: 0.5em;
        border-radius: 8px;
        padding-left: 2em;
        border: 1px solid #E1E3E6;
        font-family: 'Ubuntu';
        font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
	}

    input:focus {
        outline: none;
        border: 1px solid #43DFA8;
        box-shadow: 0 0 10px rgba(67, 223, 168, 0.5);
    }

    .buttonsBox {
        margin: 1em;
    }

    .auth-button {
        background-color: #00160A;
		color: #fff;
		font-family: 'Ubuntu';
		font-weight: 500;
		border-color: #00160A;
		border-radius: 30px;
		padding: 0.75em 2em;
		font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
    }

    .reg-button {
        background-color: transparent;
		color: #00160A;
		font-family: 'Ubuntu';
		font-weight: 500;
        border: 2px solid #00160A;
		border-radius: 30px;
		padding: 0.75em 2em;
		font-size: calc(14px + (18 - 14) * ((100vw - 300px) / (1440 - 300)));
    }

</style>