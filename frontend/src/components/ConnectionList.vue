<template>
 <div id="connection-list" class="container">
  <b-table striped hover outlined :items="posts"></b-table>
 </div>
</template>
<script>
 export default {
  name: "ConnectionList",
  data() {
   return {
    posts: [
     {
      userId: 1,
      id: 1,
      title: "sunt aut facere repellat provident occaecati",
     },
     {
      userId: 1,
      id: 2,
      title: "qui est esse",
     },
     {
      userId: 1,
      id: 3,
      title: "ea molestias quasi exercitationem repellat qui",
     },
    ],
   };
  }
 }
</script>