import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("메뉴바 예제")

# 메뉴바 생성
menubar = tk.Menu(root)
root.config(menu=menubar)

# 파일 메뉴
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="파일", menu=file_menu)
file_menu.add_command(label="새로 만들기")
file_menu.add_command(label="열기")
file_menu.add_separator()  # 구분선
file_menu.add_command(label="종료", command=root.quit)

# 편집 메뉴
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="편집", menu=edit_menu)
edit_menu.add_command(label="복사")
edit_menu.add_command(label="붙여넣기")

# 도움말 메뉴
def show_about():
    messagebox.showinfo("정보", "메뉴바 예제 프로그램 v1.0")

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="도움말", menu=help_menu)
help_menu.add_command(label="정보", command=show_about)

root.mainloop()