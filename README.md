Эмулятор СМЭВ-3
===============

Установка
---------
1. Для работы эмулятора нужен Python3, у меня версия 3.7, 
но вероятно, будет работать и на более низких. Установить с оф. сайта.
2. Скопируйте репозитарий к себе на компьютер.
3. Запустите файл main.py. Должен написать:
```
    starting server...
    running server...
```    
Если выдал, значит работает. Остановить программу, переходите к настройке.

Настройка
---------
1. В папке `Шаблоны` найдите файл `wsdl.xml`. Укажите в строке 
```<soap:address location="http://192.168.0.130:8081/"/>```
свой IP адрес.
2. В папку `Шаблоны\Запросы к нам` скопируйте запросы, которые нужно 
отправлять. Обратите внимание, что шаблон для аккуратной работы желательно
(но не обязательно) подготовить - указать переменные для заполения 
UUID и Timestamp (в примере они {})
3. На ТИ  в задаче `Сервис -> Настройка СМЭВ 3` укаите URL адрес WSDL как 
`http://192.168.0.130:8081/smev3`


Принцип работы
--------------
1. На любой GET запрос запущенный эмулятор отвечает своей WSDL. Которая 
потом будет использована ТИ для отправки запросов, поэтому настройте ее
правильно.
2. Эмулятор может отпработать сценарий предоставления запросов для ВИС,
реагирую на следующие запросы.
3. SendRequest - получив начинает обрабатывать папку `Запросы к нам`:
   * если папка пуста, то говорит, что запросов нет. И заполняет папку из
   `Шаблоны/Запросы к нам`
   * если не пуста, то отдает первый запрос и удаляет его. 
4. Получив подтверждение запрос на подтверждение `ACK` всегда 
подтверждает.
5. Получив ответ от ВИС `GetResponse` всегда подтверждает получение.

Отправка запросов в ВИС
-----------------------
Чтобы направить запросы в ВИС скопируйте их в папку `Шаблоны\Запросы к нам`. 
Для аккуратной работы сделайте в них переменные для подстановки uuid и даты,
см. образец в этой папке (поиск {})

Предоставление ответов
----------------------
Ответы предоставлять несколько сложнее.
1. Для каждого вида ответов надо завести отдельную папку в `Шаблоны\Ответы`
2. В папку скопировать ответы (если несколько то отдает в случайном порядке)
3. В функции send_request (файл sendRequest.py) нужно добавлять отбработчики 
для каждого ВС (по namespace) и указывать обработчику папку с ответами.
 
**Сейчас эмулятор может предоставлять ответы по следующим ВС:**
1. Выписки из ЕГРИП по запросам органов государственной власти, имеющих право на получение закрытых сведений 
(urn://x-artefacts-fns-vipip-tosmv-ru/311-15/4.0.5)
2. Сведения о состоянии расчетов по страх. взносам, пеням и штрафам 
(http://fss.ru/smev-3/rasch_registration/1.0.2)
3. Предоставление страхового номера индивидуального лицевого счёта (СНИЛС) 
застрахованного лица с учётом дополнительных сведений о месте рождения, документе, 
удостоверяющем личность (http://kvs.pfr.com/snils-by-additionalData/1.0.1)
4. Об ИНН физических лиц на основании полных паспортных данных по единичному запросу
 органов исполнительной власти (urn://x-artefacts-fns-inn-singular/root/270-18/4.0.1)
5. Выписки из ЕГРЮЛ по запросам органов государственной власти (urn://x-artefacts-fns-vipul-tosmv-ru/311-14/4.0.5)
6. Новые сведения в ЕГРЮЛ или ЕГРИП (urn://x-artefacts-fns-nsvuidat/root/311-31/4.0.0)
7. Сведения об учете организации в налоговом органе по месту нахождения ее 
обособленного подразделения (urn://x-artefacts-fns-uchorgop-tosmv-ru/370_68/4.0.1)
8. Сведения о среднесписочной численности работников за предшествующий календарный 
год (urn://x-artefacts-fns-SRCHIS/082-2/4.0.1)
  
  
   