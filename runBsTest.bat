echo off

path=%path%;D:\Python37;

set /p tmp="week: " 

python BsTest.py %tmp%

pause