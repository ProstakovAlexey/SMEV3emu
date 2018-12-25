import smev3
import glob
import random
import uuid
import os.path
from termcolor import colored


def get_file(dir_name):
    """
    Возвращает случайный файл из папки
    :param dir_name:
    :return:
    """
    # //TODO сделать по умолчанию ошибку доступа, а не пусто
    result = None
    file_names = glob.glob(os.path.join(dir_name, '*.xml'))
    if file_names:
        file_name = random.choice(file_names)
        with open(file_name, encoding='utf-8') as fp:
            result = fp.read()
        xml = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:GetResponseResponse xmlns="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1" xmlns:ns2="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1" xmlns:ns3="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/faults/1.1">
         <ns2:ResponseMessage>
            <ns2:Response Id="SIGNED_BY_SMEV">
               <ns2:OriginalMessageId>{OriginalMessageId}</ns2:OriginalMessageId>
               <ns2:SenderProvidedResponseData Id="SIGNED_BY_CALLER">
                  <ns2:MessageID>{MessageID}</ns2:MessageID>
                  <ns2:To>eyJzaWQiOjMxOTM5LCJtaWQiOiJhMmVlZGUxNS1hYzczLTExZTgtYTcyNy03YjljMDQwNjc1NWEiLCJlb2wiOjAsInNsYyI6ImZzcy5ydV9zbWV2LTNfcmFzY2hfcmVnaXN0cmF0aW9uXzEuMC4wX1N2ZWRTb3N0UmFzY2hSZXF1ZXN0IiwibW5tIjoiNzIwNDAxIn0=</ns2:To>
                  <MessagePrimaryContent>
                     %s
                  </MessagePrimaryContent>
               </ns2:SenderProvidedResponseData>
               <ns2:MessageMetadata>
                  <ns2:MessageId>{MessageID}</ns2:MessageId>
                  <ns2:MessageType>RESPONSE</ns2:MessageType>
                  <ns2:Sender>
                     <ns2:Mnemonic>emu</ns2:Mnemonic>
                     <ns2:HumanReadableName>emu</ns2:HumanReadableName>
                  </ns2:Sender>
                  <ns2:SendingTimestamp>{Timestamp}</ns2:SendingTimestamp>
                  <ns2:DestinationName>unknown</ns2:DestinationName>
                  <ns2:Recipient>
                     <ns2:Mnemonic>720401</ns2:Mnemonic>
                     <ns2:HumanReadableName>ИС СЗН</ns2:HumanReadableName>
                  </ns2:Recipient>
                  <ns2:SupplementaryData>
                     <ns2:DetectedContentTypeName>not detected</ns2:DetectedContentTypeName>
                     <ns2:InteractionType>NotDetected</ns2:InteractionType>
                  </ns2:SupplementaryData>
                  <ns2:DeliveryTimestamp>{Timestamp}</ns2:DeliveryTimestamp>
                  <ns2:Status>responseIsDelivered</ns2:Status>
               </ns2:MessageMetadata>
               <ns2:SenderInformationSystemSignature>
                  <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
                     <ds:SignedInfo>
                        <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
                        <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#gostr34102001-gostr3411"/>
                        <ds:Reference URI="#SIGNED_BY_CALLER">
                           <ds:Transforms>
                              <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
                              <ds:Transform Algorithm="urn://smev-gov-ru/xmldsig/transform"/>
                           </ds:Transforms>
                           <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#gostr3411"/>
                           <ds:DigestValue>slyk8zKBNKiPsOzsh/BNHWAG5uv8BQx7sbO6I77HnGY=</ds:DigestValue>
                        </ds:Reference>
                     </ds:SignedInfo>
                     <ds:SignatureValue>LxyzBo4Hl5UCD24n127IiV/ab3xA9tHdEYrI1Nojj4djKDyLrx7mPf815LIlKWXAEzSSfj95wD0Ct5rEaYk84g==</ds:SignatureValue>
                     <ds:KeyInfo>
                        <ds:X509Data>
                           <ds:X509Certificate>MIIH3DCCB4ugAwIBAgIRAXILAVZQAHCj6BFWMr8dB1owCAYGKoUDAgIDMIIBRjEYMBYGBSqFA2QBEg0xMjM0NTY3ODkwMTIzMRowGAYIKoUDA4EDAQESDDAwMTIzNDU2Nzg5MDEpMCcGA1UECQwg0KHRg9GJ0LXQstGB0LrQuNC5INCy0LDQuyDQtC4gMjYxFzAVBgkqhkiG9w0BCQEWCGNhQHJ0LnJ1MQswCQYDVQQGEwJSVTEYMBYGA1UECAwPNzcg0JzQvtGB0LrQstCwMRUwEwYDVQQHDAzQnNC+0YHQutCy0LAxJDAiBgNVBAoMG9Ce0JDQniDQoNC+0YHRgtC10LvQtdC60L7QvDEwMC4GA1UECwwn0KPQtNC+0YHRgtC+0LLQtdGA0Y/RjtGJ0LjQuSDRhtC10L3RgtGAMTQwMgYDVQQDDCvQotC10YHRgtC+0LLRi9C5INCj0KYg0KDQotCaICjQoNCi0JvQsNCx0YEpMB4XDTE4MDMyODA2NTUxMVoXDTE5MDMyODA3MDUxMVowggEPMR8wHQYJKoZIhvcNAQkCDBDQotCh0JzQrdCSM1/QrdCcMRowGAYIKoUDA4EDAQESDDAwNzcwNzA0OTM4ODEYMBYGBSqFA2QBEg0xMDI3NzAwMTk4NzY3MSgwJgYDVQQKDB/Qn9CQ0J4gwqvQoNC+0YHRgtC10LvQtdC60L7QvMK7MSYwJAYDVQQHDB3QodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQszEtMCsGA1UECAwkNzgg0LMuINCh0LDQvdC60YIt0J/QtdGC0LXRgNCx0YPRgNCzMQswCQYDVQQGEwJSVTEoMCYGA1UEAwwf0J/QkNCeIMKr0KDQvtGB0YLQtdC70LXQutC+0LzCuzBjMBwGBiqFAwICEzASBgcqhQMCAiQABgcqhQMCAh4BA0MABEDt/NkbN2KN5D7zCI5yysq8B3b19K4YrnYo3CvHvStJcSFfH5m2oBI/sS+I4URk7caRdrMqgleRcAmpwI1oWlfeo4IEgzCCBH8wDgYDVR0PAQH/BAQDAgTwMB0GA1UdDgQWBBRZdtXJC9SYq9wCOjQMH8YaLHyT2DCCAYgGA1UdIwSCAX8wggF7gBQ+7xk/D7l5sPHmKSGj5LmVuaXukKGCAU6kggFKMIIBRjEYMBYGBSqFA2QBEg0xMjM0NTY3ODkwMTIzMRowGAYIKoUDA4EDAQESDDAwMTIzNDU2Nzg5MDEpMCcGA1UECQwg0KHRg9GJ0LXQstGB0LrQuNC5INCy0LDQuyDQtC4gMjYxFzAVBgkqhkiG9w0BCQEWCGNhQHJ0LnJ1MQswCQYDVQQGEwJSVTEYMBYGA1UECAwPNzcg0JzQvtGB0LrQstCwMRUwEwYDVQQHDAzQnNC+0YHQutCy0LAxJDAiBgNVBAoMG9Ce0JDQniDQoNC+0YHRgtC10LvQtdC60L7QvDEwMC4GA1UECwwn0KPQtNC+0YHRgtC+0LLQtdGA0Y/RjtGJ0LjQuSDRhtC10L3RgtGAMTQwMgYDVQQDDCvQotC10YHRgtC+0LLRi9C5INCj0KYg0KDQotCaICjQoNCi0JvQsNCx0YEpghEBcgsBVlAAubPnEc86vjR3oDAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYBBQUHAwQwJwYJKwYBBAGCNxUKBBowGDAKBggrBgEFBQcDAjAKBggrBgEFBQcDBDAdBgNVHSAEFjAUMAgGBiqFA2RxATAIBgYqhQNkcQIwKwYDVR0QBCQwIoAPMjAxODAzMjgwNjU1MTBagQ8yMDE5MDMyODA2NTUxMFowggE0BgUqhQNkcASCASkwggElDCsi0JrRgNC40L/RgtC+0J/RgNC+IENTUCIgKNCy0LXRgNGB0LjRjyAzLjkpDCwi0JrRgNC40L/RgtC+0J/RgNC+INCj0KYiICjQstC10YDRgdC40LggMi4wKQxj0KHQtdGA0YLQuNGE0LjQutCw0YIg0YHQvtC+0YLQstC10YLRgdGC0LLQuNGPINCk0KHQkSDQoNC+0YHRgdC40Lgg4oSWINCh0KQvMTI0LTI1Mzkg0L7RgiAxNS4wMS4yMDE1DGPQodC10YDRgtC40YTQuNC60LDRgiDRgdC+0L7RgtCy0LXRgtGB0YLQstC40Y8g0KTQodCRINCg0L7RgdGB0LjQuCDihJYg0KHQpC8xMjgtMjg4MSDQvtGCIDEyLjA0LjIwMTYwNgYFKoUDZG8ELQwrItCa0YDQuNC/0YLQvtCf0YDQviBDU1AiICjQstC10YDRgdC40Y8gMy45KTBlBgNVHR8EXjBcMFqgWKBWhlRodHRwOi8vY2VydGVucm9sbC50ZXN0Lmdvc3VzbHVnaS5ydS9jZHAvM2VlZjE5M2YwZmI5NzliMGYxZTYyOTIxYTNlNGI5OTViOWE1ZWU5MC5jcmwwVwYIKwYBBQUHAQEESzBJMEcGCCsGAQUFBzAChjtodHRwOi8vY2VydGVucm9sbC50ZXN0Lmdvc3VzbHVnaS5ydS9jZHAvdGVzdF9jYV9ydGxhYnMyLmNlcjAIBgYqhQMCAgMDQQDC4cx4P093b5ai+RKhGdvvkxFMVxK0UPy3JEUUs3zmsC1parcrJK/QqCIVmPmdUehIIHSBDid/kcE1xUdE6X32</ds:X509Certificate>
                        </ds:X509Data>
                     </ds:KeyInfo>
                  </ds:Signature>
               </ns2:SenderInformationSystemSignature>
            </ns2:Response>
            <ns2:SMEVSignature>
               <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
                  <ds:SignedInfo>
                     <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
                     <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#gostr34102001-gostr3411"/>
                     <ds:Reference URI="#SIGNED_BY_SMEV">
                        <ds:Transforms>
                           <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
                           <ds:Transform Algorithm="urn://smev-gov-ru/xmldsig/transform"/>
                        </ds:Transforms>
                        <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#gostr3411"/>
                        <ds:DigestValue>vqBoDCPCjg1HjlgEpX09HgqbKjSkAjqnNn3QLn5JAuQ=</ds:DigestValue>
                     </ds:Reference>
                  </ds:SignedInfo>
                  <ds:SignatureValue>DFe/Wxpx35gYdPd7ewY8thwN5nA0Zhg8P/rhyNYJmBtTr0J2fvpKq9ajzRBl7s3ZnZN/zJ2O/+/3BCLK/euKLw==</ds:SignatureValue>
                  <ds:KeyInfo>
                     <ds:X509Data>
                        <ds:X509Certificate>MIIH2DCCB4egAwIBAgIRAXILAVZQAHCj6BHaIfbqMnEwCAYGKoUDAgIDMIIBRjEYMBYGBSqFA2QBEg0xMjM0NTY3ODkwMTIzMRowGAYIKoUDA4EDAQESDDAwMTIzNDU2Nzg5MDEpMCcGA1UECQwg0KHRg9GJ0LXQstGB0LrQuNC5INCy0LDQuyDQtC4gMjYxFzAVBgkqhkiG9w0BCQEWCGNhQHJ0LnJ1MQswCQYDVQQGEwJSVTEYMBYGA1UECAwPNzcg0JzQvtGB0LrQstCwMRUwEwYDVQQHDAzQnNC+0YHQutCy0LAxJDAiBgNVBAoMG9Ce0JDQniDQoNC+0YHRgtC10LvQtdC60L7QvDEwMC4GA1UECwwn0KPQtNC+0YHRgtC+0LLQtdGA0Y/RjtGJ0LjQuSDRhtC10L3RgtGAMTQwMgYDVQQDDCvQotC10YHRgtC+0LLRi9C5INCj0KYg0KDQotCaICjQoNCi0JvQsNCx0YEpMB4XDTE4MDMwNzA3Mjc1M1oXDTE5MDMwNzA3Mzc1M1owggELMR8wHQYJKoZIhvcNAQkCDBDQotCh0JzQrdCSM1/QmtCaMRowGAYIKoUDA4EDAQESDDAwNzcwNzA0OTM4ODEYMBYGBSqFA2QBEg0xMDI3NzAwMTk4NzY3MSgwJgYDVQQKDB/Qn9CQ0J4gwqvQoNC+0YHRgtC10LvQtdC60L7QvMK7MSYwJAYDVQQHDB3QodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQszEpMCcGA1UECAwgNzgg0KHQsNC90LrRgi3Qn9C10YLQtdGA0LHRg9GA0LMxCzAJBgNVBAYTAlJVMSgwJgYDVQQDDB/Qn9CQ0J4gwqvQoNC+0YHRgtC10LvQtdC60L7QvMK7MGMwHAYGKoUDAgITMBIGByqFAwICJAAGByqFAwICHgEDQwAEQMC71XesoJAavwGJgMlhlPywcaFx3HYPwMUIYBhtoglDW3BhQUzgIXFQ6uvD7FUshBl38VH+AXZM/BkzGGzpzFSjggSDMIIEfzAOBgNVHQ8BAf8EBAMCBPAwHQYDVR0OBBYEFItxgSnIqbor48DVSfsV11JpIwXDMIIBiAYDVR0jBIIBfzCCAXuAFD7vGT8PuXmw8eYpIaPkuZW5pe6QoYIBTqSCAUowggFGMRgwFgYFKoUDZAESDTEyMzQ1Njc4OTAxMjMxGjAYBggqhQMDgQMBARIMMDAxMjM0NTY3ODkwMSkwJwYDVQQJDCDQodGD0YnQtdCy0YHQutC40Lkg0LLQsNC7INC0LiAyNjEXMBUGCSqGSIb3DQEJARYIY2FAcnQucnUxCzAJBgNVBAYTAlJVMRgwFgYDVQQIDA83NyDQnNC+0YHQutCy0LAxFTATBgNVBAcMDNCc0L7RgdC60LLQsDEkMCIGA1UECgwb0J7QkNCeINCg0L7RgdGC0LXQu9C10LrQvtC8MTAwLgYDVQQLDCfQo9C00L7RgdGC0L7QstC10YDRj9GO0YnQuNC5INGG0LXQvdGC0YAxNDAyBgNVBAMMK9Ci0LXRgdGC0L7QstGL0Lkg0KPQpiDQoNCi0JogKNCg0KLQm9Cw0LHRgSmCEQFyCwFWUAC5s+cRzzq+NHegMB0GA1UdJQQWMBQGCCsGAQUFBwMCBggrBgEFBQcDBDAnBgkrBgEEAYI3FQoEGjAYMAoGCCsGAQUFBwMCMAoGCCsGAQUFBwMEMB0GA1UdIAQWMBQwCAYGKoUDZHEBMAgGBiqFA2RxAjArBgNVHRAEJDAigA8yMDE4MDMwNzA3Mjc1M1qBDzIwMTkwMzA3MDcyNzUzWjCCATQGBSqFA2RwBIIBKTCCASUMKyLQmtGA0LjQv9GC0L7Qn9GA0L4gQ1NQIiAo0LLQtdGA0YHQuNGPIDMuOSkMLCLQmtGA0LjQv9GC0L7Qn9GA0L4g0KPQpiIgKNCy0LXRgNGB0LjQuCAyLjApDGPQodC10YDRgtC40YTQuNC60LDRgiDRgdC+0L7RgtCy0LXRgtGB0YLQstC40Y8g0KTQodCRINCg0L7RgdGB0LjQuCDihJYg0KHQpC8xMjQtMjUzOSDQvtGCIDE1LjAxLjIwMTUMY9Ch0LXRgNGC0LjRhNC40LrQsNGCINGB0L7QvtGC0LLQtdGC0YHRgtCy0LjRjyDQpNCh0JEg0KDQvtGB0YHQuNC4IOKEliDQodCkLzEyOC0yODgxINC+0YIgMTIuMDQuMjAxNjA2BgUqhQNkbwQtDCsi0JrRgNC40L/RgtC+0J/RgNC+IENTUCIgKNCy0LXRgNGB0LjRjyAzLjkpMGUGA1UdHwReMFwwWqBYoFaGVGh0dHA6Ly9jZXJ0ZW5yb2xsLnRlc3QuZ29zdXNsdWdpLnJ1L2NkcC8zZWVmMTkzZjBmYjk3OWIwZjFlNjI5MjFhM2U0Yjk5NWI5YTVlZTkwLmNybDBXBggrBgEFBQcBAQRLMEkwRwYIKwYBBQUHMAKGO2h0dHA6Ly9jZXJ0ZW5yb2xsLnRlc3QuZ29zdXNsdWdpLnJ1L2NkcC90ZXN0X2NhX3J0bGFiczIuY2VyMAgGBiqFAwICAwNBAAfuLimwLO1RNL+ekh4hgnPu+yyLSiF2xGN4yZqWeA4d5VKU2zxveBMmSb4nvJFZ/3Qod1aQDdlgTRObLhKnEO8=</ds:X509Certificate>
                     </ds:X509Data>
                  </ds:KeyInfo>
               </ds:Signature>
            </ns2:SMEVSignature>
         </ns2:ResponseMessage>
      </ns2:GetResponseResponse>
   </soap:Body>
