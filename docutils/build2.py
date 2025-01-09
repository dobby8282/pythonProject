# build.py
import PyInstaller.__main__
import os
import shutil
import sys
import site

# sv_ttk 패키지 경로 찾기
sv_ttk_path = None
for path in site.getsitepackages():
    possible_path = os.path.join(path, 'sv_ttk')
    if os.path.exists(possible_path):
        sv_ttk_path = possible_path
        break

if not sv_ttk_path:
    print("Error: sv_ttk package not found")
    sys.exit(1)

# 빌드 전 dist 폴더가 있다면 삭제
if os.path.exists("dist"):
    shutil.rmtree("dist")

# 빌드 설정
PyInstaller.__main__.run([
    'logp.py',
    '--onefile',
    '--noconsole',
    '--name=logp',
    '--icon=NONE',
    '--clean',
    '--noconfirm',
    '--windowed',
    '--add-data', f'{sv_ttk_path}{os.pathsep}sv_ttk',  # sv_ttk 리소스 추가
    '--hidden-import', 'sv_ttk',  # sv_ttk 모듈
    '--hidden-import', 'tkinter',  # tkinter 모듈
    '--hidden-import', 'tkinter.ttk',  # tkinter.ttk 모듈
    '--hidden-import', 'tkinter.scrolledtext',  # scrolledtext 모듈
    '--hidden-import', 're',  # re 모듈
    '--hidden-import', 'threading',  # threading 모듈
    '--hidden-import', 'json',  # json 모듈
    '--collect-all', 'sv_ttk',  # sv_ttk의 모든 의존성 수집
])