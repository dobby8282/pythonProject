'''
파일명: Ex25-4-sqlite-board.py
'''
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as msg
import sqlite3

class BoardApp(tk.Tk):
    def __init__(self): # 생성자
        super().__init__()
        
        self.title('게시판')
        
        # 컨트롤 변수 선언
        self.combobox_search = ttk.Combobox(self)
        self.textfield_search = tk.Entry(self)
        self.button_search = tk.Button(self, text='검색')
        self.button_insert = tk.Button(self, text='신규')
        self.button_delete = tk.Button(self, text='삭제')
        self.button_update = tk.Button(self, text='수정')
        self.treeview_boardlist = ttk.Treeview(self,
                                               columns=('id', 'title', 'writer', 'date'),
                                               show='headings'
                                               )

        # 컨트롤 배치
        self.combobox_search.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.textfield_search.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        self.button_search.grid(row=0, column=2, padx=5, pady=5, sticky='ns')
        self.treeview_boardlist.grid(row=1, column=0, rowspan=3, columnspan=2,
                                     padx=5, pady=5, sticky='nsew')
        self.button_insert.grid(row=1, column=2, padx=5, pady=5, sticky='ns')
        self.button_update.grid(row=2, column=2, padx=5, pady=5, sticky='ns')
        self.button_delete.grid(row=3, column=2, padx=5, pady=5, sticky='ns')

        # 트리뷰 컬럼 설정


# 실행코드
if __name__ == '__main__':
    app = BoardApp()
    app.mainloop()

