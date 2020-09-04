<template>
  <div class="novel" >

    <!--<van-swipe :autoplay="3000" style="width: 100%;" indicator-color="#e95e57">-->
      <!--<van-swipe-item v-for="(image, index) in images" :key="index">-->
        <!--<img v-lazy="image" style="width: 100%" />-->
      <!--</van-swipe-item>-->
    <!--</van-swipe>-->

    <!--<van-notice-bar :text=text left-icon="volume-o" />-->


    <div class="topdiv">
      <p>
        <span class="title">云梦泽</span>
        <span class="login" @click="loginUrl">{{logintext}}</span>
      </p>
      <van-grid clickable :column-num="3">
        <van-grid-item  text="首页" to="/" />
        <van-grid-item  text="排行榜" to="/novels/rank" />
        <van-grid-item  text="全部" to="/novels/all" />
      </van-grid>

    </div>

    <div v-for="(items,i) in homedata" v-if="i<1">

    <div class="novelblock" >
      <p class="title lijian"> <span></span>编辑力荐</p>
      <div class="content" v-for="(home ,j) in items.content" v-if="home.intro" @click="routerhref(home.id)">
        <div class="leftimg" :style = '{ backgroundImage : "url("+home.headimg +")"}'  ></div>
        <div class="right divright">
          <p>{{home.name}}</p>
          <span>
            {{home.intro}}
          </span>
          <p class="intro">
            <van-tag mark type="warning" text-color="#fff" v-model="home.author">{{home.author|authorfilter}}</van-tag>
            <van-tag mark type="success" text-color="#fff" v-model="home.root">{{home.root|pathroot}}</van-tag>
            <!--<van-tag mark type="warning" text-color="#fff">完结</van-tag>-->
          </p>
        </div>
      </div>
    </div>

    </div>

<div v-for="(item,i) in homedata" v-if="i>0">
    <div class="novelblock">
      <p class="title"> <span></span>{{item['content'][0]['area']}}</p>
      <div class="content"  v-for="(itemj,jj) in item.content"   v-if="jj<1" :id="'str_'+itemj.id" @click="routerhref(itemj.id)">
        <div class="leftimg" :style = '{ backgroundImage : "url("+itemj.headimg +")"}'></div>
        <div class="right">
          <p >{{itemj.name}}</p>
          <span>
            {{itemj.intro}}
          </span>
          <p class="intro" >
            <van-tag mark type="warning" text-color="#fff" v-model="itemj.author">{{itemj.author|authorfilter}}</van-tag>
            <van-tag mark type="success" text-color="#fff" v-model="itemj.root">{{itemj.root|pathroot}}</van-tag>
            <!--<van-tag mark type="success" text-color="#fff">完结</van-tag>-->
          </p>
        </div>
      </div>

      <ul class="list">
        <li v-for="(itemm,m) in item.content"  v-if="m>0 && itemm.author" :id="'str_'+itemm.id" @click="routerhref(itemm.id)">
          {{itemm.name}} : <span style="color: #999; font-size: 14px;" v-model="itemm.author" >{{itemm.author|authorfilter}}</span>
        </li>
      </ul>
    </div>
</div>

    <p class="bottom">本站所有小说为转载作品，所有章节均由网友上传，转载至本站只是为了宣传本书让更多读者欣赏。</p>


  </div>
</template>

