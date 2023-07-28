import os
import glob
from collections import defaultdict, Counter
from heapq import nlargest
from datetime import datetime, timedelta

# Function to process the daily log
def process_daily_log(file_name, date):
    country_song_counts = defaultdict(Counter)

    # Open file and read line by line
    with open(file_name, 'r') as file:
        for line in file:
            # Check if line respects the expected format
            try:
                sng_id, user_id, country = line.strip().replace(" ", "").split('|')
                sng_id = int(sng_id)
                user_id = int(user_id)
                assert len(country) == 2
            except (ValueError, AssertionError):
                # Line is corrupted, continue with the next one
                continue

            # Update count for song in the corresponding country
            country_song_counts[country][sng_id] += 1

    # For each country, keep a list of the 50 top songs and write to a file
    for country, song_counts in country_song_counts.items():
        top_songs = nlargest(50, song_counts.items(), key=lambda item: item[1])
        with open(f'country_top50_logs/{date.strftime("%Y%m%d")}/{country}_{date.strftime("%Y%m%d")}.txt', 'w') as file:
            file.write(f'{country}|' + ','.join([f'{sng_id}:{count}' for sng_id, count in top_songs]))

# Function to compute the top 50 songs for the last 7 days for each country
def compute_weekly_top50(date):
    last_7_days = [date - timedelta(days=i) for i in range(7)]
    for country in os.listdir(f'country_top50_logs/{date.strftime("%Y%m%d")}'):
        weekly_song_counts = Counter()
        for day in last_7_days:
            file_name = f'country_top50_logs/{day.strftime("%Y%m%d")}/{country}_{day.strftime("%Y%m%d")}.txt'
            if os.path.exists(file_name):
                with open(file_name, 'r') as file:
                    _, song_counts = file.read().split('|')
                    for song_count in song_counts.split(','):
                        sng_id, count = map(int, song_count.split(':'))
                        weekly_song_counts[sng_id] += count
        top_songs = nlargest(50, weekly_song_counts.items(), key=lambda item: item[1])
        with open(f'weekly_country_top50_logs/{date.strftime("%Y%m%d")}/{country}_{date.strftime("%Y%m%d")}.txt', 'w') as file:
            file.write(f'{country}|' + ','.join([f'{sng_id}:{count}' for sng_id, count in top_songs]))

# Function to create a directory for the day if it does not exist
def create_daily_directory(date):
    if not os.path.exists(f'country_top50_logs/{date.strftime("%Y%m%d")}'):
        os.makedirs(f'country_top50_logs/{date.strftime("%Y%m%d")}')
    if not os.path.exists(f'weekly_country_top50_logs/{date.strftime("%Y%m%d")}'):
        os.makedirs(f'weekly_country_top50_logs/{date.strftime("%Y%m%d")}')

# Find the most recent file that matches the pattern 'sample_listen-*.txt'
files = glob.glob('sample_listen-*.txt')
latest_file = max(files, key=os.path.getmtime)
date_string = latest_file[14:24]  # Extract the date from the file name
date = datetime.strptime(date_string, "%Y-%m-%d")

# Run the daily process
create_daily_directory(date)
process_daily_log(latest_file, date)
compute_weekly_top50(date)
