# Deezer Top 50 Songs Tracker

This project tracks the top 50 most listened songs daily and weekly on Deezer for each country.

## How does it work?

The main Python script parses a music listening log file, calculates the listening count for each song in each country, and writes the top 50 songs for each country into a file. It also calculates the weekly top 50 songs for each country, based on the daily top 50 files from the previous seven days.

## Prerequisites

- Python 3.x
- PyInstaller (optional, for creating executables)

## Usage

1. Ensure you have the music listening log files in the same directory as the script. These files should be in .txt format and contain a line for each song listening. Each line should be formatted as: `sng_id|user_id|country`.
     **Note**: The log files should match the pattern `'sample_listen-*.txt'` and only the last version will be compute.


3. Run the Python script `deezer_top50_tracker.py`:

   - On Windows:
     ```
     Click on : Deezer.exe
     ```
   - On Linux:
     ```
     python3 Deezer.py
     ```

   This will generate the top 50 files for each country in the `country_top50_logs` directory and the weekly top 50 files in the `weekly_country_top50_logs` directory.

4. To delete all generated files, run the Python script `delete_files.py`:

   - On Windows:
     ```
     Click on : delete_files.exe
     ```
   - On Linux:
     ```
     python3 delete_files.py
     ```

   This will delete the `country_top50_logs` and `weekly_country_top50_logs` directories, along with all the files they contain.

## Notes

- Be careful when running the `delete_files.py` script, as file deletion is irreversible.
- If you encounter any issues, check that the listening log files are correctly formatted and the script has permission to read and write files in the directories.
