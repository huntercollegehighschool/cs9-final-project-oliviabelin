"""
Name(s): Olivia Belin, Ella Cohen
Name of Project: Mad Libs Final Project
"""

import random 
lis = ['story1', 'story2', 'story3', 'story4'] 
f = random.choice(lis)
print(f)

if f == 'story1':
  pluralnoun1 = input("Enter a plural noun: ")
  celebrity1 = input("Enter a celebrity: ")
  articleofclothing1 = input("Enter an article of clothing: ")
  adjective1 = input("Enter an adjective: ")
  noun1 =  input("Enter a noun: ")
  pluralnoun2 = input("Enter a plural noun: ")
  articleofclothing2 =  input("Enter an article of clothing: ")
  verb1=  input("Enter a verb: ")
  pluralnoun3 =  input("Enter another plural noun: ")
  typeofliquid = input("Enter a type of liquid: ")
  adjective2 = input("Enter an adjective: ")
  noun2 = input("Enter a noun: ")

  story1 = ('In the 1960s, tie-dyed ' + pluralnoun1 + ' became a popular fashion fad after ' + celebrity1 + ' wore a psychedelic ' + articleofclothing1 + ' at a concert. Soon after, hippies donned this ' + adjective1 + ' apparel while promoting peace and ' + noun1 + '. Today, anyone can create colorful ' + pluralnoun2 + ' in their backyard. First, take a damp ' + articleofclothing2 + ', ' + verb1 + ' and roll the fabric, then tie it tight with some rubber ' + pluralnoun3 + '. Next, dip sections into vats of colored ' + typeofliquid + '. The longer it soaks, the more ' + adjective2 + ' the colors become! Finally, soak your creation in a mixture of ' + noun2 + ' and vinegar. ')
  print(story1)
elif f == 'story2':
  foreigncountry = input("Enter a foreign country: ")
  adverb = input("Enter an adverb: ")
  adjective3 = input("Enter an adjective: ")
  animal =  input("Enter an animal: ")
  verbing1 = input("Enter a verb ending in ing: ")
  verb2=  input("Enter a verb: ")
  verbing2 = input("Enter a verb ending in ing: ")
  adverb1 = input("Enter an adverb: ")
  adjective3 = input("Enter an adjective: ")

  story2 = ('If you are traveling in ' + foreigncountry + ' and find yourself having to cross a piranha-filled river, heres how to do it ' + adverb + '. Piranhas are more ' + adjective3 + ' during the day, so cross the river at night. Avoid areas with netted ' + animal + ' traps - piranhas may be ' + verbing1 + ' there looking to ' + verb2 + ' them! When ' + verbing2 + ' the river, swim ' + adverb1 + '. You do not want to wake them up and make them ' + adjective3 + '!')
  print(story2)
elif f == 'story3':
  pluralnoun1 = input("Enter a plural noun: ")
  adjective1 = input("Enter an adjective: ")
  pluralnounanimal = input("Enter an animal (plural): ")
  pluralnoun2 = input("Enter a plural noun: ")
  adjective2 =  input("Enter a adjective: ")
  color = input("Enter a color: ")
  adjective3 =  input("Enter an adjective: ")
  noun=  input("Enter a noun: ")
  pluralnoun3 =  input("Enter a plural noun: ")
  adjective4 = input("Enter an adjective: ")
  verb = input("Enter a verb: ")
  pluralnoun4 = input("Enter a plural noun: ")

  story3 = ('Unicorns are not like other ' + pluralnoun1 + '; they are ' + adjective1 + '. They look like ' + pluralnounanimal + ', with ' + pluralnoun2 + ' for feet and a ' + adjective2 + ' mane of hair. But unicorns are ' + color + ' and have a ' + adjective3 + ' ' + noun + ' on their heads. Some ' + pluralnoun3 + ' do not believe unicorns are ' + adjective4 + ' but I believe in them. I would like to ' + verb + ' a unicorn to a faraway ' + pluralnoun4 + '.')
  print(story3)
else:
  number1 = input("Enter a number: ")
  pluralnoun1 = input("Enter a plural noun: ")
  verb1 = input("Enter a verb: ")
  adjective = input("Enter an adjective: ")
  number2 = input("Enter a number: ")
  place = input("Enter a place: ")
  verbed1 = input("Enter a verb ending in -ed: ")
  pluralnoun2 = input("Enter a plural noun: ")
  verb2 = input("Enter a verb: ")
  adverb = input("Enter an adverb: ")
  number3 = input("Enter a number: ")

  story4 = ('On July ' + number1 + ' 1969, two American ' + pluralnoun1 + ' were the first to ' + verb1 + ' on the moon. This ' + adjective + ' trip took ' + number2 + ' days to reach the moon from ' + place + '. They ' + verbed1 + ' ' + pluralnoun2 + ' from the surface of the moon to ' + verb2 + ' back to Earth and ' + adverb + ' returned home ' + number3 + ' days later.' )
  print(story4)