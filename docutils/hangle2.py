import win32com.client as win32
import os
from datetime import datetime


def create_advanced_hwp(output_path):
    """
    표, 스타일, 이미지 등이 포함된 HWP 파일을 생성하는 함수

    Args:
        output_path (str): 생성할 HWP 파일의 절대 경로
    """
    try:
        # 한글 실행
        hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
        hwp.XHwpWindows.Item(0).Visible = True

        # 새 문서 생성
        hwp.Run("FileNew")

        # 제목 추가 (글자 크기 키우고 가운데 정렬)
        hwp.HAction.GetDefault("CharShape", hwp.HParameterSet.HCharShape.HSet)
        hwp.HParameterSet.HCharShape.Height = 1800  # 글자 크기
        hwp.HAction.Execute("CharShape", hwp.HParameterSet.HCharShape.HSet)

        hwp.HAction.GetDefault("ParaShape", hwp.HParameterSet.HParaShape.HSet)
        # hwp.HParameterSet.HParaShape.Alignment = 1  # 가운데 정렬
        hwp.HAction.Execute("ParaShape", hwp.HParameterSet.HParaShape.HSet)

        hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
        hwp.HParameterSet.HInsertText.Text = "회사 업무 보고서"
        hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)
        hwp.HAction.Execute("BreakPara", hwp.HParameterSet.HInsertText.HSet)

        # 기본 글자 크기로 복귀
        hwp.HAction.GetDefault("CharShape", hwp.HParameterSet.HCharShape.HSet)
        hwp.HParameterSet.HCharShape.Height = 1000
        hwp.HAction.Execute("CharShape", hwp.HParameterSet.HCharShape.HSet)

        # 왼쪽 정렬로 복귀
        hwp.HAction.GetDefault("ParaShape", hwp.HParameterSet.HParaShape.HSet)
        # hwp.HParameterSet.HParaShape.Alignment = 0
        hwp.HAction.Execute("ParaShape", hwp.HParameterSet.HParaShape.HSet)

        # 날짜 추가
        current_date = datetime.now().strftime("%Y년 %m월 %d일")
        hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
        hwp.HParameterSet.HInsertText.Text = f"작성일: {current_date}"
        hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)
        hwp.HAction.Execute("BreakPara", hwp.HParameterSet.HInsertText.HSet)
        hwp.HAction.Execute("BreakPara", hwp.HParameterSet.HInsertText.HSet)

        # 표 생성
        hwp.Run("TableCreate", "4;3;1;8000;0;0;0")  # 4행 3열 표 생성

        # 표 선택
        hwp.Run("TableCellBlock")

        # 표 첫 행 배경색 지정 (연한 회색)
        hwp.Run("TableCellBlockCol")
        hwp.Run("CellFill", "ColorFill;RGB(220,220,220)")
        hwp.Run("TableSelectCell")  # 선택 해제

        # 표 내용 입력
        table_contents = [
            ["구분", "진행률", "담당자"],
            ["AI 챗봇", "75%", "홍길동"],
            ["데이터 분석", "90%", "김철수"],
            ["서버 구축", "85%", "이영희"]
        ]

        # 첫 셀로 이동
        hwp.Run("TableFirstCell")

        # 표 내용 입력
        for row in table_contents:
            for cell in row:
                hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
                hwp.HParameterSet.HInsertText.Text = cell
                hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)
                if cell != row[-1]:  # 행의 마지막 셀이 아니면
                    hwp.Run("TableRightCell")  # 오른쪽 셀로 이동
            if row != table_contents[-1]:  # 마지막 행이 아니면
                hwp.Run("TableDownCell")  # 아래 셀로 이동
                hwp.Run("TableFirstCell")  # 행의 첫 번째 셀로 이동

        # 표 끝으로 이동하고 줄바꿈
        hwp.Run("TableRightCell")
        hwp.Run("BreakPara")

        # 이미지 삽입 (샘플 이미지 경로를 실제 이미지 경로로 변경하세요)
        # image_path = "sampleimage.png"  # 실제 이미지 경로로 변경 필요
        # if os.path.exists(image_path):
        #     hwp.InsertPicture(image_path, True)

        # 파일 저장
        abs_path = os.path.abspath(output_path)
        hwp.SaveAs(abs_path)

        # 한글 종료
        hwp.Quit()

        print(f"HWP 파일이 성공적으로 생성되었습니다: {abs_path}")

    except Exception as e:
        print(f"에러 발생: {str(e)}")


def main():
    current_dir = os.getcwd()
    output_file = os.path.join(current_dir, "고급업무보고서.hwp")
    create_advanced_hwp(output_file)


if __name__ == "__main__":
    main()