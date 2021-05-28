<script>
	let mail = "";
	let password1 = "";
	let password2 = "";

	function validate(){
        if(mail === "") {
            alert("Введите mail")
            return false;
        }
        if(password1 === "") {
            alert("Введите пароль")
            return false;
        }
		if(password2 === "") {
            alert("Введите пароль для подтверждения")
            return false;
        }
		if(password1 !== password2) {
            alert("Пароли не совпадают")
			password1 = "";
			password2 = "";
            return false;
        }
        return true;
    }

	function submit(){
		console.log("start");
        if(!validate()) return;
        //тута запрос к серверу
		console.log("end");
	}
</script>

<h1>registration</h1>
<div class="regBox">
	<input bind:value={mail} placeholder="Mail" type="email">
	<input bind:value={password1} placeholder="Пароль" type="password">
	<input bind:value={password2} placeholder="Подтверждение пароля" type="password">
	<button on:click={submit}>Зарегистрировать</button>
</div>

<style>
	.regBox{
		display: flex;
		flex-direction: column;
	}
	.regBox *{
		width: 200px;
	}
</style>