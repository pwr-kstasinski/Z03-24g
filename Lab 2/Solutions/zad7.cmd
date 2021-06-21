@ECHO ON
SETLOCAL ENABLEDELAYEDEXPANSION
SET accum=1

for /l %%I in (1, 1, %1) do (
    set /A accum=!accum!*%%I
)
echo %accum%
ENDLOCAL