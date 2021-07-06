# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#PART 1
#Goalscorers of the Dutch soccer team in the finals of EC'88
NL_doelpuntenmaker_1 = "Ruud Gullit"
NL_doelpuntenmaker_2 = "Marco van Basten"

#Goal that was scored in the match in minutes
goal_1 = 32
goal_2 = 54

scorers = NL_doelpuntenmaker_1 + " " + str(goal_1), NL_doelpuntenmaker_2 + " " + str(goal_2)
print (scorers)

report = f'{NL_doelpuntenmaker_1} scored in the {goal_1}nd minute\n{NL_doelpuntenmaker_2} scored in the {goal_2}th minute'
print(report)

#PART 2
#Player that played in the soccermatch of the finals of EC '88
player = "Oleksiy Mykhaylychenko"
first_name = player[:player.find(" ")] 
print(first_name)

last_name = player[player.find(" "):]
last_name_len = len(last_name[1:])
print(last_name_len)

name_short = player[0] + "." + last_name
print(name_short)

multiple_chant = (first_name + "!" + " ") * len(first_name)
chant = multiple_chant[:-1]
print(chant)

good_chant = multiple_chant != chant
print (good_chant)
