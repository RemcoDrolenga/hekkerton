import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!help':
        return '```Usable Commands \n 1. !vote```'
    
    if message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == '!vote':
        return '`Lets your vote`'
    
    return 'If u need help with the commands please use !help'

