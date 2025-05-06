# 📚 API de Gerenciamento de Biblioteca

Esta API fornece acesso a um sistema de gerenciamento de biblioteca, permitindo o cadastro e manipulação de livros, autores, usuários, empréstimos, reservas, multas, categorias e editoras.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Django 4+
- Django Rest Framework
- PostgreSQL
- drf-yasg (para documentação Swagger e Redoc)

---

## ⚙️ Instalação e Configuração

1. Clone o repositório
2. Crie e ative um ambiente virtual
3. Instale as dependências:
```python
pip install -r requirements.txt
```
4. Configure o `settings.py` com suas credenciais do PostgreSQL.
5. Execute as migrações:
```python
python manage.py makemigrations
python manage.py migrate
```
6. Rode o servidor:
```python
python manage.py runserver
```


## Acesso à API

- Swagger: http://localhost:8000/api/swagger/
- Redoc: http://localhost:8000/api/redoc/

## Testes

Use o Postman para testar os endpoints CRUD de cada entidade.

## 🔍 Endpoints da API REST

Você pode acessar os endpoints diretamente no navegador ou usando ferramentas como Postman.

| Entidade     | Endpoint Base                             |
|--------------|-------------------------------------------|
| Livros       | `http://localhost:8000/api/livros/`       |
| Autores      | `http://localhost:8000/api/autores/`      |
| Usuários     | `http://localhost:8000/api/usuarios/`     |
| Empréstimos  | `http://localhost:8000/api/emprestimos/`  |
| Reservas     | `http://localhost:8000/api/reservas/`     |
| Multas       | `http://localhost:8000/api/multas/`       |
| Categorias   | `http://localhost:8000/api/categorias/`   |
| Editoras     | `http://localhost:8000/api/editoras/`     |

## 📝 Licença
Este projeto está licenciado sob a licença MIT.


