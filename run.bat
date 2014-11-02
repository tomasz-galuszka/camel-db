@echo off
set HOST=localhost
set USER=root
set PASSWORD=abc

echo %1%

if exist %1 (

	mysql -h %HOST% -u %USER% -p < %1%
	echo  ---OK

) else (
	echo --- Brak pliku wejsciowego
	echo "%1%"

)