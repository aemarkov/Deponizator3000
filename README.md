# Deponizator3000
Осуществляет депонирование исходного кода программы (копирование в один файл)

## Возможности
 - Считывает все файлы указанных расширений в указанных директориях и собирает их в один выходной файл
 - В выходном файле перед текстом каждого файла указывается путь к нему
 - Игнорирование указанных директорий
 - Файлы с одинаковыми именами, но разными расширениями ранжируются в порядке указания расширений в аргументах. Например, указав '.h, .cpp',
 сначала будут выводиться заголовочные файлы, а затем файлы исходного кода
 
## Использование
```
usage: deponizator.py [-h] -d dir [dir ...] -o result.txt [-e .ext [.ext ...]]
                      [-ignore dir [dir ...]] [-c config.ini]

Собирает все файлы в один

optional arguments:
  -h, --help            show this help message and exit
  -d dir [dir ...]      Список директорий, в которых осуществляется сбор
                        файлов
  -o result.txt         Выходной файл

Фильтрация при помощи командной строки:
  -e .ext [.ext ...]    Список разрешенных расширений файлов. Если не указан -
                        будут добавлены все
  -ignore dir [dir ...]
                        Список игнорируемых директорий
  ```
  
## Известные проблемы
   - Не работает поддержка конфигурационных файлов для фильтрации
   - Некоторые символы могут считываться некорректно
   - Нельзя считывать файлы всех расширений без их указания

## Системные требования
 - Python 3
 
 
 ## Do What The Fuck You Want To Public License ![](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-2.png)
```
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
```
```
Марков Алексей, 2018
```
