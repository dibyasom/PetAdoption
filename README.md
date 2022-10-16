# Pet Adoption - CMS | Tutorial

## Get started

### Create a virtual python environment

```bash
python3 -m venv env
# Activate the enviroment
source ./env/bin/activate
```

### Install python packages required for syntax highlighting to work

```bash
pip install django djangorestframework black
```

### Create an enviroment file, and add credentials

```bash
# Open thy editor
nano .env

# Add the following code
DB_PASSWORD=diby1234
DB_USER=diby
DB_NAME=petadoption
DB_HOST=db
# ...
# Hit ctrl+o to save, and ctrl+x to exit editor
```

### Install Docker Engine
<hr>  

Download here, for Mac/Linux/Windows [HERE](https://docs.docker.com/engine/install/)


### Create a superuser
```bash
docker-compose run backend sh -c "python3 manage.py createsuperuser --username <username>"
# ...
# Follow the questions on terminal now.
```