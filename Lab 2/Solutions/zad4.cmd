@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION
SET actual=0
SET next=1

for /l %%I in (1, 1, %1) do (
    echo !actual!
    set /A temp=!actual!+!next!
	set actual=!next!
	set next=!temp!
)
ENDLOCAL