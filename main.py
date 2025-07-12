from convertor import convertor_csv_to_json 
from convertor import convertor_csv_to_xlsx
from convertor import convertor_json_to_csv
from convertor import convertor_json_to_xlsx
from convertor import convertor_xlsx_to_csv
from convertor import convertor_xlsx_to_json
import os

def main():
    file_path = input("Enter file path: ").strip()
    file_name = os.path.basename(file_path).lower()

    if file_name.endswith(".csv"):
        print("\nDetected: CSV")
        while True:
            print("1  Convert to JSON")
            print("2  Convert to XLSX")
            opt = input("Choice: ").strip()
            if opt == "1":
                convertor_csv_to_json(file_path)
                break
            elif opt == "2":
                convertor_csv_to_xlsx(file_path)
                break
            else:
                print("Invalid option try again.")

    elif file_name.endswith(".json"):
        print("\nDetected: JSON")
        while True:
            print("1  Convert to CSV")
            print("2 Convert to XLSX")
            opt = input("Choice: ").strip()
            if opt == "1":
                convertor_json_to_csv(file_path)
                break
            elif opt == "2":
                convertor_json_to_xlsx(file_path)
                break
            else:
                print("Invalid option try again.")

    elif file_name.endswith(".xlsx"):
        print("\nDetected: XLSX")
        while True:
            print("1  Convert to CSV")
            print("2  Convert to JSON")
            opt = input("Choice: ").strip()
            if opt == "1":
                convertor_xlsx_to_csv(file_path)
                break
            elif opt == "2":
                convertor_xlsx_to_json(file_path)
                break
            else:
                print("Invalid option try again.")

    else:
        print("Unsupported file type.")

if __name__ == "__main__":
    main()

        
        
