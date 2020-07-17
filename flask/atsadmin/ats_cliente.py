from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
import fdb
from flask import jsonify
import json
import datetime
from atsadmin.tabelas_ats import Cliente
from atsadmin.conexao_firebird import AtsConn
#from browser import document
#from browser.html import INPUT, LABEL, BR, FORM

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    #import pudb;pu.db
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

class AtsCliente:
    _name = 'ats.cliente'
    _description = "Cadastro Clientes"
    
    def __init__(self):
        #import pudb;pu.db
        #con = AtsConn.sessao()
        #for cli in con.query(Cliente).order_by(Cliente.codcliente):
        #    print('Cliente : %s' %(cli.nomecliente))
        return None

    def ver_cliente(self):
        con = AtsConn.sessao()
        #session.query(User).filter(User.name=='John').first()

        lista = []
        #import pudb;pu.db
        #indice = 0
        for cli in con.query(Cliente).order_by(Cliente.codcliente).limit(80):
            cliente = {}
            cliente['codcliente'] = cli.codcliente
            cliente['nomecliente'] = cli.nomecliente
            cliente['razaosocial'] = cli.razaosocial
            x = cli.razaosocial
            print ('Cliente: %s' %(cli.nomecliente))
            lista.append(cliente)
            #indice += 1
        #import pudb;pu.db
        return jsonify(lista)
        
    def edita_cliente(self, dados):
        #import pudb;pu.db
        if dados:
            nome = dados['nomecliente']
            codigo = dados['codcliente']
        return 'Cliente atualizado com sucesso'

    def estrutura_cliente(self):
        # LEIO A TABELA INTEIR E CRIO UM JSON COM OS CAMPOS
        tabela = []
        for cli in Cliente.__table__.columns:
            campos = {}
            campos['campo'] = cli.name
            campos['tipo'] = str(cli.type)
            campos['tam'] = '0'
            if str(cli.type) not in ('INTEGER', 'SMALLINT', 'FLOAT', 'DATE', 'DATETIME'):
                campos['tam'] = str(cli.type.length)
            tabela.append(campos)
        #import pudb;pu.db
        return jsonify(tabela)

    def estrutura_cliente_grid(self):
        # VOU CRIAR UM JSON SOMENTE CAMPOS PRA EXIBIR GRID
        tabela = []
        campos = {
            'campo': 'codcliente',
            'titulo': 'Código',
            'tipo': 'INTEGER',
            'tam': '70',
            }
        tabela.append(campos)
        campos = {
            'campo': 'nomecliente',
            'titulo': 'Nome',
            'tipo': 'VARCHAR',
            'tam': '400',
            }
        tabela.append(campos)
        campos = {
            'campo': 'razaosocial',
            'titulo': 'Razão Social',
            'tipo': 'VARCHAR',
            'tam': '300',
            }
        tabela.append(campos)
        return jsonify(tabela)

    def consulta_cliente(self, codcliente=None, outros=None):
        con = AtsConn.sessao()
        lista = []
        #for cli in Cliente.__table__.columns:
        #    campos = {}
        #    campos['campo'] = cli.name
        #    tabela.append(campos)

        cli_ids = con.query(Cliente).filter(
            Cliente.codcliente==int(codcliente['codcliente'])).first()
        cli_dict = dict((col, getattr(cli_ids, col)) for col in cli_ids.__table__.columns.keys())
        linha = {}
        for value in cli_dict:
            # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # TODO tratar campos DATA, e campos Relacionados
            linha[value] = cli_dict[value]
        #import pudb;pu.db
        lista.append(linha)
        return jsonify(lista)

