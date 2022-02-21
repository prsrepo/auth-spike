<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="title">Title</label>
        <input
          type="text"
          class="form-control"
          id="title"
          required
          v-model="krmap.title"
          name="title"
        />
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <input
          class="form-control"
          id="description"
          required
          v-model="krmap.description"
          name="description"
        />
      </div>
      <button @click="saveKRMap" class="btn btn-success">Submit</button>
    </div>
    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newKRMap">Add</button>
    </div>
  </div>
</template>
<script>
import KRMapDataService from "../services/KRMapDataService";
export default {
  name: "add-krmap",
  data() {
    return {
      krmap: {
        id: null,
        title: "",
        description: "",
        published: false
      },
      submitted: false
    };
  },
  methods: {
    saveKRMap() {
      var data = {
        title: this.krmap.title,
        description: this.krmap.description
      };
      KRMapDataService.create(data)
        .then(response => {
          this.krmap.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
    
    newKRMap() {
      this.submitted = false;
      this.krmap = {};
    }
  }
};
</script>
<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>