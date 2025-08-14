import json

def read_logs(file_paths):
    logs = []
    for path in file_paths:
        with open(path, 'r') as f:
            for line in f:
                logs.append(json.loads(line))
    return logs
