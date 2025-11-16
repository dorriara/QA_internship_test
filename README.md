# Тестовое задание для стажировки по направлению QA Avito

Выполнение тестовых заданий 1 и 2.1  

Директория проекта:  
```
QA_internship_test
│   BUGS.md               # баг-репорты задания 2.1  
│   Bugs.png  
│   Bugs_task_1.md        # баг-репорты задания 1  
│   postman_collection.json  
│   Task.md  
│   TESTCASES.md          # тест-кейсы задания 2.1  
├───img                   # папка со скринами к файлу Bugs_task_1.md  
└───Task2                 # реализация автотестов задания 2.1  
    │   conftest.py  
    │   requirements.txt  
    │   __init__.py  
    ├───data  
    │       test_data.py  
    │       __init__.py  
    ├───tests  
    │       test_create.py  
    │       test_delete.py  
    │       test_get.py  
    │       test_get_by_sellerid.py  
    │       test_get_statistics.py  
    │       test_others.py  
    │       __init__.py  
    └───utils  
           api_client.py  
           __init__.py
```
    
## Установка

1. Склонируйте репозиторий  
2. Перейдите в папку Task2, cоздайте и активируйте виртуальное окружение:
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```
3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

## Запуск тестов

Запустите тесты:
  ```
  pytest tests\ --tb=no -q
  ```
Данная команда запускает тесты в сокращенном виде, чтобы не засорять консоль. На все упавшие тесты оформлены баг-репорты в файле BUGS.md  

