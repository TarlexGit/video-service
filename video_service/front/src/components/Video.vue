<template>
  <div class="hello">
    <h1>Video Service</h1>

    <h3>select folder</h3>

    <select v-model="selected">
      <option @click="getData(v)" v-for="v in folders" :key="v">
        {{ v }}
      </option>
    </select>
    <span>Выбрано: {{ selected }}</span>
    <div class="media">
      <video
        v-if="video_path"
        id="video"
        width="640"
        height="486"
        class="box1 auto-fill"
        controls
        :src="video_path"
      ></video>
      <div v-if="getVideoData">
        {{ getVideoData }}
      </div>
      <div class="box2 auto-fill" v-if="picture_path">
        <img :src="picture_path" />
      </div>
    </div>
    <ul id="array-rendering">
      <li v-for="item in timecodes['Time']" :key="item">
        <button @click="toTime(item)">
          {{ Number(item.toFixed(2)) }}
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  created() {
    this.getFolders();
  },
  data() {
    return {
      items: [{ message: "Foo" }, { message: "Bar" }],
      selected: "None",
      picture: "../../assets/pic.png",
      timecodes: {},
      video_path: "",
      folders: [],
      loading: false,
      data: {},
      backToFilesPath: "@/../../../files/",
      picture_path: "",
      currentTime: "",
    };
  },
  methods: {
    getFolders() {
      fetch("http://127.0.0.1:8000/api/folders", {
        method: "get",
        headers: {
          "content-type": "application/json",
        },
      })
        .then(async (response) => {
          const data = await response.json();

          this.folders = data.folders;
          console.log(data.folders);
        })
        .catch((error) => {
          this.errorMessage = error;
          console.error("There was an error!", error);
        });
      console.log("go");
    },

    getData(folder) {
      fetch(`http://127.0.0.1:8000/api/data/${folder}`, {
        method: "get",
        headers: {
          "content-type": "application/json",
        },
      }).then(async (response) => {
        const data = await response.json();
        this.data = data;
        this.selected = folder;
        this.video_path = require(`@/../../../files/${data.video_path}`);

        this.timecodes = JSON.parse(data.timecodes);
        console.log(this.timecodes);
        this.picture_path = require(`@/../../../files/${data.picture_path}`);
      });
    },
    toTime(timecode) {
      let video = document.getElementById("video");
      video.currentTime = timecode;
      video.play();
    },
  },
  computed: {
    getVideoData() {
      return this.selected == "None"
        ? console.log("None pass")
        : this.getData(this.selected);
    },
  },
};
</script>


<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.media {
  padding-left: 5%;
  padding-right: 5%;
  display: grid;
  grid-template-columns: repeat(2, fit-content(20%));
  grid-template-rows: repeat(2, 100px);
}
.box1 {
  grid-column-start: 1;
  grid-column-end: 1;
  grid-row-start: 1;
  grid-row-end: 4;
  padding-right: 5%;
}
.box2 {
  grid-column-start: 2;
  grid-column-end: 2;
  grid-row-start: 1;
  grid-row-end: 4;
  padding-left: 5%;
}
.auto-fill {
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
}
</style>
