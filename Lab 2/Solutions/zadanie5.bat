@echo off

ffmpeg -i %1 -ss 00:00:01.000 -vframes 1 miniaturka.png