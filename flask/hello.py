from flask import Flask
from flask import request        
from atsadmin.ats_cliente import AtsCliente


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.json
        if 'dados' in data:
            cli = AtsCliente()
            x = cli.edita_cliente(data['dados'])
        if 'cliente_tabela' in data:
            cli = AtsCliente()
            x = cli.cliente_tabela()
            #import pudb;pu.db
        if 'estrutura_grid' in data:
            cli = AtsCliente()
            x = cli.estrutura_cliente_grid()
            #import pudb;pu.db
        if 'cliente' in data:
            cli = AtsCliente()
            x = cli.consulta_cliente(data['cliente'])
            #import pudb;pu.db

        return x
    else:
        #import pudb;pu.db
        cli = AtsCliente()
        z = cli.ver_cliente()
        return z

if __name__ == "__main__":
    app.run('0.0.0.0', debug=False)
