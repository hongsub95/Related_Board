from string import punctuation

def remove_punctuation(text):
    text = text.encode('utf-8').decode('ascii', 'ignore')
    result = ""
    for t in text:
    	if t not in punctuation:
            result += t
    return result.strip()