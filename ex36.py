def roomgame():
	print """
	Hello welcome to my virtual adventure game.

	In this game, there are multiple choices and each of them has either positive or negative consequences.

	Let's get started.
	"""
 	def choose_a_door():
		print "There are three doors. Middle, right, and left."
		print "Which one do you go in?"
		choice1 =  raw_input("> ")
	

		if choice1 = "middle":
			print "In this room there are a bunch of stuffed bears blocking the door. What do you do?"
			print "Do you move them or climb to the top of the pile."
			print "You can also go back a door."
			bears = raw_input("> ")
	
			if "move" in choice1:
				print dead("The stuffed bears explode because they are stuffed with C4 explosives. Good job!")
	
			elif "climb" in choice:
				print "Nice job. You found a hidden door in the ceiling."

			elif "go back" in choice:
				choose_a_door()
	
			else:
				print "I got no idea what that means."

		if choice1 = "right":
			print "In this room, there is the Captain Davy Jones (from Pirates of the Carribean) blocking the door. He is holding a sword. There is also a s                        sword laying next to him. What do you do?"

			davyjones = raw_input("> ")

			if "fight" in davyjones:
				print dead("Bad idea. He stabs you in the chest. Good Job!")

			elif "run" or "away" in choice:
				print "Good choice. You have just spared your life."
				choose_a_door()


		


