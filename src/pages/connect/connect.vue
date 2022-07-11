<template>
  <div id="netweb">
    <div class = "center">
      <!-- info-message to show the name,time of connection,usage of flux -->
      <div class = "greet">欢迎，&nbsp;Welcome,</div>
      <div id = "info">
        <h2 class = "name" id = "uname">{{user_name}}</h2>
        <div id = "info_content">
          <div class = "label_text">
            <div class = "chinese-txt">已连接</div>
            <div class = "english-txt">Duration</div>
          </div>
          <div class = "content-text">
            <t_Clock id = "clock">00:00:00</t_Clock>
          </div>
          <div class = "label_text">
            <div class = "chinese-txt">已用流量</div>
            <div class = "english-txt">Usage</div>
          </div>
          <!-- draw the usage of flux -->
          <div id = "usage-bar">
            <ul class = "calibration">
              <li>125</li>
              <li>100</li>
              <li>75</li>
              <li>50</li>
            </ul>
            <div id = "usage-value"></div>
            <div id = "firststripe"></div>
            <div id = "secondstripe"></div>
            <div class = "content-text">
              <t_Flux class="unit" id="usage-flux" ></t_Flux>
            </div>
          </div>
        </div>
      </div>
      <div class = "disbar">
        <button id = "disconnect" onclick="window.location.href='index.html'"></button>
      </div>
      <!-- four links on the bottom of the page -->
      <ul id = "links">
        <li>
          <a id = "link-info" href = "https://info.tsinghua.edu.cn" target = "_new" title = "清华大学信息门户">Info</a>
        </li>
        <li>
          <a id = "link-lib" href = "https://lib.tsinghua.edu.cn" targer = "_new" title = "清华大学图书馆">Lib</a> 
        </li>
        <li>
          <a id = "link-learn" href = "https://learn.tsinghua.edu.cn" target = "_new" title = "网络学堂">Learn</a> 
        </li>
        <li>
          <a id = "link-mail" href = "https://mails.tsinghua.edu.cn" target = "_new" title = "清华邮箱">Mail</a>
        </li>
      </ul>
      <!-- two trangles to make the page better -->
      <div class = "triangle"></div>
      <div class = "corner"></div>

    </div>
  </div>
</template>

<script>


import t_Clock from "./clock.vue"
import t_Flux from "./flux.vue"

