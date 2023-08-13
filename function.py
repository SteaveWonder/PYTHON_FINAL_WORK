import fileInteraction
import note
import ui

number = 6  


def add():
    note = ui.create_note(number)
    array = fileInteraction.read_file()
    for notes in array:
        if note.note.get_id(note) == note.note.get_id(notes):
            note.note.set_id(note)
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
            print(note.note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + note.note.get_id(notes))
        if text == 'date':
            logic = False
            if date in note.note.get_date(notes):
                print(note.note.map_note(notes))
    if logic == True:
        print('Sorry, no records...')


def id_edit_del_show(text):
    id = input('Insert id note: ')
    array = fileInteraction.read_file()
    logic = True
    for notes in array:
        if id == note.note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                note.note.set_title(notes, note.get_title())
                note.note.set_body(notes, note.get_body())
                note.note.set_date(notes)
                print('Note change...')
            if text == 'del':
                array.remove(notes)
                print('Note deleted...')
            if text == 'show':
                print(note.note.map_note(notes))
    if logic == True:
        print('Sorry, no records\n Please check id note')
    fileInteraction.write_file(array, 'a')