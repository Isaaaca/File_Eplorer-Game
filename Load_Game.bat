@echo off
setlocal
:PROMPT
SET /P AREYOUSURE=Are you sure you want to load? This will overwrite your current game.(Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END
rmdir /q /S Laws 2>nul
rmdir /q /S World 2>nul
del /q File_Explorer.py 2>nul
xcopy /y /q /H /E /I .\Time\Saved
echo game loaded.
python-3.8.1\python.exe -i -B File_Explorer.py

:END
endlocal