from pyhwp import hwp
hwp_file = hwp.File('example.hwp')

# 문서 읽기
for page in hwp_file.iter_pages():
    for paragraph in page.paragraphs:
        print(paragraph.text)

# 새 문서 만들기
doc = hwp.Document()
doc.add_paragraph("안녕하세요")
doc.save("new_document.hwp")