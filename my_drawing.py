# coding: utf-8
get_ipython().run_line_magic('load', 'my_drawing.py')
# %load my_drawing.py
import cs1graphics as cg
paper = cg.Canvas()
paper.setBackgroundColor('skyBlue')
paper.setWidth(800)
paper.setHeight(600)
paper.setTitle('My World')
dir(paper)
paper.getBackgroundColor()
paper.getWidth()
sun = cg.Circle()
paper.add(sun)
sun.setFillColor('yellow')
sun.setRadius(50)
sun.moveTo(700, 100)
sunCenter = cg.Point(900, 100)
sun2 = cg.Circle(50, sunCenter)
sun2 = cg.Circle(50, cg.Point(900, 100))
sun2.setFillColor('lightYellow')
paper.add(sun2)
sun2 = cg.Circle(50, cg.Point(100, 100))
paper.add(sun2)
sun2.setFillColor('lightYellow')
sun.setFillColor('skyblue')
sun.getFillColor()
sun2.moveTo(700,100)
sun2.moveTo(900,100)
sun2.moveTo(800,100)
sun2.moveTo(700,100)
sun2.moveTo(700,300)
sun2.moveTo(700,100)
sun2.setFillColor('yellow')
facade = cg.Square(200, cg.Point(400, 350))
paper.add(facade)
facade.setFillColor('white')
chimney = cg.Rectangle(50, 70, cg.Point(450,215)
)
chimney.setFillColor('red')
paper.add(chimney)
tree = cg.Polygon(cg.Point(150, 220), cg.Point(120, 380), cg.Point(180, 380))
tree.setFillColor('darkGreen')
paper.add(tree)
sunraySW = cg.Path(cg.Point(660, 140), cg.Point(635, 165))
paper.add(sunraySW)
sunraySW.setBorderColor('yellow')
sunraySW.setBorderWidth(6)
sunraySW.setBorderWidth(10)
sunraySE = cd.Path(cg.Point(740, 140), cg.Point(765, 165))
sunraySE = cg.Path(cg.Point(740, 140), cg.Point(765, 165))
paper.add(sunraySE)
sunraySE.setBorderWidth(10)
sunraySE.setBorderColor('yellow')
sunrayNE = cg.Path(cg.Point(740, 60), cg.Point(765, 35))
paper.add(sunraySE)
paper.add(sunrayNE)
sunrayNE.setBorderColor('yellow')
sunrayNE.setBorderWidth(10)
sunrayNW = cg.Path(cg.Point(660, 60), cg.Point(635, 35))
paper.add(sunrayNW)
sunrayNW.setBorderWidth(10)
sunrayNW.setBorderColor('yellow')
chimney.getDepth()
grass = cg.Rectangle(800, 300, cg.Point(400, 450))
paper.add(grass)
grass.setBorderColor('green')
grass.setFillColor('green')
grass.setDepth(100)
grass.setDepth(20)
grass.setDepth(100)
window = cg.Square(50, cg.Point(450, 400))
paper.add(window)
window.moveTo(450, 350)
window.moveTo(450, 300)
window.moveTo(450, 325)
window.setFillColor('black')
roof = cg.Polygon(cg.Point(400, 200), cg.Point(300, 300), cg.Point(500,300))
paper.add(roof)
del roof
roof = cg.Polygon(cg.Point(400, 200), cg.Point(300, 300), cg.Point(500,300))
roof.setBorderColor('white')
paper.add(roof)
roof = cg.Polygon(cg.Point(500, 100), cg.Point(300, 300), cg.Point(500,300))
paper.add(roof)
remove(roof)
paper.remove(roof)
roof = cg.Polygon(cg.Point(400, 100), cg.Point(280, 300), cg.Point(520,300))
paper.add(roof)
paper.remove(roof)
roof = cg.Polygon(cg.Point(400, 150), cg.Point(280, 270), cg.Point(520,270))
paper.add(roof)
roof.setFillColor("grey")
paper.saveToFile('my-drawing.ps')
get_ipython().run_line_magic('save', 'my_drawing ~0/')
