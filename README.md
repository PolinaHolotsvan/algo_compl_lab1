# Умови роботи.

## Спільна частина.

Реалізувати структуру даних типу «множина рядків». Рядки – непусті послідовності довжиною до 15 символів з рядкових
латинських літер. Структура даних повинна підтримувати операції додавання рядку до множини, вилучення та перевірки
належності даного рядку множині. Максимальна кількість рядків у множині, що зберігається, не більше 10^6.
Вхідні дані. Кожен рядок вхідних даних задає одну операцію над множиною. Запис операції складається з типу операції та
наступного за ним через пробіл ряду, над яким проводять операцію. Тип операції – символ: «+» - додавання рядку, «-» -
вилучення, «?» - перевірка на належність. Загальні кількість операцій у вхідному файлі не більше 10^6. Список операцій
завершується рядком із символом # (ознака кінця вхідних даних).
При додаванні елементу до множини не гарантується, що він відсутній у множині, а при вилученні елементу з множини не
гарантується, що він є у множині.
Вихідні дані. Виводяться для кожної операції типу «?» рядок yes або no, в залежності від того, чи зустрічається дане
слово у множині.

## Частина за варіантами.

1. Знайти усі повторювані рядки та поділити їх на групи, щоб у кожній групі виводився повторюваний рядок та
   кількість його повторювань. Оцінити час виконання.
2. Знайти усі паліндроми в множині рядків. Оцінити час виконання.
