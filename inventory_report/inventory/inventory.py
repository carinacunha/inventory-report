from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        if (path.endswith('.csv')):
            data = cls.read_csv(path)
        elif (path.endswith('.json')):
            data = cls.read_json(path)
        return cls.select_type(data, report_type)

    @classmethod
    def select_type(cls, data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)

    @classmethod
    def read_csv(cls, path):
        data = []
        with open(path, 'r') as file:
            csvReader = csv.DictReader(file)
            for rows in csvReader:
                data.append(rows)
        return data

    @classmethod
    def read_json(cls, path):
        with open(path, 'r') as file:
            return json.load(file)
