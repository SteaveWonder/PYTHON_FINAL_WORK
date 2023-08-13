import fileInteraction
import note
import ui

number = 6  


def add():
    note = ui.create_note(number)
    array = fileInteraction.read_file()
    for notes in array:
        if note.Note.get_id(note) == note.Note.get_id(notes):
            note.Note.set_id(note)
    array.append(note)
    fileInteraction.write_file(array, 'a')
    print('Note add...')


def show(text):
    logic = True
    array = fileInteraction.read_file()
    if text == 'date':
        date = input('Insert date in format dd.mm.yy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in note.Note.get_date(notes):
                print(note.Note.map_note(notes))
    if logic == True:
        print('Sorry, no records...')


def id_edit_del_show(text):
    id = input('Insert id note: ')
    array = fileInteraction.read_file()
    logic = True
    for notes in array:
        if id == note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                note.Note.set_title(notes, note.get_title())
                note.Note.set_body(notes, note.get_body())
                note.Note.set_date(notes)
                print('Note change...')
            if text == 'del':
                array.remove(notes)
                print('Note deleted...')
            if text == 'show':
                print(note.Note.map_note(notes))
    if logic == True:
        print('Sorry, no records\n Please check id note')
    fileInteraction.write_file(array, 'a')