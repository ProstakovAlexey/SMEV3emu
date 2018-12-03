import datetime
import re
import random
sh = re.compile('<\S{0,}messageid>(.*?)</\S{0,}messageid>', re.S)


def get_message_id(xml_str):
    """
    Выдает message_id, если его нет, то None
    :param xml_str: строка
    :return: message_id
    """
    res = sh.findall(xml_str.lower())
    if res:
        res = res[len(res) - 1]
    return res


def time_stamp():
    """
    Выдаем метку времени, для печати на экране
    :return:
    """
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+03:00")


def case_num(n=6, init=0):
    '''Возвращает случайный номер состоящий из n цифр'''
    if init != 0:
        random.seed(init)
    result = ''
    for i in range(0, n):
        s = random.randint(0, 9)
        result += str(s)
    return result