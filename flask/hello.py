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
        if 'cliente_filtro' in data:
            cli = AtsCliente()
            x = cli.cliente_filtro()
            #import pudb;pu.db
        if 'cliente' in data:
            cli = AtsCliente()
            x = cli.consulta_cliente(data['cliente'])
        if 'cliente_update' in data:
            cli = AtsCliente()
            x = cli.cliente_update(data['cliente_update'])
        if 'cliente_insert' in data:
            cli = AtsCliente()
            x = cli.cliente_insert(data['cliente_insert'])
        if 'tab_venda' in data:
            cli = AtsCliente()
            x = cli.integra_venda(data['tab_venda'])
        return x
    else:
        #import pudb;pu.db
        cli = AtsCliente()
        z = cli.ver_cliente()
        return z

if __name__ == "__main__":
    app.run('0.0.0.0', port=8905, debug=False)