<script>

  import Vue from 'vue';
  import { Lazyload } from 'vant';
  import { NoticeBar } from 'vant';
  import { Grid, GridItem } from 'vant';
  import { Skeleton } from 'vant';
  import { Tag } from 'vant';

  Vue.use(Tag);

  Vue.use(Skeleton);

  Vue.use(Grid);
  Vue.use(GridItem);

  Vue.use(NoticeBar);

  Vue.use(Lazyload);


  export default {
    name: 'Novels',
    data () {
      return {
        msg: 'novels',
        text:'通知：近期网站暂未更新，请读者们耐心等候',
        homedata:'',
        tagdata:[],
        images: [
          '../static/images/read1.jpeg',
          '../static/images/read1.jpeg',
          '../static/images/read3.jpeg'
        ],
        logintext:'登录/注册'
      }
    },
    filters:{
      authorfilter: (author)=> {
        return author.split('作    者：')[1];
      },pathroot:(root)=>{
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

        return root;
      }
    },
    created(){

      if(localStorage.getItem('user')){
        var user=JSON.parse(localStorage.getItem('user'));
        if(user['username']){

          this.logintext=user['username']
        }
      }

      this.axios.get('/vantdemo/readphp/data.php?Action=home').then(res=>{
        var arr=[];
        // console.log(res.data.res);

        this.homedata=res.data.res;
        console.log(this.homedata);

      }).catch(function (error) {
        console.log(error);
      });

    },
    methods:{
      routerhref:function(id){
        this.$router.push({path:'/novels/intro',query:{id:id}})
      },
      loginUrl:function(id){
        this.$router.push({path:'/novels/login'})
      },
      tm:function(e){
        console.log(e);
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
  .novel .van-swipe__indicators{
    left: 90%;
    bottom: 30px;
  }
  .novel .novelblock{
    width:100%;
    overflow: hidden;
  }

  .novel .novelblock .title{
    text-align: left;
  }

  .novel .novelblock .title span{
    display: inline-block;
    width: 0;
    height: 0;
    border-top: 8px solid transparent;
    border-left: 12px solid red;
    border-bottom: 8px solid transparent;
    margin-right: 10px;
  }

  .novel .novelblock .content{
    width: 100%;
    overflow: hidden;
    margin-bottom: 10px;
  }


  .novel .novelblock .content .leftimg{
    height: 130px;
    width: 30%;
    background: url(https://static.zongheng.com/upload/s_image/cover/08/d2/08d2db3532306b6d614bea53f8a4a6ff.jpeg) center center no-repeat;
    background-size: contain;
    float: left;

  }
  .novel .novelblock .content .right{
    float: left;
    width: 60%;
    overflow: hidden;
  }
  .novel .novelblock .content .right p{
    margin: 0;
    margin-bottom: 10px;
    text-align: left;
  }
  .novel .novelblock .content .right span{
    display: inline-block;
    width: 100%;
    font-size: 0.9em;
    color: #888;
    text-align: left;

    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;



  }
  .novel .novelblock .content .right .intro{
    margin-top: 10px;
  }
  .novel .novelblock .content .right .intro span{
    display: inline;
    font-size: 0.6em;
    margin-right: 8px;
  }
  .novel .novelblock .list li{
    display: block;
    border-top: 1px solid #e6e6e6;
    color: #333;
    line-height: 50px;
    text-align: left;
  }

  .novel .novelblock .list li:last-child{
    border-bottom: 1px solid #e6e6e6;
  }
  .novel .novelblock .content .divright{
    border-bottom: 1px solid #e6e6e6;
  }
  .novel .novelblock .lijian span{
    margin:0;
    padding: 0;
    border: 0;
    border-left: 5px solid red;
    height: 18px;
    border-left-width: 4px;
    border-left-height: 10px;
    border-radius: 1px;
    margin-left: 10px;
    margin-right: 10px;
  }
  .topdiv{
    background-color: darkgrey;
    overflow: hidden;
  }
  .topdiv .van-grid-item__content{
    background-color: darkgrey;
    color: #fff;


  }
  .topdiv .van-grid-item__content span{
    color: #fff;

  }
  .topdiv p{
    margin: 0;
    width: 100%;
    height: 40px;
    background-color: darkgrey;
    color: #fff;
    line-height: 40px;
    text-align: left;
    padding: 10px 5px;
  }
  .topdiv p .title{
    font-size: 26px;
    font-weight: 400;
    margin-left: 10px;
  }
  .topdiv p .login{
    float: right;
    margin-right: 20px;
    font-size: 14px;
  }

  .novel .van-grid-item__text{
    font-size: 16px;
  }

  .bottom{
    line-height: 20px;
    font-size: 12px;
    color: #a1a1a1;
    width: 70%;
    margin-left: 15%;
    margin-top: 30px;
    padding-bottom: 20px;
    margin-bottom: 0;
  }


</style>
