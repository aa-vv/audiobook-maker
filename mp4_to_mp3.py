import os
import subprocess

INPUT_DIR = "mp4"
OUTPUT_DIR = "m4b"
OUTPUT_FORMAT = "mp3"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

for folder in os.listdir(INPUT_DIR):
  for file in os.listdir(INPUT_DIR + "/" + folder):
    if file[-3:] == 'mp4':
      f_path = (INPUT_DIR + "/" + folder + "/" + file).replace(' ', '\ ')
      folder_new = folder.split(' ')[0] + '. ' + ' '.join(folder.split(' ')[1:])
      t_path = (OUTPUT_DIR + "/" + folder_new)
      if not os.path.exists(t_path):
        os.mkdir(t_path)
      file_new = file.split(' ')[0] + '. ' + ' '.join(file.split(' ')[1:])
      t_path = (t_path + "/" + file_new[:-3] + OUTPUT_FORMAT).replace(' ', '\ ')
      # print(path)
      command = "ffmpeg -i " + f_path + " -ab 160k -ac 2 -ar 44100 -vn " + t_path
      subprocess.Popen(command, shell=True)
