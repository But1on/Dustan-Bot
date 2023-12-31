# Телеграм-бот для сообщества Destiny 2
Данный код представляет собой телеграм-бота (далее `тг-бот`) для создания билдов для игры `Destiny 2`.

## Краткое описание функционала:
Данный бот дает пользователю несколько функций в распоряжение:
- Во-первых - это первоначальные `вход / регистрация` пользователя в `базу / базе`
- Во-вторых - это непосредственно создание билдов, это занимает довольно много времени, но благодаря этому бот не превысит лимит сообщений (надеюсь)
- В-третьих - это просмотр билдов, как своих, так и всех созданных
- В-четвертых - это система рейтинга, каждый пользователь может оценить билды, кроме своих, чтобы приблизиться к объективности и накинуть фишек
- В-пятых - это возможность удалять свои аккаунты, а также сборки (функция пока не доработана)

## Используемые библиотеки:
- `telebot` - библиотека для работы с телеграммом и связи программы и тг-бота
- `qlite3` - встроенная библеотека для работы с базой данных
- `os` - встроенная библиотека для работы с директориями файлов

## Установка библеотеки telebot:
Установить можно либо через команду `pip install telebot`, либо через `python -m pip install telebot`

## Пояснение за эксплуатацию:
Самое главное - чтобы файлы лежали в таких же дирикториях, как здесь, ведь программа ищет картинки исключительно на позицию ниже. В остальном - ваша задача установить все содержимое, `поменять токен бота`, чтобы не запустить чужого, а затем запустить программу. 
Переходим в бота и наслаждаемся.

## Использование бота:
Пользователь бота всегда будет объят неотступающей заботой, ведб ничего, кроме предложенных кнопок бот пользователю не разрешит делать, в редких случаях нужна будет клавиатура, но это сккорее исключение. Управление простое и интуитивно понятное. 
Надеюсь этот был полезен, приятной эксплуатации!
