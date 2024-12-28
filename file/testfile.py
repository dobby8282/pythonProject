import os
import shutil


def copy_files(source_path, dest_path):
    # temp 폴더가 없으면 생성
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # 모든 하위 폴더 탐색
    for root, dirs, files in os.walk(source_path):
        for file in files:
            # 원본 파일 경로
            src_file = os.path.join(root, file)
            # 대상 파일 경로 (파일명만 사용)
            dst_file = os.path.join(dest_path, file)
            # 파일 복사
            shutil.copy2(src_file, dst_file)


# 사용 예시
source_path = "//192.168.0.3/omen/work/mdf/mdsp-admin/src/main/resources/egovframework/mapper/mdsp/admin/stats"
dest_path = "temp"  # 대상 temp 폴더 지정
copy_files(source_path, dest_path)