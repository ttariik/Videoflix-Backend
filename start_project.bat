@echo off
start "" "C:\Program Files\Redis\redis-server.exe"

timeout /t 10 /nobreak >nul

start "" cmd /k "C:\Program Files\Redis\redis-cli.exe" auth foobared

timeout /t 5 /nobreak >nul

start "" powershell -NoExit -Command "cd 'C:\2_dev\1_DeveloperAkademie\2 Projekte Backend\10_videoflix_backend'; python manage.py rqworker --worker-class patch_rq_worker.PatchedWindowsWorker default"

start "" powershell -NoExit -Command "cd 'C:\2_dev\1_DeveloperAkademie\2 Projekte Backend\10_videoflix_backend'; python manage.py runserver"
