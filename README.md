## Django REST framework API
Api para gerenciamento de estacionamento de condominios.

#### Como Instalar o Django e o REST framework

1. Vá para a pasta do seu projeto e execute os próximos comandos
```
pip install virtualenv

virtualenv nome_da_sua_env
``` 
2. Inicie sua ENV
Para Windows:
```
nome_da_sua_env/Scripts/Activate
```
Para Mac e Linux:
```
source nome_da_virtualenv/bin/activate
```

3. Instale os Pacotes Django e Django REST framework.
Para Windows
```
pip install Django

pip install djangorestframework
```

4. Coloque o Django REST framework nos seus installed apps em settings
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #libs
    'rest_framework', <- desse jeito

    #apps
    'parkingslot.apps.ParkingslotConfig',
]
```


#### Funcionalidades
API rest com funcionalidades CRUD para gerenciamento de vagas para condomínios.

#### Referências 
* https://www.django-rest-framework.org/
* https://www.djangoproject.com/

