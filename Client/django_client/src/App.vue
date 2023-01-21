<template>
  <header> 
    <div class="wrapper">
      <nav>
        <RouterLink to="/" class="link">Match</RouterLink>
        <RouterLink to="/stats" class="link">Stats</RouterLink>
        <RouterLink to="/groupe" class="link">Groupe</RouterLink>
      </nav>
    </div>
  </header>

  <div class="content">
    <RouterView/>
  </div>
</template>



<script>
import { RouterLink, RouterView } from 'vue-router'
</script>



<style scoped>
  .wrapper{
    max-width: 1000px;
    height: 80px;
    position: relative;
    top: 10px;
    left: 400px;
    background-color: #fafafa;
    border-radius: 20px;
    box-shadow: var(--box-shadow);
  }

  nav
  {
    margin: 0;
    margin-left: 140px;
    position: absolute;
    top: 50%;
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
  }

  .link{
    margin-left: 100px;
    margin-right: 100px;
    font-size: 20px;
    text-decoration: none;
    color: #444;
    border-radius: 10px;
    padding: 5px;
    background-color: var(--primary);
    color: var(--color-primary);
    font-weight: 300;
  }
  .link:hover{
    opacity: 0.8;
    transition: opacity 0.4s;
}

  .content
  {
    position: relative;
    max-width: 1500px;
    min-height: 800px;
    border-radius: 20px;
    top: 50px;
    left: 200px;
    background-color: #fafafa;
    border-radius: 20px;
    box-shadow: var(--box-shadow);
  }
</style>
