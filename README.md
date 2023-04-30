# Related_Board

## 목적 및 준비물
목적 :연관게시물 만들어보기\
언어 : Python, Django\
DB : sqlite

## 원리
nltk, konlpy 모듈을 이용하여 한글, 영어 단어들을 가져와 다른 게시물과 단어들과 얼마나 연관되었는지 확인하여 연관 게시물인지 확인

## Start Project
게시글 스키마 : 제목, 내용, 작성날짜\
konlpy : text의 단어나 어절등 나눠주는 모듈\
nltk : konlpy와 비슷하나 konlpy는 영어를 인식하지 않아 따로 했음\
### 게시글 구현
목록 : 게시글 쿼리셋을 가져와 목록 구현\
생성 : 게시글 폼을 만들어 유효하면 생성\
삭제 : 게시글 삭제
### 연관 게시글
각 게시글을 단어들로 잘라서 같은 단어 2개 이상 있으면 연관되었다고 인지하여 연관게시글로 인식(단, 내용중의 특정단어가 많이 차지하면 그 단어는 연관단어를 취급하지 않음)\
많이 나타날수록, 내용중 연관단어의 비중이 많으면 우선도를 
