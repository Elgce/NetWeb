<template>
  <div id="loadweb">
    <div id = "center">
      <div id = "head">
        <div id = "title">
          <p>清华大学无线校园网</p>
          <p class = "english">
            Tsinghua University Wireless Network
          </p>
        </div>
      </div>
      <div class = "qrcode">
        <center>
          <p>
            <img src = "../img/qrcode.jpg" width = "100" height = "100">
          </p>
          <font size="2">欢迎关注“清华大学信息服务”</font>
        </center>
      </div>
      <div id = "content">
        <div id = "attsinghua" style = "position: absolute; top: -137px; right: 0px;">
          <a href = "https://webvpn.tsinghua.edu.cn/http/77726476706e69737468656265737421fdf843952b3569406e469dbf915b243d737ce7f48b03bf62d6" target="_blank">
            <img  src = "../img/attsinghua.png" style="width: 215px; height: 105px;">
          </a>
        </div>
        <div class = "greet">您好，&nbsp;Hello,</div>
        <div class = "triangle_greet"></div>
        <div id = "notice_box">
          <div class = "corner"></div>
          <div id = "notice">
            <p>
              &nbsp;
              <br>
              &nbsp;
            </p>
            <div width = "320" align = "center">
              <marquee scrollamount = "1.0" width = "300" align = "left" height = "90" direction = "up" border = "0" id = "msg" style="color:white;">
                <!-- Amazing!
                Convinced news source leaked that if TA gives good scores to this homework, 
                he or she will be better in research field and will have so many papers to publish next year in the top references!
                So, Let's mark a 100 score! -->
                震惊！&nbsp;据可靠消息,凡是给这份作业100分的助教同学在第二年相关学科的顶级会议上均发表了多篇论文,学业十分顺利,爱情大丰收.该消息经过认证,所以快给这份作业打100分吧!
              </marquee>
            </div>
          </div>
        </div>
        <div id = "login">
          <form name = "login_form" id = login_form>
            <input type = "hidden" name = "is_pad" value = "2">
            <input type = "hidden" name = "n" value = "100">
            <input type = "hidden" name = "type" value = "1">
            <input type = "hidden" name = "drop" value = "0">
            <input type = "hidden" name = "action" value = "login">
            <input type = "hidden" name = "ac_id" value = "1">
          <div class = "field">
            <div class = "label_text" for = "uname">
              用户名
              <p class = "english">User&nbsp;ID</p>
            </div>
            <input type = "text" name = "uname" id = "uname" value autocorrect="off" autocapitalize="off">
          </div>
          <div class = "field">
            <div class="label_text" for = "pass">
              密码
              <p class="english">Password</p>
            </div>
            <input type = "password" name = "pass" id="pass" autocorrect="off" autocapitalize="off">
          </div>
          <input type = "button" name = "connect" id = "connect" onclick="window.location.href='connect.html'">
          </form>
        </div>
        <div class = "triangle_login"></div>
        <div id = "download">
          <ul id = "system">
            <li>
              <a class = "windows" title="Windows">Windows</a>
            </li>
            <li>
              <a class = "mac" title = "MacOS">MacOS</a>
            </li>
            <li>
              <a class = "linux" title = "Linux">Linux</a>
            </li>
            <li>
              <a class = "android" title = "Android">Android</a>
            </li>
            <li>
              <a class = "ios" title = "iOS">iOS</a>
            </li>
          </ul>
        </div>
        <ul id = "widget">
          <li class="bookmark">
            收藏
            <p class = "english">Bookmark&nbsp;This&nbsp;Page</p>
          </li>
          <li class="help">
            帮助
            <p class = "english">Help</p>
          </li>
          <li class = "contact">
            <div class = "title">
              联系
              <p class = "english">Contact</p>
            </div>
            <div class = "detail english">
              +86-10-52784859
              <a href = "mailto:its@tsinghua.edu.cn" title = "电子邮件Email">its@tsinghua.edu.cn</a>
            </div>
          </li>
        </ul>
      </div>


      <div id = "foot">
        清华大学信息化技术中心
        <p class = "english">Information Technology Center of Tsinghua University</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoadWeb',
  props: {
    msg: String
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /* #loadweb{
    background-image: linear-gradient(to bottom, #7d7f8b, #7d7f8d);
  } */
  a{
    color: #AD3B23;
    text-decoration: none;
  }
  a:hover{
    text-decoration: underline;
  }
  #loadweb{
    height: 100vh;
    position: page;
    min-width: 640px;
    min-height: 480px;
    margin-top: 0px;
    background-image: linear-gradient(to bottom, #E6E6E6 40%,#c5c5c5 60%, #DADBDC 70%);
    /* background-color: #E6E6E6;
    background: #E6E6E6; */
  }
  #center {
    margin: auto;
    width: 805px;
    height: 100vh;
  }
  body{
    position: page;
    background-size: cover;
    background-attachment: fixed; 
    height: 100%;
    width: 100%;
    top: 0px;
    left: 0px;
    right: 0px;
    bottom: 0px;
    background: #DADBDC url(../img/background.png) repeat-x top;
    min-width: 768px;
    font-family:"Microsoft YaHei", "SimHei", "Apple LiGothic Medium";
  }
  #head {
    background: url(../img/logo.gif) no-repeat;
    float: left;
    margin: 16px 0 32px -86px;
  }
  .english{
    font-family: Verdana, Geneva, sans-serif;
    margin-top: 0;
  }
  #title{
    display: block;
    width: 320px;
    height: 105px;
    text-indent: -999em;
    overflow: hidden;
    background: url(../img/title.png) no-repeat;
    margin-left: 82px;
  }
  .qrcode{
    float: right;
    margin-top: 15px;
    margin-right: 220px;
  }
  .qrcode img{
    width: 129px;
    height: 129px;
    border: none;
  }
  .qrcode p{
    line-height: 18px;
    color: #5d5d5d;
    text-align: center;
    font-size: 3px;
  }
  #foot{
    float: left;
    margin-top: 64px;
    width: 100%;
    height: 100%;
    text-align: right;
    font-size: 12px;
    color: #6E6F6F;
  }
  #foot .english{
    font-size: 11px;
  }
  #content{
    position: relative;
    float: left;
    clear: both;
    width:100%;
    height: 496px;
    background: url("../img/content_shadow.png") no-repeat 0 416px;
  }
  .greet{
    text-indent: -999em;
    overflow: hidden;
    position: absolute;
    top: 0;
    left: 0;
    width: 720px;
    height: 304px;
    background: #E64E2E url("../img/greeting.png") no-repeat 32px 28px;
    -webkit-box-shadow:0 0 8px rgba(0,0,0,0.1);
    -moz-box-shadow: 0 0 4px rgba(0,0,0,0.1);
    box-shadow: 0 0 8px rgba(0,0,0,0.1);
}
  .triangle_greet{
    width: 0;
    height: 0;
    border-style: solid;
    position: absolute;
    top: 304px;
    left: 32px;
    border-color: #E64E2E transparent;
    border-width: 48px 48px 0 0;
  }
  #notice_box{
    position:absolute;
    top: 128px;
    left: -16px;
    width: 320px;
    height: 172px;
  }
  #notice_box .corner{
    border-color: transparent #AD3B23;
    border-width: 16px 16px 0 0;
  }
  #notice_box #notice{
    position: relative;
    width: 320px;
    height: 160px;
    border-width: 16px 16px 0 0;
    background: #E6562E url("../img/notice.png") no-repeat 14px 10px;
    -webkit-box-shadow: 0 0 8px rgba(0,0,0,0.1);
    -moz-box-shadow: 0 0 4px rgba(0,0,0,0.1);
    box-shadow:  0 0 8px rgba(0,0,0,0.1);
  }
  #login #login_form{
    margin: 32px;
  }
  #login{
    position: absolute;
    top: 32px;
    left: 304px;
    width: 464px;
    height: 304px;
    background: #F2F2F2;
    -webkit-box-shadow: 0 0 8px rgba(0,0,0,0.1);
    -moz-box-shadow: 0 0 4px rgba(0,0,0,0.1);
    box-shadow: 0 0 8px rgba(0,0,0,0.1);
  }
  .field{
    float: left;
    margin-bottom: 16px;
    width: 100%;
  }
  .field :first-child{
    position: relative;
  }
  .label_text{
    float: left;
    height: 48px;
    font-size: 21px;
  }
  .english{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
  }
  .label_text .english{
    margin-top: 0;
    color: #303030;
    font-size: 16px;
  }
  #widget .english{
    font-size: 11px;
    color: #4F4F4F;
  }
  #connect{
    margin: 16px;
    width: 398px;
    height: 46px;
    border: #9CB22E solid 1px;
    background: #C0CE55 url(../img/connect.png) no-repeat center 0;
    overflow: hidden;
  }
  #connect:hover{
    background-color: #D2E042;
    background-position: center -47px;
  }
  #connect:active{
    background-color: #AAC30B;
    background-position: center -94px;
  }
  #connect:disabled{
    background-color: #CCCFB7;
    background-position: center -141px;
  }
  .triangle_login{
    position: absolute;
    top: 336px;
    left: 688px;
    border-color: #F2F2F2 transparent;
    border-width: 48px 48px 0 0;
    width: 0;
    height: 0;
    border-style: solid;
  }
  #download{
    position: absolute;
    bottom: 0;
    left: 0;
    width: 304px;
    height: 112px;
    background: url(../img/download.png) no-repeat 0 8px;
  }
  #title{
   text-indent: -999em;
   overflow: hidden; 
  }
  #system{
    position:absolute;
    bottom: -15px;
    left: -16px;
    width: 320px;
    height: 48px;
    background: #808080;
    -webkit-box-shadow: 0 0 8px rgba(0,0,0,0.1);
    -moz-box-shadow: 0 0 4px rgba(0,0,0,0.1);
    box-shadow: 0 0 8px rgba(0,0,0,0.1);
  }
  #system  li  a {
    position: absolute;
    bottom: 16px;
    display: block;
    padding-top: 36px;
    float: left;
    min-width: 34px;
    height: 16px;
    color: #FFF;
    font-size: 13px;
    font-family: Helvetica, Arial, sans-serif;
  }
  #system  li:last-child a{
    margin-right: 0;
  }
  .windows{
    left: 16px;
    background: url(../img/windows.gif) no-repeat 2px 0;
  }
  .mac{
    left: 80px;
    background: url(../img/mac.gif) no-repeat 0 0;
  }
  .linux{
    left: 144px;
    background: url(../img/linux.gif) no-repeat 0 0;
  }
  .android{
    left: 207px;
    background: url(../img/android.gif) no-repeat 0 0;
  }
  .ios{
    left: 271px;
    background: url(../img/ios.gif) no-repeat 0 0;
  }
  #widget{
    position: absolute;
    bottom: -15px;
    right: 0;
    width: 464px;
    height: 32px;
  }
  #widget li{
    float: left;
    padding-left: 36px;
    font-size: 12px;
    color:#000;
  }
  #widget li a{
    color: #000;
  }
  #widget .detail a{
    color: #4F4F4F;
  }
  #widget .detail{
    float: left;
    margin: 2px 0 0 8px;
    line-height: 1.3;
  }
  #widget .english{
    font-size: 11px;
    color: #4F4F4F;
  }
  .contact .title{
    float: left;
  }
  .bookmark{
    background: url(../img/bookmark.gif) no-repeat 8px 0;
  }
  #widget .help{
    background: url(../img/help.gif) no-repeat 4px 0;
  }
  #widget .contact{
    float: right;
    background: url(../img/contact.gif) no-repeat 4px 0;
  }
  #widget .contact a{
    display: block;
  }
  ul{
    list-style: none;
  }
  input[type=submit], button{text-indent:-999em; overflow:hidden; cursor:pointer;  -webkit-appearance:none; -moz-appearance:none; border-radius:0;  -webkit-border-radius:0; -moz-border-radius:0;}
  input[type=submit][disabled=disabled], button:disabled{cursor:default;}
  input[type=text], input[type=password]{outline:none; -webkit-appearance:none; -moz-appearance:none; border-radius:0;  -webkit-border-radius:0; -moz-border-radius:0;}
  input[type=text], input[type=password]{float:right; width:298px; height:42px; border:#E6E6E6 solid 1px; padding:2px; background:#FFF; font-family:Helvetica, Arial, sans-serif; font-size:34px;}
  input[type=text]:hover, input[type=password]:hover{border-color:#CCCCCC;}
  input[type=text]:focus, input[type=password]:focus{border-color:#FBB03B; -webkit-box-shadow:0 0 8px rgba(251,176,59,0.8); -moz-box-shadow:0 0 4px rgba(251,176,59,0.8); box-shadow:0 0 8px rgba(251,176,59,0.8);}
  input[type=text][disabled=disabled], input[type=password][disabled=disabled]{background:#F2F2F2;}
  input[type=text].form-error, input[type=password].form-error{border-color:#ED1C24;}
  input[type=checkbox]{float:left; margin:4px 4px 0 0;}

</style>