</soap:Envelope>
    """ % result
    else:
        xml = '''<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body><ns2:GetResponseResponse 
        xmlns="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1" 
        xmlns:ns2="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1" 
        xmlns:ns3="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/faults/1.1"/>
        </soap:Body></soap:Envelope>
        '''
    return xml



def send_request(text):
    """
    Выдает подтверждение приема ответа
    :return:
    """
    original_message_id = text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                                    '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                                    '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                                    '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}MessageID').text
    message_id = original_message_id
    t = smev3.time_stamp()
    dir_name = 'Ответы для передачи в ВИС'

    # Ответ с подтверждением
    s = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
      <ns2:SendRequestResponse xmlns="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1" xmlns:ns2="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1" xmlns:ns3="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/faults/1.1">
         <ns2:MessageMetadata Id="SIGNED_BY_SMEV">
            <ns2:MessageId>%s</ns2:MessageId>
            <ns2:MessageType>REQUEST</ns2:MessageType>
            <ns2:Sender>
               <ns2:Mnemonic>720401</ns2:Mnemonic>
               <ns2:HumanReadableName>ИС СЗН</ns2:HumanReadableName>
            </ns2:Sender>
            <ns2:SendingTimestamp>%s</ns2:SendingTimestamp>
            <ns2:DestinationName>unknown</ns2:DestinationName>
            <ns2:Recipient>
               <ns2:Mnemonic>emu</ns2:Mnemonic>
               <ns2:HumanReadableName>emu</ns2:HumanReadableName>
            </ns2:Recipient>
            <ns2:SupplementaryData>
               <ns2:DetectedContentTypeName>not detected</ns2:DetectedContentTypeName>
               <ns2:InteractionType>NotDetected</ns2:InteractionType>
            </ns2:SupplementaryData>
            <ns2:Status>requestIsQueued</ns2:Status>
         </ns2:MessageMetadata>
         <ns2:SMEVSignature>
            <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
               <ds:SignedInfo>
                  <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
                  <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#gostr34102001-gostr3411"/>
                  <ds:Reference URI="#SIGNED_BY_SMEV">
                     <ds:Transforms>
                        <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
                        <ds:Transform Algorithm="urn://smev-gov-ru/xmldsig/transform"/>
                     </ds:Transforms>
                     <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#gostr3411"/>
                     <ds:DigestValue>dHg5f57cLWtDBjCM7jXrHvqtT1oebRrkYyH0m+G8DPE=</ds:DigestValue>
                  </ds:Reference>
               </ds:SignedInfo>
               <ds:SignatureValue>d116U/XM9kTKz8ZziDjsxYvLS4Hz+TiNqRHpniyvKihM/HjuYqOwm20tYEshRKRXJ7s6CDsZYXFRiCUNRbhgQA==</ds:SignatureValue>
               <ds:KeyInfo>
                  <ds:X509Data>
                     <ds:X509Certificate>MIIH2DCCB4egAwIBAgIRAXILAVZQAHCj6BHaIfbqMnEwCAYGKoUDAgIDMIIBRjEYMBYGBSqFA2QBEg0xMjM0NTY3ODkwMTIzMRowGAYIKoUDA4EDAQESDDAwMTIzNDU2Nzg5MDEpMCcGA1UECQwg0KHRg9GJ0LXQstGB0LrQuNC5INCy0LDQuyDQtC4gMjYxFzAVBgkqhkiG9w0BCQEWCGNhQHJ0LnJ1MQswCQYDVQQGEwJSVTEYMBYGA1UECAwPNzcg0JzQvtGB0LrQstCwMRUwEwYDVQQHDAzQnNC+0YHQutCy0LAxJDAiBgNVBAoMG9Ce0JDQniDQoNC+0YHRgtC10LvQtdC60L7QvDEwMC4GA1UECwwn0KPQtNC+0YHRgtC+0LLQtdGA0Y/RjtGJ0LjQuSDRhtC10L3RgtGAMTQwMgYDVQQDDCvQotC10YHRgtC+0LLRi9C5INCj0KYg0KDQotCaICjQoNCi0JvQsNCx0YEpMB4XDTE4MDMwNzA3Mjc1M1oXDTE5MDMwNzA3Mzc1M1owggELMR8wHQYJKoZIhvcNAQkCDBDQotCh0JzQrdCSM1/QmtCaMRowGAYIKoUDA4EDAQESDDAwNzcwNzA0OTM4ODEYMBYGBSqFA2QBEg0xMDI3NzAwMTk4NzY3MSgwJgYDVQQKDB/Qn9CQ0J4gwqvQoNC+0YHRgtC10LvQtdC60L7QvMK7MSYwJAYDVQQHDB3QodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQszEpMCcGA1UECAwgNzgg0KHQsNC90LrRgi3Qn9C10YLQtdGA0LHRg9GA0LMxCzAJBgNVBAYTAlJVMSgwJgYDVQQDDB/Qn9CQ0J4gwqvQoNC+0YHRgtC10LvQtdC60L7QvMK7MGMwHAYGKoUDAgITMBIGByqFAwICJAAGByqFAwICHgEDQwAEQMC71XesoJAavwGJgMlhlPywcaFx3HYPwMUIYBhtoglDW3BhQUzgIXFQ6uvD7FUshBl38VH+AXZM/BkzGGzpzFSjggSDMIIEfzAOBgNVHQ8BAf8EBAMCBPAwHQYDVR0OBBYEFItxgSnIqbor48DVSfsV11JpIwXDMIIBiAYDVR0jBIIBfzCCAXuAFD7vGT8PuXmw8eYpIaPkuZW5pe6QoYIBTqSCAUowggFGMRgwFgYFKoUDZAESDTEyMzQ1Njc4OTAxMjMxGjAYBggqhQMDgQMBARIMMDAxMjM0NTY3ODkwMSkwJwYDVQQJDCDQodGD0YnQtdCy0YHQutC40Lkg0LLQsNC7INC0LiAyNjEXMBUGCSqGSIb3DQEJARYIY2FAcnQucnUxCzAJBgNVBAYTAlJVMRgwFgYDVQQIDA83NyDQnNC+0YHQutCy0LAxFTATBgNVBAcMDNCc0L7RgdC60LLQsDEkMCIGA1UECgwb0J7QkNCeINCg0L7RgdGC0LXQu9C10LrQvtC8MTAwLgYDVQQLDCfQo9C00L7RgdGC0L7QstC10YDRj9GO0YnQuNC5INGG0LXQvdGC0YAxNDAyBgNVBAMMK9Ci0LXRgdGC0L7QstGL0Lkg0KPQpiDQoNCi0JogKNCg0KLQm9Cw0LHRgSmCEQFyCwFWUAC5s+cRzzq+NHegMB0GA1UdJQQWMBQGCCsGAQUFBwMCBggrBgEFBQcDBDAnBgkrBgEEAYI3FQoEGjAYMAoGCCsGAQUFBwMCMAoGCCsGAQUFBwMEMB0GA1UdIAQWMBQwCAYGKoUDZHEBMAgGBiqFA2RxAjArBgNVHRAEJDAigA8yMDE4MDMwNzA3Mjc1M1qBDzIwMTkwMzA3MDcyNzUzWjCCATQGBSqFA2RwBIIBKTCCASUMKyLQmtGA0LjQv9GC0L7Qn9GA0L4gQ1NQIiAo0LLQtdGA0YHQuNGPIDMuOSkMLCLQmtGA0LjQv9GC0L7Qn9GA0L4g0KPQpiIgKNCy0LXRgNGB0LjQuCAyLjApDGPQodC10YDRgtC40YTQuNC60LDRgiDRgdC+0L7RgtCy0LXRgtGB0YLQstC40Y8g0KTQodCRINCg0L7RgdGB0LjQuCDihJYg0KHQpC8xMjQtMjUzOSDQvtGCIDE1LjAxLjIwMTUMY9Ch0LXRgNGC0LjRhNC40LrQsNGCINGB0L7QvtGC0LLQtdGC0YHRgtCy0LjRjyDQpNCh0JEg0KDQvtGB0YHQuNC4IOKEliDQodCkLzEyOC0yODgxINC+0YIgMTIuMDQuMjAxNjA2BgUqhQNkbwQtDCsi0JrRgNC40L/RgtC+0J/RgNC+IENTUCIgKNCy0LXRgNGB0LjRjyAzLjkpMGUGA1UdHwReMFwwWqBYoFaGVGh0dHA6Ly9jZXJ0ZW5yb2xsLnRlc3QuZ29zdXNsdWdpLnJ1L2NkcC8zZWVmMTkzZjBmYjk3OWIwZjFlNjI5MjFhM2U0Yjk5NWI5YTVlZTkwLmNybDBXBggrBgEFBQcBAQRLMEkwRwYIKwYBBQUHMAKGO2h0dHA6Ly9jZXJ0ZW5yb2xsLnRlc3QuZ29zdXNsdWdpLnJ1L2NkcC90ZXN0X2NhX3J0bGFiczIuY2VyMAgGBiqFAwICAwNBAAfuLimwLO1RNL+ekh4hgnPu+yyLSiF2xGN4yZqWeA4d5VKU2zxveBMmSb4nvJFZ/3Qod1aQDdlgTRObLhKnEO8=</ds:X509Certificate>
                  </ds:X509Data>
               </ds:KeyInfo>
            </ds:Signature>
         </ns2:SMEVSignature>
      </ns2:SendRequestResponse>
   </soap:Body>
</soap:Envelope>
    """ % (message_id, t)
    # Теперь нужно подготовить ответ, на запрос и положить его в Ответы для передачи в ВИС
    # Выписки из ЕГРИП по запросам органов государственной власти, имеющих право на получение закрытых сведений
    if text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                 '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                 '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                 '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1}MessagePrimaryContent/'
                 '{urn://x-artefacts-fns-vipip-tosmv-ru/311-15/4.0.5}FNSVipIPRequest'):
        print(colored('Запрос на Выписки из ЕГРИП по запросам органов государственной власти', 'blue'))
        response = get_file(os.path.join('Шаблоны', 'Ответы', 'ЕГРИП по ИНН ФЛ'))
    # Для организаций Сведения о состоянии расчетов по страх. взносам, пеням и штрафам (ЮЛ)
    elif text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                   '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                   '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                   '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1}MessagePrimaryContent/'
                   '{http://fss.ru/smev-3/rasch_registration/1.0.2}SvedSostRaschRequest'):
        print(colored('Запрос на Сведения о состоянии расчетов по страх. взносам, пеням и штрафам', 'blue'))
        response = get_file(os.path.join('Шаблоны', 'Ответы',
                                         'Cостоянии расчетов по страховым взносам пеням и штрафам'))
    # Предоставление страхового номера индивидуального лицевого счёта (СНИЛС) застрахованного лица с
    # учётом дополнительных сведений о месте рождения, документе, удостоверяющем личность
    elif text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                   '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                   '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                   '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1}MessagePrimaryContent/'
                   '{http://kvs.pfr.com/snils-by-additionalData/1.0.1}SnilsByAdditionalDataRequest'):
        print(colored('Предоставление страхового номера индивидуального лицевого счёта (СНИЛС) застрахованного лица '
                      'с учётом дополнительных сведений о месте рождения, документе, удостоверяющем личность', 'blue'))
        response = get_file(os.path.join('Шаблоны', 'Ответы', 'СНИЛС с доп. данными'))

    # Об ИНН физических лиц на основании полных паспортных данных по единичному запросу органов исполнительной власти
    elif text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1}MessagePrimaryContent/'
                       '{urn://x-artefacts-fns-inn-singular/root/270-18/4.0.1}FNSINNSingularRequest'):
        print(colored('Предоставление ИНН физических лиц на основании полных паспортных данных по единичному запросу '
                      'органов исполнительной власти', 'blue'))
        response = get_file(os.path.join('Шаблоны', 'Ответы',
                                         'ИНН физических лиц на основании полных паспортных данных'))
    # Выписки из ЕГРЮЛ по запросам органов государственной власти
    elif text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1}MessagePrimaryContent/'
                       '{urn://x-artefacts-fns-vipul-tosmv-ru/311-14/4.0.5}FNSVipULRequest'):
        print(colored('Выписки из ЕГРЮЛ по запросам органов государственной власти', 'blue'))
        response = get_file(os.path.join('Шаблоны', 'Ответы',
                                         'Выписки из ЕГРЮЛ по запросам органов государственной власти'))
    # Новые сведения в ЕГРЮЛ или ЕГРИП
    elif text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1}MessagePrimaryContent/'
                   '{urn://x-artefacts-fns-nsvuidat/root/311-31/4.0.0}NSVUIDATRequest') is not None:
        print(colored('Новые сведения в ЕГРЮЛ или ЕГРИП', 'blue'))
        response = get_file(os.path.join('Шаблоны', 'Ответы',
                                         'Новые сведения в ЕГРЮЛ или ЕГРИП'))

    # Сведения об учете организации в налоговом органе по месту нахождения ее обособленного подразделения
    elif text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1}MessagePrimaryContent/'
                       '{urn://x-artefacts-fns-uchorgop-tosmv-ru/370_68/4.0.1}FNSUchOrgOPRequest'):
        print(colored('Сведения об учете организации в налоговом органе по месту нахождения ее'
                      ' обособленного подразделения', 'blue'))
        response = get_file(os.path.join('Шаблоны', 'Ответы',
                                         'Сведения из НО по месту обособленного подразделения'))

    # Сведения о среднесписочной численности работников за предшествующий календарный год
    elif text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1}MessagePrimaryContent/'
                       '{urn://x-artefacts-fns-SRCHIS/082-2/4.0.1}RequestDocument'):
        print(colored('Сведения о среднесписочной численности работников за предшествующий календарный год', 'blue'))
        response = get_file(os.path.join('Шаблоны', 'Ответы',
                                         'Среднесписочная численность работников'))
    # Сведения о налич. (отсут) задолж-ти по уплате налогов, сбор., пеней, штраф
    elif text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1}MessagePrimaryContent/'
                       '{urn://x-artefacts-fns-zadorg/root/548-04/4.0.4}ZadorgRequest'):
        print(colored('Сведения о налич. (отсут) задолж-ти по уплате налогов', 'blue'))
        response = get_file(os.path.join('Шаблоны', 'Ответы',
                                         'Сведения о налич. (отсут) задолж-ти по уплате налогов'))
    # Ответ на заявление по детским
    elif text.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendRequestRequest/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SenderProvidedRequestData/'
                       '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1}MessagePrimaryContent/'
                       '{http://epgu.gosuslugi.ru/hub/familyallowance/3.1.2}FormDataResponse'):
        print(colored('Ответ на заявление по детским', 'blue'))
        response = get_file(os.path.join('Шаблоны', 'Ответы',
                                         'Ответ на заявление КУ по детям'))

    # Неизвестный запрос, ответ на него не даем
    else:
        print(colored('Запрос с неизветсным URI', 'red'))
        response = '''<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body><ns2:GetResponseResponse 
        xmlns="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/basic/1.1" 
        xmlns:ns2="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1" 
        xmlns:ns3="urn://x-artefacts-smev-gov-ru/services/message-exchange/types/faults/1.1"/>
        </soap:Body></soap:Envelope>
        '''

    # Атрибуты для заполнения ответа

    attr = {'MessageID': str(uuid.uuid1()), 'TransactionCode': str(uuid.uuid1()),
            'Timestamp': smev3.time_stamp(), 'OriginalMessageId': original_message_id}
    with open(os.path.join(dir_name, message_id + '.xml'), 'w', encoding='utf-8') as fp:
        fp.write(response.format(**attr))
    return s
