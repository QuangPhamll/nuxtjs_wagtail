import axios from 'axios'

export default axios.create({
  baseURL:  process.env.URL_BACKEND_SERVER || process.env.URL_BACKEND_CLIENT
})
