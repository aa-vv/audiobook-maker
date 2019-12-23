import os
import subprocess

INPUT_DIR = "mp4"
INPUT_FORMAT = "mp4"
OUTPUT_DIR = "mp3"
OUTPUT_FORMAT = "mp3"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

for folder in os.listdir(INPUT_DIR):
  for file in os.listdir(os.path.join(INPUT_DIR, folder)):
    if file[-len(INPUT_FORMAT):] == INPUT_FORMAT:
      f_path = os.path.join(INPUT_DIR, folder, file)
      t_folder = os.path.join(OUTPUT_DIR, folder)
      if not os.path.exists(t_folder):
        os.mkdir(t_folder)
      t_path = os.path.join(t_folder, file.replace(INPUT_FORMAT, OUTPUT_FORMAT))
      command = "ffmpeg -i " + f_path.replace(' ', '\ ') + " -ab 160k -ac 2 -ar 44100 -vn " + t_path.replace(' ', '\ ')
      subprocess.Popen(command, shell=True)
