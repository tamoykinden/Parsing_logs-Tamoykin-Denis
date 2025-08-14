import argparse

def par_args():
    """Функция для обработки аргументов"""
    # Создаю "парсер"
    parser = argparse.ArgumentParser()
    # Добавляю аргументы
    parser.add_argument('--file', required=True, nargs='+', help='путь к log-файлу')
    parser.add_argument('--report', choices=['average'], default='average', help='Тип отчета')
    parser.add_argument('--date', help='YYYY-MM-DD')
    # Парсим переданные аргументы
    return parser.parse_args()


