import win32com.client

# 한글 오토메이션 객체 생성
hwp = win32com.client.Dispatch("HWPFrame.HwpObject.1")

# 새 문서 생성
hwp.XHwpDocuments.Add(True)

# 표 생성 설정
hwp.HAction.GetDefault("TableCreate", hwp.HParameterSet.HTableCreation.HSet)
hwp.HParameterSet.HTableCreation.Rows = 3  # 행 개수
hwp.HParameterSet.HTableCreation.Cols = 4  # 열 개수
hwp.HParameterSet.HTableCreation.WidthValue = 150  # 표 너비
hwp.HParameterSet.HTableCreation.HeightValue = 30  # 표 높이

# 표 생성 실행
hwp.HAction.Execute("TableCreate", hwp.HParameterSet.HTableCreation.HSet)

# 표 내용 입력
cell_data = [
    ["헤더1", "헤더2", "헤더3", "헤더4"],
    ["데이터1", "데이터2", "데이터3", "데이터4"],
    ["데이터5", "데이터6", "데이터7", "데이터8"]
]

# 각 셀에 데이터 삽입
for row_idx, row in enumerate(cell_data):
    for col_idx, text in enumerate(row):
        hwp.HAction.Run("TableLowerCell")  # 현재 셀로 이동
        hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
        hwp.HParameterSet.HInsertText.Text = text  # 텍스트 설정
        hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)

# 문서 저장
hwp.XHwpDocuments.Item(0).SaveAs("C:\\Users\\taeho\\Desktop\\TableExample.hwp", "HWP", "")

# 한글 종료
hwp.Quit()
