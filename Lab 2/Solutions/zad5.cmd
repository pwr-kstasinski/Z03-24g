@ECHO OFF
ffmpeg.exe -i %1 -vframes 1 -ss %2 output.png