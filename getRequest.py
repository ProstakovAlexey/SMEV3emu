import glob
import os
import shutil
import uuid
import smev3



def get_request():
    """
    Выдает запросы из папки
    :return:
    """
    dir = 'Запросы к нам'
    requests_list = glob.glob(os.path.join(dir, '*.xml'))
    if not requests_list:
        message = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1" xmlns:ns1="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:GetRequestResponse /> 
   </soapenv:Body>
</soapenv:Envelope>
"""
        for sh in glob.glob(os.path.join('Шаблоны', 'Запросы к нам', '*.xml')):
            shutil.copy(sh, dir)
    else:
        with open(requests_list[0], mode='r', encoding='utf-8') as fp:
            message = fp.read()
        try:
            os.remove(requests_list[0])
        except PermissionError:
            print('Не смог удалить файл', requests_list[0])
        # Нужно заполнить в сообщении UUI и дату
        attr = {'MessageID': str(uuid.uuid1()), 'TransactionCode': str(uuid.uuid1()), 'Timestamp': smev3.time_stamp()}
        message = message.format(** attr)
    return message


