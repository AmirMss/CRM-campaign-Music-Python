import shutil

# Specify the directory names
dir1 = "country_top50_logs"
dir2 = "weekly_country_top50_logs"

# Use shutil.rmtree() to delete each directory
try:
    shutil.rmtree(dir1)
    print(f"{dir1} has been deleted successfully")
except FileNotFoundError:
    print(f"{dir1} does not exist")

try:
    shutil.rmtree(dir2)
    print(f"{dir2} has been deleted successfully")
except FileNotFoundError:
    print(f"{dir2} does not exist")
