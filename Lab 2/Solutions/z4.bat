@echo off

set /p n="Enter N - "

setlocal EnableDelayedExpansion


    set f1=0
    set f2=1

for /l %%i in (1,1,%n%) do  (
    
    echo !f1!

    set /a f3= !f1! + !f2!
    set /a f1=!f2!
    set /a f2=!f3!
   
)

endlocal
pause

