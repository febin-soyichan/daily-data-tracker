import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "productivity_data.csv"
IMAGE_FILE = "productivity_trend.png"

def log_daily_data():
    print("--- 📊 Daily Data Entry ---")
    date_str = datetime.today().strftime("%Y-%m-%d")
    try:
        screen_time = float(input("Enter today's phone/screen time (in hours): "))
        focus_hours = float(input("Enter today's focused work/study time (in hours): "))
        productivity_rating = int(input("Rate your productivity today (1 to 10): "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return False

    new_data = pd.DataFrame([{
        "Date": date_str,
        "Screen_Time_Hours": screen_time,
        "Focus_Hours": focus_hours,
        "Productivity_Rating": productivity_rating
    }])

    if not os.path.exists(CSV_FILE):
        new_data.to_csv(CSV_FILE, index=False)
    else:
        new_data.to_csv(CSV_FILE, mode="a", header=False, index=False)
    
    print("✅ Data logged successfully!")
    return True

def generate_insights_and_plots():
    if not os.path.exists(CSV_FILE): return
    df = pd.read_csv(CSV_FILE)
    print("\n--- 📈 Current Insights ---")
    print(f"Total days tracked: {len(df)}")
    print(f"Average Daily Screen Time: {df['Screen_Time_Hours'].mean():.1f} hrs")
    print(f"Average Daily Focus Time: {df['Focus_Hours'].mean():.1f} hrs")

    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Screen_Time_Hours"], marker="o", label="Screen Time", color="crimson")
    plt.plot(df["Date"], df["Focus_Hours"], marker="s", label="Focus Hours", color="seagreen")
    plt.title("Screen Time vs. Focus Hours Over Time")
    plt.xlabel("Date")
    plt.ylabel("Hours")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(IMAGE_FILE)
    plt.close()
    print("📉 Chart updated successfully!")

if __name__ == "__main__":
    if log_daily_data():
        generate_insights_and_plots()
