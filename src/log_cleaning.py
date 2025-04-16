import re

def clean_log(log):
    '''Removes unnecessary characters, lowercases, and deletes extra space in a 
    singular log.'''

    log = log.strip().lower()
    log = re.sub(r'\s+', ' ',log)
    log = re.sub(r'[^a-zA-Z0-9\s,.?!]','',log)

    return log

def clean_logs(logs):
    '''Removes duplicate and short logs'''

    cleaned_logs = list(set(clean_log(log) for log in logs))
    cleaned_logs = [log for log in cleaned_logs if len(log)>5]

    return cleaned_logs