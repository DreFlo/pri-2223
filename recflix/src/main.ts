import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import axios from 'axios';

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faSearch, faUserCircle, faEnvelope, faUpload, faPenToSquare, faPlus, faMinus } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'

library.add(faSearch, fab, faUserCircle, faEnvelope, faUpload, faPenToSquare, faPlus, faMinus)

axios.defaults.withCredentials = false;

let app = createApp(App)

app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
