import note


def create_note(number):
    title = check_len_text_input(
        input('Insert Name of note: '), number)
    body = check_len_text_input(
        input('Insert Description of note: '), number)
    return note.Note(title=title, body=body)


def menu():
    print("\nThis is NoteApp. Functions:\n\n1 - Output all notes\n2 - Add notes\n3 - Delete notes\n4 - Edit notes\n5 - choose notes by the date\n6 - Show notes with it ID\n7 - Exit\n\nInsert function number: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Text should be bigger than {n} symbols\n')
        text = input('Insert text: ')
    else:
        return text


def goodbuy():
    print("Thank you! Goodbye!")