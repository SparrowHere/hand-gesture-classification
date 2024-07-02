import os

DIR = os.getcwd() + "\\test"
idx = 0

for file in os.listdir(DIR):
    if file.endswith(".jpg"):
        old_path = os.path.join(DIR, file)
        new_file = f"test_{idx}.jpg"
        new_path = os.path.join(DIR, new_file)
        os.rename(old_path, new_path)
    idx += 1