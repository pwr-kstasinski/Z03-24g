@echo off
@REM "Pierwszy parametr - sciezka pliku, drugi parametr - czas generowania miniaturki"

ffmpeg -ss %2 -i %1 -vframes 1 miniaturka.jpg