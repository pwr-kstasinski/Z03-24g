
@echo off

net session >NUL 2>NUL

if %errorlevel% == 0 (echo "odpowiedni komunikat o posiadaniu praw admina") else (echo "odpowiedni komunikat o niemaniu praw admina")