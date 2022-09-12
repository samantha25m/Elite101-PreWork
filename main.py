#Samantha Murphy Chatbot Python prework Elite 101 Project
#this includes the chatbot project

#------functions--------

#pet texture function, what texture their pet has
def about_pet(pet_texture):
  print(f'So the texture is {pet_texture}')
  if pet_texture == 'fur':
    print('Ahh, a fluffy pet! How nice.')
  elif pet_texture == 'feathers':
    print('Feathers! How fun, I bet your pet can fly!')
  elif pet_texture == 'scales':
    print('Scales are very cool!')
  else:
    print('Something else! Wow, how fancy!')

#possible pet function, what type of pet they should get
def possible_pet(wanted_pet_movement):
  print(f'So you want a pet who {wanted_pet_movement}, huh')
  if wanted_pet_movement == 'flies':
    print('If you want a pet who flies you should get a bird!')
  elif wanted_pet_movement == 'swims':
    print('You should get a fish, or amphibian if you want a pet that swims! You can get a reptile too, like a turtle!')
  elif wanted_pet_movement == 'slithers':
    print('A pet that slithers is a snake! You should get one of those!')
  elif wanted_pet_movement == 'walks':
    print('Lots of pets walk! You could get a dog, cat, rodent, the options are endless!')
  else:
    print("Wow, I've never heard of a pet that does that, good luck finding a pet like that!")

#whether or not user has pet function
def havepet(haspet):
  yes_answers = ['yes', 'y', 'yep', 'yeah', 'of course', 'sure']
  no_answers = ['no', 'nope', 'no way', 'n', 'negative']
  
  if haspet in yes_answers:
    print("that's so cool!")
    pet_texture = input('Does your pet have "fur", "feathers", or "scales"?\n> ').lower()
    about_pet(pet_texture)
    
  elif haspet in no_answers:
    print('How sad. How about we get to work on that?')
    wanted_pet_movement = input('Would you prefer a pet that "flies", "swims", "slithers" or "walks"?\n> ').lower()
    possible_pet(wanted_pet_movement)
    
  else:
    print('Hmm, interesting')
    


#####

#talking and calling functions- most are called within code
print('Hello!')
name = input('What is your name?\n> ')
print(f'Welcome to this chatbot, {name}!')

haspet = input('Do you have a pet?\n> ').lower()
havepet(haspet)
