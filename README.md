<h1 align="center">First Code with FastAPI</h1>

<p>Este é o meu primeiro projeto em FastAPI, foi feita consultando a documentação, 
não é uma aplicação robusta pois é o meu primeiro contato com a bilbioteca, o objetivo 
é ter o primeiro contato com a tecnologia</p>

<p>Este é uma api que implementa uma loja de produtos online, onde o cliente pode 
realizar suas vendas</p>

```bash
Documentação Swagger
http://127.0.0.1:8000/docs#
```

```bash
Documentação Redoc
http://localhost:8000/redoc
```

```bash
Chamada para api
http://127.0.0.1:8000/
```

# Rodar o serviço
```bash
$ uvicorn main:app --reload
ou
$ uvicorn src.main:app --reload

Saída:
←[32mINFO←[0m:     Will watch for changes in these directories: ['C:\\Users\\User\\PycharmProjects\\fastApi']
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://127.0.0.1:8000←[0m (Press CTRL+C to quit)
←[32mINFO←[0m:     Started reloader process [←[36m←[1m19836←[0m] using ←[36m←[1mStatReload←[0m
←[32mINFO←[0m:     Started server process [←[36m15920←[0m]
←[32mINFO←[0m:     Waiting for application startup.
←[32mINFO←[0m:     Application startup complete.
```

|ENDPOINT|METHOD|DESCRIÇÃO|
|---|---|---|
|/|GET|Raiz da API|
|/healthcheck|GET|Consultar o estado do serviço|
|/sale|POST|Gerar QRCode|
|/store|POST|Criar dados|
|/product|POSR|Criar dados|

### Tecnologias do projeto
- [ ] S3
- [x] API Rest(FastAPI)
- [ ] MongoDB
- [ ] Docker
- [ ] PostgreSQL
- [ ] Fila (Kafka)


# Links de referência
[Doc FastAPI](https://fastapi.tiangolo.com/)
[bigger-applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)