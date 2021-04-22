set base_dir=%~dp0..
set ver=0.1.8.1.20210901

set twine=%base_dir%\venv\scripts\twine.exe
set ver_name32=%base_dir%\dist\wrap_engine-%ver%-cp38-cp38-win32.whl
set ver_name64=%base_dir%\dist\wrap_engine-%ver%-cp38-cp38-win_amd64.whl

IF EXIST %ver_name32% (%twine% upload %ver_name32%)
IF EXIST %ver_name64% (%twine% upload %ver_name64%)
