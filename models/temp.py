#!/usr/bin/python3
from base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


# [BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
# [BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
# {'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
# JSON of my_model:
#     my_number: (<class 'int'>) - 89
#     name: (<class 'str'>) - My First Model
#     __class__: (<class 'str'>) - BaseModel
#     updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
#     id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
#     created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

# [BaseModel] (4f59e345-1ca3-4d30-8186-b1ac395a22c6) {'id': '4f59e345-1ca3-4d30-8186-b1ac395a22c6', 'created_at': datetime.datetime(2023, 12, 10, 8, 58, 24, 598095), 'updated_at': datetime.datetime(2023, 12, 10, 8, 58, 24, 598095), 'name': 'My First Model', 'my_number': 89}
# [BaseModel] (4f59e345-1ca3-4d30-8186-b1ac395a22c6) {'id': '4f59e345-1ca3-4d30-8186-b1ac395a22c6', 'created_at': datetime.datetime(2023, 12, 10, 8, 58, 24, 598095), 'updated_at': datetime.datetime(2023, 12, 10, 8, 58, 24, 598237), 'name': 'My First Model', 'my_number': 89}
# {'id': '4f59e345-1ca3-4d30-8186-b1ac395a22c6', 'created_at': '2023-12-10T08:58:24.598095', 'updated_at': datetime.datetime(2023, 12, 10, 8, 58, 24, 598237), 'name': 'My First Model', 'my_number': 89, '__class__': 'BaseModel'}
# JSON of my_model:
#         id: (<class 'str'>) - 4f59e345-1ca3-4d30-8186-b1ac395a22c6
#         created_at: (<class 'str'>) - 2023-12-10T08:58:24.598095
#         updated_at: (<class 'datetime.datetime'>) - 2023-12-10 08:58:24.598237
#         name: (<class 'str'>) - My First Model
#         my_number: (<class 'int'>) - 89
#         __class__: (<class 'str'>) - BaseModel