<script context="module">
  import {fetches} from "$lib/api"

  export async function load({page, session}) {
    let {token, role} = session;
    if (!token || !role) {
      return {redirect: "/users/signin", status: 301};
    }

    let invite = page.params.token;
    let promise = fetches.get(`/teams/enter/${invite}`);

    return {props: {promise}}
  }
</script>

<script>
  export let promise;

</script>

<div>
  {#await $promise}
  {:then d}
    <p>{JSON.stringify(d)}</p>
  {/await}
  <h1>Hello</h1>
</div>
