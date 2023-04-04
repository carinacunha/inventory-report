from inventory_report.reports.simple_report import SimpleReport
from collections import Counter
import statistics
from datetime import datetime


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        oldest_manuf_date = min(
            [product["data_de_fabricacao"] for product in products])

        closest_exp_date = min(
            [product["data_de_validade"] for product in products
                if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                >= datetime.today()])

        companies = [product["nome_da_empresa"] for product in products]
        qnty_per_company = Counter(companies)

        resume = (
            f"Data de fabricação mais antiga: {oldest_manuf_date}\n"
            f"Data de validade mais próxima: {closest_exp_date}\n"
            f"Empresa com mais produtos: {statistics.mode(companies)}\n"
            f"Produtos estocados por empresa:\n"
        )
        for company, quantity in qnty_per_company.items():
            resume += f"- {company}: {quantity}\n"

        return resume
