# YaTube_API

![1678783996391](image/README/1678783996391.png)

### **Проект выполнен в рамках обучения в YandexPracticum.**

API часть проекта YaTube выполнена согласно представленной в ТЗ документации, оформленой по стандартам OpenAPI в виде ReDoc веб станицы. Для соблюдения принципов DRY и SOLID в разработке используются Rest_framework ViewSet, Generics, Mixins. Для авторизации применяются JWT токены.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Bigbrotherx/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3.9 -m venv env
```

* Если у вас Linux/macOS

  ```
  source env/bin/activate
  ```
* Если у вас windows

  ```
  source env/scripts/activate
  ```

```
python3.9 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
