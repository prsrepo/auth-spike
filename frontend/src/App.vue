<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <router-link to="/" class="navbar-brand">KR Integrations</router-link>
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/search" class="nav-link">Search</router-link>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Connections
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <router-link to="/oauth2" class="dropdown-item">Create(Auth)</router-link>
              <!-- <router-link to="/connlist" class="dropdown-item">List</router-link> -->
          </div>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            KRMap
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link to="/krmaps" class="dropdown-item">List</router-link>
            <router-link to="/add" class="dropdown-item">Create</router-link>
          </div>
        </li>
        
      </div>
    </nav>
    <div class="container mt-3">
      <router-view />
    </div>
  </div>
</template>
<script>
export default {
  name: "app"
};
</script>