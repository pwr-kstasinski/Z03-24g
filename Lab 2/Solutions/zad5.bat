@echo off

rem podajemy plik z ktorego chcemy zrobic miniaturke oraz w jaki sposob chcemy ja zapisac, czas jej zrobienia to 1/2 filmu.

ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 %1>temp.txt

set /p VAR=<temp.txt

echo %VAR%

set /a VAR/=2

echo %VAR%

ffmpeg -i %1 -ss 00:00:%VAR%.000 -vframes 1 %2

pauses6