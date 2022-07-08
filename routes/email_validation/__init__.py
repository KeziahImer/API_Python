from flask import Blueprint, request

blueprint = Blueprint('emailValidation', __name__, url_prefix='/emailValidation')

@blueprint.route('', methods=['POST'])
def emailValidation():
    data = request.args['email']
    i = 0
    cpt = 0
    for letter in data:
        if cpt == 0:
            cpt += 1
            if ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z')):
                break
            else:
                return False
        if cpt == 1:
            if letter == '@':
                cpt += 1
        if cpt == 2:
            if letter == '.':
                cpt += 1
            if letter == '@':
                return False
        if cpt == 3:
            if ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z')):
                break
            else:
                return False
        i += 1
    return True
