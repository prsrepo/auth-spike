<template>
  <div v-if="currentKRMap" class="edit-form">
    <h4>KRMap</h4>
    <form>
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" class="form-control" id="title"
          v-model="currentKRMap.title"
        />
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <input type="text" class="form-control" id="description"
          v-model="currentKRMap.description"
        />
      </div>
      <div class="form-group">
        <label><strong>Status:</strong></label>
        {{ currentKRMap.published ? "Published" : "Pending" }}
      </div>
    </form>
    <button class="badge badge-primary mr-2"
      v-if="currentKRMap.published"
      @click="updatePublished(false)"
    >
      UnPublish
    </button>
    <button v-else class="badge badge-primary mr-2"
      @click="updatePublished(true)"
    >
      Publish
    </button>
    <button class="badge badge-danger mr-2"
      @click="deleteKRMap"
    >
      Delete
    </button>
    <button type="submit" class="badge badge-success"
      @click="updateKRMap"
    >
      Update
    </button>
    <p>{{ message }}</p>
  </div>
  <div v-else>
    <br />
    <p>Please click on a KRMap...</p>
  </div>
</template>
<script>
import KRmapDataService from "../services/KRMapDataService";
export default {
  name: "krmap-details",
  data() {
    return {
      currentKRMap: null,
      message: ''
    };
  },
  methods: {
    getKRMap(id) {
      KRmapDataService.get(id)
        .then(response => {
          this.currentKRMap = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    updatePublished(status) {
      var data = {
        id: this.currentKRMap.id,
        title: this.currentKRMap.title,
        description: this.currentKRMap.description,
        published: status
      };
      KRmapDataService.update(this.currentKRMap.id, data)
        .then(response => {
          console.log(response.data);
          this.currentKRMap.published = status;
          this.message = 'The status was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },
    updateKRMap() {
      KRmapDataService.update(this.currentKRMap.id, this.currentKRMap)
        .then(response => {
          console.log(response.data);
          this.message = 'The krmap was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },
    deleteKRMap() {
      KRmapDataService.delete(this.currentKRMap.id)
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "krmaps" });
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getKRMap(this.$route.params.id);
  }
};
</script>
<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>