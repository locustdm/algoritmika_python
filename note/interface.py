from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QListWidget, QPushButton, QGroupBox, QLineEdit

# ----СОЗДАНИЕ ПРИЛОЖЕНИЯ С ОДНИМ ОКНОМ----
#конструктор, создающий объект типа приложение
app = QApplication([]) 
#конструктор, создающий объект типа окно
main_win = QWidget()
#сделать окно видимым
main_win.show()
#подпись окошка
main_win.setWindowTitle('Умные заметки')

# ----ГЛАВНЫЕ НАПРАВЛЯЮЩИЕ----
#Горизонтальная - самая главная
main_h_line = QHBoxLayout() #horizonal
main_win.setLayout(main_h_line) #прикрепить к окну main_win

#Две вертикальные главные
v_line_note = QVBoxLayout()
v_line_interface = QVBoxLayout()
main_h_line.addLayout(v_line_note)
main_h_line.addLayout(v_line_interface)

# ----ВИДЖЕТЫ ЛЕВОЙ НАПРАВЛЯЮЩЕЙ----
#больше окошко для печатания
w_note = QTextEdit() 
v_line_note.addWidget(w_note) #добавить к левой направляющей виджет

# ----ВИДЖЕТЫ И ПОДНАПРАВЛЯЮЩИЕ ПРАВОЙ НАПРАВЛЯЮЩЕЙ----

# ----группа управления заметками----
layout_note = QVBoxLayout() 
group_note = QGroupBox("Список заметок:") 

l_notes = QListWidget() #список заметок

b_create_note = QPushButton("Создать заметку") 
b_del_note = QPushButton("Удалить заметку") 
b_save_note = QPushButton("Сохранить заметку") 

layout_note.addWidget(l_notes)
layout_note.addWidget(b_create_note)
layout_note.addWidget(b_del_note)
layout_note.addWidget(b_save_note)

group_note.setLayout(layout_note)

v_line_interface.addWidget(group_note)


#----группа управления тегами---
layout_tag = QVBoxLayout()
group_tag = QGroupBox("Список тегов:")

l_tags =  QListWidget() #список тегов

ed_tag = QLineEdit("Введите тег")
b_create_tag = QPushButton("Дабавить к заметке")
b_unlock_tag = QPushButton("Открепить от заметки")
b_find_tag = QPushButton("Искать заметки по тегу")

layout_tag.addWidget(l_tags)
layout_tag.addWidget(ed_tag)
layout_tag.addWidget(b_create_tag)
layout_tag.addWidget(b_unlock_tag)
layout_tag.addWidget(b_find_tag)

group_tag.setLayout(layout_tag)

v_line_interface.addWidget(group_tag)




#оставлять приложение открытым, пока не будет нажата кнопка выхода
app.exec_()
