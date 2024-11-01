#   a123_apple_1.py
import turtle as trtl
import random as random

#-----lists-----

possible_letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
typeable_letters = []
falling_fruits = []
falling_letters = []

#-----setup-----
apple_image = "apple.gif"  # Store the file name of your shape (Apple)
pear_image = "pear.gif"  # Store the file name of your shape (Pear)

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image)  # Make the screen aware of the new file
wn.addshape(apple_image)  # Make the screen aware of the new file

active_apple = trtl.Turtle()
active_pear = trtl.Turtle()
active_apple2 = trtl.Turtle()
active_pear2 = trtl.Turtle()
active_apple3 = trtl.Turtle()

letter_turtle = trtl.Turtle()
current_fruit = trtl.Turtle()
falling_letter_turtle = trtl.Turtle()

wn.bgpic("background.gif")  # Place the background image

timer_active = False

fruits = []

num_of_apples = 3
num_of_pears = 2

fruit_cor = []

To_Fall_Fruits = []

letter_turtle_two = trtl.Turtle()
letter_turtle_three = trtl.Turtle()
letter_turt_four = trtl.Turtle()
letter_turt_five = trtl.Turtle()

letter_trtl_list = [letter_turtle, letter_turtle_two, letter_turtle_three]
letter_trtl_list.append(letter_turt_four)
letter_trtl_list.append(letter_turt_five)

typed_fruits = set()

index = 0

falling_index = 0

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file


def draw_apple():
  global typeable_letters
  global fruits
  for i in range(num_of_apples):
    active_apple = trtl.Turtle(shape=apple_image)
    active_apple.penup()
    active_apple.goto(random.randint(-200, 200), random.randint(0, 200))
    fruits.append(active_apple)
  for i in range(num_of_pears):
    active_pear = trtl.Turtle(shape=pear_image)
    active_pear.penup()
    active_pear.goto(random.randint(-200, 200), random.randint(0, 200))
    fruits.append(active_pear)
  print(fruits)
  wn.update()


# moves the fruit so that it falls down the screen
def fruit_fall():  #defines the function
  print("Fruit Fall")
  global falling_index
  global typeable_letters
  if falling_index == 0:
    print(fruits[0])
    current_fruit = fruits[0]
    if current_fruit.ycor() > -200:
      i = falling_index
      current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 10)
      letter_trtl_list[i].clear()
      letter_trtl_list[i].goto(current_fruit.xcor() - 10,
                               current_fruit.ycor() - 25)
      letter_trtl_list[i].write(typeable_letters[i],
                                font=("Arial", 30, "bold"))
      wn.ontimer(fruit_fall, 100)
    else:
      respawn_fruit()

  elif falling_index == 1:
    print(fruits[1])
    current_fruit = fruits[1]
    if current_fruit.ycor() > -200:
      i = falling_index
      current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 10)
      letter_trtl_list[i].clear()
      letter_trtl_list[i].goto(current_fruit.xcor() - 10,
                               current_fruit.ycor() - 25)
      letter_trtl_list[i].write(typeable_letters[i],
                                font=("Arial", 30, "bold"))
      wn.ontimer(fruit_fall, 100)
    else:
      respawn_fruit()
  elif falling_index == 2:
    print(fruits[2])
    current_fruit = fruits[2]
    if current_fruit.ycor() > -200:
      i = falling_index
      current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 10)
      letter_trtl_list[i].clear()
      letter_trtl_list[i].goto(current_fruit.xcor() - 10,
                               current_fruit.ycor() - 25)
      letter_trtl_list[i].write(typeable_letters[i],
                                font=("Arial", 30, "bold"))
      wn.ontimer(fruit_fall, 100)
    else:
      respawn_fruit()
  elif falling_index == 3:
    print(fruits[3])
    current_fruit = fruits[3]
    if current_fruit.ycor() > -200:
      i = falling_index
      current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 10)
      letter_trtl_list[i].clear()
      letter_trtl_list[i].goto(current_fruit.xcor() - 10,
                               current_fruit.ycor() - 25)
      letter_trtl_list[i].write(typeable_letters[i],
                                font=("Arial", 30, "bold"))
      wn.ontimer(fruit_fall, 100)
    else:
      respawn_fruit()
  elif falling_index == 4:
    print(fruits[4])
    current_fruit = fruits[4]
    if current_fruit.ycor() > -200:
      i = falling_index
      current_fruit.goto(current_fruit.xcor(), current_fruit.ycor() - 10)
      letter_trtl_list[i].clear()
      letter_trtl_list[i].goto(current_fruit.xcor() - 10,
                               current_fruit.ycor() - 25)
      letter_trtl_list[i].write(typeable_letters[i],
                                font=("Arial", 30, "bold"))
      wn.ontimer(fruit_fall, 100)
    else:
      respawn_fruit()

  respawn_fruit()


