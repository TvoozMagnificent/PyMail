
from rich import print
from parse import parse
from readmail import read
from deletemail import delete
from getfolders import folders

print('\n'*20)

for folder in {*folders()[:-1]}:

    print(f"\nSearching folder [cyan][b]{folder}[/][/]: ")
    try: messages = read(folder)
    except Exception as e: print(f"Exception raised: [red][b]{e}[/][/]; "); continue

    if messages == []: print(f"No messages in folder [cyan][b]{folder}[/][/]; "); continue

    print(f"Found {len(messages)} message(s) in folder [cyan][b]{folder}[/][/]: ")

    for index, message in enumerate(messages):

        print(f"Parsing message {index+1} / {len(messages)}: ")

        print(f"[yellow][b]Parsing message: [/][/]")
        should_delete = parse(message)
        print(f"[yellow][b]Done! [/][/]")

        if should_delete:
            print(f"[yellow]Deleting message: [/]")
            delete(message['id'], folder)
            print(f"[yellow]Done! [/]")

print('\n\n\n')

# bruh