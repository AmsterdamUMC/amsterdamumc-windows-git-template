@ECHO OFF
REM 
REM Used the DOS/CMD command findstr for performance reasons
REM


ECHO Scanning for surnames in %1
findstr /I /N /S /G:.amsterdamumc-scripts\lookup_items\surnames.txt %1*

REM TODO remove the temp-output.txt file
ECHO:
ECHO: 
IF ERRORLEVEL 0 ECHO Found one or more surnames in project. Please review these

@ECHO ON 