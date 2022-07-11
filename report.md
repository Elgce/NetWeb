# Web前端 基础实验2

> 姓名：贲清炜
>
> 学号：2020013061
>
> 邮箱：bqw20@mails.tsinghua.edu.cn



## 运行步骤

* 在命令行中打开fakewifi文件夹
* 依次在命令行中执行
  * npm install
  * npm run build
  * pip install -r requirements.txt
  * python backend/app.py
* 在浏览器端打开localhost:5000
* 移动端打开方式：
  * 首先查询到电脑的IPV4地址，如192.168.2.4，在后面加上:5000即可在手机的浏览器上访问，总链接示例：http://192.168.2.4:5000



## 项目内容

### 前端页面

* 实现了两个页面：登陆页面index.html和连接页面connect.html
  * <img src=".\report_img\connect.jpg" alt="image-20220711190334169" style="zoom:33%;" />
  * <img src=".\report_img\index.jpg" alt="image-20220711190345986" style="zoom:33%;" />
* 移动端兼容良好，在小屏幕上也能够完整呈现内容
  * <img src=".\report_img\image-20220711190308983.png" alt="image-20220711190308983" style="zoom:33%;" />
  * <img src=".\report_img\image-20220711190255041.png" alt="image-20220711190255041" style="zoom:33%;" />
* 自动计时工具
  * 现在，连接时间不再作为硬编码出现在页面中，而是会实时在页面中刷新
  * 这部分内容直接通过Javascript实现



### 前后端通信

* 实现了两个不同的用户，用户名分别为lizy14和bqw20，密码均为123456
* 在最初的登录过程中，两个的流量数值均设定为0
  * <img src=".\report_img\image-20220711190345986.png" alt="image-20220711190345986" style="zoom:33%;" />
* 用户退出后每次增加0.25G的流量并对于每个用户的使用额度在后端单独保存，单次后端开启过程中能够不断读取相应的数值
  * <img src=".\report_img\image-20220711190902777.png" alt="image-20220711190902777" style="zoom:33%;" />
* 用户再次登录过程中能够读取到相应的流量数额并进行反馈
  * <img src=".\report_img\image-20220711191004017.png" alt="image-20220711191004017" style="zoom:33%;" />



### 额外功能实现

* 增加了账户密码不对时的alert
  * <img src=".\report_img\image-20220711191041471.png" alt="image-20220711191041471" style="zoom:33%;" />



## 难点及解决方案

* 实验实现方式
  * 首先在Vue中实现了多个页面，除开始页面初始文件位置未更改外，将其余页面的文件放在了pages中，本次仅实现了一个多的页面，因此放在了响应的pages/connect文件夹中
  * 构造了flask后端并且设计了与前端的响应，通过vue相关关键字实现在不同页面阶段加载的需求
  * 本次操作过程中有保存不同用户信息的需求，因此选用了flask中的session模块，在相应位置设置和清空，极大方便了数据的处理
* 难点
  * 前端页面设计index.html时发现原页面背景色的渐变不是通过图片，但又很好的使上下两种不同的颜色得以过度
    * 经过尝试，通过使用backgroud-image: linear-gradient实现，并使用了其中指定每种颜色从页面多少比例开始的方法，实现效果较好
  * 前后端的连接及数据交互遇到了困难，最终通过学习路由、前后端交互的相关知识以及flask的文档，最后较好的实现了需要的功能。同时通过vue框架中的created、mounted、methods、data等功能成功实现了在页面加载的不同阶段操作资源的需求
  * fetch方法帮忙实现了前后端数据的交互，学习到了fetch相关的独特语法，同时经过半天的debug深刻认识到headers不是header的血泪教训:cry: 