import pickle
from openpyxl import load_workbook


class XlToList():
    def replace_newline_with_comma(self, str):
        return str.replace("\n", ",")

    def convert(self, file_path, sheet_name="Cars-Corpus",
                title_column="B", desc_column="C"):

        workbook = load_workbook(file_path, False, False, True)
        corpus = workbook[sheet_name]
        dimension = corpus.calculate_dimension()
        range = corpus.range(dimension)
        columns = zip(*range)
        # titles = [title.value for title in columns[1]]
        # titles = map(self.replace_newline_with_comma, titles)

        ads = [ad.value for ad in columns[2]]
        ads = map(self.replace_newline_with_comma, ads)
        full_ads = [unicode(ad) for ad in ads]
        return full_ads

    def convert_and_pickle(self, file_path, save_path,
                           sheet_name="Cars-Corpus",
                           title_column="B", desc_column="C"):
        data_file = open(save_path, "wb")
        full_ads = self.convert(file_path, sheet_name,
                                title_column, desc_column)
        pickle.dump(full_ads, data_file)
        return full_ads

