from db.database import Graph
from helper.write_a_json import write_a_json as wj


# inicializando banco (NÃO APLICAVEL NO MOMENTO)
# with open('./BD.txt') as bd_init:
#     for line in bd_init:
#         n_line = line.replace('\n','')
#         db.execute_query(f'{n_line}')
#     print("Bd started!")



class UsedCarCrud():

    def __init__(self):
        self.db = Graph(uri='bolt://xx.xx.xx.xx:xxxx', user='neo4j', password='xxxxxxxxxxxxxxxx')

    # TBD
    # def create(self, name, ano_nasc, cpf):  # cria um Teacher`
    #     return wj(self.db.execute_query('CREATE (t:Teacher {name:$name, ano_nasc:$ano_nasc, cpf:$cpf}) return t',
    #                                     {'name': name, 'ano_nasc': ano_nasc,
    #                                      'cpf': cpf}), 'create')
    #
    # def read(self, name):  # retorna apenas um Teacher`
    #     return wj(self.db.execute_query('MATCH (t:Teacher {name:$name}) return t',
    #                                     {'name': name}), 'read')
    #
    # def update(self, name, newCpf):  # atualiza cpf com base no name`
    #     return wj(self.db.execute_query('MATCH (t:Teacher {name:$name}) SET t.cpf = $cpf RETURN t',
    #                                     {'name': name, 'cpf': newCpf}), 'update')
    #
    # def delete(self, name):  # deleta Teacher com base no name`
    #     return wj(self.db.execute_query('MATCH (t:Teacher {name:$name}) DELETE t',
    #                                     {'name': name}), 'delete')

if __name__ == '__main__':

    # instanciando objeto
    CarCrud = UsedCarCrud()
    carro = Car('VW','Gol',2015,'Flex',99000,'1.0','FGH8P99')

    print("Job finished")
