# Подготовка данных для задания 1, 2
import random
import dateutil.parser
from bson.json_util import dumps, RELAXED_JSON_OPTIONS


data = [{
     'number': f'780000000000{i}',
     'name': 'Пользователь №',
     'sessions': [
         {
             'created_at': dateutil.parser.parse('2016-01-01T00:00:00'),
             'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZc',
             'actions': [
                 {
                     'type': 'read',
                     'created_at': dateutil.parser.parse('2016-01-01T01:20:01'),
                 },
                 {
                     'type': 'read',
                     'created_at': dateutil.parser.parse('2016-01-01T01:21:13'),
                 },
                 {
                     'type': 'create',
                     'created_at': dateutil.parser.parse('2016-01-01T01:33:59'),
                 }
             ],
         }
     ]
 } for i in [random.randint(0, 9) for i in range(int(input("Enter number of users")))]]


with open("Account.bson", "w") as f:
    f.write(dumps(data, json_options=RELAXED_JSON_OPTIONS))
