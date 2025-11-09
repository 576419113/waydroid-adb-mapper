import evdev
import os
import sys
#类遥杆
def joy(mapp,sta):
    ax,ay,rx,ry=mapp[2:]   #绝对相对坐标
    #mapp坐标，偏移。sta状态up/hold/down。
    global ishold
    if(sta=="down"):
        os.system(f"adb shell input motionevent DOWN {ax} {ay}")
    if(sta=="up"):
        os.system(f"adb shell input motionevent UP {ax} {ay}")
        gishold=0
    if(sta=="hold" and not ishold):
        os.system(f"adb shell input motionevent MOVE {ax+rx} {ay+ry}")
        ishold=1
#单击
def tap(mapp,sta):
    ax,ay=mapp[2:]   #绝对坐标
    if(sta=="down"):
        os.system(f"adb shell input tap {ax} {ay}")
#长按
def longpress(mapp,sta):
    ax,ay=mapp[2:]   #绝对坐标
    #mapp坐标，偏移。sta状态up/hold/down。
    global ishold
    if(sta=="down"):
        os.system(f"adb shell input motionevent DOWN {ax} {ay}")
    if(sta=="up"):
        os.system(f"adb shell input motionevent UP {ax} {ay}")
        gishold=0
#改变指针的值
def changepointer():
    global ispointer
    #print(os.popen("adb shell settings get system pointer_location").read())
    ispointer=int(os.popen("adb shell settings get system pointer_location").read())
    if ispointer:
        os.system(f"adb shell settings put system pointer_location 0")
    else:
        os.system(f"adb shell settings put system pointer_location 1")
global_vars={}
with open(sys.argv[1],"r") as f:
    exec(f.read(),global_vars)      #读取字典到global_vars字典中
mapperlist=global_vars["mapperlist"]
device = evdev.InputDevice('/dev/input/event3')
print("初始化完成\n")
ishold=0     #是否已经有hold
ispointer=0  #检测指针是否开启
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        resu=str(evdev.categorize(event))
        crash,key,state=resu.split(", ")
        #按Q退出
        #if("KEY_Q" in key):
          #  sys.exit()
        #按X切换屏幕指针模式
        if("KEY_X" in key and state=="down"):
            changepointer()
        #mapper开始
        for mapper in mapperlist:
            if(mapper[0] in key):
                if(mapper[1]=="joy"):
                    joy(mapper,state)
                if(mapper[1]=="tap"):
                    tap(mapper,state)
                if(mapper[1]=="longpress"):
                    longpress(mapper,state)
