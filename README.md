# projeto-propostas

Este é o meu projeto Django com Django Rest Framework, Postgres, Celery e Redis.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Docker
- Docker Compose

## Configuração
1. Clone o repositório do projeto:
   https://github.com/msvasconcelos/projeto-propostas.git
   cd projeto-propostas
2. Execute o seguinte comando para construir as imagens do Docker e instalar as dependências:
   docker-compose up

O projeto estará disponível em `http://localhost:8000/`.

## Principais links:
- http://localhost:8000/proposals/
- http://localhost:8000/admin/

  Para acessar o admin pode utilizar:
  User: admin
  Pass: admin

## Encerrando o Projeto
Para encerrar o projeto, pressione `Ctrl+C` nos terminais em que o projeto está em execução e execute o seguinte comando:
docker-compose down
Isso encerrará os contêineres Docker associados ao projeto.
