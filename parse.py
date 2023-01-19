
from sendmail import send
from rich import print

bot_signals = ["!b", "@b", "#b"]

introduction = f'''
Hello, Nice to meet you! I am a Python bot that automatically replies E-mails. 
If you do not want to see my messages, you can reply this message (or create a new message)
and send the following:

@b avoid messages

To view the list of commands, send:

@b commands

If you think you have wrongly recieved this message (you have typed in a valid command), 
contact Number Basher using the same email, but do not add bot identifiers. 
The bot identifiers are {', '.join(bot_signals)}. 
'''

avoid_messages = f'''
If you do not want to see my messages, you can do the following: 

1. Avoid including bot signals. 

If you include any of the following identifiers: {', '.join(bot_signals)}
Then the bot will automatically reply you. 

2. Check if you are in the whitelist. 

Reply this message (or create a new message) and send the following message:

@b whitelist remove

This will remove you from the whitelist, if you are in it. 

3. Add yourself to the blacklist. 

WARNING: This is not reversible. 
Reply this message (or create a new message) and send the following message:

@b blacklist add

Be warned that YOU WILL NOT BE ABLE TO GET ANY EMAILS FROM THIS BOT, 
EVEN IF YOU INCLUDE BOT IDENTIFIERS. 
'''

def parse(message):

    with open('white_list.txt') as f: white_list = f.read().strip().split('\n')
    with open('black_list.txt') as f: black_list = f.read().strip().split('\n')

    if message['from'] in black_list:
        print(f"[magenta][b]Ignored:[/][/] message is [b]black listed[/]; ")
        return False

    if message['from'] in white_list:
        print(f"[magenta][b]Will Consider:[/][/] message is [b]white listed[/]; ")

    elif all([_ not in message['subject'] + ' ' + message['content'] for _ in bot_signals]):
        print(f"[magenta][b]Ignored:[/][/] message does not contain bot signals; ")
        return False

    send(
        f"Re: {message['subject']}",
        introduction,
        message['from'],
    )

    return True
