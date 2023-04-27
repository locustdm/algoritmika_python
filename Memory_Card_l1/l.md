# Задачи на сегодня:
1.  Интерфейс для вопросов
2.  Интерфейс для ответа

# Этапы разработки:
1.  Заготовка проекта
2.  Организация системы Layout
3.  Определения QGroupBox для интерфейсов (вопросы / ответы) и установка соответствующих Layout
4.  Создание виджетов и добавление их в Layout
5.  Некоторые визуальные настройки (не обязательно)

# Организация Layout
*Структура описана по мере углубления внутрь* 
1.  layout_v_main - VL - главный
2.  layout_h_ques - HL - для вопроса. - внутри layout_v_main  
3.  layout_h_group - HL - для вариантов ответа или результата - внутри layout_v_main
4.  layout_h_button - HL - для кнопки отправить - внутри layout_v_main
5.  layout_v_group_c1 - VL - внутри layout_h_group
6.  layout_v_group_c2 - VL - внутри layout_h_group

# Организация Групп
```python
#группа для RadioButton
group_ask = QGroupBox("Варианты ответов:")

#группа для результатов ответа
group_answer = QGroupBox("Результат теста:")

#прикрепить их Layout
group_ask.setLayout(layout_h_group)
group_answer.setLayout(layout_h_group)
```

