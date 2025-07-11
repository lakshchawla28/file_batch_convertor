import pandas as pd
import os


def convertor_csv_to_json(file_path):
    df = pd.read_csv(file_path)
    base = os.path.splitext(os.path.basename(file_path))[0]
    out = base + ".json"
    df.to_json(out, orient="records", indent=2)
    print(f" JSON file created: {out}")

def convertor_csv_to_xlsx(file_path):
    df = pd.read_csv(file_path)
    base = os.path.splitext(os.path.basename(file_path))[0]
    out = base + ".xlsx"
    df.to_excel(out, index=False)
    print(f" XLSX file created: {out}")

def convertor_json_to_csv(file_path):
    df = pd.read_json(file_path)
    base = os.path.splitext(os.path.basename(file_path))[0]
    out = base + ".csv"
    df.to_csv(out, index=False)
    print(f" CSV file created: {out}")

def convertor_json_to_xlsx(file_path):
    df = pd.read_json(file_path)
    base = os.path.splitext(os.path.basename(file_path))[0]
    out = base + ".xlsx"
    df.to_excel(out, index=False)
    print(f" XLSX file created: {out}")


def convertor_xlsx_to_csv(file_path):
    df = pd.read_excel(file_path)
    base = os.path.splitext(os.path.basename(file_path))[0]
    out = base + ".csv"
    df.to_csv(out, index=False)
    print(f"CSV file created: {out}")

def convertor_xlsx_to_json(file_path):
    df = pd.read_excel(file_path)
    base = os.path.splitext(os.path.basename(file_path))[0]
    out = base + ".json"
    df.to_json(out, orient="records", indent=2)
    print(f"JSON file created: {out}")
    