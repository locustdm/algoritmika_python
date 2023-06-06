# Задача 1
Генераторы списка ребята не проходили (и пока об этом упоминать не нужно) \
Очень классный прикол с переводом в словарь из списка таплов, но они так же об этом не знают :( \
Есть конструктор `str()`, поэтому не рекомендуется так называть переменные \
В связи с этим ниже предложены некоторые корректировки в решении 

Спасибо, что приложили свое решение задач! :)

```python
def get_dict(s_dict):
    d = dict()
    for s in s_dict.split():
        el = s.split("=")
        d[el[0]] = int(el[1])

    return d


s_dict = "one=1 two=2 three=3"
print(get_dict(s_dict))
```
# Задача 2
```python
def print_dict(s_dict): #поменяла с get_dict на print_dict
    d = dict()
    for s in s_dict.split():
        el = s.split("=")
        if el[0] not in ["False", "3"]:
            d[el[0]] = int(el[1])
    print(d)


s_dict = "one=1 two=2 three=3"
print_dict(s_dict)
```
