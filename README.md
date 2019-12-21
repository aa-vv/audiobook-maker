# Dependency

[FFmpeg](https://www.ffmpeg.org/)

[m4b-tool](https://github.com/sandreas/m4b-tool)

# Instruction


## Download Videos

If you want to make an audiobook out of videos, please first download the videos as mp4.

For Udemy courses, you can use the [Udemy Downloader GUI](https://github.com/FaisalUmair/udemy-downloader-gui) or [Udemy DL](https://github.com/r0oth3x49/udemy-dl).

## MP4 to MP3

Then use the mp4_to_mp3.py script to convert the videos into mp3.

## MP3 to M4B

Visit [m4b-tool](https://github.com/sandreas/m4b-tool) and install the latest version.

Then follow the instruction on its page to set up folder structure and run the following command:

```bash
m4b-tool merge "m4b/input/" --output-file="m4b/audiobook.m4b"
```

The tool will generate a chapters.txt if none is given as input, which describe the timeline of the audiobook. You may want to modify this file to add chapter names and run the above command again. If chapters.txt is given, the program will use it instead of creating a new one.