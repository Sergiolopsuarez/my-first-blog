import os

from fabric.api import local
from fabric.context_managers import lcd


PROJECT_NAME = "django_polls"
PROJECT_PATH = f"/tmp/new_dp/{PROJECT_NAME}"
REPO_URL = "https://github.com/Sergiolopsuarez/my-first-blog.git"
VENV_PYTHON = f'{PROJECT_PATH}/.venv/bin/python'
VENV_PIP = f'{PROJECT_PATH}/.venv/bin/pip'

#Descarga el proyecto del repo con git
def clone():
    print(f"clone repo {REPO_URL}...")

    if os.path.exists(PROJECT_PATH):
        print("project already exists")
    else:
        local(f"git clone {REPO_URL} {PROJECT_PATH}")

#Crea un entorno virtual. Activa el entorno virtual
def create_venv():

    print("creating venv....")

    with lcd(PROJECT_PATH):
        local("python3 -m venv .venv")

#Instala las librerías del requirements.txt
def install_requirements():

    print("installing requirements.txt...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PIP} install -r requirements.txt ")

#Genera las migraciones del proyecto con python manage.py makemigrations
def django_makemigrations():

    print("executing django migrations...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py makemigrations ")

#Ejecuta las migraciones en la base de datos con python manage.py migrate
def django_migrate():

    print("executing django migrations...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py migrate ")

#Carga los datos iniciales del fichero db.json con python manage.py loaddata db.json
def django_loaddata():

    print("loading initial data...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py loaddata db.json")

#Ejecuta el servidor de django para probar la aplicación
def django_runserver():

    print("runing server...")

    with lcd(PROJECT_PATH):
        local(f"{VENV_PYTHON} manage.py runserver")


def deploy():
    clone()
    create_venv()
    install_requirements()
    django_makemigrations()
    django_migrate()
    django_loaddata()
    django_runserver()