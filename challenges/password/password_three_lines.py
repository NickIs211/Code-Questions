params = {'weak': [0, 6, 8, 0, 0], 'medium': [
    0, 8, 10, 1, 2], 'strong': [1, 12, 16, 3, 2]}
type = input(
    "What's your wish, a strong, weak, or medium password? (If unsure, type 'help') ").lower()
print('This is a password generator! It gives you a password based on your choice,\n with a weak password having only lowercase letters,\n a medium password having lowercase letters, numbers, and a special character,\n and a strong password having upper/lower case, special characters, and numbers.' if type == 'help' else "Unrecognized strength! try again. " if type not in params else ''.join(
    __import__('random').sample(__import__('random').choices(__import__('string').ascii_lowercase if params[type][0] == 0 else __import__('string').ascii_letters, k=params[type][2]) + __import__('random').choices(__import__('string').digits, k=params[type][4]) + __import__('random').choices("!@#$%^&*+-", k=params[type][3]), params[type][2] + params[type][3] + params[type][4])))
