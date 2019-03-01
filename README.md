# host_ads
一个python构成通过更改host屏蔽广告并拥有可视化GUI界面的简易程序
<br>
 <br><br>经常上网的童鞋对于HOSTS文件应该非常熟悉了
 <br><br>我经常编辑HOSTS文件来达到屏蔽网页广告的目的。
 <br><br>但是HOSTS文件藏在WINDOWS目录的子子子目录下，而且没有后缀名，每次打开都非常的不方便
 <br><br>在吾爱破解论坛也看到有人发布了编辑HOSTS文件的小工具【https://www.52pojie.cn/thread-855929-1-3.html】
 <br><br>于是我也手痒，花了点时间简单用python做了一个小程序
 <br><br>没啥技术含量，纯粹是方便自己，大神别笑话
 <br><br>可以直接在批处理里面屏蔽/取消屏蔽指定域名，还原host文件防止host被污染
 <br><br>最关键的是更小巧方便，才3KB，而且是傻瓜式操作。
 <p><b>主要内容：</b></p>
 <ol>
 <li>添加host屏蔽以达到屏蔽某些广告域名的目的</li>
 <li>删除host屏蔽，使用循环的方式循环每一行，确保除去本软件屏蔽此域名外其他用户或软件利用host屏蔽而达不到取消屏蔽的效果</li>
 <li>查看host文件，解决大部分人找不到host文件和host文件目录较深打开麻烦的问题</li>
 <li>还原纯净host文件，解决部分host深度患者经常修改导致host污染和host小白错误修改以及部分恶意软件恶意修改host的问题</li>
 </ol>
 <br><br>
 <p><b>使用方式：</b></p>
 <ol type="I">
 <li>直接在python环境下运行</li>
 <li>使用pyinstaller编译为exe文件运行
  <ol type="i">
   <li>安装pyinstaller（需要python环境）:<br>在命令行中执行<code>pip install pyinstaller</code></li>
   <li>用命令行打开文件所在目录<br>执行<code>pyinstaller -w -F py文件地址</code><br>其中 -F指打包成独立exe文件，-w指屏蔽命令行界面</li>
  </ol>
 </li>
</ol>
<br/>
<img src="https://s2.ax1x.com/2019/03/01/kb8Mex.png" alt="kb8Mex.png" border="0">
<img src="https://s2.ax1x.com/2019/03/01/kb8Qw6.png" alt="kb8Qw6.png" border="0">
<img src="https://s2.ax1x.com/2019/03/01/kb83FO.png" alt="kb83FO.png" border="0">
<img src="https://s2.ax1x.com/2019/03/01/kb8lTK.png" alt="kb8lTK.png" border="0">
