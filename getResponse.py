import glob
import os

def get_response():
    """Выдает ответ на запрос.
    """
    dir_name = 'Ответы для передачи в ВИС'
    file_names = glob.glob(os.path.join(dir_name, '*.xml'))
    if file_names:
        # Ответы есть, отдадим первый
        with open(file_names[0], encoding='utf-8') as fp:
            result = fp.read()
        os.remove(file_names[0])
    else:
        result = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <ns2:GetResponseResponse xmlns="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1" 
                xmlns:ns2="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1" 
                xmlns:ns3="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/faults/1.1"/>
            </soap:Body>
        </soap:Envelope>"""
    return result

