import viz
import vizact
import vizcam
import vizshape
import vizconfig
import random
import vizdlg
import viztask
import vizinfo

viz.fov(60)
viz.go()
viz.MainView.move([0,17,-5])
viz.phys.enable()
viz.phys.setGravity(0,-10,0)#重力设置
viz.mouse(viz.OFF)
viz.lookAt([0,0,8])
#视野设置为0重力
viz.MainView.gravity (0) 
viz.collision(viz.ON)


viz.mouse.setVisible(True)
tex=viz.addTexQuad(viz.SCREEN,texture=viz.add('dot.tif'))
viz.link(viz.Mouse,tex)
music=viz.add('carousel.wav',volume=0.15,loop=1)
music.play()
music2=viz.add('yizeruier2.wav',volume=0.15)
music2.play()

# Script settings
TRIAL_COUNT = 5             # Number of trials per game
TRIAL_DURATION = 20         # Amount of time allowed for finding each pigeon (in seconds)

# Create status bar background
status_bar = viz.addTexQuad(parent=viz.ORTHO)
status_bar.color(viz.BLACK)
status_bar.alpha(0.5)
status_bar.alignment(viz.ALIGN_LEFT_BOTTOM)
status_bar.drawOrder(-1)
viz.link(viz.MainWindow.LeftTop,status_bar,offset=[0,-80,0])
viz.link(viz.MainWindow.WindowSize,status_bar,mask=viz.LINK_SCALE)


INSTRUCTIONS = """Press "1" to start game, Use your mouse to control Avatar to avoid 
obstacles, Cross the finish line and press "w" to win the game. 
(x,y,z = male.getPosition() If z>20, you cross the finish line. 
The avatar has a special forward teleportation skill (press "2"), 
but it also activates a hidden penalty mechanism.
Attention!!! if your life value down to 0 you will die and resurrect.

""".format(TRIAL_COUNT,TRIAL_DURATION)


# Create score text
scoreLabel = viz.addText('',parent=viz.ORTHO,fontSize=40)
scoreLabel.alignment(viz.ALIGN_LEFT_TOP)
scoreLabel.setBackdrop(viz.BACKDROP_OUTLINE)
viz.link(viz.MainWindow.LeftTop,scoreLabel,offset=[20,-20,0])



#scoreLabel=viz.addText('')

scoreLabel.score=100

scoreLabel.setPosition(-1,0,0)

ground = viz.addChild('piazza.osgb')
ground.collidePlane()


male = viz.add('vcc_male.cfg')
male.setPosition(0.7,5,-2)
male.state(2)
male.collideBox(1,0.5,1)
male.enable( viz.COLLIDE_NOTIFY ) 
# Add piazza animations
animations = viz.add('piazza_animations.osgb')
pigeon_path = animations.getChild('walk').copy()
pigeon_path.setAnimationSpeed(0.5)
pigeon_path2 = animations.getChild('walk').copy()
pigeon_path2.setAnimationSpeed(2)
pigeon = viz.addAvatar('pigeon.cfg')
pigeon2 = viz.addAvatar('pigeon.cfg')
pigeon.collideBox()
pigeon2.collideBox()
pigeon.setParent(pigeon_path,node='walk')
pigeon2.setParent(pigeon_path2,node='walk')
pigeon.state(3)
pigeon2.state(2)

#Create the animation path  
path = viz.addAnimationPath()

#Initialize an array of control points
positions = [  [-1.5,0,2.7], [-1.5,0,11],[-1.5,0,8]]
for x,pos in enumerate(positions):

    #Add the control point to the animation path.
    path.addControlPoint(x+1,pos=pos)

wheel=viz.addChild('wheelbarrow.ive')

wheel.collideBox()
#Set the loop mode to circular
path.setLoopMode(viz.CIRCULAR)
#Automatically compute tangent vectors for cubic bezier translations
path.computeTangents()
#Automatically rotate the path
path.setAutoRotate(viz.ON)
link = viz.link(path,wheel)




pigeon4 = viz.addAvatar('pigeon.cfg')
pigeon4.setPosition(-3,0,-0.2)
pigeon4.collideBox()

pigeon5 = viz.addAvatar('pigeon.cfg')
pigeon5.setPosition(1,0,3)
pigeon5.collideBox()



soccer = viz.add('soccerball.ive')
soccer.setPosition(1,0,3)
soccer.setScale(2,2,2)
soccer.collideBox()
boxs = []


#男右墙
for i in range(1,3):#i表示高度
	for j in range(3,4):#j表示左右
		for k in range(-6,3):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
#右墙右
for i in range(1,10):#i表示高度
	for j in range(5,10):#j表示左右
		for k in range(2,3):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
			

			