def assign_letters():
  for i in range(len(fruits)):
    global letter_trtl_list
    current_fruit = fruits[i]
    current_letter_trtl = letter_trtl_list[i]
    current_letter_trtl.penup()
    current_letter = possible_letters[random.randint(0, 25)]
    if current_letter in typeable_letters:
      while current_letter in typeable_letters:
        current_letter = possible_letters[random.randint(0, 25)]
    current_letter_trtl.goto(current_fruit.xcor() - 10,
                             current_fruit.ycor() - 25)
    current_letter_trtl.write(current_letter, font=("Arial", 30, "bold"))
    current_letter_trtl.hideturtle()
    typeable_letters.append(current_letter)


def start_fruit_fall():
  global timer_active
  timer_active = True
  fruit_fall()


def letter_to_type():
  global typeable_letters
  for letter in typeable_letters:
    wn.onkeypress(lambda l=letter: check_keypress(l), letter)


def check_keypress(key):
  global falling_index
  global typeable_letters
  global falling_letters
  if key in typeable_letters:
    print("You pressed the correct key!")
    falling_letters.append(key)
    for i in range(len(fruits)):
      if key == typeable_letters[i]:
        falling_index = i
        print(falling_index)
        print(falling_letters)
        start_fruit_fall()
      else:
        i += i


def respawn_fruit():
  global falling_index
  i = falling_index
  if fruits[i].ycor() < -200:
    letter_trtl_list[i].clear()
    fruits[i].hideturtle()
    if fruits[i].shape() == "apple.gif":
      active_apple = trtl.Turtle(shape=apple_image)
      active_apple.penup()
      active_apple.goto(random.randint(-200, 200), random.randint(0, 200))
      letter_trtl_list[i].clear()
      letter_trtl_list[i].goto(fruits[i].xcor() - 10, fruits[i].ycor() - 25)
      current_letter = possible_letters[random.randint(0, 25)]
      letter_trtl_list[i].write(current_letter, font=("Arial", 30, "bold"))
      del fruits[i]
      fruits.append(active_apple)
    elif fruits[i].shape() == "pear.gif":
      active_pear = trtl.Turtle(shape=pear_image)
      active_pear.penup()
      active_pear.goto(random.randint(-200, 200), random.randint(0, 200))
      letter_trtl_list[i].clear()
      letter_trtl_list[i].goto(fruits[i].xcor() - 10, fruits[i].ycor() - 25)
      current_letter = possible_letters[random.randint(0, 25)]
      letter_trtl_list[i].write(current_letter, font=("Arial", 30, "bold"))
      del fruits[i]
      fruits.append(active_pear)
  else:
    print("continuing")
  wn.ontimer(respawn_fruit, 500)


#this is a change
# Fix all of fruit fall so that the letter falls too for all possible
#falling fruits

#Update respawn to use the new lists and whatnot so it works

#Update the way we keep track of letters so each letter is a different turtle
#So that clearing one turtle does not clear the other turtles
#this will mean if the falling index is 0, the fruit is in index 0 of the
#fruit list and the letter is in index 0 of the letter list

#-----function calls-----

draw_apple()
assign_letters()
letter_to_type()
#respawn_fruit()
wn.listen()

wn.mainloop()

#When clicked one letter, all fruits fall! FIX!
