<template>
  <div class="intro" v-if="content">

    <van-skeleton title avatar :row="3" :loading="loading">

      <van-nav-bar
        title=""
        :left-text="content.name"
        right-text=""
        left-arrow
        @click-left="onClickLeft"
        style="color: #000;"
      />


      <div class="novelblock">
        <div class="content">
          <div class="leftimg" :style = '{ backgroundImage : "url("+content.headimg +")"}'></div>

          <div class="right">
            <p class="name" >{{content.name}}</p>
            <p><span>{{content.author}}</span></p>
            <p><span v-model="content.root">{{content.root|rootfrom}}</span></p>
            <p><span>{{content.utime}}</span></p>
          </div>

        </div>
        <div style="margin-bottom: 20px;">
          <van-button style="width: 70%;" type="primary" @click="routerchapter()">立即阅读</van-button>
        </div>

      </div>

      <div class="introcontent">
        <p>简介</p>
        <div>
          {{content.intro}}
        </div>
      </div>

      <div class="contentb">
        <p>作品目录</p>
        <ul v-if="content.chapternum>0">
          <li v-for="key in 10" v-if="content.chapternum>10" @click="routerchapter()">第{{key}}章</li>
          <li v-for="key in content.chapternum" @click="routerchapter()" v-else >第{{key}}章</li>
        </ul>
        <ul v-else>
          <li>稍后更新！请耐心等待！</li>
        </ul>
      </div>

      <van-button plain type="primary" size="large" v-if="content.chapternum>5"  @click="routerchapter">查看更多</van-button>

    </van-skeleton>


  </div>
</template>

<script>

  import Vue from 'vue';
  import { NavBar } from 'vant';
  import { Toast } from 'vant';
  import { Tag } from 'vant';
  import { Button } from 'vant';
  import { Skeleton } from 'vant';

  Vue.use(Skeleton);
  Vue.use(Button);

  Vue.use(Tag);


  Vue.use(NavBar);


  export default {
    name: 'Novels',
    data () {
      return {
        id:this.$route.query.id,
        content:[],
        loading: true,
      }
    },
    filters:{
      rootfrom: (root)=> {
        switch (root){
          case 'xuanhuan':
            root='奇幻玄幻'
            break;
          case "chuanyue":
            root='历史军事穿越'
            break;
          case "xiuzhen":
            root='仙剑修真'
            break;
          case "dushi":
            root='言情都市'
            break;
          case "kehuan":
            root='灵异科幻'
            break;
          case "wangyou":
            root='电竞网游'
            break;
          default:
            break;
        }

        return '分类：'+root;
      }
    },
    mounted() {
      this.loading = false;
    },
    beforeRouteLeave(to,from,next){
      to.meta.keepAlive=true;
      next();
    },
    created(){
      console.log(this.id);
        this.axios.get('/vantdemo/readphp/data.php?Action=currintro&id='+this.id).then(res=>{
          console.log(res.data.res);
          this.content=res.data.res;
          console.log(this.content);

        }).catch(function (error) {
          console.log(error);
        });

    },
    methods:{
      onClickLeft() {
        this.$router.back()
      },onClickRight() {
        // Toast('按钮');
      },readnow(root,name){
        this.$router.push({path:'/novels/read',query:{name:this.content.name,root:this.content.root,chaptertotal:this.content.chapternum,startchapter:0}})
      },routerchapter(){
        this.$router.push({path:'/novels/chapter',query:{name:this.content.name,root:this.content.root,chaptertotal:this.content.chapternum}})
      }

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style >
  h1, h2 {
    font-weight: normal;
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
  .intro{
    background-color: #ffffff;
    position: relative;
  }

  .intro .van-swipe__indicators{
    left: 90%;
    bottom: 30px;
  }
  .intro .novelblock{
    width:100%;
    overflow: hidden;
    margin-top: 10px;
  }


  .intro .novelblock .title span{
    display: inline-block;
    width: 0;
    height: 0;
    border-top: 10px solid transparent;
    border-left: 20px solid red;
    border-bottom: 10px solid transparent;
    margin-right: 10px;
  }

  .intro .novelblock .content{
    width: 100%;
    overflow: hidden;
    margin-bottom: 10px;
  }


  .intro .novelblock .content .leftimg{
    height: 130px;
    width: 30%;
    background: url(https://static.zongheng.com/upload/s_image/cover/08/d2/08d2db3532306b6d614bea53f8a4a6ff.jpeg) center center no-repeat;
    background-size: contain;
    float: left;

  }
  .intro .novelblock .content .right{
    float: left;
    width: 60%;
    overflow: hidden;
  }
  .intro .novelblock .content .right p{
    text-align: left;
    margin: 0;
    font-size: 14px;
    margin-top: 8px;
    color: #1a1a1a;
  }
  .intro .novelblock .content .right .name{
    margin: 0;
    text-align: left;
    font-weight: 600;
    font-size: 20px;
    color: #000;
  }
  /*.intro .novelblock .content .right span{*/
    /*display: inline-block;*/
    /*width: 100%;*/
    /*font-size: 0.9em;*/
    /*color: #888;*/
    /*text-align: left;*/
  /*}*/
  .intro .novelblock .content .right .intro{
    margin-top: 10px;
  }
  .intro .novelblock .content .right .intro span{
    display: inline;
    font-size: 0.6em;
    margin-right: 8px;

  }

  .intro .introcontent{
    padding: 10px;
    border-top: 1px solid #eee;
  }

  .intro .introcontent p{
    margin:0;
    text-align: left;
    margin-bottom: 10px;
    color: #000;
  }
  .intro .introcontent div{
    font-size: 14px;
    text-align: left;
    line-height: 24px;
    color: #1a1a1a;

  }
  .intro .contentb{
    padding: 10px;
    border-top: 1px solid #eee;



  }
  .intro .contentb p{
    text-align: left;
    margin: 0;
    color: #1a1a1a;
    margin-bottom: 10px;
  }
  .intro .contentb ul{
    overflow: hidden;
    text-align: left;
  }
  .intro .contentb ul li{
    float: left;
    display: block;
    width: 100%;
    border-bottom: 1px solid #eee;
    padding:3px 0;
    font-size: 14px;
    line-height: 30px;
    color: #1a1a1a;
  }
  .intro .van-button--plain{
    left: 0;
    bottom: 0;
  }


  .van-nav-bar .van-icon {
    color: #000;
  }
  .van-nav-bar__text{
    color: #000;
  }

</style>
