
#!/bin/bash

# Verifica se o Python está instalado
if ! command -v python &> /dev/null; then
    echo "Python não está instalado. Por favor, instale o Python."
    exit 1
fi

# Verifica se o Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "Docker não está instalado. Por favor, instale o Docker."
    exit 1
fi

# Verifica se o Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose não está instalado.instale o Docker Compose."
    exit 1
fi

cd C:/Users/douglas/Desktop/git/teste/appmed

# Cria um ambiente virtual (venv) se não existir
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Ativa o ambiente virtual
source venv/Scripts/activate

# Instala o Django dentro do ambiente virtual
pip install django


# Cria um novo projeto Django na pasta 'django_app'
django-admin startproject appmed .


# Aplica as migrações do banco de dados
python manage.py migrate

# Inicia o servidor Django
python manage.py runserver 0.0.0.0:8000

    