import requests
import io
from xml.etree.ElementTree import iterparse
from xml.etree.ElementTree import parse
from collections import defaultdict
import time

def gene_xml(id):
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=Gene&id={}&retmode=xml'.format(id)
    while True:
        try:
            get = requests.get(url, stream=True)
            data = ''
            for chunk in get.iter_content(chunk_size=1024):
                if chunk:
                    data = ''.join((data, chunk.decode('utf-8')))
            return data
        except:
            time.sleep(0.3)
            pass

def friendly_parser(xml_doc, path):
    path = path.split('/')
    xml_doc=io.StringIO(xml_doc)
    tag_stack = []
    elem_stack = []
    xml_doc = iterparse(xml_doc,('start','end'))
    _, root = next(xml_doc)
    for event, elem in xml_doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path:
                yield elem
                elem.clear()
                root.clear()
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass
def names(gene_xml):
        names = []
        for item in friendly_parser(gene_xml, 'Entrezgene/Entrezgene_prot/Prot-ref'):
            for thing in item.iter():
                if thing.tag == 'Prot-ref_name_E':
                    try:
                        names.append(thing.text)
                    except:
                        pass
            try:
                names.append(item.find('Prot-ref_desc').text)
            except:
                pass
        return names

if __name__ == '__main__':
    titles = []
    doc = parse("file3.xml")
    for elem in doc.iterfind("PubmedArticle/MedlineCitation"):
        print(elem.findtext('PMID'))
        for elem2 in elem.iterfind
    print(titles)