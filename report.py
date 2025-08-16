import json
from typing import List, Dict
from tabulate import tabulate

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
        filter = []
        for log in logs:
            if log.get('@timestamp', '').startswith(date):
                filter.append(log)
                return filter
    else:
        return logs


def gen_rep(file_paths: List[str], report_type: str, date):
    """Функция для генерации отчета лог-файлов"""
    logs = read_logs(file_paths)
    filt_logs = filter_by_date(logs, date)

    end_stats = {}
    for log in filt_logs:
        url = log.get('url') # Получаю url из отфильтрованного по времени лога
        time = log.get('response_time') # Получаю время


        if url not in end_stats:
            end_stats[url]= {
                'count': 0, #Количество запросов
                'total_time': 0 # Время ответа
            }

        #Обновление данных
        end_stats[url]['count'] +=1
        end_stats[url]['total_time']+=time

    #Таблица
    rep_table = []

    for index, (endpoint, data) in enumerate(end_stats.items(), start=1):
        #Рассчитываю среднее время ответа
        avg_time = data['total_time']/data['count']
        #Добавляю индекс
        rep_table.append([index,endpoint,data['count'], avg_time])

    if rep_table:
        return tabulate(rep_table, headers=['id','handler', 'total', 'avg_response_time'], tablefmt='pipe')