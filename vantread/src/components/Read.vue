<template>
  <div class="read">
  <!--阅读页面-->

    <van-nav-bar
      :title="name"
      left-text="返回"
      right-text="目录"
      left-arrow
      @click-left="onClickLeft"
      @click-right="onClickRight"
      style="color: #000;"
    />

    <p class="setting">
        <span class="font">
          <span>字</span>
          <span @click="fontchange(3)" :class='[fontsizec==3 ? "currspan":""]' >大</span>
          <span @click="fontchange(2)" :class='[fontsizec==2 ? "currspan":""]'>中</span>
          <span @click="fontchange(1)" :class='[fontsizec==1 ? "curryan":""]'>小</span>
        </span>

      <span class="yan">
          <span @click="huyan" :class='[ishuyan==1 ? "curryan":""]' >护眼</span>
          <span @click="guandeng"  v-if="isguandeng==0">关灯</span>
          <span @click="guandeng" :class='[isguandeng==1 ? "curryan":""]' v-if="isguandeng==1">开灯</span>
        </span>
    </p>

    <div  :class='{"readcontent":1===1,"guandeng":isguandeng==1 , "huyan":ishuyan==1}'>
      <van-row style="margin-top: 10px;margin-bottom: 26px">
        <van-col span="8" @click="routerpre">上一章</van-col>
        <van-col span="8" >目录</van-col>
        <van-col span="8" @click="routernext()">下一章</van-col>
      </van-row>

      <div id="text" v-html="content"  :class='{"textsize3":fontsizec==3,"textsize2":fontsizec==2,"textsize1":fontsizec==1}'>
        <van-dialog id="van-dialog" />
      </div>

      <van-row style="margin-top: 10px;margin-bottom: 26px">
        <van-col span="8" @click="routerpre">上一章</van-col>
        <van-col span="8">目录</van-col>
        <van-col span="8" @click="routernext()">下一章</van-col>
      </van-row>
    </div>


  </div>
</template>

<script>
  import Vue from 'vue';

  import { NavBar } from 'vant';

  import { Dialog } from 'vant'
  Vue.use(Dialog);

  Vue.use(NavBar);

  export default {
    name: 'read',
    data () {
      return {
        root:this.$route.query.root,
        name:this.$route.query.name,
        chaptertotal:this.$route.query.chaptertotal,
        // root:'kehuan',
        // name:'暗月纪元-仐三',
        // chapteridx:0,
        // chaptertotal:123,
        content:'',
        ishuyan:0,
        isguandeng:0,
        fontsizec:2,
        idx:this.$route.query.startchapter,
      }
    },
    filters:{

    },

    created(){
      console.log(this.$route.query.root)
      console.log(this.$route.query.name)
      console.log(this.$route.query.chaptertotal)
      console.log(this.$route.query.startchapter)
      console.log('reaad');
      this.axiosfuncByIdx(this.idx);
    },
    methods:{
      onClickLeft() {
        this.$router.back()
      },onClickRight() {
      }, onChange(){

      },huyan(){
          this.ishuyan=!this.ishuyan
      },guandeng(){
        this.isguandeng=!this.isguandeng
      },fontchange(size){
        this.fontsizec=parseInt(size)
      },routerpre(){
        // 获取下一章内容
        if(this.idx>0){
          this.idx=this.idx-1
          this.axiosfuncByIdx(this.idx)
        }else{
          console.log('不能再减')
          Dialog.alert({
            message: '无上一章！',
          }).then(() => {
          });
        }

      },routernext(){
        // 获取下一章内容
        this.idx=this.idx+1
        this.axiosfuncByIdx(this.idx)
      },axiosfuncByIdx(idx){
        if(idx<this.chaptertotal){
          this.axios.get('/vantdemo/readphp/data.php?Action=read&name='+this.name+'&root='+this.root+'&chapteridx='+idx+'&chaptertotal='+this.chaptertotal).then(res=>{
            console.log(res.data);
            if(res.data.msg=='success'){
              this.content=res.data.content;
              document.body.scrollTop = 0
            }else{
              this.content='稍后更新！请耐心等待！';
              document.body.scrollTop = 0
            }
          }).catch(function (error) {
            console.log(error);
          });
        }

      }
    }
  }
</script>

<style >
  .readcontent{
    padding: 0 10px;
    background-color: #FBF6EC;
    overflow: hidden;
  }
  .readcontent #text{
    margin-top: 20px;
    color: #000;
    font-size: 18px;
    margin: 0;
    padding: 0;
    text-align: left;

    margin: 10px 5px;
    line-height: 30px;
  }


  .readcontent .textsize3{
    font-size: 20px !important;

  }
  .readcontent .textsize2{
    font-size: 18px !important;

  }
  .readcontent .textsize1{
    font-size: 16px !important;

  }
  .read .huyan{
    background-color: rgb(204, 226, 191);
    color: green;
    /*border: 1px solid rgb(187, 214, 170);*/
  }
  .read .guandeng{
    background-color: rgb(62, 66, 69);
    color: rgb(204, 204, 204);
    /*border: 1px solid rgb(49, 53, 56);*/
  }

  .van-col{
    /*background-color: #f4f0e9;*/
    padding: 10px 0;
  }
  .setting {
    overflow: hidden;
    padding:  10px;
    background-color: #ececec;
    margin: 0;
  }
   .setting span span{
    display: inline-block;
    border: 1px solid #999999;
    font-size: 14px;
    padding: 2px 3px;
  }
   .setting .font{
    float: left;
  }
   .setting .yan{
    float: right;
  }
   .setting .currspan{
    background-color: #999999;
    color: #fff;
    border: none;
  }
  .setting .curryan{
    background-color: #999999;
    color: #fff;
    border: none;
  }






</style>
