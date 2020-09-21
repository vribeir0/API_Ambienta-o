import pymongo
from bson.objectid import ObjectId
import time

class DataBase:
    def __init__(self):
        self.db = ''
        self.client = ''
        self.subCategoria = []
        self.categoria = []
        self.connectBD()
        
    def connectBD(self):
        try:
            self.client = pymongo.MongoClient("#######")
            self.db = self.client["dbAkira"]
            print('Conexão bem sucedida!')
            # return db
        except:
            print("BD error")
    #arrumar classe
    def closeBD(self):
        try:
            self.client.close()
            print('Conexão fechada com sucesso!')
        except:
            print("fechamento falhou")
        
    
    def getConteudo(self):
        collection = self.getProblemsCollection()

        # Criando um dicionário para as categorias
        conteudoDict = dict()

        #Buscado todas as categorias do banco
        setCategorias = self.findCategoria(collection)

        #Iterando nesse set para a criação de um dicinário de subcategorias
        for categoria in setCategorias:

            # Criando um dicionário de subcategorias
            dictSubCategoria = dict()

            # Buscando todas as subcategorias de uma categoria específica
            setSubCategoria = self.findSubCategoria(categoria, collection)

            # Iterando sobre em cada subcategoria 
            for subCategoria in setSubCategoria:
                
                # Buscando cada problema de cada subcategoria
                dictSubCategoria[subCategoria] = self.createListProblems(categoria, subCategoria, collection)
            
            # Inserindo o dicionário de problemas das subcategoria na categoias nas categorias
            conteudoDict[categoria] = dictSubCategoria

        self.closeBD()
        #print(conteudoDict['Windows']['Mouse'])
        return conteudoDict

    def findCategoria(self, collection):
 
        query = collection.find({}).distinct('Categoria')
        for item in query:
            self.categoria.append(item)
        return self.categoria
    
    def findSubCategoria(self, categoria,collection ):
        subCategoria = []
        #recebendo o nome da categoria a ser realizada a query
        query = collection.find({"Categoria":categoria}).distinct('Subcategoria')
        for item in query:
            subCategoria.append(item)
        return subCategoria
    
    def createListProblems(self,categoria,subCategoria, collection):
        listProblems = []
        query = collection.find({"Categoria": categoria, "Subcategoria": subCategoria})
        for item in query:
            listProblems.append(item)

        return listProblems
    def getTagsColletion(self):
        return self.db["tagsCollection"]
    def getProblemsCollection(self):
        return self.db["problemCollection"]
    def getSubCategoria(self):
        return self.subCategoria
    def getCategoria(self):
        return self.categoria

teste = DataBase()
conteudo = teste.getConteudo()
