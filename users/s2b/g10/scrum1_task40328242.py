# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template, make_response

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
scrum1_task40328242 = Blueprint('scrum1_task40328242', __name__, url_prefix='/bg10', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@scrum1_task40328242.route('/scrum1_40328242_1')
def scrum1_40328242_1():
    outstring = '''

from javascript import JSConstructor
from browser import window
import math
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
cgo.setWorldCoords(-250, -250, 500, 500) 



#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })
deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })
   
   
    basic1 = cmbr.dup()
    basic1.rotate(0)
    basic1.translate(0,1*20)
    basic2 = cmbr.dup()
    basic2.rotate(0)
    basic2.translate(0,2*20)
    basic3 = cmbr.dup()
    basic3.rotate(45)
    basic3.translate(0,0)
    basic4 = cmbr.dup()
    basic4.rotate(45)
    basic4.translate(1*20*math.cos(45*deg), -1*20*math.sin(45*deg))
    basic5 = cmbr.dup()
    basic5.rotate(45)
    basic5.translate(2*20*math.cos(45*deg), -2*20*math.sin(45*deg))
    basic6 = cmbr.dup()
    basic6.rotate(0)
    basic6.translate(0,-1*20)
    basic7 = cmbr.dup()
    basic7.rotate(0)
    basic7.translate(0,-2*20)
    basic8 = cmbr.dup()
    basic8.rotate(0)
    basic8.translate(0,3*20)
    basic9 = cmbr.dup()
    basic9.rotate(-135)
    basic9.translate(0, 0)
    basic10 = cmbr.dup()
    basic10.rotate(-135)
    basic10.translate(-1*20*math.cos(45*deg), 1*20*math.sin(45*deg))
    basic11 = cmbr.dup()
    basic11.rotate(-135)
    basic11.translate(-2*20*math.cos(45*deg), 2*20*math.sin(45*deg))
    
    
    
    
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    
    
    
    # hole 為原點位置
    # hole = cobj(shapedefs.circle(4), "PATH")
    #cmbr.appendPath(hole)
    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)
O(0, 0, 0, 0, -22.5, "blue", True, 4)



'''
    response = make_response(outstring)
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Origin'] = 'http://2016spring-40328242.rhcloud.com'
    response.headers['Access-Control-Allow-Origin'] = 'localhost:5000'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    response.headers['Access-Control-Max-Age'] = '86400'
    return response    
    
@scrum1_task40328242.route('/scrum1_40328242_2')
def scrum1_40328242_2():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>
</head>
<body>
<script>
window.onload=function(){
brython(1);
}
</script>
<canvas id="plotarea" width="800" height="800"></canvas>
<script type="text/python">
from javascript import JSConstructor
from browser import window
import math
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
cgo.setWorldCoords(-250, -250, 500, 500) 
# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })
deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })
    # 複製 cmbr, 然後命名為 basic1
    
   basic1 = cmbr.dup()
    basic1.rotate(0)
    basic1.translate(0,1*20)
    basic2 = cmbr.dup()
    basic2.rotate(0)
    basic2.translate(0,2*20)
    basic3 = cmbr.dup()
    basic3.rotate(45)
    basic3.translate(0,0)
    basic4 = cmbr.dup()
    basic4.rotate(45)
    basic4.translate(1*20*math.cos(45*deg), -1*20*math.sin(45*deg))
    basic5 = cmbr.dup()
    basic5.rotate(45)
    basic5.translate(2*20*math.cos(45*deg), -2*20*math.sin(45*deg))
    basic6 = cmbr.dup()
    basic6.rotate(0)
    basic6.translate(0,-1*20)
    basic7 = cmbr.dup()
    basic7.rotate(0)
    basic7.translate(0,-2*20)
    basic8 = cmbr.dup()
    basic8.rotate(0)
    basic8.translate(0,3*20)
    basic9 = cmbr.dup()
    basic9.rotate(-135)
    basic9.translate(0, 0)
    basic10 = cmbr.dup()
    basic10.rotate(-135)
    basic10.translate(-1*20*math.cos(45*deg), 1*20*math.sin(45*deg))
    basic11 = cmbr.dup()
    basic11.rotate(-135)
    basic11.translate(-2*20*math.cos(45*deg), 2*20*math.sin(45*deg))
    
    
    
    
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11) 
    
    
    # hole 為原點位置
    # hole = cobj(shapedefs.circle(4), "PATH")
    #cmbr.appendPath(hole)
    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)
O(0, 0, 0, 0, -22.5, "blue", True, 4)
</script>


'''
    return outstring