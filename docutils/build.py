# build.py
import PyInstaller.__main__
import os
import shutil

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
])