import turtle as trtl

horiz_turtles = []
vert_turtles = []
pcrashht = []
pcrashvt = []

turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
horiz_colors2 = ["gold", "purple", "orange", "green", "blue", "red"]
vert_colors2 = ["brown", "indigo", "salmon", "lime", "darkblue", "darkred"]

tloc = 50
for s in turtle_shapes:

	ht = trtl.Turtle(shape=s)
	ht.speed(0)
	horiz_turtles.append(ht)
	ht.penup()
	new_ht_color = horiz_colors.pop()
	ht.fillcolor(new_ht_color)
	ht.goto(-350, tloc)
	ht.setheading(0)
	
	vt = trtl.Turtle(shape=s)
	vt.speed(0)
	vert_turtles.append(vt)
	vt.penup()
	new_vt_color = vert_colors.pop()
	vt.fillcolor(new_vt_color)
	vt.goto( -tloc, 350)
	vt.setheading(270)
	
	tloc += 50

steps = 0
speed = 4
c = 0
while c < 6:
	vt.speed(0)
	ht.speed(0)
	for vt in vert_turtles:
		vt.forward(speed)
	for ht in horiz_turtles:
		ht.forward(speed)
	if((vt.xcor()) - (ht.xcor()) < 15):
		if((vt.ycor()) - (ht.ycor()) < 15):
			steps = 501
			vt.fillcolor("gray")
			ht.fillcolor("gray")
			vt.speed(1)
			ht.speed(1)
			vt.back(40)
			ht.back(80)
			new_vt_color = vert_colors2.pop()
			new_ht_color = horiz_colors2.pop()
			vt.fillcolor(new_vt_color)
			ht.fillcolor(new_ht_color)
			pcrashvt.append(vt)
			pcrashht.append(ht)
			vert_turtles.remove(vt)
			horiz_turtles.remove(ht)
			steps = 0
			c += 1
	else:
		steps += 1

c = 0

while c <= 50:
	for vt in pcrashvt:
		vt.forward(speed)
	for ht in pcrashht:
		ht.forward(speed)
	c += 1


wn = trtl.Screen()
wn.mainloop()