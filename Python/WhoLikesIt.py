# https://www.codewars.com/kata/reviews/564425cc55d0e45b8c000087/groups/5a0a9ac705414a4e9f000090
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return str(names[0]) + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others like this"