@echo off

set result=1

for /L %%x in (1, 1, %1) do set /a result *= %%x

echo %result%