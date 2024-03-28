def solution(text, ending):
    return len(text) >= len(ending) and text[len(text)-len(ending):] == ending