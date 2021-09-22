import requests


URL = 'https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback'


def maistodos(request, document, cashback):
    data = {
        "document": document,
        "cashback": cashback
    }

    return requests.post(url=URL, params=data)