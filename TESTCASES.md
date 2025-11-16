# Задание 2.1 – Баг-репорт

*Примечание: Помимо заявленных ручек при анализе postman-коллекции был найден функционал для удаления объявления. Также функция получения статистики по id представлена в 2-х версиях API. Дальнейшее тестирование будет проводится с учетом данных моментов.*

## 1. Создание объявления
___

**ID**: TC1  
**Название**: Создание объявления со всеми полями  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c корректным JSON
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Проверка ответа на наличие ID

**Ожидаемый результат**: HTTP 200 и сообщение с ID  
**ID бага**: -
___

**ID**: TC2  
**Название**: Создание объявления без поля sellerID  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c JSON без поля sellerID
```json
{
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```

**Ожидаемый результат**: HTTP 400 и сообщение об обязательности поля sellerID   
**ID бага**: -
___

**ID**: TC3  
**Название**: Создание объявления без поля name  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c JSON без поля name
```json
{
    "sellerID": 111121,
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```

**Ожидаемый результат**: HTTP 400 и сообщение об обязательности поля name   
**ID бага**: -
___

**ID**: TC4  
**Название**: Создание объявления без поля price  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c JSON без поля price
```json
{
    "sellerID": 111121,
    "name": "Test Item"
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```

**Ожидаемый результат**: HTTP 400 и сообщение об обязательности поля price   
**ID бага**: -
___

**ID**: TC5  
**Название**: Создание объявления без поля statistics  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c JSON без поля statistics
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100
}
```

**Ожидаемый результат**: HTTP 200 или 201 и сообщение с ID   
**ID бага**: BR1
___

**ID**: TC6  
**Название**: Создание объявления c некорректным sellerID  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c JSON с sellerID вне диапазона 111111-999999
```json
{
    "sellerID": 11111,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c JSON с sellerID строкой
```json
{
    "sellerID": "aaaaaa",
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c JSON с пустым sellerID
```json
{
    "sellerID": "",
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```

**Ожидаемый результат**: HTTP 400   
**ID бага**: BR2
___

**ID**: TC7  
**Название**: Создание объявления с некорректным price  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c JSON с отрицательным price
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": -100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c JSON с price строкой
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": "aaa",
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c JSON с пустым price
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": "",
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```

**Ожидаемый результат**: HTTP 400   
**ID бага**: BR3
___

**ID**: TC8  
**Название**: Создание объявления с некорректными параметрами statistics  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c JSON c likes отрицательным числом
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": -10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c JSON c viewCount отрицательным числом
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": -15,
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c JSON c contacts отрицательным числом
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": -3
    }
}
```
* Отправка POST /api/1/item c JSON c likes строкой
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": "aaa",
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c JSON c viewCount строкой
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": "aaa",
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c JSON c contacts строкой
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": "aaa"
    }
}
```
* Отправка POST /api/1/item c JSON c пустым likes
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": "",
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c JSON c пустым viewCount
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": "",
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c JSON c пустым contacts
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": ""
    }
}
```
* Отправка POST /api/1/item c JSON c statistics пустым массивом
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {}
}
```

**Ожидаемый результат**: HTTP 400   
**ID бага**: BR4, BR5, BR6
___

**ID**: TC9  
**Название**: Создание объявления с лишним полем  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c JSON c дополнительным полем extra
```json
{
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    },
    "extra": 100
}
```

**Ожидаемый результат**: HTTP 400 и сообщение о некорректном JSON   
**ID бага**: BR7
___

**ID**: TC10  
**Название**: Запрос на создание с пустым JSON  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c пустым JSON

**Ожидаемый результат**: HTTP 400 и сообщение о некорректном JSON   
**ID бага**: -
___


## 2. Получение объявления по идентификатору
___

