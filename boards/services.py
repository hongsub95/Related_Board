from .models import Board

from string import punctuation
from collections import defaultdict
from copy import deepcopy

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
        copy_dict = deepcopy(related_word_dict)
        cnt = 0
        related_word_cnt = 0
        for w in b_word:
            if w not in copy_dict.keys():
                continue
            else:
                copy_dict[w]+=1
                related_word_cnt+=1
                if copy_dict[w] >= 2:
                    continue
                else:
                    cnt+=1
        # 첫번째 조건(두개 이상)
        if cnt > 2:
            #연관게시물pk, 두번째 조건(연관단어 빈도수), 세번째 조건(연관단어빈도수/연관될 수 있는 후보단어들)들을 각각 담아서 우선도를 비교할때 사용
            related_board.append((b.pk,related_word_cnt,related_word_cnt/len(b_word))) 
            
    return related_board.sort(key=lambda x:(x[1],x[2]),reverse=True) #sort함수를 이용하여 연관도가 높은순으로 내림차순