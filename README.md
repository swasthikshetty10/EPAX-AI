
# [EPAX-AI](https://epaxai.azurewebsites.net/)

A machine learning based ai assistant,which can assist you in a various field,  the complete guide to use is provided below😀


![Blueprint](https://media.discordapp.net/attachments/770563766370566180/805070659684139018/virtualassistant.html_-_Google_Chrome_30-01-2021_19_11_10_3.png)
#HOW TO USE?
<br>
<br>
1) Visit https://epaxai.azurewebsites.net/ in your latest chrome browser (Note : use chrome only or else voice will not be recognised) 
<br>
2) Click on mic button and speak with epax ai ✔️
<br>
<img align="center"  src="https://cdn.discordapp.com/attachments/770563766370566180/805074123533451344/ezgif-5-5f38d8c31fd1.gif">

<br>
<br>

3) if you dont want to speak you can even chat! ✔️
<br>
<img align="center"  src="https://cdn.discordapp.com/attachments/770563766370566180/805077620383416380/ezgif-5-d6f1b3e1c1b9.gif">
<br>
<br>



4) has lots of features to use visit : https://epaxai.azurewebsites.net/help to know more ✔️
<br>
<img align="center"  src="https://cdn.discordapp.com/attachments/770563766370566180/805079326067392512/help.gif">
<br>
<br>
<br>
# HOW TO USE ON LOCALHOST(FOR DEVELOPER USE ONLY)
<br>

1) to install dependencies:
<br>
```
pip install -r requirements.txt
```
<br>
<br>
2) configure database at AssistantWeb/settings.py
<br>

postgresql
```python
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'yor-postgresql-sql-database-name',

        'USER': 'username',

        'PASSWORD': 'password',

        'HOST': 'host',

        'PORT': 'port_no',

    }
}
```
sqlite3
```

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```




