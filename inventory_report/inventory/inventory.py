from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        if (path.endswith('.csv')):
            data = cls.read_csv_file(path)

        return cls.select_type(data, report_type)

    @classmethod
    def select_type(cls, product_list, report_type):
        if report_type == "simples":
            return SimpleReport.generate(product_list)
        elif report_type == "completo":
            return CompleteReport.generate(product_list)

    @classmethod
    def read_csv_file(cls, filepath):
        data = []
        with open(filepath, 'r') as file:
            csvReader = csv.DictReader(file)
            for rows in csvReader:
                data.append(rows)
        return data
