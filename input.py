import json
import os

FILENAME = "expenses.json"

def load_data():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f)

def main():
    data = load_data()

    while True:
        date = input("日期：")
        amount = float(input("金額："))
        category = input("類別：")
        notes = input("備註（可空）：")

        data.append([amount, category])  

        cont = input("繼續？(y/n)：").lower()
        if cont != "y":
            break

    save_data(data)
    print("已儲存至 expenses.json")

if __name__ == "__main__":
    main()