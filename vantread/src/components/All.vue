<template>
  <div class="all">
    <van-nav-bar
      title="全本"
      left-text="返回"
      left-arrow
      @click-left="onClickLeft"
      @click-right="onClickRight"
    />

    <!-- 居中 -->
    <van-row type="flex" justify="center" >
      <van-col span="8" style="padding-top: 10px;" :class="{styleclass:isActive==='xuanhuan'}" @click="classrouter('xuanhuan')">玄幻小说</van-col>
      <van-col span="8"  style="padding-top: 10px;" :class="{styleclass:isActive==='xiuzhen'}" @click="classrouter('xiuzhen')">仙侠小说</van-col>
      <van-col span="8"  style="padding-top: 10px;" :class="{styleclass:isActive==='dushi'}" @click="classrouter('dushi')">都市小说</van-col>
    </van-row>
    <!-- 居中 -->
    <van-row type="flex" justify="center" >
      <van-col span="8" style="padding-bottom: 10px;" :class="{styleclass:isActive==='chuanyue'}" @click="classrouter('chuanyue')">穿越小说</van-col>
      <van-col span="8" style="padding-bottom: 10px;" :class="{styleclass:isActive==='wangyou'}" @click="classrouter('wangyou')">网游小说</van-col>
      <van-col span="8" style="padding-bottom: 10px;" :class="{styleclass:isActive==='kehuan'}" @click="classrouter('kehuan')">科幻小说</van-col>
    </van-row>


    &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;
    &nbsp;  &nbsp;  &nbsp;  &nbsp;
    <hr>

    <ul class="allul">

      <p style="margin-bottom: 0">{{classnametitle}}</p>

      <li v-for="(item,key) in content" @click="routeintro(item.id)">
        <div class="content">
          <p class="title">{{item.name}}</p>
          <p v-model="item.author">作者:{{item.author|authorfilter}}</p>
          <p>总章节:{{item.chapternum}}章</p>
          <p class="intro">简介:{{item.intro}}</p>
        </div>

      </li>

    </ul>
    <van-pagination v-model="currentPage" :page-count="pagecounts" :items-per-page="5" @change="paginfunc" mode="simple"/>

  </div>
</template>

<script>
  import Vue from 'vue';
  import { NavBar } from 'vant';
  import { Toast } from 'vant';

  import { Col, Row } from 'vant';
  import { Pagination } from 'vant';

  Vue.use(Pagination);
  Vue.use(Col);
  Vue.use(Row);
  Vue.use(Toast);
  Vue.use(NavBar);


  export default {
    name: "All",
    data () {
      return {
        content:'',
        nums:20,
        page:0,
        classname:'all',
        currentPage: 1,
        classnametitle:'列表',
        pagecounts:20,
        isActive:''
      }
    },
    filters:{
      authorfilter: (author)=> {
        return author.split('作    者：')[1];
      },utimefilter:(utime)=>{
        var str= utime.split('最后更新：')[1];
        str=str.split(' ')[0]
        return str;
      }
    },
    created(){
      this.axiosfuncByNum(this.nums,this.page,this.classname)
    },
    methods:{
      onClickLeft() {
        this.$router.back()
      },onClickRight() {
      },axiosfuncByNum(nums,page,classname){
        this.axios.get('/vantdemo/readphp/data.php?Action=all&classname='+classname+'&page='+page+'&nums='+nums).then(res=>{
          console.log(res.data.res);
          if((res.data.msg=='success')&&(res.data.res.length>0)){
            this.content=res.data.res;
            this.pagecounts=Math.floor((res.data.total)/this.nums);

          }else{
            this.content='稍后更新！请耐心等待！';
          }
        }).catch(function (error) {
          console.log(error);
        });
      },paginfunc(){ //点击page
        console.log(this.currentPage)
        this.page=this.currentPage-1;
        this.axiosfuncByNum(this.nums,this.page,this.classname)

      }, routeintro(id){
        if(id!==0){
          this.$router.push({path:'/novels/intro',query:{id:id}})
        }else{
          Toast('请稍后！');
        }
      },classrouter(str){
        console.log(str)
        this.page=0
        this.currentPage=0
        this.classname=str
        this.isActive=str;
        var root=''
        switch (str){
          case 'xuanhuan':
            root='玄幻小说'
            break;
          case "chuanyue":
            root='穿越小说'
            break;
          case "xiuzhen":
            root='仙侠小说'
            break;
          case "dushi":
            root='都市小说'
            break;
          case "kehuan":
            root='科幻小说'
            break;
          case "wangyou":
            root='网游小说'
            break;
          default:
            break;
        }
        this.classnametitle=root;

        this.axiosfuncByNum(this.nums,this.page,this.classname)

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

  .all{
    overflow: hidden;
  }
  .all .van-col {
    line-height: 38px;
    float: left;
    box-sizing: border-box;
    min-height: 1px;
  }
  .all .van-col--8 {
    /* border-bottom: 1px solid #bbb; */
    /*border-left: 1px solid #bbb;*/
    background-color: #07c160;
    color: #fff;
    border: none;
  }
  .all .allul li{
    text-align: left;
    margin: 0;
    padding: 0;
    width: 100%;
    padding: 0 10px;
    border-bottom: 1px solid #07c160;
    padding-top: 10px;
    padding-bottom: 20px;
  }

  .all .allul li p{
    margin:0;
    font-size: 14px;
    line-height: 24px;
    overflow: hidden;
  }
  .all .allul .allrank{
    text-align: center;
    display: inline-block;
    width: 30px;
    height: 20px;
    background-color: #07c160;
    color: #fff;
    float: left;
    margin-right: 10px;
    border-radius: 4px;

  }
  .all .allul .content{
    width: 97%;
    padding-right: 10px;
    box-sizing: border-box;
    overflow: hidden;
    float: left;
  }
  .all .allul .content .intro{
    /*white-space: nowrap;*/
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
  }
  .all .allul .content .title{
    font-size: 15px;
    color: #07c160;
    margin-bottom: 6px;
  }
  .all .van-pagination{
    font-size: 14px;
    margin-top: 20px;
    margin-bottom: 30px;
  }
  .all .van-pagination__item{
    font-size: 12px !important;
    color: #07c160;
    border: 1px solid #07c160;
    min-width: 30px;
    height: 32px;
  }
  .all .van-pagination__item--active{
    color: #fff !important;
    background-color: #07c160;
  }
  .all .van-pagination__item:active{
    background-color:#07c160;
  }
  .all .styleclass{
    color: aqua;
  }





</style>
