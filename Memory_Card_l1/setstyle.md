# Настройка стилей QT, используя css
Создайте файл с раширением css и назовите его так, как вам удобно. Например: `style.css`. У меня файл будет называться `q.css`.
Далее вам нужно вставить себе код:
```python
file = QFile("q.css")                            
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
app.setStyleSheet(stream.readAll())
```
Обратите внимание на строчку:
```python
file = QFile("q.css") 
```
В ней в качестве файла указан `q.css`. Укажите свое имя файла. 

Пример содержимого в css файле:
```css
*{
    font-size: 20px;
}

QWidget{
    background-color: #303136;
    color: #303136;
    /* color:black; */
    color: #7680FF;
}
QGroupBox{
    background-color: #7680FF;
    color: #7680FF;
}

QPushButton:hover{ 
    background-color: #7680FF; 
    color: #303136;
}
```

`background-color` отвечает за цвет фона, `color` за цвет текста. В примере выше они одинаковые, поэтому вы не видите текста :)

[Туториал W3SCHOOL](https://www.w3schools.com/css/default.asp)

