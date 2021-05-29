import { writable } from 'svelte/store';

//ввиды статуса: participant

function createToken() {
	const { subscribe, set, update } = writable("none");

	return {
		subscribe,
		updateInfo: (a) => {
            console.log("Token!");
            localStorage.setItem('token', a);
            update(n => a);
        },
		reset: () => set("")
	};
}

function createStatus() {
	const { subscribe, set, update } = writable("none");

	return {
		subscribe,
		updateInfo: (a) => {
            console.log("Status!");
            localStorage.setItem('status', a);
            update(n => a);
        },
		reset: () => set("")
	};
}

export const userToken = createToken();
export const userStatus = createStatus();
export const testStore = writable(null);