import time

class ETL:
    
    def __init__(self):
      pass
  
    def minas_gerais(self,dados):
        try:
            if (str(dados[0]).index('MG') ==0):
                flag= True
            else:
                flag= False
        except Exception as e:
            flag = False
        
        return flag
    def carregar_dados(self):
        x = 0
        i = 0
        while (x <= 0):
            with open("municipios.csv", 'r') as textfile:  
                try:
                    lines = textfile.readlines()
                    dados = lines[i].split(',')
                    if (self.minas_gerais(dados)):
                        print(dados)
                    i += 1
                    textfile.close()
                except Exception as e:
                    print(e)
                    x = 1       
                    textfile.close() 

if __name__ == "__main__":
    etl = ETL()
    inicio = time.time()
    etl.carregar_dados()
    fim = time.time()
    print(fim - inicio)