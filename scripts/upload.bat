set base_dir=%~dp0..
set ver=0.1.3

set twine=%base_dir%\venv\scripts\twine.exe
set ver_name=%base_dir%\dist\wrap_engine-%ver%-cp38-cp38-win_amd64.whl

%twine% upload %ver_name%
