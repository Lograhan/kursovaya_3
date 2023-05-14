import json
from datetime import datetime

with open('/home/roman/skypro/kurs_3/operations.json', 'r') as file:
    data = json.load(file)

    def last_operations():
        new_data = []
        for i in data:
            if i == {}:
                data.remove(i)
            elif i['state'] == 'EXECUTED':
                new_data.append(i)
        date_sort = sorted(new_data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
        return date_sort[:5]
