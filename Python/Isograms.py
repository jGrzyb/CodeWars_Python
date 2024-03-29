# https://www.codewars.com/kata/reviews/553a8421f3cc94444200007b/groups/6606e0edeab9090001a1e2af
import re

def is_isogram(string):
    for x in string:
        if len(re.findall(r""+x.lower()+r"", string.lower())) > 1:
            return False
    return True