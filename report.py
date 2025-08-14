import json
from typing import List, Dict

def read_logs(file_paths: List[str]) -> List[Dict]:
    """Функция для чтения логов"""
    #Создаю список для логов
    logs = []
    #Прохожу по переданным путям и открываем через контекстный менеджер
    for path in file_paths:
        with open(path, 'r') as f:
            for line in f:
                #Десериализую каждую строку и добавляю в список logs
                logs.append(json.loads(line))
    return logs

def filter_by_date(logs:List[Dict], date) -> List[Dict]:
    """Функция для указания даты (доп)"""
    if date:
        for log in logs:
            if log.get('@timestamp', '').startswith(date):
                return log
    else:
        return logs