export default {
  name: 'NetWeb',
  props: {
    msg: String
  },
  components: {
    t_Clock,
    t_Flux,
  },
  data () {
    return{
      flux: 0,
      flux_wid: "",
      user_name: "pp",
    }
  },
  created () {
    this.get_name();
  },
  mounted () {
    this.get_flux();
  },
  methods: {
    get_flux() {
      let that = this;
      fetch("/api/get_flux").then((res) => res.json().then((j) => {
        that.flux = j.flux
        let ff = this.flux * 2.16
        this.flux_wid = ff + "px"
        document.getElementById("usage-value").style.width = this.flux_wid
      }))
      
    },
    get_name(){
      let that = this;
      fetch("/api/name").then((res) => res.json().then((j) => {
        that.user_name = j.user_name
      }))
    }
  },
    
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  body{
    position: page;
    background: #DADBDC url(../../static/img/background.png) repeat-x top;
    background-size: cover;
    background-attachment: fixed; 
    height: 100%;
    width: 100%;
    top: 0px;
    left: 0px;
    right: 0px;
    bottom: 0px;
    font-family:"Microsoft YaHei", "SimHei", "Apple LiGothic Medium";
  }
  ul{
    list-style: none;
  }
  a{
    text-decoration: none;
  }
  a:hover{
    text-decoration: underline;
  }
  #netweb{
    height: 100vh;
    position: page;
    min-width: 640px;
    min-height: 480px;
    margin-top: 0px;
    background-color: #E6E6E6;
    background: #E6E6E6 url(../../static/img/popup_bg.png) no-repeat top right;
  }
  .center{
    position: relative;
    background: url(../../static/img/popup_shadow.png) no-repeat 48px 344px;
    width: 640px;
    margin: auto;
    height: 480px;
    text-align: center;
    float: center;
  }
  #clock{
    color: #ec6677;
  }

  #link-info{
    background: url(../../static/img/popup_info.gif) no-repeat 2px 2px;
  }
  #link-lib{
    background: url(../../static/img/popup_lib.gif) no-repeat 2px 2px;
  }
  #link-mail{
    background: url(../../static/img/popup_mail.gif) no-repeat 2px 2px;
  }
  #link-learn{
    background: url(../../static/img/popup_mail.gif) no-repeat 2px 2px;
  }

  a{
    color: #AD3B23;
  }

  .greet{
    position: absolute;
    top: 64px;
    left: 48px;
    width: 512px;
    height: 224px;
    background: #E64E2E url(../../static/img/popup_greeting.png) no-repeat 30px 46px;
    text-indent: -999em;
    overflow: hidden;
    -webkit-box-shadow:0 0 8px rgba(0,0,0,0.1); 
    -moz-box-shadow:0 0 4px rgba(0,0,0,0.1); 
    box-shadow:0 0 8px rgba(0,0,0,0.1);
  }
  .triangle{
    position: absolute;
    top: 288px;
    left: 80px;
    width: 0;
    height: 0;
    border-color: #E64E2E transparent;
    border-width: 48px 48px 0 0; 
    border-style: solid;
  }
  #info{
    position: absolute; 
    top: 96px; 
    left: 176px;
    padding: 32px; 
    width: 352px; 
    height: 208px; 
    background: #F2F2F2; 
    -webkit-box-shadow: 0 0 8px rgba(0,0,0,0.1); 
    -moz-box-shadow: 0 0 4px rgba(0,0,0,0.1); 
    box-shadow: 0 0 8px rgba(0,0,0,0.1);
  }
  #info #info_content{
    float: left;
    margin-top: -35px;
  }
  #info .chinese-txt{
    text-align: right;
  }
  #info .label_text{
    clear: left;
    float: left;
    width: 56px;
    height: 32px;
    margin-top: 22px;
    text-align: right;
    font-size: 13px;
  }
  #info .english-txt, #info .chinese-txt{
    font-size: 13px;
  }
  #info .content-text{
    float: left;
    margin: 24px 0 0 20px;
    padding-top: 4px;
    height: 28px;
    font-family: Helvetica, Arial, sans-serif;
    font-size: 28px;
    font-weight: lighter;
  }
  #usage-bar{
    position: relative;
    float: left;
    margin: 24px 0 0 16px;
    padding: 0;
    width: 280px;
    height: 32px;
    background: url(../../static/img/usage_bg.gif) repeat-y;
  }
  #usage-bar .calibration{
    position: absolute;
    top: -30px;
    right: 14px;
    font-family: Verdana, Geneva, sans-serif;
    font-size: 13px;
    color: #969696;
  }
  #usage-bar .content-text{
    position: absolute;
    top: 2px;
    left: 4px;
    float: none;
    margin: 0;
    padding: 0;
  }
  #usage-bar .content-text .unit{
    font-size: 24px;
    /* color: #AD3B23;
    z-index: 999em; */
  }
  .calibration li{
    float: right;
    width: 53px;
    text-align: right;
  }
  #usage-bar #firststripe{
    position: absolute;
    top: 0;
    right: 4px;
    width: 4px;
    height: 100%;
    background: #F2F2F2;
  }
  #usage-bar #secondstripe{
    right: 12px;
  }
  #usage-bar #usage-value{
    position: absolute;
    float: left;
    height: 32px;
    max-width: 280px;
    background: #FBB03B;
  }
  
  .name{
    float:left; 
    color:#E64E2E; 
    font-family:Helvetica, Arial, sans-serif; 
    font-size:34px; 
    font-weight:lighter;
    margin-top: 5px;
  }
  #links{
    position: absolute;
    bottom: 32px;
    right: 32px;
    width: 234px;
  }
  #links li{
    top: 10px;
    float: left;
    margin-right: 12px;
    font-size: 11px;
    font-family: Verdana, Geneva, sans-serif;
  }
  
  .disbar{
    position: absolute;
    top: 304px;
    right: 32px;
    width: 208px;
    height: 80px;
    background: #FFFFFF;
    -webkit-box-shadow:0 0 8px rgba(0,0,0,0.1); 
    -moz-box-shadow:0 0 4px rgba(0,0,0,0.1); 
    box-shadow:0 0 8px rgba(0,0,0,0.1);
  }
  #disconnect{
    margin: 16px;
    width: 174px;
    height: 46px;
    border: #B2AABE solid 1px;
    background: #C0BDCC url(../../static/img/disconnect.png) no-repeat center 0;
    overflow: hidden;
  }
  #disconnect:hover{
    background-color: #D6D2E0;
    background-position:center -47px;
  }
  #disconnect:active{
    background-color: #B1AAC4;
    background-position:center -94px;
  }
  #disconnect:disable{
    background-color: #CFCFCF;
    background-position:center -141px;
  }
  .corner{
    width: 0; 
    height: 0;
    border-style: solid;
    position: absolute;
    top: 288px;
    left: 592px;
    border-color: transparent #CCCCCC;
    border-width: 16px 0 0 16px;
  }
  #links li{
    float: left;
    margin-right: 12px;
    margin-left: -12px;
    font-size: 11px;
    font-family: Verdana, Geneva, sans-serif;
  }
  #links li a{
    padding: 16px 5px 0 26px;
    height: 16px;
  }
</style>
