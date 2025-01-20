import inspect
from pprint import pprint


class Modul():

    def test(x):
        pass


def introspection_info(obj=None, **kwargs):
    info_dic: dict = {}
    try:
        print(f'Исследуем объект {obj.__name__}')
    except AttributeError:
        print(f'Исследуем объект {obj}')
    print('Тип объекта:', type(obj))
    info_dic['type'] = type(obj)
    print('Атрибуты объекта:', dir(obj))
    info_dic['attributes'] = dir(obj)
    print('Модуль объекта:', inspect.getmodule(obj))
    info_dic['module'] = inspect.getmodule(obj)
    return info_dic


number_info = introspection_info(42)

print(number_info)
