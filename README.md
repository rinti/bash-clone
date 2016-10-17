# bash.org-klon i Django

1. Sätt upp virtualenv med python3 och aktivera
2. pip install -r requirements.txt
3. Skapa en .env-fil med DATABASE\_NAME och DATABASE\_USER
4. `export $(cat .env | xargs)`
5. fyll databasen med lite exempelinnehåll, öppna shell och: `from django.contrib.auth.models import User; user = User.objects.create_user(username='qwer', password='qwer'); from bash.models import Quote; import random; [Quote.objects.create(user=user, score=random.randrange(0,1000), quote='quote {}'.format(x)) for x in range(100)]`
6. yarn install
7. grunt
6. ./manage.py runserver
