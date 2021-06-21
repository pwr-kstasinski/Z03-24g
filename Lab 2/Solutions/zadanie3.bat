@echo off

net session >NUL 2>NUL

if %errorlevel% == 0 (echo you have admin privileges) else (echo you don't have admin privileges)
