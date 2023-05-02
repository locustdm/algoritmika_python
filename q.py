from PyQt5.QtCore import Qt, QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QRadioButton, QPushButton, QGroupBox, QButtonGroup

from random import choice, shuffle #! - суфле перемешивает элементы списка



#конструктор, создающий объект типа приложение
app = QApplication([]) 

file = QFile("q.css")                            
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
app.setStyleSheet(stream.readAll())

#конструктор, создающий объект типа окно
main_win = QWidget()
main_win.status = 0 #! 0 - форма вопроса, 1 - форма ответа, ПРИ СТАРТЕ - форма вопроса. (ЭТО МОЕ СВОЙСТВО)
main_win.elem = {} #! пустой словарь, будет хранить словарь вопроса. (ЭТО МОЕ СВОЙСТВО)

main_win.setWindowTitle('ВАШ Текст!')
main_win.setFixedSize(800, 400)
main_win.show()

#логика Layout 
layout_v_main  = QVBoxLayout()
layout_h_ques = QHBoxLayout()
layout_h_group = QHBoxLayout()
layout_h_group_helpme = QHBoxLayout()
layout_h_group_res = QHBoxLayout() #!----------
layout_h_button = QHBoxLayout()
layout_v_group_c1 = QVBoxLayout()
layout_v_group_c2 = QVBoxLayout()

main_win.setLayout(layout_v_main)

layout_v_main.addLayout(layout_h_ques)
layout_v_main.addLayout(layout_h_group)
layout_v_main.addLayout(layout_h_button)

layout_h_group_helpme.addLayout(layout_v_group_c1)
layout_h_group_helpme.addLayout(layout_v_group_c2)

#определение виджетов
l_text = QLabel('')
radio_button_1 = QRadioButton('')  #!удалю текст по умолчанию, потому что даже в начала должен быть рандомный вопрос :)
radio_button_2 = QRadioButton('')
radio_button_3 = QRadioButton('')
radio_button_4 = QRadioButton('')
but = QPushButton("Ответить")

list_radio_button = [radio_button_1, radio_button_2, radio_button_3, radio_button_4] #!список радио кнопок

layout_h_ques.addWidget(l_text)
layout_v_group_c1.addWidget(list_radio_button[0])
layout_v_group_c1.addWidget(list_radio_button[1])
layout_v_group_c2.addWidget(list_radio_button[2])
layout_v_group_c2.addWidget(list_radio_button[3])
layout_h_button.addWidget(but)

#работа с группами
group_ask = QGroupBox("Варианты ответов:")
group_res = QGroupBox("Результаты теста")

label_res = QLabel("Какой-то правильный ответ :)") 
layout_h_group_res.addWidget(label_res)
group_res.setLayout(layout_h_group_res)
layout_h_group.addWidget(group_res)

group_res.hide()
# group_ask.hide()
group_ask.setLayout(layout_h_group_helpme)
layout_h_group.addWidget(group_ask)

#словарь с вопросами и ответами
questions_ld = [
    {
        'ques' : "Кто захватит мир?",
        'ans' : ['Коты', 'Собаки', 'Жабы', 'Python' ],
        'correct': 0
    },
    {
        'ques' : "Проект какой категории взяли больше всего людей?",
        'ans' : ['Приложение на Qt', 'Аркада', 'Платформер', 'Не знаю' ],
        'correct': 1
    },
    {
        'ques' : "Как жить?",
        'ans' : ['Не знаю', 'Никак', 'Кушать', 'Не жить' ],
        'correct': 2
    },
] 

def set_radio_button_text():
    main_win.elem = choice(questions_ld) #случайный словарь из списка #!сохранено в свойство окна
    l_text.setText(main_win.elem['ques'])

    shuffle(list_radio_button) #! перемешиваю элементы списка с помощью суфлешки :)

    for i in range(4): #пробегаемся по radio_button
        list_radio_button[i].setText(main_win.elem['ans'][i])

#! функция будет проверять, правильный ли дал ответ пользователь
def check_answer():
    correct = main_win.elem['ans'][main_win.elem['correct']] #правильный ответ
    for i in range(4):
        if list_radio_button[i].isChecked(): #если кнопка была нажата
            if list_radio_button[i].text() ==  correct: #сравниваем ответ пользователя с правильным ответом
                return True #пользователь ответил верно
    
    return False #не один элемент списка не совпал с правильным ответом

RadioGroup = QButtonGroup() 
RadioGroup.addButton(list_radio_button[0])
RadioGroup.addButton(list_radio_button[1])
RadioGroup.addButton(list_radio_button[2])
RadioGroup.addButton(list_radio_button[3])

#очистить радио кнопки от ответов пользователя
def reset_radiobutton():
    RadioGroup.setExclusive(False)
    list_radio_button[0].setChecked(False)
    list_radio_button[1].setChecked(False)
    list_radio_button[2].setChecked(False)
    list_radio_button[3].setChecked(False)
    RadioGroup.setExclusive(True)

#показать форму с варинатами ответов
def show_result():
    res = check_answer() #! True - если пользователю прав, False - не прав
    if res: #если пользователь прав
        label_res.setText("Ты оказался прав!")
    else:
        label_res.setText("Ты оказался не прав! Правильный ответ: " + main_win.elem['ans'][main_win.elem['correct']])
    group_ask.hide()
    group_res.show()
    but.setText("Следующий уровень")
    
#показать форму с вопросом
def show_ask():
    group_ask.show()
    group_res.hide()
    but.setText("Ответить")
    set_radio_button_text()
    reset_radiobutton()


def show():

    if main_win.status == 1: #!если 1, то должен быть отображен результат
        show_result()
    elif main_win.status == 0: #!если 0, то должен быть вопрос с вариантами ответа
        show_ask()

    main_win.status = int(not bool(main_win.status)) #! 1 станет 0, а 0 станет 1
    
but.clicked.connect(show)

show() #!вызовем один раз без факта клика, чтобы какой-то текст отображался 

#оставлять приложение открытым, пока не будет нажата кнопка выхода
app.exec_()