#男前墙
for i in range(1,3):#i表示高度
	for j in range(-3,3):#j表示左右
		for k in range(-2,-1):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
			
#男前柱子
for i in range(1,6):#i表示高度
	for j in range(-6,-5):#j表示左右
		for k in range(-2,-1):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
#男前柱子2
for i in range(1,6):#i表示高度
	for j in range(-9,-8):#j表示左右
		for k in range(-2,-1):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
#前墙续作
for i in range(1,3):#i表示高度
	for j in range(-3,-2):#j表示左右
		for k in range(0,3):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
#前墙续作1——1
for i in range(1,3):#i表示高度
	for j in range(0,3):#j表示左右
		for k in range(2,3):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
		
			

			
			
#前墙续作1——2
for i in range(1,2):#i表示高度
	for j in range(0,2):#j表示左右
		for k in range(8,9):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
#前墙续作1——2
for i in range(1,3):#i表示高度
	for j in range(3,9):#j表示左右
		for k in range(8,9):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
for i in range(1,3):#i表示高度
	for j in range(2,3):#j表示左右
		for k in range(6,7):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
for i in range(1,2):#i表示高度
	for j in range(1,2):#j表示左右
		for k in range(6,7):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)




			
#前墙续作1——2
for i in range(1,3):#i表示高度
	for j in range(-8,-2):#j表示左右
		for k in range(8,9):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
#堵墙
for i in range(1,5):#i表示高度
	for j in range(-6,-5):#j表示左右
		for k in range(9,10):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
#堵墙
for i in range(1,6):#i表示高度
	for j in range(-3,-2):#j表示左右
		for k in range(9,10):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)			

#前墙续作1——3
for i in range(1,2):#i表示高度
	for j in range(-11,0):#j表示左右
		for k in range(10,11):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			

			
#前墙续作1——4
for i in range(1,3):#i表示高度
	for j in range(-8,0):#j表示左右
		for k in range(13,14):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
#前墙续作1——4
for i in range(1,2):#i表示高度
	for j in range(2,8):#j表示左右
		for k in range(13,14):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
						
#前墙续作1——4
for i in range(1,2):#i表示高度
	for j in range(2,4):#j表示左右
		for k in range(10,12):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)


#最前墙
for i in range(1,2):#i表示高度
	for j in range(-8,-7):#j表示左右
		for k in range(14,17):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
for i in range(1,2):#i表示高度
	for j in range(-13,-8):#j表示左右
		for k in range(14,16):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)

			
#最前墙
for i in range(1,2):#i表示高度
	for j in range(-7,17):#j表示左右
		for k in range(17,18):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			

for i in range(1,2):#i表示高度
	for j in range(-13,-8):#j表示左右
		for k in range(17,18):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)

#前墙续作2——1
for i in range(1,3):#i表示高度
	for j in range(-6,-3):#j表示左右
		for k in range(0,1):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			

			
			
for i in range(1,3):#i表示高度
	for j in range(-13,-8):#j表示左右
		for k in range(0,1):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
for i in range(1,4):#i表示高度
	for j in range(-9,-8):#j表示左右
		for k in range(2,4):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			
for i in range(1,3):#i表示高度
	for j in range(-7,-2):#j表示左右
		for k in range(5,6):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
			




#男左墙
for i in range(1,3):#i表示高度
	for j in range(-13,-1):#j表示左右
		for k in range(-5,-4):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)
#男后墙
for i in range(1,3):#i表示高度
	for j in range(-13,2):#j表示左右
		for k in range(-7,-6):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)



#男左墙
for i in range(1,3):#i表示高度
	for j in range(-14,-13):#j表示左右
		for k in range(-10,20):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)


#男左墙
for i in range(1,3):#i表示高度
	for j in range(13,14):#j表示左右
		for k in range(-10,20):#k表示前后
			box = viz.add('crate.osgb') 
			box.setPosition(j,i,3+k)
			box.collideBox()
			#box.density = .5
			#box.collideBox( node = 'Top', hardness = .5 )
			boxs.append(box)


male.enable(viz.COLLIDE_NOTIFY)

viz.phys.enable()

def DisplayInstructionsTask():
    """Task that display instructions and waits for keypress to continue"""
    panel = vizinfo.InfoPanel(INSTRUCTIONS,align=viz.ALIGN_CENTER,fontSize=22,icon=False,key=None)
    pigeonClone = pigeon.clone(scale=[200]*3)
    pigeonClone.addAction(vizact.spin(0,1,0,45))
    pigeonClone.enable(viz.DEPTH_TEST,op=viz.OP_ROOT)
    panel.addItem(pigeonClone,align=viz.ALIGN_CENTER)
    yield viztask.waitKeyDown('1')
    panel.remove()


