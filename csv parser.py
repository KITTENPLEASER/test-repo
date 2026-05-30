import time

def timer_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'Вы вызвали функцию.')
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Функция была завершена. Время выполнения: {end - start}мс')
        return result
    return wrapper

@timer_function
def parse_csv(filename: str):
    data = []
    with open(f'{filename}', 'r', encoding='utf-8') as data_filename:
        data_keys = [element.strip() for element in data_filename.readline().split(',')]
        data_elements = [element.strip().split(',') for element in data_filename.readlines()]
        for data_element in data_elements:
            data.append(dict(zip(data_keys, data_element)))
    return data

print(parse_csv('data.csv'))


