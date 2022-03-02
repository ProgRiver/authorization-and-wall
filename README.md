### Авторизация пользователя и размещение записи на стене.
___
![Python](https://img.shields.io/pypi/pyversions/pip?color=g&label=Python%20version&style=plastic)
![pip](https://img.shields.io/pypi/v/pip?style=plastic)
___
Установить `Python` можно на официальном [сайте](https://www.python.org/downloads/).
___
Код написан с применением библиотеки `Selenium`

Некоторые настройки:

+ для установки выполнить команду
```
pip install selenium==3.14.0
```
+ проверить установленную версию библиотеки
```
pip list
```
+ скачать и установить [ChromeDriver](https://chromedriver.chromium.org/downloads) (версия должна соответствовать версии вашего браузера Chrome)

___
В коде необходимо использовать ваши данные при регистрации на сайте:

+ заменить ***config.user_email*** на ваш email или телефон
+ заменить ***config.password*** на ваш пароль

Текст вашей публикации в переменной ***post_text***

Проверьте селекторы, т.к. могут быть изменения.
___
Успехов :hand:
___
