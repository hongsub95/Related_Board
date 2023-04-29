import nltk
from konlpy.tag import Okt
from collections import Counter

from django.db import models
from .services import remove_punctuation

class Board(models.Model):
    title = models.CharField(max_length=20,verbose_name="제목")
    content = models.TextField(max_length=200,verbose_name="내용")
    created = models.DateTimeField(auto_now_add=True,verbose_name='등록날짜')
    updated = models.DateTimeField(auto_now=True,verbose_name='수정날짜')
    
    class Meta:
        ordering = ["-created"]

    def cand_realted_word(self):
        okt = Okt()
        korean_nouns = okt.nouns(self.content)
        english_nouns = 
        okt.po
        
