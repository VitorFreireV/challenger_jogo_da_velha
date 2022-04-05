# Como executar a aplicação
## Sem docker

- Crie environment com python 3.8.10
- Instale as dependencias: pip install -r requirements.txt
- Execute a aplicação: uvicorn src.main:app
- Por padrão a url base é http://127.0.0.1:8000


## Com docker
- Com docker instalado (pode ser necessario executar o dockerd antes)
- docker build -t jogodavelha .
- docker run -d --name mycontainer -p 80:80 jogodavelha
- pode ser acessado por localhost/


# Documentação
Documentação é auto gerada pelo FastApi e Pydantic. Pode ser acessada por localhost/docs ou localhost/redoc

