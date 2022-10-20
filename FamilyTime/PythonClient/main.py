from helper.write_a_json import write_a_json
from db.database import Graph

#CONEXAO
db = Graph("bolt://34.234.215.220:7687", "neo4j", "purchase-unit-chattels")

def Estagiario():
    return db.execute_query("match (n:Estagiario) return n")

def idadeDaPessoa(nomeP):
    return db.execute_query("Match (p:Pessoa) WHERE p.nome = $nomeP RETURN p.nome,p.idade",{'nomeP':nomeP})
    
def dataCasamento(nomeP):
    return db.execute_query("match (n2:Pessoa)-[cc:CASADO_COM]->(n1:Pessoa) WHERE n2.nome=$nomeP return n1.nome,n2.nome,cc.desde",{'nomeP':nomeP})


r = Estagiario()
write_a_json(r,'Estagiario')

r = idadeDaPessoa('Paulo Henrique Ribeiro')
write_a_json(r,'idade')

r = dataCasamento('Ronaldo Martha')
write_a_json(r,'casado')