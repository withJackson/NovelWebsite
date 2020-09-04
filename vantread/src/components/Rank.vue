<template>

  <div class="rank">

    <van-nav-bar
      title="分类排行榜"
      left-text=""
      right-text=""
      left-arrow
      @click-left="onClickLeft"
      style="color: #000;"
    />

    <van-dropdown-menu>
      <van-dropdown-item v-model="value1" :options="option1" @change="onSwitch1Change" />
      <van-dropdown-item v-model="value2" :options="option2" @change="onSwitch2Change" />
    </van-dropdown-menu>


  <div class="classdiv">
    <!--<p class="tags" > <span v-model="content[0].classname">{{content[0].classname|pathroot}}</span> <span class="datetag" v-model="this.value2">{{this.value2|datetext}}</span></p>-->
    <ul>
      <li v-for="(item) in content" @click="routeintro(item.id)">
        <span class="ranknum">{{item.rank}}</span>
        <span>{{item.name}}</span>
      </li>

    </ul>
  </div>


  </div>
</template>

<script>
  import Vue from 'vue';
  import { DropdownMenu, DropdownItem } from 'vant';
  import { Toast } from 'vant';

  Vue.use(Toast);
  Vue.use(DropdownMenu);
  Vue.use(DropdownItem);

  export default {
    name: 'Novels',
    data () {
      return {
        content:'',
        tag:'xuanhuan',
        date:'total',
        number:20,
        value1: 0,
        value2: 3,
        option1: [
          { text: '奇幻.玄幻', value: 0 },
          { text: '仙侠.修真', value: 1 },
          { text: '青春.都市', value: 2 },
          { text: '历史.穿越', value: 3 },
          { text: '网游.竞技', value: 4 },
          { text: '灵异.科幻', value: 5 },
          { text: '女生', value: 6 },
          { text: '男生', value: 7 },
        ],
        option2: [
          { text: '日排行榜', value: 0 },
          { text: '周排行榜', value: 1 },
          { text: '月排行榜', value: 2 },
          { text: '总排行榜', value: 3 },
        ],
      }
    },
    filters:{
      authorfilter: (author)=> {
        return author.split('作    者：')[1];
      },pathroot:(root)=>{
        switch (root){
          case 'nv':
            root='女生小说推荐排行榜'
            break;
          case 'nan':
            root='男生小说推荐排行榜'
            break;
          case 'xuanhuan':
            root='奇幻.玄幻小说推荐排行榜'
            break;
          case "chuanyue":
            root='历史.军事穿越小说推荐排行榜'
            break;
          case "xiuzhen":
            root='仙剑.修真小说推荐排行榜'
            break;
          case "dushi":
            root='言情.都市小说推荐排行榜'
            break;
          case "kehuan":
            root='灵异.科幻小说推荐排行榜'
            break;
          case "wangyou":
            root='电竞.网游小说推荐排行榜'
            break;
          default:
            break;
        }

        return root;
      },datetext:(value2)=>{
        switch (value2){
          case 0:
            value2='日排行榜'
            break;
          case 1:
            value2='周排行榜'
            break;
          case 2:
            value2='月排行榜'
            break;
          case 3:
            value2='总排行榜'
            break;

          default:
            break;
        }
        return value2;
      }
    },


    created(){
      this.axiosfuncByNum();
    },
    methods:{
      onClickLeft() {
        this.$router.back()
      },onClickRight() {
        // Toast('按钮');
      },axiosfuncByNum(){
          this.axios.get('/vantdemo/readphp/data.php?Action=rank&tag='+this.tag+'&date='+this.date+'&number='+this.number).then(res=>{
            console.log(res.data.res);
            if(res.data.msg=='success'){
              this.content=res.data.res;
            }else{
              this.content='稍后更新！请耐心等待！';
            }
          }).catch(function (error) {
            console.log(error);
          });

      },onSwitch1Change(){
        this.textByValue(this.value1)
        this.axiosfuncByNum()
      },onSwitch2Change(){
        this.dateByValue(this.value2)
        this.axiosfuncByNum()
      },textByValue(value1){
        switch (value1){
          case 0:
            this.tag='xuanhuan';
            break;
          case 1:
            this.tag='xiuzhen';
            break;
          case 2:
            this.tag='dushi';
            break;
          case 3:
            this.tag='chuanyue';
            break;
          case 4:
            this.tag='wangyou';
            break;
          case 5:
            this.tag='kehuan';
            break;
          case 6:
            this.tag='nv';
            break;
          case 7:
            this.tag='nan';
            break;
          default:
            break;
        }


      },dateByValue(value2){
        switch (value2){
          case 0:
            this.date='day';
            break;
          case 1:
            this.date='week';
            break;
          case 2:
            this.date='month';
            break;
          case 3:
            this.date='total';
            break;

          default:
            break;
        }
      },routeintro(id){
        if(id!==0){
          this.$router.push({path:'/novels/intro',query:{id:id}})
        }else{
          Toast('请稍后！');
        }

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
  .rank .tags{
    text-align: left;
    color: #07c160;
    font-size: 14px;
    padding-left: 10px;

  }
  .rank ul li{
    display: block;
    text-align: left;
    border-top: 1px solid #bbb;
    font-weight: 400;
    line-height: 38px;
    font-size: 16px;
  }
  .rank ul li:last-child{
    border-bottom: 1px solid #bbb;
  }
  .rank ul li span{
    margin-left: 10px;

  }
  .rank ul li .ranknum{
    display: inline-block;
    color: #07c160;
    /*background-color: #07c160;*/
    font-size: 14px;
    text-align: center;
  }
  .rank li .readmore{
    color: #3366BB;
    margin-left: 90%;

  }
  .classdiv{
    padding-bottom: 20px;
  }
  .tags span{
    display: inline-block;
    width: 49%;
    text-align: center;
  }






</style>
