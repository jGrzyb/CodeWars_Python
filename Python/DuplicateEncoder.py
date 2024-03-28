# https://www.codewars.com/kata/reviews/55249a95de8b4b5ae2000464/groups/6605d1b36298af00013ac03c

def duplicate_encode(word):
    s = ""
    for l in word:
        if word.lower().count(l.lower()) == 1:
            s += "("
        else:
            s += ")"
    return s