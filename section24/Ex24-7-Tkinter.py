'''
파일명: Ex24-9-MessageBox.py

tkinter의 다양한 메시지박스 사용 예제
'''
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("메시지박스 예제")

def show_info():
    messagebox.showinfo("정보", "정보 메시지입니다.")

def show_warning():
    messagebox.showwarning("경고", "경고 메시지입니다.")

def show_error():
    messagebox.showerror("오류", "오류 메시지입니다.")

def show_question():
    result = messagebox.askquestion("질문", "계속하시겠습니까?")
    print("응답:", result)  # 'yes' 또는 'no' 반환

def show_okcancel():
    result = messagebox.askokcancel("확인", "변경사항을 저장하시겠습니까?")
    print("응답:", result)  # True 또는 False 반환

# 버튼 생성
tk.Button(root, text="정보 메시지", command=show_info).pack(pady=5)
tk.Button(root, text="경고 메시지", command=show_warning).pack(pady=5)
tk.Button(root, text="오류 메시지", command=show_error).pack(pady=5)
tk.Button(root, text="질문 메시지", command=show_question).pack(pady=5)
tk.Button(root, text="확인/취소 메시지", command=show_okcancel).pack(pady=5)

root.mainloop()