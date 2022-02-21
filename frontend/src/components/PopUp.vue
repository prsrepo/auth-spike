<template>
  <div class="pop-up">
    <div class="modal" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" @click="closeModal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <iframe :src="redirectUrl"></iframe>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "pop-up",
    props: {
        redirectUrl: String
    },
    setup(props) {
        console.log(props.redirectUrl)
    },
    methods: {
      closeModal() {
        this.$emit('close-modal-event');
      }
    }
  }
</script>

<style scoped>
  /* Override default value of 'none' */
  .modal {
    display: block;
  }
</style>