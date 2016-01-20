from sys import exit

def END():
	print "Good Job! You made it to the end congratulations"
	loop = 0

def room_of_teachers():
	print "This is the room of techears."
	print "There are three teachers standing in front of you."
	print "Mr. Olinda, Miss Chae, and Mr. Welch"
	print "Who do you want to talk to?"
	print "You are also allowed to go back a door."
	teach = raw_input("> ")
        if teach == "Mr. Olinda":
		print "You may pass."
		END()
	
	elif teach == "Miss Chae":
		print "She makes you study so much you die. Good  Job!"
		loop = 0

	elif teach == "Mr. Welch":
		print "Mr. Welch: Let's fight"
		print "Mr. Welch kills you. Nice!"
		loop = 0

	elif "go" or "back" in teach:
		print "OK Going back."
		stuffed_bears()


	else:
		"Mr. Olinda, Miss Chae, or Mr. Welch. Write them exactly as specified."
		room_of_teachers()


def insane():
	print "This is the room of insanity."
	print "Do you jump around like a monkey or eat your own brain. You can also go back."
	insane = raw_input("> ")

	if "monkey" or "jump" in insane:
		print "Bad choice. You fall into a pit of doom. Good Job!"
		loop = 0

	elif "eat" or "brain" in insane:
		print "Good choice you failed and while trying to eat your brain and fell out the door."
		END()

	else:
		print "I made it as simple as possible. Two choices dude. Two choices."
		insane()
def fairies():
	print "There are evil fairies blocking the door how do you get past them?"
	print "You can make a run for it, try to disguise yourself, or go back."
	fairy = raw_input("> ")

	if "run" in fairy:
		print "Good choice you may go through the door."
		insane()

	elif "disguise" in fairy:
		print "Nice try, but you were to big to be a fairy remember?"

	elif "back" in fairy:
		"OK going back."
		stuffed_bears()

def stuffed_bears():
        print "In this room there are a bunch of stuffed bears blocking the door. What do you do?"
        print "Do you move them or climb to the top of the pile."
	print "You can also go back a door."
	bears = raw_input("> ")
	
	if "move" in bears:
	    print "The stuffed bears explode because they are stuffed with C4 explosives. Good job!"
	
	elif "climb" in bears:
	    print "Nice job. You found a two hidden doors in the ceiling."
	    print "Do you go left or right"
	    which_door = raw_input("> ")
	    
	    if which_door == "right":
		    fairies()

            if which_door == "left":
		    room_of_teachers()


	

	elif "back" in bears:
	    roomgame()
	
	else:
	    print "I got no idea what that means."

def davy_jones_room():
        print "In this room, there is the Captain Davy Jones (from Pirates of the Carribean) blocking the door. He is holding a sword. There is also a sword laying next to him. What do you do?"
	print "Fight or run away?" 

        davyjones = raw_input("> ")

	if "fight" in davyjones:
		print "Bad idea. He stabs you in the chest. Good Job!"
		loop = 0

	elif "run" or "away" in choice:
		print "Good choice. You have just spared your life."
		roomgame()
		

	else:
	    print "I got no idea what that means."
def dragons():
	print "This is the hall of dragons"
	print "How are you gonna get past."
	print "There is fireproof armor, a sword, and and a shield."
	print "Which one are you going to use?"
	print "You can only use one."
	print "You can also go back."
	drag_ch = raw_input(" >")

	if "armor" in drag_ch:
		print "It was fake armor. The dragons destroyed your body. Good job!"
		loop = 0

	elif 'sword' in drag_ch:
		print "Bad idea. The dragons got scared and burned the life outta you. Good Job!"
		loop = 0
				

	elif "shield" in drag_ch:
		print "Nice choice you survived. You will now be teleported to the stuffed bear room."
		stuffed_bears() 

	elif "back" in drag_ch:
		print "OK we are going back"
		roomgame()

def roomgame():
	print """
	Hello welcome to my virtual adventure game.

	In this game, there are multiple choices and each of them has either positive or negative consequences.

	Try to get to the end without dying.

	GOOD LUCK!
	"""
	print "There are three doors. Middle, right, and left."
    	print "Which one do you go in?"
	choice1 =  raw_input("> ") 

	if choice1 == "middle":
		stuffed_bears()

	elif choice1 == "left":
		dragons()

	elif choice1 == "right":
		davy_jones_room()

	else:
		print "Middle, right, or left."
		roomgame()




roomgame()


             
  
