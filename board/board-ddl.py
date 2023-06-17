'''
파일명: Ex06-sqlite-board-ddl.py
'''
import sqlite3
# 데이터베이스 연결
conn = sqlite3.connect('py_board.db')
cur = conn.cursor()

# 테이블 생성
cur.execute('''
   CREATE TABLE PY_BOARD (
     BOARD_ID INTEGER PRIMARY KEY,
     BOARD_TITLE TEXT DEFAULT NULL,
     BOARD_WRITER TEXT DEFAULT NULL,
     BOARD_CONTENT TEXT,
     BOARD_DATE TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
   );        
''')

conn.commit()

cur.close()
conn.close()