import csv
import os.path
import smev3
import uuid
from termcolor import colored


def getBenefit(file_name):
    """
    Читаю справочник категорий и делаю из него словарь
    :param file_name: файл со справочников в csv
    :return: словарь с категориями
    """
    result = dict()
    csv_read = open(file_name, encoding='utf-8', newline='')
    reader = csv.DictReader(csv_read, delimiter=';')
    # Читаем построчно заготовку, проверяе, пишем в справочник
    for row in reader:
        result[row['CODE'].strip()] = row['TITLE'].strip()
    csv_read.close()
    return result


def getSubservice(file_name):
    """
    Читаю справочник вариантов оказания и делаю из него словарь
    :param file_name: файл со справочников в csv
    :return: словарь с вариантами оказания услуг
    """
    result = dict()
    csv_read = open(file_name, encoding='utf-8', newline='')
    reader = csv.DictReader(csv_read, delimiter=';')
    # Читаем построчно заготовку, проверяе, пишем в справочник
    for row in reader:
        result[row['CODE'].strip()] = row['TITLE'].strip()
    csv_read.close()
    return result


def getBenefitSubservice(file_name):
    """
    Читаю справочник связки вариантов оказания и категорий и делаю из него список
    :param file_name: файл со справочников в csv
    :return: список
    """
    result = list()
    csv_read = open(file_name, encoding='utf-8', newline='')
    reader = csv.DictReader(csv_read, delimiter=';')
    # Читаем построчно заготовку, проверяе, пишем в справочник
    for row in reader:
        result.append((row['SUBSERVICE'].strip(), row['BENEFITCODE'].strip()))
    csv_read.close()
    return result


def get_time_slot(file_name):
    """
    Читает список слотов времени из файла
    :param file_name: имя файл
    :return: список слотов
    """
    result = list()
    with open(file_name, encoding='utf-8') as fp:
        for line in fp.readlines():
            result.append(line.strip())
    return result




if __name__ == '__main__':
    dir_name = 'Шаблоны/Справочники'
    time_slots = get_time_slot(os.path.join(dir_name, 'slots.txt'))
    #time_slots = list()
    orders_list = list()
    benefit = getBenefit(os.path.join(dir_name, 'SOC_BENEFIT.csv'))
    subservice = getSubservice(os.path.join(dir_name, 'SOC_SUBSERVICE.csv'))
    # Читаю шаблон заявления
    with open('Шаблоны/Заявления/Малоимущие.xml', encoding='utf-8', mode='r') as fp:
        shablon_zaiv = fp.read()
    code_list = list()
    # Скрипт для слотов времени
    script_shablon = "UPDATE ESERVICE_EPGU_TIMESLOTS SET BOOKINGID='%s',FREE=0,Reserv=1,booked=0," \
                     "BOOKINGTIME = GETDATE() WHERE GUID='%s'"
    script_result = list()
    for line in getBenefitSubservice(os.path.join(dir_name, 'SOC_BENEFIT_SUBSERVICE.csv')):
        # в line 0 - код варианта оказания услуги, 1 - код категории
        change = dict()
        change['oktmo'] = '05000000'
        #try:
        change["SubserviceCode"] = line[0] # Код варианта оказания услуг
        change["SubserviceName"] = subservice[line[0]]# Название категории
        change["OrganizationCode"] = '1_1' # Код организации
        change["OrganizationName"] = 'ОСЗН для тестирования услуг' # Название организации
        change["CategoryCode"] = line[1]  # Код категории
        change['CategoryName'] = benefit[line[1]]   # Название категории
        change['MessageID'] = str(uuid.uuid1())
        change['TransactionCode'] = str(uuid.uuid1())
        change['Timestamp'] = smev3.time_stamp()
        order =  smev3.case_num()
        change['orderId'] = order
        orders_list.append(order)
        #ts = str(uuid.uuid1()).upper()

        #time_slots.append(ts)
        ts = time_slots[0] # Номер бронирования записи на прием
                #script_result.append(script_shablon % (uuid.uuid1(), time_slots[0]))
        del time_slots[0]
        change["bookId"] = ts
        # Подставляю в шаблон и сохраняю результат
        with open(os.path.join('Запросы к нам', 'Малоимущие_%s.xml' % change['orderId']), 'w', encoding='utf-8') as fp:
                fp.write(shablon_zaiv.format(**change))
        print('{SubserviceCode}_{CategoryCode}; {SubserviceName}. {CategoryName}'.format(**change))
        code_list.append('{SubserviceCode}_{CategoryCode}'.format(**change))
        #except KeyError as err:
        #    print(colored('Не сделал заявление. Ошибка:' + str(err), 'red'))
    print('Коды всех услуг:', ';'.join(code_list))
    print('Использовал слоты времени:', ';'.join(time_slots))
    print('Номера заявлений:', ';'.join(orders_list))
    with open(os.path.join(dir_name, 'Скрипт.txt'), 'w') as fp:
        fp.write(';\n'.join(script_result))






