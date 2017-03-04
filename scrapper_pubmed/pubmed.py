__author__ = 'Bones'

from lxml import etree
import argparse
import urllib.request



'''adress = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=science[journal]+AND+breast+cancer+AND+2008[pdat]"
data = urllib.request.urlopen(adress)
root = etree.parse(data)
print(etree.tostring(root))
print(root.getroot().tag)'''


string = b'<!DOCTYPE eSearchResult PUBLIC "-//NLM//DTD esearch 20060628//EN" "http://eutils.ncbi.nlm.nih.gov/eutils/dtd/20060628/esearch.dtd">\n<eSearchResult><Count>6</Count><RetMax>6</RetMax><RetStart>0</RetStart><IdList>\n<Id>19008416</Id>\n<Id>18927361</Id>\n<Id>18787170</Id>\n<Id>18487186</Id>\n<Id>18239126</Id>\n<Id>18239125</Id>\n</IdList><TranslationSet><Translation>     <From>science[journal]</From>     <To>"Science"[Journal] OR "Science (80- )"[Journal] OR "J Zhejiang Univ Sci"[Journal]</To>    </Translation><Translation>     <From>breast cancer</From>     <To>"breast neoplasms"[MeSH Terms] OR ("breast"[All Fields] AND "neoplasms"[All Fields]) OR "breast neoplasms"[All Fields] OR ("breast"[All Fields] AND "cancer"[All Fields]) OR "breast cancer"[All Fields]</To>    </Translation></TranslationSet><TranslationStack>   <TermSet>    <Term>"Science"[Journal]</Term>    <Field>Journal</Field>    <Count>168187</Count>    <Explode>N</Explode>   </TermSet>   <TermSet>    <Term>"Science (80- )"[Journal]</Term>    <Field>Journal</Field>    <Count>10</Count>    <Explode>N</Explode>   </TermSet>   <OP>OR</OP>   <TermSet>    <Term>"J Zhejiang Univ Sci"[Journal]</Term>    <Field>Journal</Field>    <Count>364</Count>    <Explode>N</Explode>   </TermSet>   <OP>OR</OP>   <OP>GROUP</OP>   <TermSet>    <Term>"breast neoplasms"[MeSH Terms]</Term>    <Field>MeSH Terms</Field>    <Count>233441</Count>    <Explode>Y</Explode>   </TermSet>   <TermSet>    <Term>"breast"[All Fields]</Term>    <Field>All Fields</Field>    <Count>393324</Count>    <Explode>N</Explode>   </TermSet>   <TermSet>    <Term>"neoplasms"[All Fields]</Term>    <Field>All Fields</Field>    <Count>2192452</Count>    <Explode>N</Explode>   </TermSet>   <OP>AND</OP>   <OP>GROUP</OP>   <OP>OR</OP>   <TermSet>    <Term>"breast neoplasms"[All Fields]</Term>    <Field>All Fields</Field>    <Count>233461</Count>    <Explode>N</Explode>   </TermSet>   <OP>OR</OP>   <TermSet>    <Term>"breast"[All Fields]</Term>    <Field>All Fields</Field>    <Count>393324</Count>    <Explode>N</Explode>   </TermSet>   <TermSet>    <Term>"cancer"[All Fields]</Term>    <Field>All Fields</Field>    <Count>1636953</Count>    <Explode>N</Explode>   </TermSet>   <OP>AND</OP>   <OP>GROUP</OP>   <OP>OR</OP>   <TermSet>    <Term>"breast cancer"[All Fields]</Term>    <Field>All Fields</Field>    <Count>199223</Count>    <Explode>N</Explode>   </TermSet>   <OP>OR</OP>   <OP>GROUP</OP>   <OP>AND</OP>   <TermSet>    <Term>2008[pdat]</Term>    <Field>pdat</Field>    <Count>832563</Count>    <Explode>N</Explode>   </TermSet>   <OP>AND</OP>  </TranslationStack><QueryTranslation>("Science"[Journal] OR "Science (80- )"[Journal] OR "J Zhejiang Univ Sci"[Journal]) AND ("breast neoplasms"[MeSH Terms] OR ("breast"[All Fields] AND "neoplasms"[All Fields]) OR "breast neoplasms"[All Fields] OR ("breast"[All Fields] AND "cancer"[All Fields]) OR "breast cancer"[All Fields]) AND 2008[pdat]</QueryTranslation></eSearchResult>'

root = etree.fromstring(string)

tree = etree.ElementTree(root)

for node in tree.iter():
    if node.tag == 'IdList':
        for id in node.iter():
            print(id.text)

'''for element in tree.iter():
    print(tree.getpath(element))'''
