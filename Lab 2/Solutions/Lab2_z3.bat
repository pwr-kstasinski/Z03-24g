@echo off
  
net session 1>nul  2>nul
if %errorLevel% == 0 (
echo uruchomiony jako administrator
) else (
echo uruchomiony bez praw administratora 
)

pause