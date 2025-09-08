import json
from src.utils import reader_products
from tests.conftest_utils import correct_data


# Вспомогательная функция для создания файла
def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(content, file)

# Тест №1 чтение правильного JSON файл
def test_reader_correct_data(correct_data):

    filename = 'test_correct_data.json'
    write_to_file(filename, correct_data)
    result = reader_products(filename)
    assert len(result.keys()) == 2

# Тест №2 обработка отсутствующего файла
def test_reader_nonexistent_file():
    non_existent_file_path = "/path/to/nonexistent/file.json"
    result = reader_products(non_existent_file_path)
    assert result == {}, "При несуществующем файле должна возвращаться пустая структура"