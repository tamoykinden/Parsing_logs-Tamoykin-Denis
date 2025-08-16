from parse_args import par_args
import pytest

def test_par_arg(monkeypatch):
    #Заменяю sys.argv на тестовые значения
    monkeypatch.setattr('sys.argv', ['main.py', '--file', 'example1.log'])

    args = par_args()

    #Проверяю аргументы
    assert args.file == ['example1.log']
    assert args.report == 'average'
    assert args.date is None

def test_par_args_multiple_files(monkeypatch):
    monkeypatch.setattr(
        'sys.argv',
        ['main.py', '--file', 'example1.log', 'example2.log']
    )
    
    args = par_args()
    assert args.file == ['example1.log', 'example2.log']

def test_with_date(monkeypatch):
    monkeypatch.setattr(
        'sys.argv',
        ['main.py', '--file', 'example1.log', '--date', '2025-06-22']
    )
    
    args = par_args()
    assert args.date == '2025-06-22'

#Тест на пропущенный файл
def test_missing_required(monkeypatch):
    monkeypatch.setattr(
        'sys.argv',
        ['main.py', '--report', 'average']
    )
    with pytest.raises(SystemExit):
        par_args()