__author__ = 'Bones'

import urllib.request as request
import urllib.parse
import time
import lxml
from lxml import etree

class entrez_query():

    BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    utility = "esearch"

    def __init__(self, query, db="pubmed", email = "tierprot@gmail.com", tool = "nQuery"):

        if not query:
            raise print("query is empty!")

        self.__term = "&term=" + urllib.parse.quote_plus(str(query))
        self.query = query

        try:
            self.db = db
        except ValueError:
            raise ValueError("error in db name, please ensure db name is written correctly")

        self.mail = "&email="+email
        self.tool = "&tool="+tool

#==========>Methods<=======================
    def total_ids(self):
        adress = self.adress()
        tree = self.return_tree(adress)
        total = int(tree.find('Count').text)
        return total


    def request_ids(self, start = 0, gap = 500):
        adress = self.adress(start, gap)

        tree = entrez_query.return_tree(adress)

        if isinstance(tree, lxml.etree._ElementTree) == False:
            return tree

        self.__e_search_ids(tree)
        return

    def request_all_ids(self):

        adress = self.adress()

        tree = self.return_tree(adress)
        if isinstance(tree, lxml.etree._ElementTree) == False:
            return tree

        total = int(tree.find('Count').text)

        print("Total query Id`s to receive: {0}".format(total))

        start = 0
        while start < total:
            entrez_query.__e_search_ids(self, tree)

            start += 500
            adress = self.adress(start = start)

            tree = entrez_query.return_tree(adress)
            if isinstance(tree, lxml.etree._ElementTree) == False:
                return tree
            print(start)
            time.sleep(0.3)

        print("total Id`s received: {0}".format(len(self.__id_list)))

    def dump(self):
        self.__id_list
        file = open("id.txt","w")
        for rec in self.__id_list:
            file.write("{0}\n".format(rec))

#==========>Properties<======================

    @property
    def id_list(self):
        try:
            return self.__id_list
        except AttributeError:
            self.__id_list = []

    @id_list.deleter
    def id_list(self):
        del self.__id_list

    @property
    def db(self):
        try:
            return self.__db_name
        except AttributeError:
            self.__db_name = None

    @db.setter
    def db(self, db):
        self.db
        list = ["bioproject","biosample","biosystems","books","cdd","gap","dbvar",
                "epigenomics","nucest","gene","genome","gds",
                "geoprofiles","nucgss","homologene","mesh",
                "toolkit","ncbisearch","nlmcatalog","nuccore",
                "omia","popset","probe","protein","proteinclusters",
                "pcassay","pccompound","pcsubstance","pubmed","pmc",
                "snp","sra","structure","taxonomy","unigene","unists"]
        if db in list:
            self.__db_name = "db="+db
        else:
            raise ValueError

#==========>Inner helper functions<==========

    def adress(self, start = 0, gap = 500):
        retmax = "&retmax="+ str(gap)
        retstart = "&retstart=" + str(start)
        adress = entrez_query.BASE + "esearch.fcgi?" + self.db + self.__term + self.tool + self.mail + retmax + retstart
        return adress

    @staticmethod
    def return_tree(adress):
       attempts = 100
       while attempts > 0:
            try:
                data = urllib.request.urlopen(adress)
                return etree.parse(data)
            except urllib.error.HTTPError as err:
                if err.code == 503:
                    print(err)
                    print("trying to reconnect, wait for 15 sec")
                    time.sleep(15)
                    attempts-=1
                else:
                    print(err)
                    return err
    def search_ids(self,tree):
        ids = []
        IdList=tree.find('IdList')
        for id in IdList.iter():
            if id.tag == 'Id':
                ids.append(id.text)
        return ids

    def __e_search_ids(self, tree):
        self.id_list
        IdList=tree.find('IdList')
        for id in IdList.iter():
            if id.tag == 'Id':
                self.__id_list.append(id.text)