def Movementcar2():
	
	
	moveForward3 = vizact.move(2,0,4,1)
	turnRight3 = vizact.spin(0,1,0,90,1)
	moveInSquare3  = vizact.sequence(moveForward3,turnRight3,100)
	wheel3=viz.addChild('wheelbarrow.ive')
	wheel3.collideBox()
	wheel3.setPosition(0,5,14)
	wheel3.collideBox(2,0.1,2)
	wheel3.addAction(moveInSquare3)

def Movementcar3():
	
	
	moveForward3 = vizact.move(2,0,4,1)
	turnRight3 = vizact.spin(0,1,0,90,1)
	moveInSquare3  = vizact.sequence(moveForward3,turnRight3,100)
	wheel3=viz.addChild('wheelbarrow.ive')
	wheel3.collideBox()
	wheel3.setPosition(4,5,3)
	wheel3.collideBox(2,0.1,2)
	wheel3.addAction(moveInSquare3)

def Movementcar1():
	
	
	moveForward3 = vizact.move(2,0,4,1)
	turnRight3 = vizact.spin(0,1,0,90,1)
	moveInSquare3  = vizact.sequence(moveForward3,turnRight3,100)
	wheel3=viz.addChild('wheelbarrow.ive')
	wheel3.collideBox()
	wheel3.setPosition(-3,5,12)
	wheel3.collideBox(2,0.1,2)
	wheel3.addAction(moveInSquare3)
	

def Movementcar_crazy():
	
	
	moveForward3 = vizact.move(2,0,4,1)
	turnRight3 = vizact.spin(0,1,0,90,1)
	moveInSquare3  = vizact.sequence(moveForward3,turnRight3,100)
	wheel3=viz.addChild('wheelbarrow.ive')
	wheel3.collideBox()
	wheel3.setPosition(-3,5,11)
	wheel3.collideBox(2,0.1,2)
	wheel3.addAction(moveInSquare3)
	Movementcar1()
	wheel=viz.addChild('wheelbarrow.ive')
	wheel.collideBox()
	wheel.setPosition(1,0,10)
	wheel.collideBox(2,0.1,2)
	moveForward = vizact.move(0,0,8,1)
	turnRight = vizact.spin(0,1,0,90,1)
	moveInSquare  = vizact.sequence(moveForward,turnRight,100)
	wheel.addAction(moveInSquare)
	Movementcar2()
	wheel2=viz.addChild('wheelbarrow.ive')
	wheel2.collideBox()
	wheel2.setPosition(2,0,4)
	wheel2.collideBox(2,0.1,2)
	moveForward2 = vizact.move(0,0,-4,1)
	turnRight2 = vizact.spin(0,-1,0,-80,1)
	moveInSquare2  = vizact.sequence(moveForward2,turnRight2,100)
	wheel2.addAction(moveInSquare2)
	Movementcar3()
	
	

def avatarWalk():
	if scoreLabel.score<=0:
		male.setPosition(0.7,0,-2)
		male.addAction(vizact.animation(5))
		scoreLabel2 = viz.addText('GAME OVER',parent=viz.ORTHO,fontSize=40)
		scoreLabel2.alignment(viz.ALIGN_RIGHT_TOP)
		scoreLabel2.setBackdrop(viz.BACKDROP_OUTLINE)
		viz.link(viz.MainWindow.LeftTop,scoreLabel2,offset=[500,-20,0])
	else :
		info = viz.pick(1)
		if info.valid and info.object == ground:
			walk = vizact.walkTo([info.point[0],0,info.point[2]],verb='run')
			male.runAction(walk)

foot_sound = viz.addAudio('birds.wav')



#random flash
def flashback():
	male.addAction(vizact.animation(8))
	x,y,z = male.getPosition()
	i=random.randint(-1,1)
	j=random.randint(2,5)
	if j==2:
		male.setPosition(x+i,y,z+i)
	elif j==3:
		male.setPosition(x+i,y,z-i)
	elif j==4:
		male.setPosition(x-i,y,z-i)
	else:
		male.setPosition(x-i,y,z+i)
	scoreLabel.score-=5
	scoreLabel.message(str(scoreLabel.score))
	scoreLabel.setPosition(-5,0,2)
	#生命条为0时候回到原点
	if(scoreLabel.score<=0):
		male.setPosition(0.7,0,-5)
vizact.onkeydown(' ',flashback)

