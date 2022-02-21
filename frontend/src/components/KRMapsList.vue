<template>
  <div class="list row">
    <div class="col-md-8">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Search by title"
          v-model="title"/>
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button"
            @click="searchTitle"
          >
            Search
          </button>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <h4>KRMaps List</h4>
      <ul class="list-group">
        <li class="list-group-item"
          :class="{ active: index == currentIndex }"
          v-for="(krmap, index) in KRMaps"
          :key="index"
          @click="setActiveKRMap(krmap, index)"
        >
          {{ krmap.title }}
        </li>
      </ul>
      <button class="m-3 btn btn-sm btn-danger" @click="removeAllKRMaps">
        Remove All
      </button>
    </div>
    <div class="col-md-6">
      <div v-if="currentKRMap">
        <h4>KRMap</h4>
        <div>
          <label><strong>Title:</strong></label> {{ currentKRMap.title }}
        </div>
        <div>
          <label><strong>Description:</strong></label> {{ currentKRMap.description }}
        </div>
        <div>
          <label><strong>Status:</strong></label> {{ currentKRMap.published ? "Published" : "Pending" }}
        </div>
        <router-link :to="'/KRMaps/' + currentKRMap.id" class="badge badge-warning">Edit</router-link>
      </div>
      <div v-else>
        <br />
        <p>Please click on a KRMap...</p>
      </div>
    </div>
  </div>
</template>
<script>
import KRmapDataService from "../services/KRMapDataService";
export default {
  name: "KRMaps-list",
  data() {
    return {
      KRMaps: [],
      currentKRMap: null,
      currentIndex: -1,
      title: ""
    };
  },
  methods: {
    retrieveKRMaps() {
      KRmapDataService.getAll()
        .then(response => {
          this.KRMaps = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    refreshList() {
      this.retrieveKRMaps();
      this.currentKRMap = null;
      this.currentIndex = -1;
    },
    setActiveKRMap(krmap, index) {
      this.currentKRMap = krmap;
      this.currentIndex = krmap ? index : -1;
    },
    removeAllKRMaps() {
      KRmapDataService.deleteAll()
        .then(response => {
          console.log(response.data);
          this.refreshList();
        })
        .catch(e => {
          console.log(e);
        });
    },
    
    searchTitle() {
      KRmapDataService.findByTitle(this.title)
        .then(response => {
          this.KRMaps = response.data;
          this.setActiveKRMap(null);
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.retrieveKRMaps();
  }
};
</script>
<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>