# waydroid-adb-mapper
使用adb为waydroid进行按键映射。Use adb to create key mapper for waydroid.
## 优势
只依赖adb和系统及python，在各种linux设备兼容性极佳。
## 前提
请自行安装python的`evdev`，并使用sudo提权（或者su）运行
并请自行使用adb连接waydroid设备
## 使用
` sudo python app.py deathdoor.txt`
其中最后一个参数为配置路径，可以是任意扩展名，只要是文本文件，其本质为py，其内容应该如下
```
mapperlist=[
["KEY_A","joy",1254,635,-100,0]
["KEY_J","longpress",1876,958],
["KEY_B","tap",262,563],
["KEY_K","longpress",2176,809],
["KEY_L","tap",2212,1104],
["KEY_I","longpress",1880,1241]
]

```
第一个参数可以用系统evtest命令获取其相应按键名，这里请自行了解一下evtest
joy为类似摇杆操作，前两个是xy坐标，后面是xy相对坐标（坐标可以用开发者模式获取，或者adb命令）
longpress长按坐标，tap单击，长按映射到waydroid正常
目前就做出了这三种。
程序中按x自动开关指针指示。
## 恰饭
![](wechat.png)
![](alipay.png)
