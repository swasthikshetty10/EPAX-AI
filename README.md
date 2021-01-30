
# [EPAX-AI](https://epaxai.azurewebsites.net/) [https://epaxai.azurewebsites.net/]

A machine learning based ai assistant made for techwithtim code-jam, which can assist you in a various field,  the complete guide to use is provided below😀 
<br>

![Blueprint](https://media.discordapp.net/attachments/770563766370566180/805070659684139018/virtualassistant.html_-_Google_Chrome_30-01-2021_19_11_10_3.png)
<br>
<h2>HOW TO USE?<h2>
<br>
<h4>1) Visit https://epaxai.azurewebsites.net/ in your latest chrome browser (Note : use chrome only or else voice will not be recognised) </h4>
<br>
<h4>2) Click on mic button and speak with epax ai ✔️<h4>

<img align="center"  src="https://cdn.discordapp.com/attachments/770563766370566180/805074123533451344/ezgif-5-5f38d8c31fd1.gif">

<br>
<br>

<h4>3) if you dont want to speak you can even chat! ✔️<h4>

<img align="center"  src="https://cdn.discordapp.com/attachments/770563766370566180/805077620383416380/ezgif-5-d6f1b3e1c1b9.gif">
<br>
<br>



<h4>4) has lots of features to use visit : https://epaxai.azurewebsites.net/help to know more ✔️<h4>

<img align="center"  src="https://cdn.discordapp.com/attachments/770563766370566180/805079326067392512/help.gif">
<br>
<br>
<br>


<h2>HOW TO USE ON LOCALHOST(FOR DEVELOPER USE ONLY)</h2>
<br>

<h4>1) to install dependencies:</h4>
<br>

```
pip install -r requirements.txt
```
<br>
<br>

<h4>2) configure database at AssistantWeb/settings.py</h4>
<br>
postgresql

```
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
<p>sqlite3</p>

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
<br>
<h4>3) configure some api keys and add firebase_config.json with firebase credentials in Backend/AssistantFunctions </h4>
<br>
<h4>4) final step to run</h4>
```
python manage.py runserver
```

if you get any error while testing pleae contact me : gmail:  swasthikshetty10902@gmail.com
