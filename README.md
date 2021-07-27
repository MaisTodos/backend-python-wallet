# backend-python-wallet

Desafio para vaga de backend na MaisTodos

![portaldetodos](https://avatars0.githubusercontent.com/u/56608703?s=400&u=ae31a7a07d28895589b42ed0fcfc102c3d5bccff&v=4)

Desafio técnico `Python`
========================

Alguns requisitos
-----------------
  - Deixe o código em inglês;
  - Use Git;
  - Procure fazer `micro commits` que são muitos commits com menos código isso nos ajuda a compreender a sua lógica;
  - Pergunte nos sobre qualquer dúvida que venha a surgir durante o desenvolvimento;
  - Documente detalhadamente quaisquer referencias/ferramentas que vc pesquisar;
  - Crie um repositório público e nos passe o link para acompanharmos o desenvolvimento;
  - Faça testes;

Problema
--------

Uma grande rede varegista do ramo alimentício, irá utilizar a carteira digital da MaisTODOS para dar cashback para os seus clientes e gerar vendas campanhas, etc.
Então basicamente vamos precisar de uma API para fazer o gerenciamento desses valores (Salvar, logs, auth) e repassar para a nossa API de cashback para dar ao cliente o valor do benefício de fato.

Basicamente funcionaria assim:

1 - ERP do varegista chama esta API com o formato:

```shell
{
    "saled_at": "2026-01-02 00:00:00",
    "customer": {
       "document": "00000000000",
       "name": "JOSE DA SILVA",
    },
    "total": "1000.00",
    "products": [
       {
          "type": "A",
          "value": "10.00",
          "qty": 1,
       },
       {
          "type": "B",
          "value": "10.00",
          "qty": 9,
       }
    ],
}
```

Onde:
- customer -> document: é o cpf do cliente
- products -> type: é a classificação do produto, você irá definir os valores mais podemos usar (A, B, C)
- products -> type: é o valor unitário do produto

2 - A API recebe e valida os dados (cpf inválido, soma errada, type fora do formato)
3 - A API salva os dados em banco

4 - Após persistir os dados, agora a API irá repassar o valor do cashback para a uma API da MaisTODOS criar o cashback
```curl
curl --request POST \
  --url https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback \
  --header 'Content-Type: application/json' \
  --data '{
	"document": "33535353535",
	"cashback": "10"
}'
```

Com o retorno
```json
{
  "createdAt": "2021-07-26T22:50:55.740Z",
  "message": "Cashback criado com sucesso!",
  "id": "NaN",
  "document": "33535353535",
  "cashback": "10"
}
```



