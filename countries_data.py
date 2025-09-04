# import requests
# import json
# import schedule
# import time

# def fetch_and_save_countries():
#     countries = ["india", "us", "uk", "china", "russia"]
#     for country in countries:
#         response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
#         data = response.json()
#         with open(f"{country}.json", "w") as file:
#             json.dump(data, file, indent=4)
#         print(f"Saved data for {country}")

# # Schedule the job at 00:00 and 12:00 IST
# schedule.every().day.at("00:00").do(fetch_and_save_countries)
# schedule.every().day.at("12:43").do(fetch_and_save_countries)

# print("Scheduler started. Waiting for tasks...")

# while True:
#     schedule.run_pending()
#     time.sleep(30)  # wait 30 seconds between checks



from datetime import datetime
import schedule
import requests
import json
import time

def fetch_and_save_countries():
    print("🚀 Running job at", datetime.now().strftime("%H:%M:%S"))
    countries = ["india", "us", "uk", "china", "russia"]
    for country in countries:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
        data = response.json()
        with open(f"{country}.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"✅ Saved data for {country}")

# Schedule the job at 12:00 AM IST
schedule.every().day.at("00:00").do(fetch_and_save_countries)

# Schedule the job at 12:00 PM IST
schedule.every().day.at("12:00").do(fetch_and_save_countries)

print("🕒 Scheduler started. Waiting for 12:00 AM and 12:00 PM IST...")

while True:
    print("Checking at:", datetime.now().strftime("%H:%M:%S"))
    schedule.run_pending()
    time.sleep(30)  # Check every 30 seconds

