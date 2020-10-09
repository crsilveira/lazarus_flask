from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.sql import insert
from sqlalchemy.exc import SQLAlchemyError
import fdb
from flask import jsonify
import json
import datetime
from atsadmin.tabelas_ats import Cliente
from atsadmin.conexao_firebird import AtsConn
import os.path
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

    def integra_cli(self):
        path_file = '/home/publico/tmp/integra/cliente.txt'
        dados = []
        #import pudb;pu.db
        if os.path.exists(path_file):
            with open(path_file) as json_file:
                dados = json.load(json_file)
        else:
            cliente = {}
            cliente['codcliente'] = 0
            dados.append(cliente)
        return jsonify(dados)
        """
        lista = []
        for cli in con.query(Cliente).order_by(Cliente.codcliente).limit():
            cliente = {}
            cliente['codcliente'] = cli.codcliente
            cliente['nomecliente'] = cli.nomecliente
            cliente['razaosocial'] = cli.razaosocial
            cliente['cnpj'] = ''
            if cli.cnpj:
                cliente['cnpj'] = cli.cnpj
            x = cli.razaosocial
            print ('Cliente: %s' %(cli.nomecliente))
            lista.append(cliente)
            #indice += 1
        #
        """
        #lista.append('opa conectou')
        #return jsonify(lista)
        

    def integra_venda(self, dados):
        #con = AtsConn.sessao()
        path_file = '/home/publico/tmp/integra/'
        #import pudb;pu.db
        dados_json = json.loads(dados)
        feito = 'N'
        for item in dados_json:
            if 'pag' in item:
                x = dados_json[item]
                ver_json = json.loads(x)
                for det in ver_json:
                    codmov = det.get('CODMOVIMENTO')
                    arquivo = '%spag_%s.txt' %(path_file,codmov)
                    with open(arquivo, 'w') as f:
                        f.write(json.dumps(dados_json))
                        f.close
                        feito = 'pag_%s' %(codmov)
                    break
                break
            if 'CODCLIENTE' in dados_json:
                codmov = dados_json['CODMOVIMENTO']
                arquivo = '%smov_%s.txt' %(path_file,codmov)
                with open(arquivo, 'w') as f:
                        f.write(json.dumps(dados_json))
                        f.close
                        feito = 'mov_%s' %(codmov)
                break
            if 'item' in item:
                x = dados_json[item]
                ver_json = json.loads(x)
                for det in ver_json:
                    codmov = det.get('CODMOVIMENTO')
                    arquivo = '%sdet_%s.txt' %(path_file,codmov)
                    #data_file = open(arquivo, 'w')
                    with open(arquivo, 'w') as f:
                        f.write(json.dumps(dados_json))
                        f.close
                        feito = 'det_%s' %(codmov)
                    break
            break
            #z = json.dumps(item)
            #d = json.loads(z)
            
            #print (x)
        return feito

    def ver_cliente(self):
        #con = AtsConn.sessao()
        #session.query(User).filter(User.name=='John').first()

        lista = []
        #import pudb;pu.db
        
        #indice = 0
        """
        for cli in con.query(Cliente).order_by(Cliente.codcliente).limit(80):
            cliente = {}
            cliente['codcliente'] = cli.codcliente
            cliente['nomecliente'] = cli.nomecliente
            cliente['razaosocial'] = cli.razaosocial
            cliente['cnpj'] = ''
            if cli.cnpj:
                cliente['cnpj'] = cli.cnpj
            x = cli.razaosocial
            print ('Cliente: %s' %(cli.nomecliente))
            lista.append(cliente)
            #indice += 1
        #import pudb;pu.db
        """
        lista.append('opa conectou')
        return jsonify(lista)

    def cliente_insert(self, dados):
        import pudb;pu.db
        con = AtsConn.sessao()
        #Cliente.insert().values(dados)
        try:
            i = insert(Cliente)
            i = i.values(dados)
            con.execute(i)
            con.commit()
            con.close_all()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            con.close_all()
            return error
        return 'Cadastro incluido com sucesso.'

    def cliente_update(self, dados):
        #import pudb;pu.db
        con = AtsConn.sessao()
        # Convert Models to dicts
        #entry_dict = dados.as_dict()
        #db_result_dict = cli_ids.first().as_dict()

        # Update database result with passed in entry. Skip of None
        #for value in dados:
        #    if dados[value] is not None:
        #        cli_ids = dados[value]

        # Update db and close connections
        #cli_ids.update(dados)
        cli = con.query(Cliente).filter_by(codcliente=dados['codcliente'])
        #update_statement = Cliente.update()\
        #   .where(codcliente = dados['codcliente'])\
        #   .values(atualiza)
        try:
            cli.update(dados)
            con.commit()
            con.close_all()
        except:
            con.close_all()
            return 'ERRO na atualização do cadastro.'
        return 'Cadastro atualizado com sucesso.'

    def cliente_tabela(self):
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

    def estrutura_filtro(self):
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
        campos = {
            'campo': 'cnpj',
            'titulo': 'CNPJ/CPF',
            'tipo': 'VARCHAR',
            'tam': '80',
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
