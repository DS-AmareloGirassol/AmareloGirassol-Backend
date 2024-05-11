# AmareloGirassol-Backend

### Comandos para rodar o projeto Sem Docker

#### Visualizar mudanças nas models
```sh
python3 mananage.py makemigrations
```

#### Criar migrações
```sh
python3 manage.py migrate
```

#### Rodar o projeto
```sh
python manage.py runserver
```

### Comandos para rodar o projeto Com Docker

#### Subir os containers
```sh
sudo docker compose up -d
```

#### Rodar o docker do projeto *
```sh
sudo docker compose up
```

*Eventualmente quando rodar na primeira vez, pode dá uma travadinha logo nas primeiras linhas. Ai é só dar um ctrl c para parar o comando e depois rodar o Docker novamente.

Agora é ir na url http://localhost:8000/api que lá estará rodando o backend do projeto