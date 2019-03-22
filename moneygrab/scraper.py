import glob

from scrapy.http import HtmlResponse


def scrape_local_pages(company_config):

    for file_name in glob.glob(f"../products/{company_config['name']}/*"):
        with open(file_name, 'r') as product_file:
            product_html = product_file.read()
        ul = scrape_page(product_html, company_config["parsers"])
        print(file_name, ul)


def scrape_page(body, parsers):
    response = HtmlResponse(url="", body=body, encoding="utf8")

    for parser in parsers:
        root = response.selector.xpath(parser["root"]).get()
        if root is None:
            continue
        else:
            data = {}
            for attribute in parser["attributes"]:
                try:
                    data[attribute] = response.selector.xpath(parser["attributes"][attribute]).get()
                except Exception:
                    print(parser["attributes"][attribute], "failed to parse")
                    continue
            break
    else:
        raise ValueError("No parser was able to parse")

    return data
