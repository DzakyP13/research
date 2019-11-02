#Source : https://www.google.com/url?sa=t&source=web&rct=j&url=https://download.atlantis-press.com/article/25894371.pdf&ved=2ahUKEwjbjfLTqJvlAhUBTY8KHXbJDU0QFjAPegQICBAB&usg=AOvVaw3r0h_YCVqwWY93nhI0rOKe
#Written in code by : Andre S. (18018024)

import math

'''
[Omnidirectional 4 Wheel]
Keterangan :
Vx 		 = Kecepatan robot sb. x
Vy 		 = Kecepatan robot sb. y
theta 	 = sudut heading robot
thetadif = kec. sudut selama bergerak
r		 = radius roda
R		 = radius robot (jarak roda berseberangan)
'''

while(1>0):
	Vx = input("Vx : ")
	Vy = input("Vy : ")
	theta = input("theta(der) : ");
	thetadif = input("thetadif : ")
	r=1; R=20;
	theta=theta*math.pi/180;
	if(Vx==0):
		Vx=0.000000000000001
	w1 = (-Vx*math.sin(theta+math.pi/4) + Vy*math.cos(theta+math.pi/4) + thetadif*R)/r
	w2 = (-Vx*math.sin(theta+3*math.pi/4) + Vy*math.cos(theta+3*math.pi/4) + thetadif*R)/r
	w3 = (-Vx*math.sin(theta+5*math.pi/4) + Vy*math.cos(theta+5*math.pi/4) + thetadif*R)/r
	w4 = (-Vx*math.sin(theta+7*math.pi/4) + Vy*math.cos(theta+7*math.pi/4) + thetadif*R)/r
	print("w1 = ",w1)
	print("w2 = ",w2)
	print("w3 = ",w3)
	print("w4 = ",w4)
	print("");
