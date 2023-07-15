'''
파일명: Ex24-2-Tkinter.py
'''
from tkinter import *
import time

tk = Tk()
# Canvas 위젯 생성 및 크기 설정
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

# 다각형 그리기
canvas.create_polygon(250, 400, 275, 450, 225, 450)
canvas.create_polygon(250, 400, 275, 450, 225, 450)

for i in range(0, 70):
    canvas.move(1, -5, -5)
    canvas.move(2, 5, -5)

    tk.update()
    time.sleep(0.05)



