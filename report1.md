# Web前端实训 作业1报告

> 姓名：贲清炜
>
> 学号：2020013061
>
> 邮箱：bqw20@mails.tsinghua.edu.cn



## 静态页面结果展示

### PC端

<img src="\imgreport\pc.png" alt="image-20220707125657687" style="zoom: 33%;" />

### 移动端

<img src="\imgreport\mob.jpg" alt="image-20220707125657687" style="zoom: 25%;" />

## 查看方法

* 本次作业使用vue脚手架vue-cli，运行需要环境包括Node.js和vue3
* 源码放置在src文件中，包括App.vue、main.js、global.css、components\NetWeb.vue等文件。
* 运行需要在fakewifi文件夹中打开终端，输入npm run serve
* 在PC端本地任一服务器上（推荐Edge或Chrome）输入localhost:8080即可浏览到本页面
* 在手机端访问网页可以通过上一步运行后终端提示的网址，如Network: http://192.168.2.4:8080/查看
* 另外已经通过npm run build命令将网页打包在dist\index.html中，可以通过直接打开该文件浏览运行效果（由于npm的打包问题部分渲染效果没有能够进入打包结果中，目前未找到原因。）



## 移动端兼容性说明

* 对整体body使用了页面居中对齐的方式，在较小的手机屏幕上依然能够很好的展示出来
* 总体文字大小在手机端依然得到很好的适配，在较小屏幕下依然能够正常运行。



## 实现思路及相关问题

* 由于本次作业要求模仿指定页面进行编写，因此选择在vue框架内使用HTML和CSS进行编写，页面中流量值和已连接的数据根据要求内容直接用固定值保存在页面中。对于尺寸的把控主要参考原来页面的数据，针对本次作业的要求对页面中的组件编写了CSS样式，并且最终生成了该页面的netweb.vue文件，通过App.vue引用实现了页面的重现。
* 由于实际编写与原页面使用技术、框架等的不同，编写过程中遇到如下问题：
  * 目前正在运行的net.tsinghua.edu.cn/wireless对于下方四个超链接的摆布并没有将他们摆放到同一行，实际操作下来也发现如果直接使用float:right和ul指令会导致Mail系列的超链接转行。
    * 通过设置margin-left和margin-right的值实现了对四个超链接列表元素的间距调整，最后使得他们位于同一行，与本次作业图例相符合。
  * 实际编写中发现若给整个前置部分使用center摆放，直接使用net页面中关于已连接和已用流量以及用户名的位置数据会使得与需要的页面对比整体位置偏下
    * 通过margin-top参数取负值进行了调整
  * 无法仅仅通过body设置width:100%来使得背景灰色覆盖整个页面，同时初始时页面有边框，无法通过指定margin和padding为0消除。
    * 通过一个global.css文件指定body和html均占据整个页面大小（height:100%;width:100%;margin:0;padding:0;）
  * 上述步骤之后发现在PC端修复成功但移动端出现不明原因的背景色缺角
    * 设置netweb整个组件的height:100vh；问题得到解决。



### 说明：

由于本次作业只用到html和css，因此只在NetWeb.vue文件中对html元素的部分内容进行了注释。

作业内容上传至[Elgce/NetWeb: A simple homework for Web 2022 Summer (github.com)](https://github.com/Elgce/NetWeb)

