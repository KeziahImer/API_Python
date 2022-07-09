from flask import Blueprint, request

blueprint = Blueprint('emailValidation', __name__, url_prefix='/emailValidation')

letters = 'abcdefghijklmnopqrstuvwxyz'

def is_letter(char):
    for i in letters:
        if char == i:
            return 1
    return 0


@blueprint.route('', methods=['POST'])
def emailValidation():
    email = request.args['email']
    step = 0
    for char in email:
        if step == 0:
            if char == '@' or char == '.':
                return {'result': 'False'}
            else:
                step = 1
        elif step == 1:
            if char == '.' and prev == '.':
                return {'result': 'False'}
            elif char == '@' and prev == '.':
                return {'result': 'False'}
            elif char == '@':
                step = 2
        elif step == 2:
            if is_letter(char) == 1:
                step = 2
            elif char == '.':
                step = 3
            else:
                return {'result': 'False'}
        else:
            if is_letter(char) != 1:
                return {'result': 'False'}
        prev = char
    return {'result': 'True'}
