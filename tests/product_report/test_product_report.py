from inventory_report.inventory.product import Product

mock = {
    "id": 1,
    "nome_do_produto": "MESA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2022-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  }


def test_relatorio_produto():
    product = Product(**mock)

    output = (
        f"O produto {mock['nome_do_produto']}"
        f" fabricado em {mock['data_de_fabricacao']}"
        f" por {mock['nome_da_empresa']} com validade"
        f" até {mock['data_de_validade']}"
        f" precisa ser armazenado {mock['instrucoes_de_armazenamento']}."
    )

    assert str(product) == output
