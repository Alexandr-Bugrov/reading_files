def counter(*files_names):
    comparer_files = {}
    for file_name in files_names:
        with open(file_name, encoding='utf-8') as file:
            data = file.readlines()
            number_of_lines = len(data)
            comparer_files[file_name] = number_of_lines
    return comparer_files


def reader(file_name):
    with open(file_name, encoding='utf-8') as file:
        data = file.read()
        return data


def get_key(dictionary, your_value):
    for key, value in dictionary.items():
        if your_value == value:
            return key


def sorting_writer(*files_names):
    writable_files = counter(*files_names)
    lines = []
    for line in writable_files.values():
        lines.append(line)
    lines = sorted(lines)
    for line in lines:
        with open('4.txt', 'a', encoding='utf-8') as written_file:
            written_file.write(f'{get_key(writable_files, line)}\n')
            written_file.write(f'{line}\n')
            written_file.write(f'{reader(get_key(writable_files, line))}\n')


sorting_writer('1.txt', '2.txt', '3.txt')