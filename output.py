import json
import os
from collections import defaultdict

import matplotlib.pyplot as plt

FILENAME = "expenses.json"


def load_data():
    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)


def summarize_by_category(data):
    totals = defaultdict(float)

    for item in data:
        # 保險一點：防止資料格式怪怪的
        if not isinstance(item, (list, tuple)) or len(item) < 2:
            continue

        amount, category = item[0], item[1]

        # 嘗試把金額轉成 float，轉不動就略過
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            continue

        # 類別轉成字串（避免 None 或其他型別）
        category = str(category)
        totals[category] += amount

    return dict(totals)


def plot_pie(totals):
    if not totals:
        print("沒有可視覺化的資料")
        return

    labels = list(totals.keys())
    values = list(totals.values())

    # 避免全部都是 0 元的極端情況
    total_amount = sum(values)
    if total_amount == 0:
        print("無法繪製圓餅圖。")
        return

    plt.figure()
    plt.title("category chart")
    plt.pie(
        values,
        labels=labels,
        autopct="%.1f%%", 
        startangle=90,      
    )
    plt.axis("equal")       
    plt.tight_layout()
    plt.show()


def main():
    data = load_data()
    totals = summarize_by_category(data)


    if not totals:
        print("沒有任何支出資料可以顯示")
        return

    print("各類別總金額：")
    for category, amount in totals.items():
        print(f"- {category}: {amount:.2f}")

    # 繪製圓餅圖
    plot_pie(totals)


if __name__ == "__main__":
    main()
