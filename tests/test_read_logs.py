from report import read_logs

def test_read_logs_have():
    logs = read_logs(['example1.log', 'example2.log'])

    #Проверка что логи есть
    assert len(logs) > 0

def test_log_str():
    logs = read_logs(['example1.log', 'example2.log'])

    #Проверка основных полей
    first_log = logs[0]

    assert 'url' in first_log
    assert 'response_time' in first_log
    assert '@timestamp' in first_log

def test_log_url():
    logs = read_logs(['example1.log', 'example2.log'])

    #Провека url
    foun_cont = False

    for log in logs:
        if log['url'].startswith('/api/context'):
            foun_cont = True
            break
    
    assert foun_cont is True

