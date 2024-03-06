# SoulTravel API

Bem-vindo ao SoulTravel API, um projeto incrível baseado no framework FastAPI em Python.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina antes de começar:

- [Python](https://www.python.org/) (versão 3.X.X)
- [pip](https://pip.pypa.io/en/stable/) (gerenciador de pacotes do Python)

## Configuração do Ambiente

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/SoulTravelApp/soultravel_api.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd soultravel_api
   ```

3. Instale as dependências do projeto utilizando o pip:

   ```bash
   pip3 install -r requirements.txt
   ```

## Rodando o Projeto

Após instalar as dependências, você pode iniciar o servidor utilizando o seguinte comando:

```bash
uvicorn app.main:app --reload
```

Este comando iniciará o servidor de desenvolvimento e fornecerá uma URL local, geralmente [http://127.0.0.1:8000](http://127.0.0.1:8000), onde você pode acessar a API.

Certifique-se de incluir a opção `--reload` para que o servidor seja reiniciado automaticamente sempre que houver alterações no código.

## Documentação da API

Acesse a documentação interativa da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para explorar os endpoints disponíveis e testar as requisições.
