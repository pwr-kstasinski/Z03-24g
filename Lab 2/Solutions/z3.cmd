@echo off
dir/b>nul
openfiles >nul 2>&1
if ERRORLEVEL 1 (
	echo Not Admin
	exit/b
)
echo Admin
