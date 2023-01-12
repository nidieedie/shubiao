import time
import datetime
import random
from pymouse import PyMouse


#function:每隔10s點擊一次
def shubiao():
    mouse=PyMouse()
    position=mouse.position()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),",当前鼠标位置坐标:",position)
    x,y=position
    print(x)
    print(y)
    #mouse.move(200,200)
    mouse.click(x+100,y,1)
    return
if __name__ =="__main__":
    shubiao()


#參考鏈接：
# https://blog.51cto.com/tryagaintry/5426955
