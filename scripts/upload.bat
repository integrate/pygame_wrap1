set base_dir=%~dp0..
set ver=0.2.5.1.21220701

set twine=%base_dir%\.venv\scripts\twine.exe
set ver_name=%base_dir%\dist\wrap_engine-0.2.5.1.21220701-py3-none-any.whl

IF EXIST %ver_name% (%twine% upload %ver_name%)
