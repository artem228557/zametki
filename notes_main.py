from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import json

notes = {
    'Добро пожаловать!': {
        'Текст' : 'Это самое лучшее приложение для заметок в мире!',
        'Теги' :["Добро", 'Инструкция']
    }
    ,
    'Про космос!': {
        'Текст' : 'В космосе только вауккуми нет кислорода. ',
        'Теги' :["Вауккум", 'Описание']
        }
}
# with  open("notes_data.json", "w", encoding='utf-8')   as file:
#      json.dump(notes, file, ensure_ascii=False, indent=4)

app = QApplication([])
ui = uic.loadUi("zametki.html")
ui.show()

def show_note():
    key = ui.list_notes.selectedItems()[0].text()
    print(key)
    ui.field_text.setText(notes [key] ['Текст'])
    ui.list_tag.clear()
    ui.list_tag.addItems(notes[key]['Теги'])



def add_note():
    note_name, ok = QInputDialog.getText(ui, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != "":
        notes[note_name] = {"Текст":"","Теги":[]}
        ui.list_notes.addItem(note_name)
        ui.list_tag.addItems(notes[note_name]['Теги'])
        print(notes)

def save_note():
    if ui.list_notes.selectedItems():
        key = ui.list_notes.selectedItems()[0].text()
        notes[key]["Текст"] = ui.field_text.toPlainText()
        with open('notes_data.json','w',encoding='utf-8') as file:
            json.dump(notes,file,ensure_ascii=False,indent=4)
        print("Заметка для сохранения не выбрана!")

def del_note():
    if ui.list_notes.selectedItems():
        key = ui.list_notes.selectedItems()[0].text()
        del notes[key]
        ui.list_notes.clear()
        ui.list_tag.clear()
        ui.field_text.clear()
        ui.list_notes.addItems(notes)
        with open ("notes_data.json","w",encoding='utf-8')as file:
            json.dump(notes,file,ensure_ascii=False,indent=4)
    else:    
        print("Заметка для сохранения не выбрана!")





def add_tag():
    if ui.list_notes.selectedItems():
        key = ui.list_notes.selectedItems()[0].text()
        tag = ui.field_tag.text()
        if not tag in notes[key]["Теги"]:
            notes[key]["Теги"].append(tag)
            ui.list_tag.addItem(tag)
            ui.field_tag.clear()
        with open("notes_data.json","w", encoding='utf-8') as file:
            json.dump(notes, file,sort_keys=True, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print("Заметка для добавления тега не выбрана!")


def del_tag():
    if ui.list_notes.selectedItems()[0].text():
        key = ui.list_notes.selectedItems()[0].text()
        tag = ui.list_tag.selectedItems()[0].text()
        notes[key]["Теги"].remove(tag)
        ui.list_tag.clear()
        ui.list_tag.addItems(notes[key]["Теги"])
        with open("notes_data.json","w", encoding='utf-8') as file:
            json.dump(notes, file,sort_keys=True, ensure_ascii=False, indent=4)
    else:
        print('Тег для удаления не выбран!')

def search_tag():
    print(ui.button_tag_search.text())
    tag = ui.field_tag.text()
    if ui.button_tag_search.text()== 'Искать' and tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['Теги']:
                notes_filtered[note]=notes[note]
        ui.button_tag_search.setText('Сбросить поиск')
        ui.list_notes.clear()
        ui.list_tag.clear()
        ui.list_notes.addItems(notes_filtered)
        print(ui.button_tag_search.text())
    elif ui.button_tag_search.text() == 'Сбросить поиск':
        ui.field_tag.clear()
        ui.list_notes.clear()
        ui.list_tag.clear()
        ui.list_notes.addItems(notes)
        ui.button_tag_search.setText("Искать")
        print(ui.button_tag_search.text())
    else:
        pass






ui.button_note_create.clicked.connect(add_note)
ui.button_note_save.clicked.connect(save_note)
ui.button_note_del.clicked.connect(del_note)
ui.list_notes.itemClicked.connect(show_note)
ui.button_tag_add.clicked.connect(add_tag)
ui.button_teg_del.clicked.connect(del_tag)
ui.button_tag_search.clicked.connect(search_tag)














with open('notes_data.json', "r", encoding='utf-8')as file:
    notes = json.load(file)









ui.list_notes.addItems(notes)
app.exec_()