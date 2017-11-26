<template>
  <div>
    <div class="f3 code" v-for="post in posts" :key="post.id">
      {{post.id}}<br/>
      {{post.topic_content}}<br/>
      {{post.post_content}}<br/>
      {{post.post_authar}}<br/>
      {{post.url}}
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  computed: mapState(['posts'])
}
</script>

