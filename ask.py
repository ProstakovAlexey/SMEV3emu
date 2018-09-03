def get_ask():
    """
    Выдает ASK ответ, по нужному messageid
    :return:
    """
    s = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1">
        <soapenv:Header/>
            <soapenv:Body>
                <ns:AckResponse/>
            </soapenv:Body>
    </soapenv:Envelope>"""
    return s