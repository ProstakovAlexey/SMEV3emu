import datetime
import re
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
    return datetime.datetime.now().strftime("%Y-%M-%dT%H:%M:%S.000+03:00")