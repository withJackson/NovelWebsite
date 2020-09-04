<template>
<div class="chapter">
  <van-nav-bar
    title="章节"
    left-text="返回"
    left-arrow
    @click-left="onClickLeft"
    @click-right="onClickRight"
  />

  <ul>
    <p>章节阅读  共 <span style="color: #07c160;">{{chaptertotal}}</span> 章</p>
    <li v-for="(item,key) in chaptertotal" @click="readnow(key)">
      第{{key+1}}章
    </li>

  </ul>
</div>

</template>


<script>
  import Vue from 'vue';
  import { NavBar } from 'vant';
  Vue.use(NavBar);
    export default {
      name: "chapter",
      data () {
        return {
          root:this.$route.query.root,
          name:this.$route.query.name,
          chaptertotal:parseInt(this.$route.query.chaptertotal),
        }
      },
      created(){
        // this.axiosfuncByNum(this.nums,this.page,this.classname)
        console.log(this.root)
        console.log(this.name)
        console.log(this.chaptertotal)
      },
      methods:{
        onClickLeft() {
          this.$router.back()
        },onClickRight() {
        },
        readnow(idx){
          console.log(idx)
          this.$router.push({path:'/novels/read',query:{name:this.name,root:this.root,chaptertotal:this.chaptertotal,startchapter:idx}})
        },

      }
    }
</script>

<style >
  .van-nav-bar__left{
    color: black;
  }
  .chapter ul{
    padding: 0 20px;
    text-align: left;
  }
  .chapter ul li{
    width: 100%;
    color: #07c160;
    line-height: 40px;
    border-bottom: 1px solid #bbb;
  }

</style>
