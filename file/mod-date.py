import os
import datetime
import time
from pathlib import Path


def modify_file_dates(file_path, created_date=None, modified_date=None):
    """
    파일의 생성일자와 수정일자를 변경하는 함수

    Parameters:
    file_path (str): 대상 파일의 경로
    created_date (datetime): 변경할 생성일자 (선택사항)
    modified_date (datetime): 변경할 수정일자 (선택사항)
    """
    # 파일 존재 여부 확인
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")

    # 현재 시간을 기본값으로 사용
    now = datetime.datetime.now()
    created_date = created_date or now
    modified_date = modified_date or now

    # 날짜를 timestamp로 변환
    created_timestamp = created_date.timestamp()
    modified_timestamp = modified_date.timestamp()

    # Windows에서는 생성일자 변경을 위해 Path 객체 사용
    if os.name == 'nt':  # Windows
        winfile = Path(file_path)
        winfile.touch(exist_ok=True)
        stats = winfile.stat()

        os.utime(file_path, (modified_timestamp, modified_timestamp))
        # Windows에서만 생성일자 변경 가능
        try:
            from win32_setctime import setctime
            setctime(file_path, created_timestamp)
        except ImportError:
            print("생성일자를 변경하려면 'win32-setctime' 패키지를 설치하세요.")
            print("pip install win32-setctime")

    else:  # Unix/Linux/Mac
        # Unix 시스템에서는 생성일자를 직접 변경할 수 없음
        os.utime(file_path, (modified_timestamp, modified_timestamp))
        print("Unix 시스템에서는 생성일자를 직접 변경할 수 없습니다.")


# 사용 예시
if __name__ == "__main__":
    # 테스트할 파일 경로
    test_file = "2. (개인)정보보호 자율점검(개인용)_혜택알리미 서비스(김태호)_241122.hwp"

    # 파일이 없으면 생성
    if not os.path.exists(test_file):
        with open(test_file, 'w') as f:
            f.write("테스트 파일입니다.")

    # 원하는 날짜 설정
    new_created_date = datetime.datetime(2024, 11, 22, 15, 32, 28)
    new_modified_date = datetime.datetime(2024, 11, 22, 16, 12, 24)

    # 파일 날짜 수정
    modify_file_dates(test_file, new_created_date, new_modified_date)