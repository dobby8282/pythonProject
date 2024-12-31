'''
파일명: Ex24-8-Scrollbar.py

tkinter의 Scrollbar와 Listbox 사용 예제
'''
import tkinter as tk

root = tk.Tk()
root.title("스크롤바와 리스트박스 예제")

# 프레임 생성
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# 스크롤바 생성
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# 리스트박스 생성
listbox = tk.Listbox(frame,
                     yscrollcommand=scrollbar.set,
                     width=30,
                     height=10)

# 리스트박스에 항목 추가
for i in range(1, 31):
    listbox.insert(tk.END, f"리스트 항목 {i}")

listbox.pack(side="left")

# 스크롤바와 리스트박스 연결
scrollbar.config(command=listbox.yview)

root.mainloop()