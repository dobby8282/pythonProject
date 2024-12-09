import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import datetime
from pathlib import Path
import calendar


class FileDateModifier(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("파일 날짜 수정 프로그램")
        self.geometry("600x400")

        # 메인 프레임
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 파일 선택
        ttk.Label(main_frame, text="파일 경로:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.file_path = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.file_path, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(main_frame, text="찾아보기", command=self.browse_file).grid(row=0, column=2)

        # 날짜 프레임
        date_frame = ttk.LabelFrame(main_frame, text="날짜 설정", padding="10")
        date_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

        # 생성일자 설정
        ttk.Label(date_frame, text="생성일자:").grid(row=0, column=0, sticky=tk.W)
        self.create_date_vars = self.create_date_widgets(date_frame, 0)

        # 수정일자 설정
        ttk.Label(date_frame, text="수정일자:").grid(row=1, column=0, sticky=tk.W)
        self.modify_date_vars = self.create_date_widgets(date_frame, 1)

        # 현재 시간 설정 버튼
        ttk.Button(main_frame, text="현재 시간으로 설정",
                   command=self.set_current_time).grid(row=2, column=0, columnspan=3, pady=10)

        # 실행 버튼
        ttk.Button(main_frame, text="날짜 변경하기",
                   command=self.modify_dates).grid(row=3, column=0, columnspan=3, pady=10)

    def create_date_widgets(self, parent, row):
        date_vars = {}

        # 년도
        date_vars['year'] = tk.StringVar(value=str(datetime.datetime.now().year))
        ttk.Spinbox(parent, from_=1970, to=2099, width=6,
                    textvariable=date_vars['year']).grid(row=row, column=1, padx=2)
        ttk.Label(parent, text="년").grid(row=row, column=2)

        # 월
        date_vars['month'] = tk.StringVar(value=str(datetime.datetime.now().month))
        ttk.Spinbox(parent, from_=1, to=12, width=4,
                    textvariable=date_vars['month']).grid(row=row, column=3, padx=2)
        ttk.Label(parent, text="월").grid(row=row, column=4)

        # 일
        date_vars['day'] = tk.StringVar(value=str(datetime.datetime.now().day))
        ttk.Spinbox(parent, from_=1, to=31, width=4,
                    textvariable=date_vars['day']).grid(row=row, column=5, padx=2)
        ttk.Label(parent, text="일").grid(row=row, column=6)

        # 시간
        date_vars['hour'] = tk.StringVar(value=str(datetime.datetime.now().hour))
        ttk.Spinbox(parent, from_=0, to=23, width=4,
                    textvariable=date_vars['hour']).grid(row=row, column=7, padx=2)
        ttk.Label(parent, text="시").grid(row=row, column=8)

        # 분
        date_vars['minute'] = tk.StringVar(value=str(datetime.datetime.now().minute))
        ttk.Spinbox(parent, from_=0, to=59, width=4,
                    textvariable=date_vars['minute']).grid(row=row, column=9, padx=2)
        ttk.Label(parent, text="분").grid(row=row, column=10)

        return date_vars

    def browse_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.file_path.set(filename)

    def set_current_time(self):
        now = datetime.datetime.now()
        for vars in [self.create_date_vars, self.modify_date_vars]:
            vars['year'].set(str(now.year))
            vars['month'].set(str(now.month))
            vars['day'].set(str(now.day))
            vars['hour'].set(str(now.hour))
            vars['minute'].set(str(now.minute))

    def get_datetime_from_vars(self, vars):
        try:
            year = int(vars['year'].get())
            month = int(vars['month'].get())
            day = int(vars['day'].get())
            hour = int(vars['hour'].get())
            minute = int(vars['minute'].get())

            # 날짜 유효성 검사
            if day > calendar.monthrange(year, month)[1]:
                raise ValueError("날짜가 해당 월의 마지막 날짜를 초과했습니다.")

            return datetime.datetime(year, month, day, hour, minute)
        except ValueError as e:
            raise ValueError("올바른 날짜를 입력해주세요: " + str(e))

    def modify_dates(self):
        if not self.file_path.get():
            messagebox.showerror("오류", "파일을 선택해주세요.")
            return

        try:
            created_date = self.get_datetime_from_vars(self.create_date_vars)
            modified_date = self.get_datetime_from_vars(self.modify_date_vars)

            file_path = self.file_path.get()

            # 파일 존재 여부 확인
            if not os.path.exists(file_path):
                raise FileNotFoundError("선택한 파일이 존재하지 않습니다.")

            # 날짜를 timestamp로 변환
            created_timestamp = created_date.timestamp()
            modified_timestamp = modified_date.timestamp()

            # Windows에서는 생성일자도 변경
            if os.name == 'nt':
                try:
                    from win32_setctime import setctime
                    setctime(file_path, created_timestamp)
                except ImportError:
                    messagebox.showwarning("경고",
                                           "생성일자를 변경하려면 'win32-setctime' 패키지가 필요합니다.\n"
                                           "명령 프롬프트에서 'pip install win32-setctime'를 실행하세요.")

            # 수정일자 변경
            os.utime(file_path, (modified_timestamp, modified_timestamp))

            messagebox.showinfo("완료", "파일 날짜가 성공적으로 변경되었습니다.")

        except ValueError as e:
            messagebox.showerror("오류", str(e))
        except Exception as e:
            messagebox.showerror("오류", f"파일 날짜 변경 중 오류가 발생했습니다:\n{str(e)}")


if __name__ == "__main__":
    app = FileDateModifier()
    app.mainloop()