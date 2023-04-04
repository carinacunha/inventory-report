import abc


class Importer:
    @abc.abstractmethod
    def import_data(clas, path):
        raise NotImplementedError
