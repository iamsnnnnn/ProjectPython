import json
import requests


def get_vacs():
    # запрос
    req = requests.get('https://api.hh.ru/vacancies', {'text': 'Name:iOS'})
    # декодим данные
    data = req.content.decode()
    # закрываем соединение
    req.close()
    # массив для 10 вакансий
    d = []
    # проходимся по странице
    for vac in json.loads(data)['items'][:10]:
        # получаем вакансии по id
        req = requests.get(vac['url'])
        # декодим данные
        data = req.content.decode()
        req.close()
        d.append(json.loads(data))
    return d


if __name__ == '__main__':
    for i in get_vacs():
        print(i['salary'])

