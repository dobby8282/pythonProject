'''
Ex19-4-matplotlib4.py
'''
import wordcloud  # 워드 클라우드 생성을 위한 라이브러리
import matplotlib.pyplot as plt  # 시각화를 위한 matplotlib 라이브러리

# 단어와 가중치(빈도수) 설정
# 각 단어별로 표시될 크기를 결정하는 값을 딕셔너리로 저장
words = {
    'Python':10,  # Python이라는 단어는 가중치 10
    'Java':5,     # Java는 가중치 5
    'C':7,        # C는 가중치 7
    'C++':9,      # C++는 가중치 9
    'JSP':12      # JSP는 가중치 12
}

# WordCloud 객체 생성 (기본 설정 사용)
wc = wordcloud.WordCloud()

# 단어 가중치 데이터로부터 워드 클라우드 생성
# generate_from_frequencies(): 단어-빈도수 딕셔너리로부터 워드 클라우드 생성
cloud = wc.generate_from_frequencies(words)

# 그래프를 그리기 위한 Figure 객체 생성
plt.figure()

# 워드 클라우드를 이미지로 표시
# imshow(): 2D 데이터를 이미지로 표시
plt.imshow(cloud)

# 그래프 화면에 표시
plt.show()




