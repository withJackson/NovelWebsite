<template>

  <div class="login">
    <div class="logindiv">
      <van-nav-bar
        :title=title
        left-text=""
        :right-text=resign
        left-arrow
        @click-left="onClickLeft"
        @click-right="onClickRight"
      />

      <div class="form">

        <van-form @submit="onSubmit">
          <van-field
            v-model="username"
            name="username"
            label="用户名"
            placeholder="用户名"

          />
          <van-field
            v-model="password"
            type="password"
            name="password"
            label="密码"
            placeholder="密码"
            :rules="[{ required: true, message: '请填写密码' }]"
          />
          <div style="margin: 16px;margin-top: 40px">
            <van-button round block type="info" native-type="submit">
              {{title}}
            </van-button>
          </div>
        </van-form>


      </div>

    </div>




  </div>
</template>

<script>
  import Vue from 'vue';
  import { NavBar } from 'vant';
  import { Form } from 'vant';
  import { Toast } from 'vant';

  Vue.use(Toast);

  Vue.use(Form);
  Vue.use(NavBar);

  export default {
    name: 'Novels',
    data () {
      return {
        title:'登录',
        resign:'注册',
        username: '',
        password: '',
      }
    },
    filters:{
      authorfilter: (author)=> {
        return author.split('作    者：')[1];
      }
    },
    created(){


    },
    methods:{
      onSubmit(values) {
        console.log('submit', values);

        var type=2
        if(this.title=='登录'){
          type=2
        }else if(this.title=='注册'){
          type=1
        }

        this.axiosfuncLogin(values.username,values.password,type)
      },
      onClickLeft() {
        this.$router.back()

      },onClickRight() {
        console.log('right');
        console.log(this.title);

        if(this.title=='登录'){
          this.title='注册'
          this.resign='登录'
        }else if(this.title=='注册'){
          this.title='登录'
          this.resign='注册'
        }

      },axiosfuncLogin(username,password,type){
        this.axios.get('/vantdemo/readphp/data.php?Action=login&username'+'='+username+'&password='+password+'&type='+type).then(res=>{
          console.log(res.data);
            Toast.success(res.data.msg);
            const user={"username":this.username,"password":this.password};
            localStorage.setItem('user',JSON.stringify(user));
            this.$router.push({path:'/novels'})
        }).catch(function (error) {
          console.log(error);
        });
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
  .form{
    margin-top: 20%;
    padding: 0 10px;
  }

  .logindiv{
    padding-bottom: 103%;
  }








</style>
