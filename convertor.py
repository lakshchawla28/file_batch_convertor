import pandas as pd
import os

def convertor_csv_to_json(file_obj):
    file_obj.seek(0)
    df = pd.read_csv(file_obj)
    base = os.path.splitext(file_obj.name)[0]
    out = base + ".json"
    df.to_json(out, orient="records", indent=2)
    return out

def convertor_csv_to_xlsx(file_obj):
    file_obj.seek(0)
    df = pd.read_csv(file_obj)
    base = os.path.splitext(file_obj.name)[0]
    out = base + ".xlsx"
    df.to_excel(out, index=False)
    return out

def convertor_json_to_csv(file_obj):
    file_obj.seek(0)
    df = pd.read_json(file_obj)
    base = os.path.splitext(file_obj.name)[0]
    out = base + ".csv"
    df.to_csv(out, index=False)
    return out

def convertor_json_to_xlsx(file_obj):
    file_obj.seek(0)
    df = pd.read_json(file_obj)
    base = os.path.splitext(file_obj.name)[0]
    out = base + ".xlsx"
    df.to_excel(out, index=False)
    return out

def convertor_xlsx_to_csv(file_obj):
    file_obj.seek(0)
    df = pd.read_excel(file_obj)
    base = os.path.splitext(file_obj.name)[0]
    out = base + ".csv"
    df.to_csv(out, index=False)
    return out

def convertor_xlsx_to_json(file_obj):
    file_obj.seek(0)
    df = pd.read_excel(file_obj)
    base = os.path.splitext(file_obj.name)[0]
    out = base + ".json"
    df.to_json(out, orient="records", indent=2)
    return out
