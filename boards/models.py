import nltk
import re
from konlpy.tag import Okt
from collections import Counter

from django.db import models

from .services import remove_punctuation


class Board(models.Model):
    title = models.CharField(max_length=20,verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created = models.DateTimeField(auto_now_add=True,verbose_name='등록날짜')
    updated = models.DateTimeField(auto_now=True,verbose_name='수정날짜')
    
    class Meta:
        ordering = ["-created"]

    def candidate_realted_word(self):
        nltk.download("all")
        cleaned_content = remove_punctuation(self.content).lower() # remove_punctutation 함수를 이용하여 한글을 제거한 영어만 분리
        word_tokens = nltk.word_tokenize(cleaned_content)
        tokens_pos = nltk.pos_tag(word_tokens)
        english_nouns = []
        for word, pos in tokens_pos:
            if 'NN' in pos:
                english_nouns.append(word) #영어 단어 추출
        okt = Okt()
        related_word_list = [] # 연관되는 단어 보관 리스트
        korean_nouns = okt.nouns(self.content)  # 한국 단어 추출 
        korean_nouns = [korean_noun for korean_noun in korean_nouns if len(korean_noun) > 1 ] # 한글자는 빼기
        korean_cnt = Counter(korean_nouns)
        len_korean = len(korean_nouns)
        english_cnt = Counter(english_nouns)
        len_english = len(english_nouns)
        
        for key,val in korean_cnt.items():  # 한국 단어 연관될 수 있는 조건중 만족하는 단어 추출
            if val/len_korean <= 0.4:
                related_word_list.append(key)
            else:
                continue
        
        for key,val in english_cnt.items(): # 영어 단어 연관될 수 있는 조건중 만족하는 단어 추출
            if val/len_english <= 0.4: # 40% 이하는 리스트에 담기
                related_word_list.append(key)
            else: 
                continue
        
        return related_word_list
        
