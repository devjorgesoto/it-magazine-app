allow refresh home with no populated db 
    python manage.py migrate --run-syncdb 

little script for when reseting db
    python manage.py migrate &&  python manage.py makemigrations && python manage.py sqlmigrate articles 0001 && python manage.py migrate --run-syncdb 