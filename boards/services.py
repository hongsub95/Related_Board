from .models import Board

from string import punctuation
from collections import defaultdict

"""
def remove_punctuation(text):
    text = text.encode('utf-8').decode('ascii', 'ignore')
    result = ""
    for t in text:
    	if t not in punctuation:
            result += t
    return result.strip()
"""
def FindRelatedBoard(board_id):
    all_board = Board.objects.all()
    board= Board.objects.filter(id=board_id).first()
    related_word_dict = defaultdict(int)
    board_word = board.candidate_realted_word()
    for word in board_word:
        related_word_dict[word] = 0
    related_board = []
    for b in all_board:
        b_word = b.candidate_realted_word()
        cnt = 0
        for w in b_word:
            if w not in related_word_dict.keys():
                continue
            else:
                related_word_dict[w]+=1
                if related_word_dict[w] >= 2:
                    continue
                else:
                    cnt+=1
        if cnt > 2:
            #첫번째 조건(두개 이상), 두번째 조건(빈번하게 사용), 세번째 조건(연관단어/연관되지않은단어)들을 각각 담아서 우선도를 비교할때 사용
            try:
                related_board.append((b.pk,cnt,cnt/len(b_word)-cnt)) 
            # 연관게시물의 연관단어 = 게시물의 연관단어 후보들
            except ZeroDivisionError:
                related_board.append((b.pk,cnt,cnt))
    return related_board