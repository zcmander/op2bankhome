# -*- coding: utf-8 -*-

import datetime
import csv
import sys
import codecs
import decimal

# class UTF8Recoder:
#     """
#     Iterator that reads an encoded stream and reencodes the input to UTF-8
#     """
#     def __init__(self, f, encoding):
#         self.reader = codecs.getreader(encoding)(f)

#     def __iter__(self):
#         return self

#     def next(self):
#         return self.reader.next().encode("utf-8")

# class UnicodeDictReader:

#     def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
#         f = UTF8Recoder(f, encoding)
#         self.reader = csv.DictReader(f, dialect=dialect, **kwds)

#     def next(self):
#         row = self.reader.next()
#         result = {}
#         for s in row:
#             value = row[s]
#             if value:
#                 value = value.decode("utf-8")
#             else:
#                 continue
#             result[s.decode("utf-8")] = value

#         return result

#     def __iter__(self):
#         return self

class Transaction:
    def __init__(self, data):
        self.raw_data = data
        self.date = datetime.datetime.strptime(data[u'Arvopäivä'], "%d.%m.%Y")
        self.value = decimal.Decimal(str.replace(data[u"Määrä  EUROA"], ",", "."))

        try:
            self.receiver = data["Saaja/Maksaja"][:20].strip()
            self.receiver2 = data["Saaja/Maksaja"][20:].strip()
        except:
            self.receiver = ""
            self.receiver2 = ""


def parse_tapahtumat_file(filepath):
    transactions = []
    with open(filepath, "r", encoding="iso8859") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")

        for row in reader:
            try:
                transactions.append(Transaction(row))
            except:
                print("Ignored transaction: {0!r}".format(row))

    return transactions


def post_process(transactions):
    grouped = {}
    for transaction in transactions:
        if transaction.receiver not in grouped:
            grouped[transaction.receiver] = decimal.Decimal("0")
        grouped[transaction.receiver] += transaction.value

    sorted_group = {}

    for group in grouped:
        sorted_group[grouped[group]] = group

    print("Summary:")
    print("-"*80)
    for group in sorted(sorted_group.keys()):
        print("{0:<10} {1}".format(group, sorted_group[group]))


def main():
    transactions = parse_tapahtumat_file(sys.argv[1])

    fh = open("converted.csv", "w", encoding="utf-8")
    for transaction in transactions:
        fh.write("{0};{1};{2};{3};{4};{5};{6};{7}\n".format(
            transaction.date.strftime("%Y-%m-%d"),
            0,
            "",
            transaction.receiver,
            transaction.receiver2,
            transaction.value,
            transaction.raw_data["Selitys"],
            transaction.receiver2
        ))
    fh.close()

if __name__ == '__main__':
    main()
