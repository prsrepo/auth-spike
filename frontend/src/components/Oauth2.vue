<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="name">name</label>
        <input
          type="text"
          class="form-control"
          id="name"
          required
          v-model="connection.name"
          name="name"
        />
      </div>
      <div class="form-group">
        <label for="email">email</label>
        <input
          class="form-control"
          id="email"
          required
          v-model="connection.email"
          name="email"
        />
      </div>
      <button @click="createConnection" class="btn btn-success">Submit</button>
      <div>
          <br><br>
          <pop-up v-if="displayModal" :redirect-url="redirectURL" @close-modal-event="hideModal" />
      </div>
    </div>
  </div>
</template>
<script>
import Oauth2Service from "../services/Oauth2Service";
import PopUp from "./PopUp"

export default {
  name: "oauth-2",
  components: {
      PopUp
  },
  data() {
    return {
      redirectURL: "",
      submitted: false,
      displayModal: false,
      connection: {
        name: "",
        email: "",
      }
    };
  },
  methods: {
    hideModal() {
    this.displayModal = false;
    },
    createConnection() {
      var data = {
        name: this.connection.name,
        email: this.connection.email
      };
      Oauth2Service.getAuthURL(data)
        .then(response => {
          console.log(response.data);
          window.open(response.data.url, '_blank');
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