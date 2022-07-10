from flask import Blueprint, request
import json

blueprint = Blueprint('longestCommonStreak', __name__, url_prefix='/longestCommonStreak')

def compare(first, second, result):
    name = first + ' and ' + second
    i = 0
    j = 0
    max = 0
    lcs = ''

    while i < len(first):
        while j < len(second):
            if first[i] == second[j]:
                new_lcs = ''
                new_max = 0
                cpy1 = i
                cpy2 = j
                while cpy1 < len(first) and cpy2 < len(second) and first[cpy1] == second[cpy2]:
                    new_lcs += first[cpy1]
                    cpy1 += 1
                    cpy2 += 1
                    new_max += 1
                if new_max > max:
                    max = new_max
                    lcs = new_lcs
            j += 1
        i += 1
        j = 0

    result[name]=lcs
    return result

@blueprint.route('', methods=['POST'])
def longestCommonStreak():
    data = request.data.decode("utf-8") 
    list = data.split()
    result = {}
    cpt = 1
    for word in list:
        new_cpt = cpt
        while new_cpt < len(list):
            result = compare(word, list[new_cpt], result)
            new_cpt += 1
        cpt += 1
    return json.dumps(result) 
