from inventory_report.inventory.product import Product

mock = {
    "id": 1,
    "nome_do_produto": "Borracha",
    "nome_da_empresa": "Papelaria Solar",
    "data_de_fabricacao": "2021-07-04",
    "data_de_validade": "2029-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Ao abrigo de luz solar"
}


def test_cria_produto():
    product = Product(**mock)

    for key, value in mock.items():
        assert getattr(product, key) == value