**ID**: TC11  
**Название**: Получение объявления по корректному ID  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c корректным JSON
```json
{
    "sellerID": 111122,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Получить ID из ответа
* Отправка GET /api/1/item/:id с полученным ID


**Ожидаемый результат**: HTTP 200 и сообщение с отправленным JSON   
**ID бага**: -
___

**ID**: TC12  
**Название**: Получение объявления по несуществующему ID  
**Шаги воспроизведения**: 
* Отправка GET /api/1/item/:id с несуществующему ID «aa111111-aa1a-1a11-a111-a11a111111aa»


**Ожидаемый результат**: HTTP 404 и сообщение о ненайденном объявлении   
**ID бага**: -
___

**ID**: TC13  
**Название**: Получение объявления по некорректному ID  
**Шаги воспроизведения**: 
* Отправка GET /api/1/item/:id с некорректным ID «123123»


**Ожидаемый результат**: HTTP 400 и сообщение ID не соответствует UUID   
**ID бага**: -
___

## 3. Получение всех объявлений по идентификатору продавца
___

**ID**: TC14  
**Название**: Получение объявлений по sellerID продавца с 0 объявлений  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c корректным JSON
```json
{
    "sellerID": 111123,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Получить ID из ответа  
* Отправка DELETE /api/2/item/:id с полученным ID  
* Отправка GET /api/1/:sellerID/item с sellerID, заданным в JSON п.1  


**Ожидаемый результат**: HTTP 200 и пустой массив   
**ID бага**: -
___

**ID**: TC15  
**Название**: Получение объявлений по sellerID продавца с 1 объявлением  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c корректным JSON
```json
{
    "sellerID": 111127,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка GET /api/1/:sellerID/item с sellerID, заданным в JSON п.1  


**Ожидаемый результат**: HTTP 200 и массив с отправленным JSON   
**ID бага**: -
___

**ID**: TC16  
**Название**: Получение объявлений по sellerID продавца с объявлениями более 1  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c корректным JSON
```json
{
    "sellerID": 111124,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c корректным JSON и sellerID, заданным в JSON п.1
```json
{
    "sellerID": 111124,
    "name": "Test Item 2",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка POST /api/1/item c корректным JSON и sellerID, заданным в JSON п.1
```json
{
    "sellerID": 111124,
    "name": "Test Item 3",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка GET /api/1/:sellerID/item с sellerID, заданным в JSON п.1  


**Ожидаемый результат**: HTTP 200 и массив с отправленными JSON   
**ID бага**: -
___

**ID**: TC17  
**Название**: Получение объявлений по некорректному sellerID  
**Шаги воспроизведения**: 
* Отправка GET /api/1/:sellerID/item c некорректным sellerID «11111»
* Отправка GET /api/1/:sellerID/item c некорректным sellerID «aaaaaa»  


**Ожидаемый результат**: HTTP 400 и сообщение о некорректном sellerID   
**ID бага**: BR8
___

## 4. Получение статистики по объявлению
___

**ID**: TC18  
**Название**: Получение статистики по корректному ID для API v.1  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c корректным JSON
```json
{
    "sellerID": 111125,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Получить ID из ответа  
* Отправка GET /api/1/statistic/:id с полученным ID  
 

**Ожидаемый результат**: HTTP 200 и массив со статистикой из отправленного JSON   
**ID бага**: -
___

**ID**: TC19  
**Название**: Получение статистики по некорректному ID для API v.1  
**Шаги воспроизведения**: 
* Отправка GET /api/1/statistic/:id с некорректным ID «123123»  
 

**Ожидаемый результат**: HTTP 400 и сообщение о некорректном ID    
**ID бага**: -
___

**ID**: TC20  
**Название**: Получение статистики по несуществующему ID для API v.1  
**Шаги воспроизведения**: 
* Отправка GET /api/1/statistic/:id с несуществующему ID «aa111111-aa1a-1a11-a111-a11a111111aa»  
 

**Ожидаемый результат**: HTTP 404 и сообщение о ненайденном объявлении    
**ID бага**: -
___

**ID**: TC21  
**Название**: Получение статистики по корректному ID для API v.2  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c корректным JSON
```json
{
    "sellerID": 111125,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Получить ID из ответа  
* Отправка GET /api/2/statistic/:id с полученным ID  
 

**Ожидаемый результат**: HTTP 200 и массив со статистикой из отправленного JSON   
**ID бага**: -
___

**ID**: TC22  
**Название**: Получение статистики по некорректному ID для API v.2  
**Шаги воспроизведения**: 
* Отправка GET /api/2/statistic/:id с некорректным ID «123123»  
 

**Ожидаемый результат**: HTTP 400 и сообщение о некорректном ID    
**ID бага**: BR9
___

**ID**: TC23  
**Название**: Получение статистики по несуществующему ID для API v.2  
**Шаги воспроизведения**: 
* Отправка GET /api/2/statistic/:id с несуществующему ID «aa111111-aa1a-1a11-a111-a11a111111aa»  
 

**Ожидаемый результат**: HTTP 404 и сообщение о ненайденном объявлении    
**ID бага**: -
___

## 5. Удаление объявления
___

**ID**: TC24  
**Название**: Удаление объявления по корректному ID  
**Шаги воспроизведения**: 
* Отправка POST /api/1/item c корректным JSON
```json
{
    "sellerID": 111126,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Получить ID из ответа  
* Отправка DELETE /api/2/item/:id с полученным ID
* Отправка GET /api/1/item/:id с полученным ID
  

**Ожидаемый результат**: HTTP 200 на запрос DELETE и HTTP 404 на запрос GET   
**ID бага**: -
___

**ID**: TC25  
**Название**: Удаление объявления по некорректному ID  
**Шаги воспроизведения**: 
* Отправка DELETE /api/2/item/:id с некорректным ID «123123»  
 

**Ожидаемый результат**: HTTP 400 и сообщение о некорректном ID    
**ID бага**: -
___

**ID**: TC26  
**Название**: Удаление объявления по несуществующему ID  
**Шаги воспроизведения**: 
* Отправка DELETE /api/2/item/:id с несуществующему ID «aa111111-aa1a-1a11-a111-a11a111111aa»  
 

**Ожидаемый результат**: HTTP 404    
**ID бага**: -
___

## 6. Прочие тесты
___

**ID**: TC27  
**Название**: Запрос с HTTP-методом PUT  
**Шаги воспроизведения**: 
* Отправка PUT /api/1/item c корректным JSON
```json
{
    "sellerID": 111126,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
* Отправка PUT /api/2/item c корректным JSON
```json
{
    "sellerID": 111126,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
```
  

**Ожидаемый результат**: HTTP 405   
**ID бага**: BR10
___

**ID**: TC28  
**Название**: Запрос на несуществующий endpoint  
**Шаги воспроизведения**: 
* Отправка GET /api/1/test
* Отправка GET /api/2/test
 

**Ожидаемый результат**: HTTP 404    
**ID бага**: -
___