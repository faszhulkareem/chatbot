
import os
import win32com.client as wincl
import turtle
speak = wincl.Dispatch("SAPI.SpVoice")

print('Enter the name of the shape you want to draw: ')
while True:
    res = input('You: ')
    if(res=='rectangle'):
        print('Bot: A rectangle will be drawn')
        window = turtle.Screen()
        s = turtle.Turtle()
        s.forward(400)
        s.left(90)
        s.forward(200)
        s.left(90)
        s.forward(400)
        s.left(90)
        s.forward(200)
        s.left(90)       
    else:
        print("np")