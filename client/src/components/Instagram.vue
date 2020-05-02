<template>
  <vue-instagram token="accessTokenHere" :count="5" :tags="['hashtag1', 'hashtag2']" mediaType="image">
    <template v-slot:loading="props">
      <h1 v-if="props.loading" class="fancy-loading">Loading, please wait...</h1>
    </template>
    <template v-slot:feeds="props">
      <li class="fancy-list"> {{ props.feed.link }} </li>
    </template>
    <template v-slot:error="props">
      <div class="fancy-alert"> {{ props.error.error_message }} </div>
    </template>
  </vue-instagram>
</template>

<script>
import VueInstagram from 'vue-instagram';

export default {
  name: 'App',

  components: {
    VueInstagram,
  },
};
</script>
