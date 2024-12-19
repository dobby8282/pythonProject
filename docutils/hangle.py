import win32com.client as win32
import os
from datetime import datetime


def create_sample_hwp(output_path):
    """
    Win32com을 사용하여 샘플 HWP 파일을 생성하는 함수

    Args:
        output_path (str): 생성할 HWP 파일의 절대 경로
    """
    try:
        # 한글 실행
        hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
        hwp.XHwpWindows.Item(0).Visible = True  # 한글 창을 보이게 함

        # 새 문서 생성
        hwp.Run("FileNew")

        # 제목 추가
        hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
        hwp.HParameterSet.HInsertText.Text = "회사 업무 보고서"
        hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)

        # 줄바꿈
        hwp.HAction.Execute("BreakPara", hwp.HParameterSet.HInsertText.HSet)

        # 날짜 추가
        current_date = datetime.now().strftime("%Y년 %m월 %d일")
        hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
        hwp.HParameterSet.HInsertText.Text = f"작성일: {current_date}"
        hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)
        hwp.HAction.Execute("BreakPara", hwp.HParameterSet.HInsertText.HSet)

        # 내용 추가
        content = [
            "1. 프로젝트 현황",
            "   - AI 챗봇 개발 진행률: 75%",
            "   - 데이터 분석 플랫폼 구축: 90%",
            "",
            "2. 주간 업무 내용",
            "   - 신규 기능 개발",
            "   - 버그 수정 및 테스트",
            "   - 성능 최적화",
            "",
            "3. 향후 계획",
            "   - 사용자 테스트 진행",
            "   - 피드백 수집 및 반영",
            "   - 최종 배포 준비"
        ]

        for line in content:
            hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
            hwp.HParameterSet.HInsertText.Text = line
            hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)
            hwp.HAction.Execute("BreakPara", hwp.HParameterSet.HInsertText.HSet)

        # 파일 저장
        abs_path = os.path.abspath(output_path)
        hwp.SaveAs(abs_path)

        # 한글 종료
        hwp.Quit()

        print(f"HWP 파일이 성공적으로 생성되었습니다: {abs_path}")

    except Exception as e:
        print(f"에러 발생: {str(e)}")


def main():
    # 현재 작업 디렉토리에 파일 생성
    current_dir = os.getcwd()
    output_file = os.path.join(current_dir, "업무보고서.hwp")
    create_sample_hwp(output_file)


if __name__ == "__main__":
    main()