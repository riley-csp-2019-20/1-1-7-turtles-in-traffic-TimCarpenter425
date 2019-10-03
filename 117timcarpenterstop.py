import turtle as trtl

horiz_turtles = []
vert_turtles = []

turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

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

	steps = 0
	speed = 5
	while steps < 100:
		vt.speed(0)
		ht.speed(0)
		vt.forward(speed)
		ht.forward(speed)
		if((vt.xcor()) - (ht.xcor()) < 15):
			if((vt.ycor()) - (ht.ycor()) < 15):
				steps = 501
				vt.fillcolor("gray")
				ht.fillcolor("gray")
				vt.speed(1)
				ht.speed(2)
				vt.back(40)
				ht.back(80)
				vt.fillcolor(new_vt_color)
				ht.fillcolor(new_ht_color)
				vt.forward(150)
				ht.forward(190)
		else:
			steps += 1
	tloc += 50

wn = trtl.Screen()
wn.mainloop()