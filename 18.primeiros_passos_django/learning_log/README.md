# Primeiros Passos com Django

## Crie um diretório para o projeto

## Criando um ambiente virtual dentro da pasta do projeto

```````
python -m venv <nome_do_ambiente>
```````

## Ativando o ambiente virtual

### MacOS/Linux

```````
source <nome_do_ambiente>/bin/activate
```````

### Windows

```````
<nome_do_ambiente>\Scripts\Activate
```````

## Desativando um ambiente virtual

```````
deactivate
```````

## Instalando o Django

Com o ambiente virtual ativado, digite:

### Atualizar o gerenciador de pacotes do python (pip)

```````
pip install -m upgrade pip
```````

### Django

```````
pip install django
```````

## Criando um projeto Django

O projeto será criado dentro do próprio diretório, por isso é necessário o "" ou o .

```````
django-admin startproject <nome_do_projeto> ""
```````

Os arquivos principais serão: settings.py, urls.py e wsgi.py

## Criando o banco de dados

```````
python manage.py migrate
```````

Sempre que alteramos um banco de dados, falamos que estamos migrando o banco de dados.

## Visualizando o projeto

Inicializando o servidor na porta padrão: localhost:8000 / 127.0.0.1:8000

```````
python manage.py runserver
```````

Caso dê erro "That port is already in use", instrua o Django a usar uma porta diferente:

```````
python manage.py runserver 8001
```````

## Iniciando uma aplicação Django

```````
python manage.py startapp <nome_da_aplicacao>
```````

Os arquivos principais serão: models.py, admin.py e views.py

## Ativando Modelos

Para utilizar os modelos, as aplicacoes criadas devem ser inseridas no arquivo settings.py, na seção INSTALLED_APPS

```````
INSTALLED_APPS = [
   # Minhas aplicacoes
   '<nome_da_aplicacao>',

   # Aplicacoes default do Django
   -----
]
```````

Em seguida, é necessário solicitar ao Django que modifique o banco de dados para que consiga armazenar informacoes
relacionadas ao modelo.

### Criando o arquivo de migracao referente ao modelo

```````
python manage.py makemigrations <nome_da_aplicacao>
```````

### Modificando o Banco de Dados

```````
python manage.py migrate
```````

Sempre que quisermos modificar os dados que a aplicacao gerencia, seguiremos esses tres passos: modificar models.py,
chamar makemigrations na aplicacao e dizer ao django para executar migrate no projeto

## Site admin Django

### Criando um superusuário

```````
python manage.py createsuperuser
```````

### Adicione o modelo no arquivo admin.py

## Shell do Django

```````
python manage.py shell
```````

## Criando páginas

A criacao de paginas com o Django tem tres etapas: definir URLs, escrever views e escrever templates.

## Recriar a estrutura do banco de dados

````````
python manage.py flush
````````