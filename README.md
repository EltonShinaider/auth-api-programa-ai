# auth-api-program-ai

API de autenticação desenvolvida como parte do curso de AppSec da
**Programa.AI**.\
Este projeto utiliza **Flask**, **Flask-Migrate** e **SQLAlchemy** para
gerenciar a aplicação e o banco de dados.

------------------------------------------------------------------------

## 🚀 Como executar o projeto

### 1. Clonar o repositório

``` bash
git clone https://github.com/seu-usuario/auth-api-program-ai.git
cd auth-api-program-ai
```

### 2. Criar e ativar um ambiente virtual (opcional, mas recomendado)

**Windows**

``` bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

``` bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo **.env** na raiz do projeto e defina variáveis como:

    FLASK_APP=app.py
    FLASK_ENV=development
    DATABASE_URL=sqlite:///app.db

Ajuste conforme o banco de dados que estiver usando.

------------------------------------------------------------------------

## 🗄️ Gerenciamento do banco de dados

### 1. Inicializar o diretório de migrações

``` bash
flask db init
```

### 2. Criar a migração inicial

``` bash
flask db migrate -m "init: users"
```

### 3. Aplicar as migrações

``` bash
flask db upgrade
```

------------------------------------------------------------------------

## ▶️ Executar a aplicação

Após configurar o ambiente e o banco de dados, execute:

``` bash
flask run
```

A aplicação estará disponível em:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 📚 Tecnologias utilizadas

-   Python + Flask\
-   Flask-Migrate\
-   SQLAlchemy\
-   Alembic\
-   Python-dotenv