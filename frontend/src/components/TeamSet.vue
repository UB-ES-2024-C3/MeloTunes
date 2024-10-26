<template>
  <div class="card-deck">
    <team v-for="(team) in data" :key="team.id" v-bind="team"></team>
  </div>
</template>

<script>
import Team from './Team.vue'

export default {
  name: 'TeamSet',
  components: { 'team': Team },
  data () {
    return {
      data: [],
      count: 0
    }
  },
  mounted () {
    this.count = 2
    this.data = [
      {
        id: 1,
        name: 'test team 1',
        country: 'test team 1 country',
        description: 'an optional description for test team 1'
      },
      {
        id: 2,
        name: 'test team 2',
        country: 'test team 2 country',
        description: null
      }
    ]
  }
}
</script>
