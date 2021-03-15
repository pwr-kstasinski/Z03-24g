@echo off
SetLocal EnableDelayedExpansion

if "%1" == "-h" (
    echo ---Help---
    echo zad4.cmd [video_path] [miniature_path] [miniature_time]
    echo This script generates a miniature of given film.
    echo default options:
    echo   video_path = .\video.mp4
    echo   miniature_path = .\video.jpg
    echo   miniature_time (in seconds) = 10
    echo ----------
    exit /B %ERRORLEVEL%
)

if "%1" == "" (
    set video_path=.\video.mp4
) else (
    set video_path=%1
)

if "%2" == "" (
    set miniature_path=.\video.jpg
) else (
    set miniature_path=%2
)

if "%3" == "" (
    set miniature_time=10
) else (
    set miniature_time=%3
)

echo Video path:: %video_path%
echo Working...

ffmpeg -ss %miniature_time% -i %video_path% -frames:v 1 -q:v 2 %miniature_path% -loglevel quiet

echo Done.
EXIT /B %ERRORLEVEL%