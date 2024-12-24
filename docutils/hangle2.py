import platform
import matplotlib.pyplot as plt
from matplotlib import rc
import win32com.client as win32
import os

# (1) 한글 폰트 설정 및 그래프 생성
if platform.system() == 'Windows':
    font_name = 'Malgun Gothic'
    rc('font', family=font_name)

plt.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title('샘플 데이터 그래프', fontsize=14)
plt.xlabel('X축 (개)', fontsize=12)
plt.ylabel('Y축 (값)', fontsize=12)
plt.grid(True)

chart_filename = os.path.join(os.getcwd(), 'chart.png')
plt.savefig(chart_filename, dpi=150, bbox_inches='tight')
plt.close()

# (2) 한글 OLE 객체 연결
hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.XHwpWindows.Item(0).Visible = True

# (3) 새 문서 생성
hwp.Run("FileNew")

# (4) 텍스트 삽입
hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
hwp.HParameterSet.HInsertText.Text = "이 문서는 파이썬을 통해 자동으로 생성된 한글 문서입니다.\n아래는 파이썬으로 만든 그래프 이미지입니다.\n\n"
hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)

# (5) 그림 삽입
set = hwp.HParameterSet # 파라미터 세트 가져오기
act = hwp.HAction      # 액션 가져오기

act.GetDefault("InsertPicture", set.HInsertPicture.HSet)    # 그림 삽입 액션의 파라미터를 기본값으로 설정
set.HInsertPicture.FileName = chart_filename    # 삽입할 그림 파일의 경로를 지정
set.HInsertPicture.Width = 100      # 그림의 너비를 100mm로 설정
set.HInsertPicture.Height = 80      # 그림의 높이를 80mm로 설정
act.Execute("InsertPicture", set.HInsertPicture.HSet)  # 설정한 파라미터로 그림 삽입 액션 실행

# (6) 문서 저장
save_path = os.path.join(os.getcwd(), "자동_생성_문서.hwp")
hwp.SaveAs(save_path)

# (7) 한글 종료
hwp.Quit()