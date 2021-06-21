
@echo off


ffmpeg -ss %2 -i %1 -vframes 1 thumbnail.png 