'''
path
'''

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime


def create_directory_pdf(start_path, output_pdf=None):
    """
    지정된 경로의 디렉토리 구조를 PDF 파일로 생성합니다.
    Java, JSP, XML, Properties 파일만 포함합니다.

    Args:
        start_path (str): 검색할 디렉토리 경로
        output_pdf (str): 생성할 PDF 파일 경로 (기본값: 시작 경로에 생성)
    """
    # 필터링할 확장자 목록
    ALLOWED_EXTENSIONS = {'.java', '.jsp', '.xml', '.properties'}

    if not os.path.exists(start_path):
        print(f"Error: 경로를 찾을 수 없습니다 - {start_path}")
        return

    # PDF 파일 이름 설정
    if output_pdf is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_pdf = os.path.join(os.path.dirname(start_path), f'source_structure_{timestamp}.pdf')

    # PDF 문서 생성 (가로 방향으로 변경)
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=landscape(A4),
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    elements = []

    # 스타일 설정
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30
    )
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=9,
        leading=12
    )
    path_style = ParagraphStyle(
        'PathStyle',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        textColor=colors.blue
    )

    # 제목과 기본 경로 추가
    title = f"소스 파일 구조 분석"
    elements.append(Paragraph(title, title_style))
    elements.append(Paragraph(f"기준 경로: {start_path}", path_style))
    elements.append(Spacer(1, 20))

    # 파일 타입별 카운터 초기화
    file_counts = {
        'java': 0,
        'jsp': 0,
        'xml': 0,
        'properties': 0
    }

    def get_directory_structure(directory, prefix=""):
        """재귀적으로 디렉토리 구조를 문자열로 반환"""
        structure = []
        try:
            entries = sorted(os.scandir(directory), key=lambda e: (not e.is_dir(), e.name.lower()))

            for entry in entries:
                name = entry.name
                full_path = entry.path
                # 숨김 파일과 특정 디렉토리 제외
                if name.startswith('.') or name in ['__pycache__', 'node_modules', 'target', 'build']:
                    continue

                if entry.is_dir():
                    # 하위 디렉토리의 구조를 가져옴
                    sub_structure = get_directory_structure(full_path, prefix + "│   ")
                    # 하위 구조에 파일이 있을 경우에만 디렉토리를 표시
                    if sub_structure:
                        relative_path = os.path.relpath(full_path, start_path)
                        structure.append(f"{prefix}├── 📁 {relative_path}")
                        structure.extend(sub_structure)
                else:
                    # 파일 확장자 확인
                    _, ext = os.path.splitext(name)
                    if ext.lower() in ALLOWED_EXTENSIONS:
                        relative_path = os.path.relpath(full_path, start_path)
                        structure.append(f"{prefix}├── 📄 {relative_path}")
                        # 파일 카운트 증가
                        ext_type = ext[1:].lower()  # 점(.)을 제외한 확장자
                        if ext_type in file_counts:
                            file_counts[ext_type] += 1

        except PermissionError:
            structure.append(f"{prefix}├── [접근 권한 없음]")
        except Exception as e:
            structure.append(f"{prefix}├── [Error: {str(e)}]")

        return structure

    # 디렉토리 구조 가져오기
    structure = get_directory_structure(start_path)

    # 파일 타입 요약 추가
    summary = ["파일 타입 요약:"]
    total_files = 0
    for ext, count in file_counts.items():
        summary.append(f"- {ext.upper()} 파일: {count:,}개")
        total_files += count
    summary.append(f"- 총 파일 수: {total_files:,}개")

    # 요약 정보를 PDF에 추가
    for line in summary:
        elements.append(Paragraph(line, normal_style))
    elements.append(Spacer(1, 20))

    # 구조를 PDF에 추가
    for line in structure:
        elements.append(Paragraph(line, normal_style))
        elements.append(Spacer(1, 1))

    # PDF 생성
    try:
        doc.build(elements)
        print(f"\nPDF 파일이 생성되었습니다: {output_pdf}")

        # 결과 요약 출력
        print("\n파일 검색 결과:")
        for ext, count in file_counts.items():
            print(f"{ext.upper()} 파일: {count:,}개")
        print(f"총 파일 수: {total_files:,}개")

    except Exception as e:
        print(f"PDF 생성 중 오류가 발생했습니다: {str(e)}")


# 사용 예시
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("디렉토리 구조를 스캔할 경로를 입력하세요: ")

    create_directory_pdf(path)