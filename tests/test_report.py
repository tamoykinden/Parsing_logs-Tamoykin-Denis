from report import gen_rep

def test_gen(tmp_path):
    """Тест с минимальным набором данных"""
    test_file = tmp_path / "test.log"
    test_file.write_text('{"url": "/api/test1", "response_time": 0.1, "@timestamp": "2025-06-22T10:00:00"}')
    result = gen_rep([str(test_file)], 'average', None)
    # Проверrf основных элементов
    assert "id" in result
    assert "handler" in result
    assert "/api/test" in result
    assert "0.1" in result  # Среднее время для одного запроса

def test_gen_rep_with_date(tmp_path):
    """Тест фильтрации по дате"""
    # Создаю файл с разнымидатами
    test_file = tmp_path / "test.log"
    test_file.write_text(
        '{"url": "/api/test1", "response_time": 0.1, "@timestamp": "2025-06-22T10:00:00"}\n'
        '{"url": "/api/test2", "response_time": 0.2, "@timestamp": "2025-06-23T10:00:00"}\n'
    )
    
    # Фильтр на 22 июня
    result = gen_rep([str(test_file)], "average", "2025-06-22")
    
    assert "/api/test1" in result
    assert "/api/test2" not in result  