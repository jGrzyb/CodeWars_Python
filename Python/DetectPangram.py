def is_pangram(s):
    all_leters = list("qwertyuiopasdfghjklzxcvbnm")
    for l in s:
        if all_leters.count(l.lower()) > 0:
            all_leters.remove(l.lower())
    return len(all_leters) == 0