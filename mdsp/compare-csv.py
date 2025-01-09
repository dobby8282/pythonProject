import pandas as pd
import csv

def check_problematic_lines(filename):
    problematic_lines = []
    try:
        with open(filename, 'r', encoding='euc-kr') as f:
            # CSV 리더 사용하여 더 정확한 파싱
            csvreader = csv.reader(f)
            header = next(csvreader)
            expected_fields = len(header)
            print(f"\n=== {filename} 파일 검사 ===")
            print(f"헤더 필드 수: {expected_fields}")

            for i, fields in enumerate(csvreader, start=2):
                if len(fields) != expected_fields:
                    problematic_lines.append({
                        'line_number': i,
                        'expected': expected_fields,
                        'actual': len(fields),
                        'content': ','.join(fields)
                    })

        if problematic_lines:
            print("\n문제가 있는 라인:")
            for problem in problematic_lines:
                print(f"줄 번호: {problem['line_number']}")
                print(f"예상 필드 수: {problem['expected']}")
                print(f"실제 필드 수: {problem['actual']}")
                print(f"내용: {problem['content']}")
                print("---")
        else:
            print("문제가 있는 라인이 없습니다.")

    except Exception as e:
        print(f"파일 검사 중 에러 발생: {str(e)}")

    return problematic_lines

def compare_urls():
    try:
        # 먼저 각 파일의 문제 있는 라인 체크
        dev_problems = check_problematic_lines('TB_PT410_DEV.csv')
        prod_problems = check_problematic_lines('TB_PT410_PROD.csv')

        if dev_problems or prod_problems:
            print("\n위의 문제 라인들은 건너뛰고 분석을 진행합니다.")

        # CSV 파일을 좀 더 유연하게 읽기 위한 옵션 추가
        csv_options = {
            'encoding': 'euc-kr',  # 실제 파일 인코딩으로 수정
            'on_bad_lines': 'skip',  # 문제가 있는 라인은 건너뛰기
            'low_memory': False,  # 대용량 파일 처리를 위한 옵션
            'quoting': csv.QUOTE_MINIMAL,  # 따옴표 처리 옵션 추가
            'escapechar': '\\',  # 이스케이프 문자 지정
        }

        # CSV 파일 읽기
        dev_df = pd.read_csv('TB_PT410_DEV.csv', **csv_options)
        prod_df = pd.read_csv('TB_PT410_PROD.csv', **csv_options)

        # 데이터 확인 및 기본 정보 출력
        print("\n=== 데이터 구조 확인 ===")
        print(f"DEV 파일 전체 레코드 수: {len(dev_df)}")
        print(f"PROD 파일 전체 레코드 수: {len(prod_df)}")
        print("\nDEV 파일 컬럼:", dev_df.columns.tolist())
        print("PROD 파일 컬럼:", prod_df.columns.tolist())

        # URL 컬럼이 있는지 확인
        if 'PRGRM_URL_ADDR' not in dev_df.columns or 'PRGRM_URL_ADDR' not in prod_df.columns:
            print("Error: PRGRM_URL_ADDR 컬럼을 찾을 수 없습니다.")
            return

        # URL 컬럼만 추출하여 set으로 변환 (중복 제거)
        dev_urls = set(dev_df['PRGRM_URL_ADDR'].dropna())
        prod_urls = set(prod_df['PRGRM_URL_ADDR'].dropna())

        # DEV에만 있는 URL 찾기
        only_in_dev = dev_urls - prod_urls

        # PROD에만 있는 URL 찾기
        only_in_prod = prod_urls - dev_urls

        # 결과 출력
        print('\n=== DEV 환경에만 있는 URL ===')
        for url in only_in_dev:
            try:
                dev_info = dev_df[dev_df['PRGRM_URL_ADDR'] == url][['PRGRM_NM', 'PRGRM_URL_ADDR']].iloc[0]
                print(f"URL: {url}")
                # print(f"프로그램명: {dev_info['PRGRM_NM']}")
                # print("---")
            except Exception as e:
                print(f"URL: {url} (정보 출력 중 오류 발생)")
                print("---")

        print('\n=== PROD 환경에만 있는 URL ===')
        for url in only_in_prod:
            try:
                prod_info = prod_df[prod_df['PRGRM_URL_ADDR'] == url][['PRGRM_NM', 'PRGRM_URL_ADDR']].iloc[0]
                print(f"URL: {url}")
                # print(f"프로그램명: {prod_info['PRGRM_NM']}")
                # print("---")
            except Exception as e:
                print(f"URL: {url} (정보 출력 중 오류 발생)")
                print("---")

        # 통계 출력
        print('\n=== 통계 ===')
        print(f'DEV 환경 전체 URL 수: {len(dev_urls)}')
        print(f'PROD 환경 전체 URL 수: {len(prod_urls)}')
        print(f'DEV에만 있는 URL 수: {len(only_in_dev)}')
        print(f'PROD에만 있는 URL 수: {len(only_in_prod)}')

    except Exception as e:
        print(f"에러 발생: {str(e)}")
        print("\n파일 내용을 확인해주세요:")
        print("1. CSV 파일이 올바른 형식인지")
        print("2. 컬럼 구분자가 쉼표(,)인지")
        print("3. 파일 경로가 올바른지")

if __name__ == '__main__':
    compare_urls()