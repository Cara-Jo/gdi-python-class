health = 100
morale = 500

cat_value = raw_input("What's your cat's name? ")
print "You have " + str(health) + " health and " + str(morale) + " morale."
print "An evil bear has captured " + str(cat_value) + ", and he's ready to eat " + str(cat_value) + ". What do you do?"
print "Your Options"
print "1 - Slap the bear in the face."
print "2 - Walk away because you don't care and bears are super scary."
print "3 - Punch the bear in the face and take back your cat!"
print "Quit - Quit the game you loser."
input_value = raw_input ("Enter your next move: ")
while input_value.lower() != "quit":
	
	if input_value == '1':
		print "You dummy, you just got slapped in the face by a bear."
		print "You die."
		health = health - 100
		morale = morale - 450
	elif input_value == '2':
		print "Why would you do that?"
		print "Your cat is enraged and cuts you in the face! You deserve it. The bear catches the cat, and eats it."
		print "You're bleeding on the floor and you're super sad that your cat hates you."
		health = health - 50
		morale = morale - 200
	elif input_value == '3':
		print "WOW! You're a hero!!"
		print "Your cat loves you and the bear feels sad and wants a hug."
		print "Your morale increases because of so many snuggles."
		if health < 100:
			health = 100
		morale = morale + 400
	elif input_value != '1' or '2' or '3' or 'quit':
		print "Please try again"
	print "Health: " + str(health)
	print "Morale: " + str(morale)
	if health <= 0:
		print "You died."
		break
	# if morale <= 400: DO STUFF			
	input_value = raw_input ("Enter your next move: ")



