import csv


def write_file(filename, content, header):
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(header)
        writer.writerows(content)
