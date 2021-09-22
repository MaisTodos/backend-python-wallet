# **MaisTodos**
## **Como executar a aplicação**
### **Requisitos**

* Docker
* 

> **_NOTE:_**  Cuidado ao utilizar no Windows, o projeto ocupará muito espaço e também muita memória RAM.

### **Configurações**

Primeiro de tudo, altere o arquivo `.env` da forma como desejar. O indicado é que apenas se alterem as portas que serão abertas, de forma que não haja conflito com outras aplicações rodando na sua máquina.

> **_NOTE:_**  VOCÊ DEVE ALTERAR O `HOST` NO `.env`, pode ser `127.0.0.1`.

### **Execução**

> **_NOTE:_**  A primeira execução pode levar alguns minutos para preparar as aplicações, devido à ter que fazer download das imagens docker e criação de novos containers.

Para executar o projeto, basta utilizar o comando `docker-compose up`.
o comando fará os seguintes procedimentos:

* Criará dois bancos de dados, sendo um para o projeto e outro para testes;
* Conectará o banco de dados do projeto ao PHPMyadmin;
* Criará um container django a partir do Dockerfile especificado;
* Executará o entrypoint especificado no docker-compose.yml:
  * O entrypoint fará a coleta de arquivos estáticos;
  * Criará novas migrations;
  * Aplicará as migrations ao banco de dados;
  * Fará testes unitários se a variável `DEBUG` estiver definida com `True` no `.env`;
  * Iniciará o servidor web;


Para acessar a aplicação no navegador, basta acessar o HOST especificado no arquivo `.env`, seguido da porta de cada container. Ex:

container django: http://192.168.0.175:8000


> **_NOTE:_**  VOCÊ DEVE CRIAR UM USUÁRIO ADMINISTRADOR NO PROJETO E GERAR UM TOKEN NO PAINEL ADMIN. PARA ISSO ACESSE O CONTAINER DO DJANGO ATRAVÉS DO COMANDO ABAIXO:

    docker exec -it (meu_container) /bin/bash

### **Testes**

Para executar os testes unitários de acordo com as configurações do arquivo `pytest.ini`, basta utilizar o comando `pytest`.

Não foram criados testes para a aplicação, foi apenas estruturado o diretório e a configuração de execução.

> **_NOTE:_**  Necessário acessar o shell do container do django.


### **Debug**

Se a variável `DEBUG`, no `.env`, estiver definida como `True`, a aplicação irá rodar em modo debug, e o desenvolvedor terá acesso ao menu do pacote debug_toolbar na aplicação.

### **API**

Todos os endpoints da aplicação estão disponíveis na rota `api/`.

#### Endpoints

| API | METHOD | ENDPOINTS |
| ------ | ------ |------ |
| List of Customer | GET | /api/customer/ |
| Customer description | GET | /api/customer/<id_category>/ |
| New Customer | POST | /api/customer/ |
| Change Customer | PUT | /api/customer/<id_category>/ |
| List of Products | GET | /api/product/ |
| Products description | GET | /api/product/<id_question>/ |
| New Products | POST | /api/product/ |
| Change Products | PUT | product/<id_category>/ |
| List of Cashback | GET | /api/cashback/ |
| Cashback description | GET | /api/cashback/<id_question>/ |
| New Cashback | POST | /api/cashback/ |
| Change Cashback | PUT | /api/cashback/<id_question>/ |

#### Postman collection

[![View Postman Documentation](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/17469376/UUxukAnb)
## **Estruturação da aplicação**
### **maistodos**

É onde se encontram as configurações do projeto, como as variáveis de ambiente, as configurações de banco de dados, etc.

### **tests**

Onde ficam os testes unitários, o arquivo conftest define o banco de dados de teste.

Não foram criados testes para a aplicação, foi apenas estruturado o diretório e a configuração de execução.

### **sales**

Onde estão definidos o modelos do sales.

### **sales/api**

Onde estão definidas as APIs, o serializer e o viewsets do sales.


## **Pontos à Melhorar**

* Foi removido `unique=True` do campo `document` em Custumer para resumir a implementação. Porém isso causa problemas de integridade que não foram tratados, se você quiser por exemplo salvar um novo customer com nome ou CPF's diferentes a partir do mesmo usuário logado.


#### FICO À DISPOSIÇÃO PARA ESCLARECER DÚVIDAS SOBRE O PROJETO