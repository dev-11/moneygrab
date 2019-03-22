import csv


def write_file(filename, content):
    with open(filename, 'wb') as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(content)