def xaingqian_flash():
	male.addAction(vizact.animation(8))
	x,y,z = male.getPosition()
	male.setPosition(x,y,z+3)
	scoreLabel.score-=40
	scoreLabel.message(str(scoreLabel.score))
	scoreLabel.setPosition(-5,0,2)
	#生命条为0时候回到原点
	Movementcar_crazy()
	if(scoreLabel.score<=0):
		male.setPosition(0.7,0,-2)
vizact.onkeydown('2',xaingqian_flash)

def win():
	male.addAction(vizact.animation(3))
	x,y,z = male.getPosition()
	if z>20:
		scoreLabel2 = viz.addText('YOU WIN',parent=viz.ORTHO,fontSize=40)
		scoreLabel2.alignment(viz.ALIGN_RIGHT_TOP)
		scoreLabel2.setBackdrop(viz.BACKDROP_OUTLINE)
		viz.link(viz.MainWindow.LeftTop,scoreLabel2,offset=[500,-20,0])
		scoreLabel.score=100000
		scoreLabel.message(str(scoreLabel.score))
		
vizact.onkeydown('w',win)

def replay() :
	scoreLabel.score=100
	scoreLabel.message(str(scoreLabel.score))
	scoreLabel.setPosition(-5,0,2)
	male.setPosition(0.7,0,-2)
	
vizact.onkeydown('r',replay)
def oncollide(e):
	#if e.obj2 == wheel or e.obj2 == wheel2:
	#	scoreLabel.score=scoreLabel.score-50
	#	scoreLabel.message(str(scoreLabel.score))
	#	scoreLabel.setPosition(-5,0,2)
		
	if e.obj2 == pigeon :
		scoreLabel.score=scoreLabel.score+100
		scoreLabel.message(str(scoreLabel.score))
		scoreLabel.setPosition(-5,0,2)
		pigeon.setPosition(-20,0,-30)
	elif e.obj2==pigeon2:
		scoreLabel.score=scoreLabel.score+100
		scoreLabel.message(str(scoreLabel.score))
		scoreLabel.setPosition(-5,0,2)
		pigeon2.setPosition(-20,0,-30)
	elif e.obj2==wheel:
		scoreLabel.score=scoreLabel.score-50
		scoreLabel.message(str(scoreLabel.score))
		scoreLabel.setPosition(-5,0,2)
		
	elif e.obj2==pigeon4:
		scoreLabel.score=scoreLabel.score+50
		scoreLabel.message(str(scoreLabel.score))
		scoreLabel.setPosition(-5,0,2)
		pigeon4.setPosition(-20,0,-30)	
		viz.playSound('sounds/pigeon_catch.wav')
	
	elif e.obj2==pigeon5:
		scoreLabel.score=scoreLabel.score+100
		scoreLabel.message(str(scoreLabel.score))
		scoreLabel.setPosition(-5,0,2)
		pigeon4.setPosition(-20,0,-30)	
		viz.playSound('sounds/pigeon_catch.wav')
		
	elif e.obj2 in boxs:
		scoreLabel.score=scoreLabel.score-30
		scoreLabel.message(str(scoreLabel.score))
		scoreLabel.setPosition(-5,0,2)
		Movementcar3()
		
	elif e.obj2 ==soccer:
		scoreLabel.score=100
		scoreLabel.message(str(scoreLabel.score))
		scoreLabel.setPosition(-5,0,2)
		male.setPosition(0.7,0,-5)
		soccer.setPosition(-10,0,-20)
		Movementcar_crazy
	if(scoreLabel.score<=0):
			male.setPosition(0.7,0,-10)
			scoreLabel2 = viz.addText('GAME OVER',parent=viz.ORTHO,fontSize=40)
			scoreLabel2.alignment(viz.ALIGN_RIGHT_TOP)
			scoreLabel2.setBackdrop(viz.BACKDROP_OUTLINE)
			viz.link(viz.MainWindow.LeftTop,scoreLabel2,offset=[500,-20,0])
		
			
viz.callback(viz.COLLIDE_BEGIN_EVENT,oncollide)


def MainTask():
    """Top level task that controls the game"""

    # Display instructions and wait for key press to continue
    yield DisplayInstructionsTask()

    # Create panel to display trial results
    resultPanel = vizinfo.InfoPanel('',align=viz.ALIGN_CENTER,fontSize=25,icon=False,key=None)
    resultPanel.visible(False)


viztask.schedule( MainTask() )


vizact.onmousedown(viz.MOUSEBUTTON_RIGHT, avatarWalk)
 
viz.mouse(viz.OFF)



moveForward = vizact.move(0,0,10,5)
turnRight = vizact.spin(0,1,0,90,1)



#Play the animation path
path.play()
