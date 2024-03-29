# https://www.codewars.com/kata/reviews/5a42028f5c697bcc15001419/groups/6606deaeacfeff00019d3884
import re

def nba_cup(result_sheet, to_find):
    if to_find == '':
        return ''
    if to_find[0] == " ":
        return to_find + ":This team didn't play!"
    all_matches = result_sheet.split(',')
    matching = []
    won = 0
    lost = 0
    draw = 0
    total_score = 0
    total_conceded = 0
    for x in all_matches:
        if len(re.findall(r"\b" + to_find + r"\b", x)) != 0:
            matching.append(x)
    if len(matching) == 0:
        return to_find + ":This team didn't play!"
    for x in matching:
        if len(re.findall(r"\b\d+\.\d+", x)) != 0:
            return "Error(float number):" + x
        
        numbers = re.findall(r"\b\d+\b", x)
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])

        if numbers[0] == numbers[1]:
            draw += 1
            total_conceded += numbers[0]
            total_score += numbers[0]

        if x.find(to_find) == 0:
            total_score += numbers[0]
            total_conceded += numbers[1]
            if numbers[0] > numbers[1]:
                won += 1
            else:
                lost += 1
        else:
            total_score += numbers[1]
            total_conceded += numbers[0]
            if numbers[0] < numbers[1]:
                won += 1
            else:
                lost += 1
    mark = won * 3 + draw
    return to_find + \
        ":W=" + str(won) + \
        ";D=" + str(draw) + \
        ";L=" + str(lost) + \
        ";Scored=" + str(total_score) + \
        ";Conceded=" + str(total_conceded) + \
        ";Points=" + str(mark)