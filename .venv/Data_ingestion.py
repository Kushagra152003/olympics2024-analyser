import pandas as pd
import os 


def ingestion():
    file_path=r'C:\Users\Hp\Desktop\olympics2024.csv'
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.csv':
        df = pd.read_csv(file_path)
    elif file_extension == '.json':
        df = pd.read_json(file_path)
    elif file_extension in ['.xls', '.xlsx']:
        df = pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")
    
    
    return df