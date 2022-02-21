<template>
  <div>
      <div>Recentfiles API response</div>
      <br>
      {{recentFiles}}
  </div>
</template>
<script>
import KRMapDataService from "../services/KRMapDataService";

export default {
  name: "oauth-2",
  created: function() {
    this.getRecentFiles();
  },
  data() {
    return {
      recentFiles: []
    };
  },
  methods: {
    getRecentFiles() {
      KRMapDataService.recentFiles()
        .then(response => {
          this.recentFiles = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
  }
};
</script>
<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>