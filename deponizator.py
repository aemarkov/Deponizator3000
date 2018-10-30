import sys
import os
import configparser
import argparse

# Проверяет, что путь соответствует фильтрам
def is_ignored(filename):
    for ignore_dir in ignore_dirs:
        if filename.startswith(ignore_dir):
            return True
    
    _, cur_ext = os.path.splitext(filename) 
    return cur_ext not in extensions
    
# Сохраняет список файлов в порядке, указанным списком расширений   
def read_file(filenames, res_file):
    if len(filenames)==0:
        return 0

    size = 0
        
    for ext in extensions:
        file = list(filter(lambda x: x[1] == ext, filenames))
        if len(file) == 0:
            continue
    
        filename = file[0][0] + file[0][1]
        print(filename)
        with open(filename, 'r', errors='ignore') as f:
            content = f.read()
            res_file.write('###################\n')
            res_file.write('{}:\n'.format(filename))
            res_file.write('###################\n\n')
            res_file.write(content)
            res_file.write('\n\n')
        
        size += os.stat(filename).st_size
    
    return size

# Рекурсивно считывает все файлы в каталоге
def parse_dir(directory, res_file):

    same_files = []
    same_file_name = ''
    total_size = 0

    tree = os.walk(directory)
    for path, _, files in tree:     
        for file in files:      
            full_path = os.path.join(path, file)
            if is_ignored(full_path):
                continue
            
            filename, ext = os.path.splitext(full_path)
            
            # Собираем одинаковые имена с разными расширениями
            if filename == same_file_name:
                same_files.append((filename, ext))
            else:               
                total_size += read_file(same_files, res_file)
                same_files = [(filename, ext)]
                same_file_name = filename
            

    return total_size

# Парсит параметры фильтрации из конфига
def parse_config(config_filename):
    raise NotImplementedError()

    
if __name__ == '__main__':  
    parser = argparse.ArgumentParser(description = 'Собирает все файлы в один')
    parser.add_argument('-d', type=str, nargs='+', metavar='dir', required=True, help='Список директорий, в которых осуществляется сбор файлов')
    parser.add_argument('-o', type=str, metavar='result.txt', required=True, help='Выходной файл')

    filter_group = parser.add_argument_group('Фильтрация')

    params_group = parser.add_argument_group('При помощи командной строки')
    params_group.add_argument('-e',  type=str, nargs='+', metavar='.ext', required=False, help='Список разрешенных расширений файлов. Если не указан - будут добавлены все')
    params_group.add_argument('-ignore', type=str, nargs='+', metavar='dir', required = False, help='Список игнорируемых директорий')

    config_group = parser.add_argument_group('При помощи конфигурационного файла')
    config_group.add_argument('-c', type=str, metavar='config.ini',  help='Конфигурационный файл')

    args = parser.parse_args()

    search_dirs = args.d
    output_file = args.o
    extensions = args.e
    ignore_dirs = args.ignore

    if args.c:
        #extensions, ignore_dirs = parse_config(args.c)
        print('Конфигурационные файлы пока не поддерживаются')
        exit(0)
                
    total_size = 0
                
    with open(output_file, 'w') as res_file:
        for dir in search_dirs:
            total_size += parse_dir(dir, res_file)
            
    print('{} kB'.format(int(total_size/1024)))

