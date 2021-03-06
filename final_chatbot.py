
import os
import win32com.client as wincl
import turtle
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
speak = wincl.Dispatch("SAPI.SpVoice")

print('what do you like to draw? ')
print("select a shape:(rectangle/circle/triangle/hexagon/heart/star)")
print("To stop ,pls enter 'end'.")
window = turtle.Screen()
s = turtle.Turtle()
while True:
    res = input('You: ')
    if(res=='rectangle'):
        s.clear()
        print('Bot: A rectangle will be drawn')
        speak.Speak('A rectangle will be draw')
        s.forward(400)
        s.left(90)
        s.forward(200)
        s.left(90)
        s.forward(400)
        s.left(90)
        s.forward(200)
        s.left(90)       
    elif(res=='circle'):
        s.clear()
        print('Bot: A circle will be drawn')
        speak.Speak('A circle will be draw')
        s.circle(50)
        
    elif(res=='triangle'):
        s.clear()
        print('Bot: A triangle will be drawn')
        speak.Speak('A triangle will be draw')
        s.forward(200)
        s.left(120)
        s.forward(200)
        s.left(120)
        s.forward(200)
    elif(res=='hexagon'):
        s.clear()
        print('Bot: A hexagon will be drawn')
        speak.Speak('A hexagon will be draw')
        for i in range(6):
            s.forward(100)
            s.left(60)
    elif(res=='star'):
        s.clear()
        print('Bot: A star will be drawn')
        speak.Speak('A star will be draw')
        for i in range(5):
            s.forward(200)
            s.left(144)
    elif(res=='heart'):
        s.clear()
        print('Bot: A heart will be drawn')
        speak.Speak('A heart will be draw')
        def curve():
            for i in range(200):
                s.right(1)
                s.forward(1)
        s.speed(0)
        s.color("red","pink")
        s.begin_fill()
        s.left(140)
        s.forward(140)
        curve()
        s.left(120)
        curve()
        s.forward(111.65)
        s.end_fill()
        s.hideturtle()
    elif(res=='end'):
        print('Thank you!,see you again')
        speak.Speak('Thank you!,see you again')
        break
    else:
        print('no shapes can be drawn')
        speak.Speak('no shapes can be drawn')


   