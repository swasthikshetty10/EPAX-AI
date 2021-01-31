

    
# [EPAX-AI](https://epaxai.azurewebsites.net/) [https://epaxai.azurewebsites.net/]



<h3>
A machine learning based ai assistant made for techwithtim code-jam 2021, which can assist you in a various field,  the complete guide to use is provided below😀( Note : Use in Chrome Browser only to use mic )<h3>

<br>
<h2 style = "color : rgb(252, 119, 223);">🦾key Features:</h2>
<ul>
<li>Voice Chat🗣️ <i style="opacity: 0.5;">(click on mic button to speak)</i></li>
<li>QUESTIONS❓<i style="opacity: 0.5;"> (weather, information, maths etc)</i></li>
<li>Note-Taking📝<i style="opacity: 0.5;">(just say take notes)</i></li>
<li>Todo-List✔️ <i style="opacity: 0.5;">(say add todo)</i></li>
<li>Optimised Web search🔍 <i style="opacity: 0.5;">(just say search and query)</i></li>
<li>Translator🌎 <i style="opacity: 0.5;">(say translate [words to translate])</i></li>
<li>Memes🤣  <i style="opacity: 0.5;">(just say show memes)</i> </li>
<li>Play Music🎵   <i style="opacity: 0.5;">(play some music)</i></li>
<li>Jokes😆  <i style="opacity: 0.5;">(say tell me a joke))</i></li>
<li>play Games🎮  <i style="opacity: 0.5;">(just say play games)</i></li>
<li>Text chat💬  <i style="opacity: 0.5;">(to enable click on the info button below)</i></li>

</ul>
<br>

![Blueprint](https://media.discordapp.net/attachments/770563766370566180/805070659684139018/virtualassistant.html_-_Google_Chrome_30-01-2021_19_11_10_3.png)
<br>
<br>
<h2 style = "color : rgb(100, 235, 95);">👩‍🏫 HOW TO USE?<h2>
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



<h4>4) has lots of features to use visit : <a href = "https://https://epaxai.azurewebsites.net/help" >https://epaxai.azurewebsites.net/help</a> to know more ✔️</h4>

<img align="center"  src="https://cdn.discordapp.com/attachments/770563766370566180/805079326067392512/help.gif">
<br>
<br>
<br>


<h2 style = "color : rgb(247, 48, 81);">👨‍💻 HOW TO RUN ON LOCALHOST</h2>
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
<p>sqlite3</p>

```python
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
<h4>4) final step to run </h4>

```
python manage.py runserver
```

<br>
<br>
<p>
if you get any error while testing pleae contact me : <br>
gmail: <a>swasthikshetty10902@gmail.com</a>
</p>
