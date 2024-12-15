import axios from '../http-common'

class CommentService {
  getAll () {
    return axios.get('/api/v1/comments/')
      .then((res) => {
        return res
      })
  }
  get (commentId) {
    return axios.get(`/api/v1/comments/${commentId}`)
      .then((res) => {
        return res
      })
  }
  getAllUser (userName) {
    return axios.get(`/api/v1/comments/comments/${userName}`)
      .then((res) => {
        return res
      })
  }
  getAllSong (songTitle) {
    return axios.get(`/api/v1/comments/comments/${songTitle}`)
      .then((res) => {
        return res
      })
  }
  createComment (text, user, song) {
    const now = new Date()
    const timestamp = now.toISOString()
    return axios.post('/api/v1/comments/', {
      text: text,
      user: user,
      song: song,
      timestamp: timestamp
    })
      .then((res) => {
        return res
      })
      .catch(error => {
        console.error(error)
        throw new Error('Something went wrong.')
      })
  }
  deleteComment (commentId) {
    return axios.delete(`/api/v1/comments/${commentId}`)
      .then((res) => {
        return res
      })
      .catch(error => {
        console.error(error)
        throw new Error('The song already exists in the system.')
      })
  }
}

export default new CommentService()
