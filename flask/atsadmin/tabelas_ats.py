# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, LargeBinary, Numeric, SmallInteger, String, Table, Text, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


t_acesso = Table(
    'acesso', metadata,
    Column('grupo', String(20)),
    Column('subgrupo', String(50)),
    Column('perfil', String(15)),
    Column('enabled', Text(1)),
    Column('visible', Text(1))
)


class AcessoSenha(Base):
    __tablename__ = 'acesso_senha'

    login = Column(String(20), primary_key=True)
    senha = Column(String(10))
    perfil = Column(String(15))
    codusuario = Column(Integer)
    micro = Column(String(30))
    p1 = Column(String(30))
    p2 = Column(String(30))


class Agencia(Base):
    __tablename__ = 'agencia'

    codagencia = Column(String(18), primary_key=True)
    codbanco = Column(ForeignKey('banco.codbanco'), nullable=False)
    nomeagencia = Column(String(30), nullable=False)
    endagencia = Column(String(40))
    gerente = Column(String(30))
    telefone = Column(String(9))
    ramal = Column(String(5))
    fax = Column(String(9))
    email = Column(String(30))

    banco = relationship('Banco')


class AgendaDoDia(Base):
    __tablename__ = 'agenda_do_dia'

    data = Column(Date, primary_key=True)
    historico = Column(LargeBinary, nullable=False)


class Agendamento(Base):
    __tablename__ = 'agendamento'

    cod_agendamento = Column(Integer, primary_key=True)
    codcliente = Column(Integer)
    assunto = Column(String(200))
    hora = Column(Time)
    data = Column(Date)
    fone = Column(String(13))
    status = Column(String(20))
    codvenda = Column(Integer)
    codusuario = Column(Integer)


class Almoxarifado(Base):
    __tablename__ = 'almoxarifado'

    codalmoxarifado = Column(Integer, primary_key=True)
    almoxarifado = Column(String(30))


class Aponthora(Base):
    __tablename__ = 'aponthoras'

    id_aponthoras = Column(Integer, primary_key=True)
    cod_cliente = Column(Integer)
    cod_fornecedor = Column(Integer)
    cod_usuario = Column(Integer)
    data_movimento = Column(Date)
    cod_produto = Column(Integer)
    cod_cc = Column(Integer)


class Aponthorasdet(Base):
    __tablename__ = 'aponthorasdet'

    id_aponthorasdet = Column(Integer, primary_key=True)
    id_aponthoras = Column(Integer, nullable=False)
    data = Column(Date)
    tarefa_local = Column(String(150))
    inicio = Column(Time)
    termino = Column(Time)
    obs = Column(String(300))
    km = Column(Float)
    km_valor = Column(Float)
    km_total = Column(Float)
    despesa = Column(Float)
    pedagio = Column(Float)
    valor_hora = Column(Float)
    total_hora = Column(Float)
    total_geral = Column(Float)
    n_relatorio = Column(Integer)


class ArquivoRetorno(Base):
    __tablename__ = 'arquivo_retorno'

    idarquivo = Column(Integer, primary_key=True)
    arquivo = Column(String(60), nullable=False)
    idcampo = Column(String(10), nullable=False)
    tamcampo = Column(String(10), nullable=False)
    tipocampo = Column(String(60))


class Associado(Base):
    __tablename__ = 'associado'

    cod_associacao = Column(Integer, primary_key=True)
    cod_cliente = Column(Integer)
    valor = Column(Float)
    cod_associado = Column(Integer)
    associado = Column(String(80))
    d_venda = Column(Date)
    d_atraso = Column(Date)
    d_entrada = Column(Date)
    d_retirada = Column(Date)
    documento = Column(String(25))
    cod_endereco = Column(Integer)


class Atualiza(Base):
    __tablename__ = 'atualiza'

    codatualiza = Column(Integer, primary_key=True)
    script = Column(String(200))
    datascript = Column(Date)
    paraqserve = Column(String(200))
    versao = Column(String(50))
    inserido = Column(Text(1))
    data_modificado = Column(DateTime)


class Avaliacao(Base):
    __tablename__ = 'avaliacao'

    nota = Column(String(4), primary_key=True)
    peso = Column(Float)
    descricao = Column(String(50))


class Aviso(Base):
    __tablename__ = 'avisos'

    codavisos = Column(Integer, primary_key=True)
    tipo = Column(String(30))
    descricao = Column(Text)


class Banco(Base):
    __tablename__ = 'banco'

    codbanco = Column(SmallInteger, primary_key=True)
    banco = Column(String(18), nullable=False)
    nomebanco = Column(String(30), nullable=False)
    carteira = Column(Text(3))
    codigo_cedente = Column(String(10))
    codigo_empresa = Column(String(10))
    codigo_agencia = Column(String(10))
    digito_agencia = Column(Text(1))
    numero_conta = Column(String(10))
    digito_conta = Column(Text(1))
    codigo_plano = Column(Integer)
    instrucao1 = Column(String(100))
    instrucao2 = Column(String(100))
    instrucao3 = Column(String(100))
    instrucao4 = Column(String(100))
    cedente = Column(String(100))
    especiedoc = Column(String(5))
    aceite = Column(String(2))
    convenio = Column(String(10))
    localpgto = Column(String(100))
    n_banco = Column(String(10))
    digitobanco = Column(Integer)
    tam_lote = Column(Integer)
    nconvenio = Column(Integer)
    variacao = Column(String(3))
    codigoboleto = Column(String(20))
    layout_bl = Column(String(10))
    layout_rm = Column(String(10))
    resp_emissao = Column(String(20))
    imp_comprovante = Column(String(3))
    pasta_remessa = Column(String(100))
    pasta_retorno = Column(String(100))
    nome_arquivo = Column(String(30))
    cc_banco = Column(Integer)
    morajuros = Column(String(10))
    percmulta = Column(Float)
    protesto = Column(Text(2))
    dia_gerou_arquivo = Column(Date)
    sequencia_dia = Column(Integer)
    sequencia_arquivo = Column(Integer)
    gerando_arquivo = Column(Integer)


class Bancodepara(Base):
    __tablename__ = 'bancodepara'

    caixa = Column(Integer, primary_key=True, nullable=False)
    conta = Column(Integer, primary_key=True, nullable=False)
    extratodoc = Column(String(100), primary_key=True, nullable=False)
    extratotipo = Column(String(20), primary_key=True, nullable=False)


class Bancoextrato(Base):
    __tablename__ = 'bancoextrato'

    extratocod = Column(String(20), primary_key=True, nullable=False)
    extratodata = Column(Date, primary_key=True, nullable=False)
    caixa = Column(Integer, primary_key=True, nullable=False)
    extratodoc = Column(String(100))
    extratotipo = Column(String(20))
    extratovalor = Column(Float)
    sel = Column(Text(1))
    conciliado = Column(Text(1))


class Caixa(Base):
    __tablename__ = 'caixa'

    cod_caixa = Column(Integer, primary_key=True)
    caixa = Column(Integer)
    data = Column(DateTime)
    situacao = Column(String(10))
    valorentrada = Column(Float)
    historicocaixa = Column(String(100))
    nomecaixa = Column(String(15))
    valorsaida = Column(Float)


class CaixaBanco(Base):
    __tablename__ = 'caixa_banco'

    cod_caixa_banco = Column(SmallInteger, primary_key=True)
    n_caixa_banco = Column(String(20))
    caixa_banco = Column(String(100))
    conta_caixa_banco = Column(String(15))


class CaixaControle(Base):
    __tablename__ = 'caixa_controle'

    idcaixacontrole = Column(Integer, primary_key=True)
    codcaixa = Column(Integer)
    codusuario = Column(Integer, nullable=False)
    datafechamento = Column(Date, nullable=False)
    situacao = Column(Text(1), nullable=False)
    nomecaixa = Column(String(60))
    maquina = Column(String(60))
    dataabertura = Column(Date)
    valorabre = Column(Float)
    valorfecha = Column(Float)


class Caixafechamento(Base):
    __tablename__ = 'caixafechamento'

    datafechamento = Column(Date, primary_key=True)
    mes = Column(SmallInteger)
    ano = Column(SmallInteger)
    situacaocaixa = Column(Text(1))


class Cargosfunco(Base):
    __tablename__ = 'cargosfuncoes'

    cod_cargosfuncoes = Column(Integer, primary_key=True)
    descricao = Column(String(100))


class Cartorio(Base):
    __tablename__ = 'cartorio'

    codcartorio = Column(SmallInteger, primary_key=True)
    nome = Column(String(30), nullable=False, index=True)
    contato = Column(String(30))
    telefone = Column(String(9))


class Categoriaproduto(Base):
    __tablename__ = 'categoriaproduto'

    desccategoria = Column(String(30), primary_key=True)
    cod_categoria = Column(Integer)
    cod_familia = Column(Integer, nullable=False)


class Cbr643(Base):
    __tablename__ = 'cbr643'

    id_cbr = Column(Integer, primary_key=True)
    databaixa = Column(Date)
    nomecbr = Column(String(100), nullable=False)
    obs = Column(LargeBinary)


t_cce = Table(
    'cce', metadata,
    Column('chave', String(44)),
    Column('orgao', Integer),
    Column('cnpj', String(19)),
    Column('dhenvio', DateTime),
    Column('sequencia', Integer),
    Column('correcao', String(1000)),
    Column('protocolo', String(20)),
    Column('selecionou', Text(1)),
    Column('condicao', String(700))
)


t_cfop = Table(
    'cfop', metadata,
    Column('cfcod', String(30), nullable=False),
    Column('cfnome', String(250)),
    Column('cfnota', Text),
    Column('tipomovimento', Text(1)),
    Column('fretebc', Text(1)),
    Column('ipibc', Text(1)),
    Column('tottrib', Text(1)),
    Column('ind_pres', Integer)
)


class CheqBoletosDupl(Base):
    __tablename__ = 'cheq_boletos_dupl'

    cod_cheq_bol = Column(Integer, primary_key=True)
    cod_origem = Column(Integer, nullable=False, index=True)
    tipo_origem = Column(String(15), nullable=False)
    numero_doc = Column(Integer, nullable=False)
    codcli_forn = Column(Integer, nullable=False)
    cli_ou_forn = Column(Text(1), nullable=False)
    contacorrente = Column(String(18))
    dataemissao = Column(Date)
    datalancamento = Column(Date)
    datadeposito = Column(Date)
    valorcheque = Column(Float)
    descricao = Column(String(50))
    banco = Column(SmallInteger)
    agencia = Column(String(18))
    tipo_doc = Column(SmallInteger)
    lancado = Column(SmallInteger)


class Chg(Base):
    __tablename__ = 'chg'

    linha1 = Column(String(500))
    id = Column(Integer, primary_key=True)


class ClassificacaoServico(Base):
    __tablename__ = 'classificacao_servicos'

    codigo = Column(String(5), primary_key=True)
    aliquota = Column(Float)
    descricao_serv = Column(String(500))


class Classificacaofiscal(Base):
    __tablename__ = 'classificacaofiscal'

    classificao = Column(String(30), primary_key=True)
    codigo_reduz = Column(String(10))
    descricao = Column(String(100))
    tipo_classifica = Column(String(30))
    icms_subst = Column(Float)
    icms_subst_ic = Column(Float)
    icms_subst_ind = Column(Float)
    uf = Column(Text(2))


class Classificacaofiscalncm(Base):
    __tablename__ = 'classificacaofiscalncm'

    ncm = Column(String(8), primary_key=True, nullable=False)
    cfop = Column(String(30), primary_key=True, nullable=False)
    uf = Column(Text(2), primary_key=True, nullable=False)
    codfiscal = Column(Text(1), primary_key=True, nullable=False)
    icms_subst = Column(Float)
    icms_subst_ic = Column(Float)
    icms_subst_ind = Column(Float)
    icms = Column(Float)
    icms_base = Column(Float)
    cst = Column(Text(3))
    ipi = Column(Float)
    csosn = Column(String(3))
    cstipi = Column(String(2))
    cstpis = Column(String(2))
    cstcofins = Column(String(2))
    pis = Column(Float)
    cofins = Column(Float)
    origem = Column(Integer, primary_key=True, nullable=False)
    dadosadc1 = Column(String(200))
    dadosadc2 = Column(String(200))
    dadosadc3 = Column(String(200))
    dadosadc4 = Column(String(200))
    dadosadc5 = Column(String(200))
    dadosadc6 = Column(String(200))
    aliq_cupom = Column(Text(4))
    vbcufdest = Column(Float)
    pfcpufdest = Column(Float)
    picmsufdest = Column(Float)
    picmsinter = Column(Float)
    picmsinterpart = Column(Float)
    vfcpufdest = Column(Float)
    vicmsufdest = Column(Float)
    vicmsufremet = Column(Float)
    cst_ipi_cenq = Column(Text(3))
    redbasepis = Column(Float)
    redbasecofins = Column(Float)
    redbaseipi = Column(Float)


class Classificacaofiscalproduto(Base):
    __tablename__ = 'classificacaofiscalproduto'

    cod_prod = Column(Integer, primary_key=True, nullable=False)
    cfop = Column(String(30), primary_key=True, nullable=False)
    uf = Column(Text(2), primary_key=True, nullable=False)
    icms_subst = Column(Float)
    icms_subst_ic = Column(Float)
    icms_subst_ind = Column(Float)
    icms = Column(Float)
    icms_base = Column(Float)
    cst = Column(Text(3))
    ipi = Column(Float)
    csosn = Column(String(3))
    cstipi = Column(String(2))
    cstpis = Column(String(2))
    cstcofins = Column(String(2))
    pis = Column(Float)
    cofins = Column(Float)
    aliq_cupom = Column(Text(4))
    vbcufdest = Column(Float)
    pfcpufdest = Column(Float)
    picmsufdest = Column(Float)
    picmsinter = Column(Float)
    picmsinterpart = Column(Float)
    vfcpufdest = Column(Float)
    vicmsufdest = Column(Float)
    vicmsufremet = Column(Float)
    cst_ipi_cenq = Column(Text(3))


class ClienteTransp(Base):
    __tablename__ = 'cliente_transp'

    cod_cli_transp = Column(Integer, primary_key=True)
    codcliente = Column(Integer)
    codtransp = Column(ForeignKey('transportadora.codtransp'))

    transportadora = relationship('Transportadora')


t_cliente_view = Table(
    'cliente_view', metadata,
    Column('codcliente', Integer),
    Column('nomecliente', String(60)),
    Column('razaosocial', String(60)),
    Column('tipofirma', SmallInteger),
    Column('cnpj', String(18)),
    Column('inscestadual', String(24)),
    Column('status', SmallInteger),
    Column('endereco', String(50)),
    Column('numero', String(5)),
    Column('fone', String(16)),
    Column('fone1', String(16)),
    Column('fone2', String(16)),
    Column('bairro', String(30)),
    Column('cod_ibge', String(10)),
    Column('cidade', String(40)),
    Column('uf', Text(2)),
    Column('complemento', String(30)),
    Column('dadosadicionais', String(200)),
    Column('email', String(256)),
    Column('pais', String(60)),
    Column('tipo_endereco', SmallInteger),
    Column('data', Date)
)


class Clientecomanda(Base):
    __tablename__ = 'clientecomanda'

    cod_clicomanda = Column(Integer, primary_key=True)
    cod_comanda = Column(Integer)
    cod_cliente = Column(Integer)
    rg = Column(String(14))
    data = Column(Date)
    horaentrada = Column(DateTime)
    horasaida = Column(DateTime)
    valorconsumo = Column(Float)


class Cliente(Base):
    __tablename__ = 'clientes'

    codcliente = Column(Integer, primary_key=True, index=True)
    nomecliente = Column(String(60), nullable=False, index=True)
    razaosocial = Column(String(60), nullable=False)
    contato = Column(String(30))
    tipofirma = Column(SmallInteger, nullable=False)
    cpf = Column(String(14))
    cnpj = Column(String(18))
    inscestadual = Column(String(24))
    rg = Column(String(14))
    segmento = Column(SmallInteger, nullable=False)
    regiao = Column(SmallInteger, nullable=False)
    limitecredito = Column(Float)
    datacadastro = Column(Date, nullable=False)
    codusuario = Column(Integer, nullable=False)
    status = Column(SmallInteger, nullable=False)
    homepage = Column(String(40))
    prazorecebimento = Column(SmallInteger)
    prazoentrega = Column(SmallInteger)
    codbanco = Column(SmallInteger)
    base_icms = Column(SmallInteger)
    datanasc = Column(Date)
    conta_cliente = Column(String(15))
    obs = Column(String(200))
    tem_ie = Column(Text(1))
    dataresc = Column(Date)
    nomemae = Column(String(80))
    sexo = Column(Text(1))
    #forma_correspond = Column(String(30))
    grupo_cliente = Column(String(30))
    #codinclucanc = Column(Integer)
    #exist_cobert = Column(String(6))
    #existcopart = Column(String(6))
    #datareinc = Column(Date)
    geraaviso = Column(Text(1))
    geraenv = Column(Text(1))
    gerabol = Column(Text(1))
    #emviagem = Column(Text(1))
    dtaaltera = Column(Date)
    #serieletra = Column(String(4))
    #serie = Column(String(4))
    #ra = Column(String(10))
    #curso = Column(String(50))
    #ip = Column(String(60))
    #n_contrato = Column(String(60))
    #mac = Column(String(60))
    #marca = Column(String(60))
    #banda_upload = Column(String(60))
    #banda_dowload = Column(String(60))
    #torre_coneccao = Column(String(60))
    #cod_faixa = Column(Integer)
    desconto = Column(Float)
    #mensalidade = Column(Float)
    #anuidade = Column(Float)
    #parcela = Column(Integer)
    #parcelageradas = Column(Integer)
    #numero = Column(Integer)
    #datanascimento = Column(DateTime)
    #anoletivo = Column(String(4))
    #situacaoescolar = Column(String(2))
    #rgmae = Column(String(15))
    #cpfmae = Column(String(14))
    #pai = Column(String(30))
    #rgpai = Column(String(15))
    #cpfpai = Column(String(14))
    #lancadoclasse = Column(Integer)
    #transporte = Column(String(50))
    #cidadenasc = Column(String(30))
    #ufnasc = Column(String(2))
    #nacionalidade = Column(String(15))
    #certidaonascnum = Column(String(10))
    #livronasc = Column(String(10))
    #fllivronasc = Column(String(5))
    #localtrabpai = Column(String(30))
    #localtrabmae = Column(String(30))
    #teltrabpai = Column(String(15))
    #teltrabmae = Column(String(15))
    #infonecessarias = Column(String(30))
    #carteiravacinacao = Column(String(10))
    #raprodesp = Column(String(10))
    #localtrabaluno = Column(String(30))
    #teltrabaluno = Column(String(15))
    #raprod = Column(String(15))
    #cert_nas_comarca = Column(String(50))
    #cert_nas_uf = Column(String(2))
    #cert_nas_municipio = Column(String(50))
    #cert_nas_distrito = Column(String(50))
    #cert_nas_subdistrito = Column(String(50))
    diverso1 = Column(String(50))
    diverso2 = Column(String(50))
    #dataemissaorg = Column(Date)
    #estadorg = Column(Text(2))
    #comunicaaluno = Column(String(50))
    #fonemae = Column(String(15))
    #celularmae = Column(String(15))
    #comunicamae = Column(String(50))
    #fonepai = Column(String(15))
    #celularpai = Column(String(15))
    #comunicapai = Column(String(50))
    #valor_matricula = Column(Float)
    #datatransf = Column(Date)
    #cor_raca = Column(String(25))
    #periodo = Column(String(15))
    #foto = Column(String(300))
    #data_matricula = Column(DateTime)
    #codresponsavel = Column(Integer)
    #id_cob = Column(Integer)
    cod_tranportadora = Column(Integer)
    bloqueio = Column(Text(1))
    codcli = Column(String(10))
    cfop = Column(Text(4))
    cod_cli = Column(String(10))
    #cortesia = Column(Text(1))
    #valor_consumo = Column(Float)
    #valor_cortesia = Column(Float)
    e_fornecedor = Column(Text(1))
    codfornecedor = Column(Integer)
    codfiscal = Column(ForeignKey('tipo_fiscal.codfiscal'))
    cargofuncao = Column(Integer)
    suframa = Column(String(9))
    bloqueado = Column(Text(1))

    tipo_fiscal = relationship('TipoFiscal')


class ClientesDep(Base):
    __tablename__ = 'clientes_dep'

    codclidepen = Column(Integer, primary_key=True)
    codcliente = Column(Integer, nullable=False)
    dependente = Column(String(30))
    nomedependente = Column(String(80))
    dtanasc = Column(Date)
    status = Column(SmallInteger)
    dtaresc = Column(Date)
    sexo = Column(Text(1))
    nomemae = Column(String(50))
    dtainc = Column(Date)
    rg = Column(String(20))
    emviagem = Column(Text(1))
    deslans = Column(Text(1))
    coddpec = Column(Integer)


class Codigo(Base):
    __tablename__ = 'codigos'

    cod_codigo = Column(Integer, primary_key=True)
    cod_produto = Column(ForeignKey('produtos.codproduto'), index=True)
    codigo = Column(String(15))
    numero = Column(String(1))

    produto = relationship('Produto')


class Comissao(Base):
    __tablename__ = 'comissao'

    cod_comissao = Column(Integer, primary_key=True)
    codigo = Column(String(3))
    descricao = Column(String(20))
    indice = Column(String(10))
    lb = Column(String(10))
    cm = Column(String(10))


class Comissaocolaborador(Base):
    __tablename__ = 'comissaocolaborador'

    cod_comissao = Column(Integer, primary_key=True)
    cod_colaborador = Column(Integer)
    cod_produto = Column(Integer)
    valorcomissao = Column(Float)


class Compra(Base):
    __tablename__ = 'compra'

    codcompra = Column(Integer, primary_key=True)
    codmovimento = Column(ForeignKey('movimento.codmovimento'), nullable=False)
    codfornecedor = Column(ForeignKey('fornecedor.codfornecedor'), nullable=False)
    datacompra = Column(Date, nullable=False, index=True)
    datavencimento = Column(Date, nullable=False)
    numerobordero = Column(Integer)
    banco = Column(SmallInteger)
    codcomprador = Column(SmallInteger)
    status = Column(SmallInteger)
    codusuario = Column(SmallInteger)
    datasistema = Column(Date)
    valor = Column(Float)
    notafiscal = Column(Integer)
    serie = Column(String(20))
    desconto = Column(Float)
    codccusto = Column(SmallInteger)
    n_parcela = Column(SmallInteger)
    operacao = Column(Text(1))
    formapagamento = Column(Text(1))
    n_documento = Column(String(20))
    caixa = Column(SmallInteger)
    multa_juros = Column(Float)
    apagar = Column(Float)
    valor_pagar = Column(Float)
    entrada = Column(Float)
    n_boleto = Column(String(30))
    status1 = Column(Text(1))
    valor_icms = Column(Float)
    valor_frete = Column(Float)
    valor_seguro = Column(Float)
    outras_desp = Column(Float)
    valor_ipi = Column(Float)
    cfop = Column(String(4))
    prazo = Column(String(40))
    codorigem = Column(Integer)
    icms_st = Column(Float)
    icms_base_st = Column(Float)
    chavenf = Column(String(44))
    indpag = Column(Integer)
    digitovalidacao = Column(String(100))
    modelo = Column(String(2))

    fornecedor = relationship('Fornecedor')
    movimento = relationship('Movimento')


class CompraCotacao(Base):
    __tablename__ = 'compra_cotacao'

    cotacao_codigo = Column(Integer, primary_key=True, nullable=False)
    cotacao_data = Column(Date, server_default=text("current_date"))
    cotacao_fornec = Column(Integer, primary_key=True, nullable=False)
    cotacao_solicit = Column(String(20))
    cotacao_item = Column(String(15), nullable=False)
    cotacao_itemdescricao = Column(String(300))
    cotacao_situacao = Column(Text(1))
    cotacao_qtde = Column(Float)
    cotacao_preco = Column(Float)
    cotacao_user = Column(String(20))
    cotacao_tipo = Column(Text(1))
    cotacao_codsolic = Column(Integer)
    cotacao_dtentrega = Column(Date)
    cotacao_prazo = Column(String(30))
    cotacao_observacao = Column(String(200))
    cotacao_ipi = Column(Float)
    cotacao_desconto = Column(Float)
    cotacao_frete = Column(Float)


class CompraSolic(Base):
    __tablename__ = 'compra_solic'

    solic_codigo = Column(Integer, primary_key=True)
    solic_data = Column(Date, server_default=text("current_date"))
    solic_produto = Column(String(15), nullable=False)
    solic_quantidade = Column(Float)
    solic_solicitante = Column(String(30))
    solic_situacao = Column(Text(1))
    solic_aprovacao = Column(String(30))
    solic_dataaprov = Column(Date)
    solic_descricao = Column(String(300))
    solic_tipo = Column(Text(1))
    solic_dtnecessit = Column(Date)


class Condico(Base):
    __tablename__ = 'condicoes'

    condicoes = Column(SmallInteger, primary_key=True)
    descricao = Column(String(20), nullable=False)


class Contacorrente(Base):
    __tablename__ = 'contacorrente'

    conta = Column(String(18), primary_key=True, index=True)
    codagencia = Column(String(18), nullable=False)
    limiteconta = Column(Numeric(8, 2))
    tipoconta = Column(SmallInteger)


class Contasapagar(Base):
    __tablename__ = 'contasapagar'

    codapagar = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(18), nullable=False, index=True)
    emissao = Column(Date, nullable=False)
    valortitulo = Column(Float)
    status = Column(SmallInteger, nullable=False)
    codfornecedor = Column(Integer)
    codreferencia = Column(SmallInteger)
    codusuario = Column(SmallInteger)
    datalancamento = Column(Date)
    datavencimento = Column(Date)


class DadosCombo(Base):
    __tablename__ = 'dados_combos'

    coddados = Column(Integer, primary_key=True)
    descricao = Column(String(80))
    uso = Column(String(30))
    codigos = Column(String(50))
    outros = Column(String(30))


class Declaracaoimportacao(Base):
    __tablename__ = 'declaracaoimportacao'

    di_coddi = Column(Integer, primary_key=True)
    di_numdi = Column(String(10), nullable=False)
    di_data = Column(Date)
    di_localdesemb = Column(String(60))
    di_ufdesemb = Column(String(2))
    di_datadesemb = Column(Date)
    di_codexportador = Column(String(60))
    notaserie = Column(String(10))
    codmovimento = Column(Integer)


t_diadicao = Table(
    'diadicao', metadata,
    Column('adic_coddet', ForeignKey('movimentodetalhe.coddetalhe')),
    Column('adic_coddi', Integer),
    Column('adic_nadicao', Integer, nullable=False),
    Column('adic_nsequen', Integer, nullable=False),
    Column('adic_codfab', String(60)),
    Column('adic_vdesc', Integer)
)


class EmailEnviar(Base):
    __tablename__ = 'email_enviar'

    codemail = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    assunto = Column(String(200))
    dataenvio = Column(Date)
    grupo = Column(String(30))
    enviado = Column(Text(1))


class Empresa(Base):
    __tablename__ = 'empresa'

    empresa = Column(String(80), nullable=False)
    razao = Column(String(80), nullable=False)
    cnpj_cpf = Column(String(20), primary_key=True)
    endereco = Column(String(80))
    logradouro = Column(String(80))
    bairro = Column(String(40))
    cidade = Column(String(50))
    uf = Column(Text(2))
    cep = Column(Text(9))
    ddd = Column(Text(2))
    fone = Column(String(12))
    fone_1 = Column(String(12))
    fone_2 = Column(String(12))
    fax = Column(String(12))
    e_mail = Column(String(100))
    web = Column(String(50))
    logotipo = Column(LargeBinary)
    codigo = Column(Integer)
    tipo = Column(Text(1))
    ie_rg = Column(String(15))
    slogan = Column(String(60))
    outras_info = Column(String(60))
    codigo_conta = Column(Integer)
    diversos1 = Column(String(50))
    diversos2 = Column(String(50))
    diversos3 = Column(String(50))
    anoletivo = Column(Integer)
    media_escola = Column(Float)
    porta = Column(Integer)
    smtp = Column(String(60))
    senha = Column(String(30))
    ccusto = Column(Integer)
    numero = Column(String(5))
    cd_ibge = Column(String(10))
    crt = Column(Integer)
    tregime = Column(Integer)
    im = Column(String(15))
    contador = Column(String(100))
    contador_crc = Column(Text(20))
    contador_cnpj = Column(Text(14))
    contador_cpf = Column(Text(11))
    contador_cep = Column(Text(10))
    contador_end = Column(String(150))
    contador_numend = Column(Text(7))
    contador_compl = Column(String(80))
    contador_bairro = Column(String(100))
    contador_fone = Column(String(14))
    contador_fax = Column(String(14))
    contador_email = Column(String(100))
    contador_cod_mun = Column(Text(10))
    codindtipocon = Column(SmallInteger)
    indaprocred = Column(SmallInteger)
    codindinctributaria = Column(SmallInteger)
    indicadoratividade = Column(SmallInteger)
    indicadornaturezapj = Column(SmallInteger)
    indcodincidencia = Column(SmallInteger)
    codindcritescrit = Column(SmallInteger)
    indescrituracao = Column(SmallInteger)
    indcta = Column(SmallInteger)
    indtipcoop = Column(SmallInteger)
    indaj = Column(SmallInteger)
    basecalculocredito = Column(SmallInteger)
    codaj = Column(SmallInteger)
    indnatrec = Column(SmallInteger)
    codcred = Column(SmallInteger)
    natcreddesc = Column(SmallInteger)
    indcredori = Column(SmallInteger)
    indrec = Column(SmallInteger)
    codcont = Column(SmallInteger)
    inddesccred = Column(SmallInteger)
    indorigemdiversas = Column(SmallInteger)
    indnatretfonte = Column(SmallInteger)
    indtpoperacaoreceita = Column(SmallInteger)
    indnatdeducao = Column(SmallInteger)
    cnpjprefeitura = Column(String(14))
    nomeprefeitura = Column(String(50))
    chavelic = Column(String(50))
    chavecont = Column(String(50))
    modelocupom = Column(String(2))
    ecfmod = Column(String(20))
    ecffab = Column(String(20))
    ecfcx = Column(String(3))


class Enderecocliente(Base):
    __tablename__ = 'enderecocliente'

    codendereco = Column(Integer, primary_key=True, index=True)
    codcliente = Column(Integer, nullable=False, index=True)
    logradouro = Column(String(50))
    bairro = Column(String(30))
    complemento = Column(String(30))
    cidade = Column(String(40))
    uf = Column(Text(2))
    cep = Column(String(10))
    telefone = Column(String(12))
    telefone1 = Column(String(12))
    telefone2 = Column(String(12))
    fax = Column(String(9))
    e_mail = Column(String(256))
    ramal = Column(String(5))
    tipoend = Column(SmallInteger, nullable=False)
    dadosadicionais = Column(String(200))
    ddd = Column(String(3))
    ddd1 = Column(String(3))
    ddd2 = Column(String(3))
    ddd3 = Column(String(3))
    numero = Column(String(5))
    cd_ibge = Column(String(10))
    pais = Column(String(60))


class Enderecofornecedor(Base):
    __tablename__ = 'enderecofornecedor'

    codendereco = Column(Integer, primary_key=True, index=True)
    codfornecedor = Column(Integer, nullable=False, index=True)
    logradouro = Column(String(50))
    bairro = Column(String(30))
    complemento = Column(String(30))
    cidade = Column(String(40))
    uf = Column(Text(2))
    cep = Column(String(10))
    ddd = Column(SmallInteger)
    telefone = Column(String(9))
    telefone1 = Column(String(9))
    telefone2 = Column(String(9))
    fax = Column(String(9))
    e_mail = Column(String(256))
    ramal = Column(String(5))
    tipoend = Column(SmallInteger, nullable=False)
    dadosadicionais = Column(String(200))
    cd_ibge = Column(String(10))
    numero = Column(String(5))
    pais = Column(String(60))


t_estado = Table(
    'estado', metadata,
    Column('codigo', Integer, nullable=False),
    Column('sigla', Text(2)),
    Column('nome', String(60))
)


class EstadoIcm(Base):
    __tablename__ = 'estado_icms'

    codestado = Column(Integer, primary_key=True)
    cfop = Column(String(30), nullable=False)
    uf = Column(Text(3))
    icms = Column(Float, server_default=text("0"))
    reducao = Column(Float, server_default=text("0"))
    subst_trib = Column(Float, server_default=text("0"))
    ipi = Column(Float, server_default=text("0"))
    icms_substrib = Column(Float)
    icms_substrib_ic = Column(Float)
    icms_substrib_ind = Column(Float)
    cst = Column(Text(3))
    pessoa = Column(String(8))
    pis = Column(Float)
    cofins = Column(Float)
    cstipi = Column(String(2))
    cstpis = Column(String(2))
    cstcofins = Column(String(2))
    dadosadc1 = Column(String(200))
    dadosadc2 = Column(String(200))
    dadosadc3 = Column(String(200))
    dadosadc4 = Column(String(200))
    naoenvfatura = Column(Text(1))
    dadosadc5 = Column(String(200))
    dadosadc6 = Column(String(200))
    csosn = Column(String(3))
    codfiscal = Column(ForeignKey('tipo_fiscal.codfiscal'))
    aliq_cupom = Column(Text(4))
    vbcufdest = Column(Float)
    pfcpufdest = Column(Float)
    picmsufdest = Column(Float)
    picmsinter = Column(Float)
    picmsinterpart = Column(Float)
    vfcpufdest = Column(Float)
    vicmsufdest = Column(Float)
    vicmsufremet = Column(Float)
    cst_ipi_cenq = Column(Text(3))

    tipo_fiscal = relationship('TipoFiscal')


class Estoque(Base):
    __tablename__ = 'estoque'

    cod_estoq = Column(String(20), primary_key=True)
    cod_movimento = Column(Integer)
    data = Column(Date)
    codproduto = Column(Integer)
    entrada = Column(Float)
    compra = Column(Float)
    devolucao = Column(Float)
    outras_ent = Column(Float)
    saida = Column(Float)
    venda = Column(Float)
    perda = Column(Float)
    reposicao = Column(Float)
    outra_sai = Column(Float)
    centrocusto = Column(Integer)


class EstoqueControle(Base):
    __tablename__ = 'estoque_controle'

    idestoquecontrole = Column(Integer, primary_key=True)
    codusuario = Column(Integer, nullable=False)
    datafechamento = Column(Date, nullable=False)
    situacao = Column(Text(1), nullable=False)


class Estoqueccusto(Base):
    __tablename__ = 'estoqueccusto'

    codtab = Column(Integer, primary_key=True)
    codproduto = Column(Integer, nullable=False)
    codccusto = Column(Integer, nullable=False)
    qtdeestoque = Column(Float)
    pmestoque = Column(Float)
    vlrestoque = Column(Float)


class Estoqueme(Base):
    __tablename__ = 'estoquemes'

    codproduto = Column(Integer, primary_key=True, nullable=False)
    lote = Column(String(60), primary_key=True, nullable=False)
    mesano = Column(Date, primary_key=True, nullable=False)
    qtdeentrada = Column(Float)
    qtdecompra = Column(Float)
    qtdedevcompra = Column(Float)
    qtdesaida = Column(Float)
    qtdevenda = Column(Float)
    qtdeperda = Column(Float)
    precocusto = Column(Float)
    precocompra = Column(Float)
    precocompraultima = Column(Float)
    precovenda = Column(Float)
    centrocusto = Column(Integer, primary_key=True, nullable=False)
    qtdedevvenda = Column(Float)
    qtdeinventario = Column(Float)
    saldomesanterior = Column(Float)
    saldoestoque = Column(Float)
    datavencimento = Column(Date)
    datafabricacao = Column(Date)


class FaixaEtaria(Base):
    __tablename__ = 'faixa_etaria'

    codfaixa = Column(Integer, primary_key=True)
    descricao = Column(String(50))
    idade_min = Column(SmallInteger)
    idade_max = Column(SmallInteger)
    valor_plano = Column(Float)
    desconto = Column(Float)
    uso = Column(String(20))
    parcela = Column(Integer)
    valorparcela = Column(Float)
    codigos = Column(Integer)


class Faixaetariadetalhe(Base):
    __tablename__ = 'faixaetariadetalhe'

    codfaixadet = Column(Integer, primary_key=True)
    codfaixa = Column(Integer)
    descricao = Column(String(80))
    tipo = Column(String(15))


class Familiaproduto(Base):
    __tablename__ = 'familiaprodutos'

    descfamilia = Column(String(30), primary_key=True)
    cod_familia = Column(Integer)
    marca = Column(String(30))


class Fichamedica(Base):
    __tablename__ = 'fichamedica'

    id_ficha = Column(Integer, primary_key=True)
    ra = Column(String(10))
    d_mental = Column(String(5))
    d_visual = Column(String(5))
    d_auditiva = Column(String(5))
    d_fisica = Column(String(5))
    d_multipla = Column(String(5))
    super_dotado = Column(String(5))
    conduta_tipica = Column(String(5))
    outros = Column(String(5))
    outros_h = Column(Text)
    tem_acompanhante = Column(Text(1))
    tipo_acompanhante = Column(String(15))
    cquemmora = Column(String(6))
    nome_outros = Column(String(150))
    empresa_outros = Column(String(150))
    fone_outros = Column(String(13))
    fone1_outros = Column(String(13))
    fone2_outros = Column(String(13))
    ramal_outros = Column(String(4))
    horas_estuda = Column(Integer)
    professores_particular = Column(Integer)
    canhoto_destro = Column(Integer)
    alergico = Column(Text(1))
    tipo_alergia = Column(String(250))
    medico_aluno = Column(Integer)
    tratamento_medico = Column(Integer)
    tipo_tratamento = Column(String(250))
    ingerindo_medicacao = Column(Integer)
    tipo_medicacao = Column(String(250))
    nome_medico = Column(String(100))
    fone_medico = Column(String(13))
    endereco_medico = Column(String(100))
    plano_saude = Column(Integer)
    qual_plano = Column(String(50))
    ser_medicado_por = Column(String(50))
    doenca_congenita = Column(Integer)
    qual_doenca = Column(String(50))
    contraiu_caxumba = Column(String(5))
    contraiu_sarampo = Column(String(5))
    contraiu_rubeola = Column(String(5))
    contraiu_catapora = Column(String(5))
    contraiu_escarlatina = Column(String(5))
    contraiu_coqueluche = Column(String(5))
    contraiu_outras = Column(String(5))
    quais_outra = Column(String(200))
    nome_aviso = Column(String(100))
    endereco_aviso = Column(String(100))
    parentesco_aviso = Column(String(30))
    fone_aviso = Column(String(13))
    hospital_aviso = Column(String(100))
    tem_hipertencao = Column(Integer)
    hipertencao = Column(String(60))
    e_epiletico = Column(Integer)
    epiletico = Column(String(60))
    e_hemofilico = Column(Integer)
    hemofilico = Column(String(60))
    e_deficiente_auditivo = Column(Integer)
    deficiente_auditivo = Column(String(60))
    e_deficiente_visual = Column(Integer)
    deficiente_visual = Column(String(60))
    e_deficiente_fisico = Column(Integer)
    deficiente_fisico = Column(String(60))
    e_diabetico = Column(Integer)
    diabetico = Column(String(60))
    usa_insulina = Column(Integer)
    autorizado_dx_escola_soz = Column(Integer)
    observacoes = Column(Text)
    motivo_medicamento = Column(String(150))
    apto = Column(Text(1))
    esperar_fora_escola = Column(Integer)
    fone_hospital = Column(String(13))
    nome_retira = Column(String(100))
    endereco_retira = Column(String(100))
    parentesco_retira = Column(String(30))
    fone_retira = Column(String(13))
    psicologo = Column(String(5))
    fisioterapia = Column(String(5))
    medico = Column(String(5))
    fonoaudiologo = Column(String(5))
    psicopedagogo = Column(String(5))
    outro_1 = Column(String(5))
    nao = Column(String(5))
    e_asmatico = Column(Integer)
    asmatico = Column(String(60))


class FormaEntrada(Base):
    __tablename__ = 'forma_entrada'

    cod_venda = Column(Integer, nullable=False)
    id_entrada = Column(Integer, nullable=False)
    forma_pgto = Column(Text(1))
    caixa = Column(SmallInteger)
    n_doc = Column(String(60))
    valor_pago = Column(Float)
    caixinha = Column(Float)
    state = Column(SmallInteger)
    troco = Column(Float)
    desconto = Column(Float)
    codforma = Column(Integer, primary_key=True)


class Fornecedor(Base):
    __tablename__ = 'fornecedor'

    codfornecedor = Column(Integer, primary_key=True, index=True)
    nomefornecedor = Column(String(60), nullable=False, index=True)
    razaosocial = Column(String(60), nullable=False)
    contato = Column(String(30))
    tipofirma = Column(SmallInteger, nullable=False)
    cpf = Column(String(14))
    cnpj = Column(String(18))
    inscestadual = Column(String(24))
    rg = Column(String(14))
    segmento = Column(SmallInteger, nullable=False)
    regiao = Column(SmallInteger, nullable=False)
    limitecredito = Column(Float)
    datacadastro = Column(Date, nullable=False)
    codusuario = Column(Integer, nullable=False)
    status = Column(SmallInteger, nullable=False)
    homepage = Column(String(40))
    prazopagamento = Column(SmallInteger)
    prazoentrega = Column(SmallInteger)
    conta_fornecedor = Column(String(15))
    codfor = Column(String(10))
    codtransp = Column(Integer)
    campoadicional = Column(String(60))
    campoadicional1 = Column(String(60))
    codfiscal = Column(ForeignKey('tipo_fiscal.codfiscal'))
    cfop = Column(String(30))

    tipo_fiscal = relationship('TipoFiscal')


class Frequencia(Base):
    __tablename__ = 'frequencia'

    cod_frequencia = Column(Integer, primary_key=True)
    cod_funcionario = Column(Integer)
    data = Column(Date)
    horainicio = Column(DateTime)
    horasaida = Column(DateTime)


class Funcao(Base):
    __tablename__ = 'funcao'

    codfuncao = Column(Integer, primary_key=True)
    descricao = Column(String(80))


class Funcionario(Base):
    __tablename__ = 'funcionario'

    cod_funcionario = Column(Integer, primary_key=True)
    sexo = Column(String(10))
    estado_civil = Column(String(15))
    data_nasc = Column(Date)
    rua = Column(String(60))
    n = Column(String(5))
    complemento = Column(String(60))
    bairro = Column(String(60))
    cidade = Column(String(60))
    uf = Column(String(3))
    cep = Column(String(10))
    rg = Column(String(13))
    telefone = Column(String(13))
    celular = Column(String(13))
    recebe_comissao = Column(String(1))
    valor_comissao = Column(Float)
    esposa = Column(String(60))
    pai = Column(String(60))
    mae = Column(String(60))
    nome_funcionario = Column(String(60))
    cpf = Column(Text(14))
    ddd = Column(Text(2))
    codusuario = Column(Integer)
    funcao_cargo = Column(String(50))
    data_admissao = Column(Date)
    data_desligamento = Column(Date)
    regiao_venda = Column(String(200))
    especialidade = Column(String(100))
    contacorrente = Column(String(30))
    banco = Column(String(30))
    agencia = Column(String(30))
    codcliente = Column(Integer)
    codfornecedor = Column(Integer)
    clifor = Column(Text(1))
    status = Column(Text(1))
    salario = Column(Float)
    email = Column(String(80))


t_furacao = Table(
    'furacao', metadata,
    Column('forn', String(3)),
    Column('ref', String(12)),
    Column('codbar', String(13)),
    Column('codbar2', String(13)),
    Column('descr', String(29)),
    Column('nrorig', String(13)),
    Column('conversao', String(13)),
    Column('unid', String(2)),
    Column('preco', Float),
    Column('multi', Float),
    Column('tipo', String(1)),
    Column('promo', String(1)),
    Column('qtdpromo', Float),
    Column('pvpromo', Float)
)


class Guiatransporte(Base):
    __tablename__ = 'guiatransporte'

    id_guia = Column(Integer, primary_key=True)
    conhecimento = Column(Integer)
    natop = Column(String(60))
    codigo = Column(String(20))
    emissaolocal = Column(String(60))
    cod_cliente = Column(Integer)
    cod_consignatario = Column(Integer)
    cod_redespacho = Column(Integer)
    pago = Column(Text(1))
    apagar = Column(Text(1))
    id_transportadora = Column(Integer)
    basecalculo = Column(Float)
    aliquota = Column(Float)
    icms = Column(Float)
    fretepesovolume = Column(String(20))
    fretevalor = Column(Float)
    cadsce = Column(String(15))
    despacho = Column(String(15))
    pedagio = Column(Float)
    outroes = Column(Float)
    totalprestacao = Column(Float)
    coleta = Column(String(100))
    entrega = Column(String(100))
    obs = Column(String(300))
    data = Column(Date)
    notafiscal = Column(Integer)
    valor_prod1 = Column(Float)
    quantidade1 = Column(Float)
    un1 = Column(Text(3))
    descproduto1 = Column(String(100))
    notafiscal2 = Column(Integer)
    valor_prod2 = Column(Float)
    quantidade2 = Column(Float)
    un2 = Column(Text(3))
    descproduto2 = Column(String(100))
    cod_remetente = Column(Integer)
    placa = Column(String(8))
    cidade_transp = Column(String(60))
    uf_transp = Column(Text(2))
    total = Column(Float)
    total2 = Column(Float)


class HistoricoContab(Base):
    __tablename__ = 'historico_contab'

    cod_contab = Column(Integer, primary_key=True)
    historico = Column(String(200), nullable=False)


class Historicocliente(Base):
    __tablename__ = 'historicocliente'

    codhistorico = Column(Integer, primary_key=True, index=True)
    codcliente = Column(Integer, nullable=False)
    data = Column(Date, nullable=False)
    assunto = Column(String(30), nullable=False)
    descricao = Column(String(200), nullable=False)


class Historicofornecedor(Base):
    __tablename__ = 'historicofornecedor'

    codhistorico = Column(Integer, primary_key=True, index=True)
    codfornecedor = Column(Integer, nullable=False)
    data = Column(Date, nullable=False)
    assunto = Column(String(30), nullable=False)
    descricao = Column(String(200), nullable=False)


t_ibpt = Table(
    'ibpt', metadata,
    Column('ncm', String(8), nullable=False),
    Column('aliqnac', Float),
    Column('aliqimp', Float),
    Column('tipo', Text(1)),
    Column('ex', Integer),
    Column('descricao', String(100)),
    Column('estadual', Float),
    Column('municipal', Float),
    Column('vigenciainicio', Date),
    Column('vigenciafim', Date),
    Column('chave', String(20)),
    Column('versao', String(20)),
    Column('fonte', String(60))
)


class Idocumento(Base):
    __tablename__ = 'idocumentos'

    id_doctos = Column(Integer, primary_key=True)
    doctos_descricao = Column(String(40))
    doctos_padrao = Column(String(1))


class ImportaTxt(Base):
    __tablename__ = 'importa_txt'

    id_importa = Column(Integer, primary_key=True)
    fornecedor = Column(String(30))
    campo = Column(String(30))
    inicio = Column(String(3))
    fim = Column(String(3))


class Importatxt(Base):
    __tablename__ = 'importatxt'

    campoa = Column(String(50), primary_key=True)
    campob = Column(String(50))
    campoc = Column(String(50))
    campod = Column(String(50))
    campoe = Column(String(50))
    campof = Column(String(50))
    campog = Column(String(50))
    campoh = Column(String(50))
    campoi = Column(String(50))
    campoj = Column(String(50))
    campok = Column(String(50))
    campol = Column(String(50))
    campom = Column(String(50))
    campon = Column(String(50))
    campoo = Column(String(50))
    campov = Column(String(50))
    campop = Column(String(50))
    campoq = Column(String(50))
    campor = Column(String(50))
    campos = Column(String(50))
    campotg = Column(String(50))
    campou = Column(String(50))


t_informativo = Table(
    'informativo', metadata,
    Column('enderecocliente', Integer, nullable=False),
    Column('enderecofornecedor', Integer, nullable=False),
    Column('historicocliente', Integer),
    Column('historicofornecedor', Integer, nullable=False),
    Column('pagamento', Integer, nullable=False),
    Column('planocontas', Integer, nullable=False),
    Column('produtos', Integer, nullable=False),
    Column('recebimento', Integer, nullable=False),
    Column('nfiscal', Integer, nullable=False),
    Column('nfiscal1', Integer, nullable=False),
    Column('nfiscal2', Integer, nullable=False),
    Column('nfiscal3', Integer, nullable=False),
    Column('contasareceber', Integer, nullable=False),
    Column('codcliente', Integer),
    Column('codmovimento', Integer),
    Column('coddetalhe', Integer),
    Column('codvenda', Integer),
    Column('numnf', Integer),
    Column('codfornecedor', Integer),
    Column('codrecebimento', Integer),
    Column('codtransp', Integer),
    Column('cod_uso', Integer),
    Column('cod_codigo', Integer),
    Column('cod_comissao', Integer),
    Column('cod_reprfor', Integer),
    Column('cod_reprcli', Integer),
    Column('cod_veiculo', Integer),
    Column('codbanco', Integer),
    Column('cod_cheq_bol', Integer),
    Column('codendereco', Integer),
    Column('id_nf', Integer)
)


class Inventario(Base):
    __tablename__ = 'inventario'

    codiventario = Column(String(40), primary_key=True, nullable=False)
    dataiventario = Column(Date)
    codproduto = Column(Integer, primary_key=True, nullable=False)
    codpro = Column(String(15))
    situacao = Column(Text(1))
    dataexecutado = Column(Date)
    estoque_atual = Column(Float, server_default=text("0"))
    qtde_inventario = Column(Float, server_default=text("0"))
    un = Column(Text(3))
    codccusto = Column(Integer)
    lote = Column(String(60))
    datafabricacao = Column(Date)
    datavencimento = Column(Date)


class Irmao(Base):
    __tablename__ = 'irmaos'

    id_irmao = Column(Integer, primary_key=True)
    ra = Column(String(10))
    nome = Column(String(100))
    ano = Column(Integer)
    curso = Column(String(50))
    serie = Column(String(4))


class ItensTransp(Base):
    __tablename__ = 'itens_transp'

    id_nf = Column(Integer, primary_key=True)
    numnf = Column(Integer, nullable=False)
    codproduto = Column(Integer, nullable=False)
    codpro = Column(String(15))
    descricao = Column(String(300))
    quantidade = Column(Float)
    un = Column(Text(2))
    icms = Column(Float)
    preco = Column(Float)
    total = Column(Float)


class Listapreco(Base):
    __tablename__ = 'listapreco'

    codlistapreco = Column(Integer, primary_key=True)
    descr = Column(String(300))
    aplic = Column(String(200))
    grupo = Column(String(30))
    subgrupo = Column(String(30))
    fornecedor = Column(String(30))
    unidade = Column(String(2))
    precolista = Column(Float)
    precovenda = Column(Float)
    margem = Column(Float)
    dataatualiza = Column(Date)
    codbarra = Column(String(20))
    codigo = Column(String(15), index=True)
    pro_cod = Column(String(15))
    usaproduto = Column(Text(3))
    codproduto = Column(Integer)
    codfornecedor = Column(Integer)
    tipooperacao = Column(Text(1))


class ListaprecoVenda(Base):
    __tablename__ = 'listapreco_venda'

    codlista = Column(Integer, primary_key=True)
    codcliente = Column(ForeignKey('clientes.codcliente'))
    nomelista = Column(String(60))
    validade = Column(Date)
    datainicial = Column(Date)
    datafinal = Column(Date)

    cliente = relationship('Cliente')


class ListaprecoVendadet(Base):
    __tablename__ = 'listapreco_vendadet'

    codlistadet = Column(Integer, primary_key=True)
    codlista = Column(ForeignKey('listapreco_venda.codlista'))
    codproduto = Column(ForeignKey('produtos.codproduto'))
    produto = Column(String(300))
    altpreco = Column(Text(1))
    desconto = Column(Text(1))
    descontomax = Column(Float)
    descontomin = Column(Float)
    margem = Column(Text(1))
    margemmax = Column(Float)
    margemmin = Column(Float)
    estoque = Column(Float)
    precocompra = Column(Float)
    precovenda = Column(Float)
    cod_cliente = Column(String(30))

    listapreco_venda = relationship('ListaprecoVenda')
    produto1 = relationship('Produto')


class LogAcesso(Base):
    __tablename__ = 'log_acesso'

    login = Column(String(20), nullable=False)
    micro = Column(String(30))
    modulo = Column(String(30))
    id_log = Column(Integer, primary_key=True)
    usuario = Column(String(60))


class LogMovimento(Base):
    __tablename__ = 'log_movimento'

    cod_log = Column(Integer, primary_key=True)
    data = Column(Date)
    codusuario = Column(SmallInteger)
    movimento = Column(String(30))
    item = Column(String(30))
    numitem = Column(Integer)


class Log(Base):
    __tablename__ = 'logs'

    id_log = Column(Integer, primary_key=True)
    tabela = Column(String(80))
    data = Column(Date)
    usuario = Column(String(80))
    micro = Column(String(50))
    hora = Column(Time)
    campo1 = Column(String(50))
    campo2 = Column(String(50))
    campo3 = Column(String(50))
    campo4 = Column(String(50))
    data_set = Column(Text)


class Lote(Base):
    __tablename__ = 'lotes'

    codlote = Column(Integer, primary_key=True)
    lote = Column(String(200), nullable=False)
    codproduto = Column(Integer, nullable=False)
    datafabricacao = Column(Date)
    datavencimento = Column(Date)
    estoque = Column(Float)
    preco = Column(Float)
    notafiscal = Column(String(15))
    serieini = Column(Integer)
    seriefim = Column(Integer)


t_mala_direta = Table(
    'mala_direta', metadata,
    Column('mala', LargeBinary)
)


class Mapeamentoestoque(Base):
    __tablename__ = 'mapeamentoestoque'

    idmapeamento = Column(Integer, primary_key=True)
    crtr = Column(String(10))
    n_bb = Column(Integer)
    lote = Column(String(15))
    i_s = Column(Text(1))
    dt_validade = Column(Date)
    rua = Column(Integer)
    travessa = Column(Text(1))
    andar = Column(Text(10))
    topo = Column(Text(1))


class Marca(Base):
    __tablename__ = 'marca'

    descmarcas = Column(String(30), primary_key=True)


class MateriaPrima(Base):
    __tablename__ = 'materia_prima'

    codmat = Column(Integer, primary_key=True)
    codproduto = Column(ForeignKey('produtos.codproduto'))
    codprodmp = Column(ForeignKey('produtos.codproduto'))
    qtdeusada = Column(Float)
    tipouso = Column(String(30))
    usapreco = Column(String(20))

    produto = relationship('Produto', primaryjoin='MateriaPrima.codprodmp == Produto.codproduto')
    produto1 = relationship('Produto', primaryjoin='MateriaPrima.codproduto == Produto.codproduto')


class MovDetalheServ(Base):
    __tablename__ = 'mov_detalhe_serv'

    coddetalhe_serv = Column(Integer, primary_key=True)
    codmovimento = Column(ForeignKey('movimentodetalhe.coddetalhe'), nullable=False)
    codservico = Column(Integer)
    descricao = Column(String(400))
    quantidade = Column(Float)
    preco = Column(Float)
    icms = Column(Float)
    un = Column(Text(2))
    valtotal = Column(Float)
    cod_comissao = Column(Integer)

    movimentodetalhe = relationship('Movimentodetalhe')


class MovRateio(Base):
    __tablename__ = 'mov_rateio'

    data = Column(Date)
    codusuario = Column(SmallInteger)
    codccusto = Column(Integer)
    codservico = Column(SmallInteger)
    status = Column(SmallInteger)
    conta = Column(String(15))
    valor = Column(Float)
    percentual = Column(Float)
    contadebito = Column(String(15))
    qtde = Column(Float)
    codmovimento = Column(Integer)
    tipo = Column(String(15))
    codrateio = Column(Integer, primary_key=True)


class Movimento(Base):
    __tablename__ = 'movimento'

    codmovimento = Column(Integer, primary_key=True, index=True)
    datamovimento = Column(Date, nullable=False)
    codcliente = Column(ForeignKey('clientes.codcliente'), ForeignKey('clientes.codcliente'), nullable=False)
    codnatureza = Column(ForeignKey('naturezaoperacao.codnatureza'), nullable=False)
    status = Column(SmallInteger, nullable=False, index=True)
    codusuario = Column(ForeignKey('usuario.codusuario'), nullable=False)
    codvendedor = Column(SmallInteger)
    codalmoxarifado = Column(Integer)
    codfornecedor = Column(ForeignKey('fornecedor.codfornecedor'))
    data_sistema = Column(DateTime)
    cod_veiculo = Column(Integer)
    controle = Column(String(30))
    obs = Column(String(100))
    totalmovimento = Column(Float)
    codmovrateio = Column(Integer)
    valorrateio = Column(Float)
    rateio = Column(Float)
    conferido = Column(Text(1))
    nfcobranca = Column(Integer)
    ordematend = Column(Integer)
    nfrevenda = Column(Integer)
    codorigem = Column(Integer)
    km = Column(String(30))
    nfe = Column(String(10))
    prazo_ent = Column(Integer)
    val_prop = Column(Date)
    forma_pag = Column(String(40))
    valor_frete = Column(Float)
    data_entrega = Column(Date)
    prazo_pagamento = Column(String(30))
    user_aprova = Column(String(20))
    codtransp = Column(Integer)
    tpfrete = Column(Text(1))
    codpedido = Column(Integer)
    codcotacao = Column(Integer)
    usuariologado = Column(String(30))
    tipo_pedido = Column(Text(1))
    entrega = Column(String(60))
    qtd = Column(Integer)
    desconto = Column(Float)
    hist_mov = Column(String(150))
    data_fechou = Column(DateTime)

    cliente = relationship('Cliente', primaryjoin='Movimento.codcliente == Cliente.codcliente')
    cliente1 = relationship('Cliente', primaryjoin='Movimento.codcliente == Cliente.codcliente')
    fornecedor = relationship('Fornecedor')
    naturezaoperacao = relationship('Naturezaoperacao')
    usuario = relationship('Usuario')


class Movimentocont(Base):
    __tablename__ = 'movimentocont'

    codcont = Column(Integer, primary_key=True)
    codorigem = Column(Integer, nullable=False, index=True)
    tipoorigem = Column(String(10), index=True)
    data = Column(Date)
    codusuario = Column(SmallInteger)
    codccusto = Column(Integer)
    codservico = Column(SmallInteger)
    status = Column(SmallInteger)
    conta = Column(String(20), index=True)
    valorcredito = Column(Float)
    valordebito = Column(Float)
    valororcado = Column(Float)
    qtdecredito = Column(Float)
    qtdedebito = Column(Float)
    qtdeorcado = Column(Float)
    codconciliacao = Column(String(50))
    forma = Column(Text(1))


class Movimentodetalhe(Base):
    __tablename__ = 'movimentodetalhe'

    coddetalhe = Column(Integer, primary_key=True, index=True)
    codmovimento = Column(ForeignKey('movimento.codmovimento'), nullable=False)
    codalmoxarifado = Column(SmallInteger)
    controle = Column(SmallInteger)
    codproduto = Column(ForeignKey('produtos.codproduto'))
    quantidade = Column(Float)
    preco = Column(Float)
    icms = Column(Float)
    un = Column(Text(2))
    qtde_alt = Column(Float)
    baixa = Column(Text(1))
    valtotal = Column(Float)
    cod_comissao = Column(Integer)
    lote = Column(String(60))
    dtafab = Column(Date)
    dtavcto = Column(Date)
    precocusto = Column(Float)
    vlrestoque = Column(Float)
    qtdeestoque = Column(Float)
    notafiscal = Column(String(15))
    descproduto = Column(String(300))
    precoultimacompra = Column(Float)
    cst = Column(String(5))
    valor_icms = Column(Float)
    vlr_base = Column(Float)
    periodoini = Column(DateTime)
    periodofim = Column(DateTime)
    codigo = Column(Integer)
    codigo1 = Column(Integer)
    codautorizacao = Column(Integer)
    status = Column(Text(1))
    pagoucomissao = Column(Text(1))
    codmovrateio = Column(Integer)
    valorrateio = Column(Float)
    pago = Column(Text(3))
    rateio = Column(Float)
    porcentagendesc = Column(Float)
    icms_subst = Column(Float)
    icms_substd = Column(Float)
    vlr_baseicms = Column(Float)
    pipi = Column(Float)
    vipi = Column(Float)
    cfop = Column(Text(4))
    frete = Column(Float)
    bcfrete = Column(Float)
    stfrete = Column(Text(4))
    bcstfrete = Column(Float)
    icmsfrete = Column(Float)
    csosn = Column(String(3))
    valor_desconto = Column(Float)
    recebido = Column(Float, server_default=text("0"))
    valor_seguro = Column(Float)
    valor_outros = Column(Float)
    obs = Column(String(300))
    cod_funcionario = Column(Integer)
    codsolicitacao = Column(Integer)
    valor_pis = Column(Float)
    valor_cofins = Column(Float)
    ii = Column(Float)
    bcii = Column(Float)
    impresso = Column(Text(3))
    cstipi = Column(String(2))
    cstpis = Column(String(2))
    cstcofins = Column(String(2))
    ppis = Column(Float)
    pcofins = Column(Float)
    pedido = Column(String(20))
    nitemped = Column(Integer)
    acrescimo = Column(Float)
    cortesia = Column(Text(1))
    atendente = Column(Integer)
    colaborador = Column(Integer)
    suite = Column(String(40))
    formarecebimento = Column(Text(1))
    pagou = Column(Text(1))
    frete_bc = Column(String(5))
    desconto_bc = Column(String(5))
    vlrbc_ipi = Column(Float)
    vlrbc_pis = Column(Float)
    vlrbc_cofins = Column(Float)
    vlrtot_trib = Column(Float)
    origem = Column(Text(2))
    ncm = Column(String(8))
    aliq_cupom = Column(Text(4))
    vbcufdest = Column(Float)
    pfcpufdest = Column(Float)
    picmsufdest = Column(Float)
    picmsinter = Column(Float)
    picmsinterpart = Column(Float)
    vfcpufdest = Column(Float)
    vicmsufdest = Column(Float)
    vicmsufremet = Column(Float)
    cst_ipi_cenq = Column(Text(3))
    cest = Column(String(7))
    un_conv = Column(Float)

    movimento = relationship('Movimento')
    produto = relationship('Produto')


class Movimentonf(Base):
    __tablename__ = 'movimentonf'

    coddetalhe = Column(Integer, primary_key=True)
    codmovimento = Column(ForeignKey('notafiscal.numnf'), nullable=False)
    codalmoxarifado = Column(SmallInteger)
    controle = Column(SmallInteger)
    codproduto = Column(Integer)
    codpro = Column(String(15))
    produto = Column(String(300), nullable=False)
    quantidade = Column(Float)
    preco = Column(Float)
    icms = Column(Float)
    un = Column(Text(2))
    qtde_alt = Column(Float)
    baixa = Column(Text(1))
    valtotal = Column(Float)
    cod_comissao = Column(Integer)
    valor_total = Column(Float)
    total_pedido = Column(Float)
    ipi = Column(Float)
    lote = Column(String(60))
    qtdeexp = Column(Float)
    precoexp = Column(Float)

    notafiscal = relationship('Notafiscal')


class Naturezanf(Base):
    __tablename__ = 'naturezanf'

    natureza = Column(String(50), nullable=False)
    outros = Column(String(50))
    cfop = Column(String(30), primary_key=True)


class Naturezaoperacao(Base):
    __tablename__ = 'naturezaoperacao'

    codnatureza = Column(SmallInteger, primary_key=True)
    descnatureza = Column(String(30), nullable=False)
    geratitulo = Column(SmallInteger, nullable=False)
    tipotitulo = Column(SmallInteger, nullable=False)
    tipomovimento = Column(SmallInteger)
    baixamovimento = Column(SmallInteger)
    cfop_estado = Column(String(30))
    cfop_fora_estado = Column(String(30))
    cfop_internacional = Column(String(30))


class Ncm(Base):
    __tablename__ = 'ncm'

    ncm = Column(String(8), primary_key=True)
    aliqnac = Column(Float)
    aliqimp = Column(Float)
    cest = Column(String(7))
    estadual = Column(Float)
    municipal = Column(Float)


class NfInutilizado(Base):
    __tablename__ = 'nf_inutilizado'

    num = Column(Integer, primary_key=True)
    data_inutilizado = Column(Date, nullable=False)
    ccusto = Column(Integer)
    serie = Column(String(10), nullable=False)
    usuario = Column(Integer)


class Notafiscal(Base):
    __tablename__ = 'notafiscal'

    notaserie = Column(String(10), nullable=False)
    numnf = Column(Integer, primary_key=True)
    natureza = Column(SmallInteger, nullable=False)
    quantidade = Column(Float)
    marca = Column(String(10))
    pesobruto = Column(Numeric(9, 2))
    pesoliquido = Column(Numeric(9, 2))
    especie = Column(String(20))
    dtaemissao = Column(Date)
    dtasaida = Column(Date)
    uf = Column(Text(2))
    codvenda = Column(Integer)
    codtransp = Column(Integer)
    numero = Column(String(20))
    notafiscal = Column(Integer)
    horasaida = Column(Time)
    data_sistema = Column(DateTime)
    base_icms = Column(Float)
    valor_icms = Column(Float)
    base_icms_subst = Column(Float)
    valor_icms_subst = Column(Float)
    valor_produto = Column(Float)
    valor_frete = Column(Float)
    valor_seguro = Column(Float)
    outras_desp = Column(Float)
    valor_ipi = Column(Float)
    valor_total_nota = Column(Float)
    corponf1 = Column(String(200))
    corponf2 = Column(String(200))
    corponf3 = Column(String(200))
    corponf4 = Column(String(200))
    corponf5 = Column(String(75))
    corponf6 = Column(String(75))
    cfop = Column(String(30))
    codcliente = Column(Integer)
    fatura = Column(String(300))
    icms = Column(Float)
    reduzicms = Column(Float)
    nometransp = Column(String(50))
    placatransp = Column(String(8))
    cnpj_cpf = Column(String(20))
    end_transp = Column(String(80))
    cidade_transp = Column(String(50))
    uf_veiculo_transp = Column(Text(2))
    uf_transp = Column(Text(2))
    frete = Column(Text(1))
    inscricaoestadual = Column(String(20))
    status = Column(Text(1))
    vlrtotalexp = Column(Float)
    impressa = Column(Text(1))
    serie = Column(String(20))
    id_guia = Column(Integer)
    selecionou = Column(Text(1))
    protocoloenv = Column(String(20))
    numrecibo = Column(String(20))
    protocolocanc = Column(String(20))
    pesoremessa = Column(Numeric(9, 2))
    notamae = Column(Integer)
    valor_pis = Column(Float)
    valor_cofins = Column(Float)
    valor_desconto = Column(Float)
    ccusto = Column(Integer)
    idcomplementar = Column(String(44))
    xmlnfe = Column(LargeBinary)
    ii = Column(Float)
    bcii = Column(Float)
    nomexml = Column(String(60))
    indpag = Column(Integer)
    base_ipi = Column(Float)
    base_pis = Column(Float)
    base_cofins = Column(Float)
    vlrtot_trib = Column(Float)
    nfe_finnfe = Column(String(20))
    nfe_modelo = Column(String(10))
    nfe_tipo = Column(String(15))
    nfe_versao = Column(String(10))
    nfe_destoperacao = Column(String(20))
    nfe_formatodanfe = Column(String(20))
    nfe_tipoemissao = Column(String(15))
    nfe_indfinal = Column(String(20))
    nfe_indpres = Column(String(20))
    ind_iedest = Column(String(30))


class NotafiscalImporta(Base):
    __tablename__ = 'notafiscal_importa'

    notafiscal = Column(Integer, primary_key=True, nullable=False)
    naturezaoperacao = Column(String(50))
    modelo = Column(Text(5))
    serie = Column(Text(5), primary_key=True, nullable=False)
    emissao = Column(Date)
    cnpj_emitente = Column(String(25), primary_key=True, nullable=False)
    cnpj_destinatario = Column(String(25))
    nome_emitente = Column(String(150))
    codcliente_ats = Column(Integer)
    razaosocial_ats = Column(String(60))
    status = Column(SmallInteger, server_default=text("0"))


class NotafiscalProdImporta(Base):
    __tablename__ = 'notafiscal_prod_importa'

    notafiscal = Column(Integer, primary_key=True, nullable=False)
    serie = Column(Text(5), primary_key=True, nullable=False)
    cnpj_emitente = Column(String(25), primary_key=True, nullable=False)
    num_item = Column(Integer, primary_key=True, nullable=False)
    codproduto_ats = Column(Integer)
    codpro_ats = Column(String(15))
    produto = Column(String(150))
    produto_ats = Column(String(150))
    ncm = Column(Text(8))
    cfop = Column(Text(4))
    un = Column(Text(5))
    qtde = Column(Float)
    vlr_unit = Column(Float)
    vlr_total = Column(Float)
    icms = Column(String(50))
    pis = Column(String(50))
    cofins = Column(String(50))
    ipi = Column(String(50))
    cod_barra = Column(String(30))
    codproduto = Column(String(30))


class NotafiscalServ(Base):
    __tablename__ = 'notafiscal_serv'

    numnf_serv = Column(Integer, primary_key=True)
    numnf = Column(Integer, nullable=False)
    servico1 = Column(String(250))
    servico2 = Column(String(250))
    servico3 = Column(String(250))
    vlrserv1 = Column(Float)
    vlrserv2 = Column(Float)
    vlrserv3 = Column(Float)
    base_iss_ir = Column(Float)
    iss_nota = Column(Float)
    iss_percent = Column(Float)
    ir_font = Column(Float)
    ir_percent = Column(Float)
    total_serv = Column(Float)


class NovosCampo(Base):
    __tablename__ = 'novos_campos'

    codcampos = Column(Integer, primary_key=True)
    campo = Column(String(60))
    tabela = Column(String(60))
    datainclusao = Column(Date)
    tipo = Column(String(60))
    obs = Column(String(160))
    tipocampo = Column(String(60))


class Ocorrencia(Base):
    __tablename__ = 'ocorrencia'

    codocorrencia = Column(Integer, primary_key=True)
    data = Column(Date)
    tipo = Column(String(30))
    ra = Column(String(10))
    descricao = Column(Text)
    anoletivo = Column(Integer)
    assuntos = Column(String(30))
    assunto = Column(String(30))


class OfOf(Base):
    __tablename__ = 'of_of'

    ofid = Column(Integer, primary_key=True, nullable=False)
    ofid_ind = Column(SmallInteger, primary_key=True, nullable=False)
    ofdata = Column(Date)
    ofstatus = Column(Text(1))
    ofqtdesolic = Column(Float)
    ofqtdeproduz = Column(Float)
    ofqtdeperda = Column(Float)
    ofmotivo = Column(String(100))
    codproduto = Column(Integer)


class Orcamento(Base):
    __tablename__ = 'orcamento'

    codorcamento = Column(Integer, primary_key=True)
    nomeorcamento = Column(String(50), nullable=False)
    dataorcamento = Column(Date)
    validoate = Column(Date)
    dataentrega = Column(Date)
    codcliente = Column(ForeignKey('clientes.codcliente'))
    produtoouservico = Column(String(300))
    codproduto = Column(ForeignKey('produtos.codproduto'))
    quantidade = Column(Float, server_default=text("0"))
    valor = Column(Float, server_default=text("0"))
    volume = Column(Float, server_default=text("0"))
    total = Column(Float)
    status = Column(String(20))

    cliente = relationship('Cliente')
    produto = relationship('Produto')


class OrcamentoTipo(Base):
    __tablename__ = 'orcamento_tipos'

    nomeorcamento = Column(String(50), primary_key=True)
    descricaoorcamento = Column(String(300))
    nvaos = Column(Float)
    nmodulos = Column(Float)
    altura = Column(Float)
    largura = Column(Float)
    comprimento = Column(Float)
    area = Column(Float)
    tipoorc = Column(Text(1))


class O(Base):
    __tablename__ = 'os'

    codos = Column(Integer, primary_key=True)
    codcliente = Column(Integer, nullable=False)
    codmovimento = Column(Integer)
    datamovimento = Column(Date)
    data_sistema = Column(DateTime)
    problemas = Column(String(300))
    status = Column(Text(1))
    data_ini = Column(Date)
    data_fim = Column(Date)
    km = Column(Integer)
    codusuario = Column(Integer)
    dataos = Column(Date)
    veiculo = Column(String(200))
    cfop = Column(String(30))


class OsDet(Base):
    __tablename__ = 'os_det'

    id_os_det = Column(Integer, primary_key=True)
    id_os = Column(Integer, nullable=False)
    descricao_serv = Column(String(1024))
    responsavel = Column(String(150))
    status = Column(Text(1))
    codproduto = Column(ForeignKey('produtos.codproduto'), nullable=False)
    tipo = Column(Text(1))
    qtde = Column(Float, server_default=text("0"))
    preco = Column(Float, server_default=text("0"))
    desconto = Column(Float, server_default=text("0"))
    valortotal = Column(Float)
    id_osdet_serv = Column(Integer)
    codusuario = Column(Integer)

    produto = relationship('Produto')


class Pagamento(Base):
    __tablename__ = 'pagamento'

    codpagamento = Column(Integer, primary_key=True)
    titulo = Column(String(18), nullable=False)
    emissao = Column(Date)
    codfornecedor = Column(ForeignKey('fornecedor.codfornecedor'), nullable=False)
    datavencimento = Column(Date)
    datapagamento = Column(Date)
    caixa = Column(SmallInteger)
    contadebito = Column(Integer)
    contacredito = Column(Integer)
    status = Column(Text(2), nullable=False)
    formapagamento = Column(Text(1), nullable=False)
    databaixa = Column(Date)
    historico = Column(String(150))
    codcompra = Column(Integer)
    codalmoxarifado = Column(SmallInteger)
    codcomprador = Column(SmallInteger)
    codusuario = Column(SmallInteger)
    n_documento = Column(String(20))
    datasistema = Column(DateTime)
    valorrecebido = Column(Float)
    juros = Column(Float)
    desconto = Column(Float)
    perda = Column(Float)
    troca = Column(Float)
    funrural = Column(Float)
    valor_prim_via = Column(Float)
    valor_resto = Column(Float)
    valortitulo = Column(Float)
    outro_credito = Column(Float)
    outro_debito = Column(Float)
    parcelas = Column(Integer)
    via = Column(Text(4))
    codorigem = Column(Integer)
    dup_rec_nf = Column(String(15))
    dp = Column(SmallInteger)
    dataconsolida = Column(Date)
    situacaocheque = Column(String(10))
    situacao = Column(Integer)
    codorigem1 = Column(Integer)
    selecionou = Column(Text(1))
    userid = Column(Text(3))
    codconciliacao = Column(String(50))

    fornecedor = relationship('Fornecedor')


class Pai(Base):
    __tablename__ = 'pais'

    codpais = Column(Text(4), primary_key=True, nullable=False)
    pais = Column(String(60), primary_key=True, nullable=False)


class Parametro(Base):
    __tablename__ = 'parametro'

    descricao = Column(String(100))
    parametro = Column(String(40), primary_key=True)
    configurado = Column(Text(1))
    dados = Column(String(40))
    d1 = Column(String(30))
    d2 = Column(String(30))
    d3 = Column(String(30))
    d4 = Column(String(30))
    d5 = Column(String(30))
    d6 = Column(String(30))
    d7 = Column(String(30))
    d8 = Column(String(30))
    d9 = Column(String(30))
    instrucoes = Column(String(200))
    valor = Column(Float)


class Permissao(Base):
    __tablename__ = 'permissao'

    chave = Column(String(40), primary_key=True)
    tabela = Column(String(20), nullable=False)
    login = Column(String(20), nullable=False)
    incluir = Column(Text(1))
    excluir = Column(Text(1))
    alterar = Column(Text(1))
    consultar = Column(Text(1))


class Plano(Base):
    __tablename__ = 'plano'

    codigo = Column(Integer, primary_key=True)
    conta = Column(String(15), nullable=False)
    contapai = Column(Integer)
    nome = Column(String(200), nullable=False)
    consolida = Column(Text(1))
    descricao = Column(String(50))
    rateio = Column(Text(1))
    codreduzido = Column(String(15))
    reduzreceita = Column(Text(1))
    codempresa = Column(Integer)
    tipolanc = Column(String(10))

    #parent = relationship('Plano', remote_side=[codigo])


class PlanoRateio(Base):
    __tablename__ = 'plano_rateio'

    cod_plano_rateio = Column(Integer, primary_key=True)
    conta_rateio = Column(ForeignKey('plano.conta'))
    ccusto = Column(ForeignKey('plano.conta'))
    percentual = Column(Float)
    conta = Column(String(15))

    plano = relationship('Plano', primaryjoin='PlanoRateio.ccusto == Plano.conta')
    plano1 = relationship('Plano', primaryjoin='PlanoRateio.conta_rateio == Plano.conta')


t_plj = Table(
    'plj', metadata,
    Column('codigo', String(10)),
    Column('sep', String(10)),
    Column('codfor', String(20)),
    Column('descricao', String(100)),
    Column('valor', String(15))
)


class ProdChg(Base):
    __tablename__ = 'prod_chg'

    descr = Column(String(40))
    aplic = Column(String(200))
    linh1 = Column(String(30))
    tipovel = Column(String(30))
    linh2 = Column(String(30))
    mont = Column(String(30))
    fabric = Column(String(30))
    unidade = Column(String(2))
    prnorm = Column(Float)
    prprom = Column(Float)
    datagrav = Column(Date)
    cod_barra = Column(String(20))
    codigo = Column(String(15), primary_key=True)
    pro_cod = Column(String(6))


class ProdutoFornecedor(Base):
    __tablename__ = 'produto_fornecedor'

    codproduto = Column(Integer, primary_key=True, nullable=False)
    codfornecedor = Column(Integer, primary_key=True, nullable=False)
    codprodfornec = Column(String(30))


class Produto(Base):
    __tablename__ = 'produtos'

    codproduto = Column(Integer, primary_key=True, index=True)
    familia = Column(ForeignKey('familiaprodutos.descfamilia'))
    categoria = Column(ForeignKey('categoriaproduto.desccategoria'))
    marca = Column(ForeignKey('marca.descmarcas'))
    unidademedida = Column(Text(2))
    dataultimacompra = Column(Date)
    estoquemaximo = Column(Float)
    estoqueatual = Column(Float)
    estoquereposicao = Column(Float)
    estoqueminimo = Column(Float)
    valorunitarioatual = Column(Float)
    valorunitarioanterior = Column(Float)
    icms = Column(Float)
    codalmoxarifado = Column(Integer)
    ipi = Column(Float)
    classific_fiscal = Column(String(30))
    cst = Column(String(30))
    base_icms = Column(Float)
    produto = Column(String(300), nullable=False)
    precomedio = Column(Numeric(9, 2), server_default=text("0"))
    cod_comissao = Column(Integer)
    margem_lucro = Column(Float)
    cod_barra = Column(String(20), unique=True)
    valor_prazo = Column(Float)
    tipo = Column(String(10))
    conta_despesa = Column(String(15))
    conta_receita = Column(String(15))
    conta_estoque = Column(String(15))
    rateio = Column(Text(1))
    codpro = Column(String(15), unique=True)
    qtde_pct = Column(Float)
    peso_qtde = Column(Float)
    datacadastro = Column(DateTime)
    margem = Column(Float)
    pro_cod = Column(String(15))
    datagrav = Column(Date)
    codforn = Column(String(60))
    fotoproduto = Column(String(80))
    lotes = Column(Text(1))
    usa = Column(String(3))
    localizacao = Column(String(50))
    tipoprecovenda = Column(Text(1))
    valorminimo = Column(Float)
    valorcomissao = Column(Float)
    geradesconto = Column(Text(1))
    imprimir = Column(Text(1))
    origem = Column(Integer)
    ncm = Column(String(8))
    impressora_1 = Column(String(10))
    impressora_2 = Column(String(10))
    impressora_3 = Column(String(10))
    qtd = Column(Integer)
    tam_lote = Column(Integer)
    obs = Column(String(300))
    peso_liq = Column(Float)
    cest = Column(String(7))
    embalagem = Column(String(40))
    cprodanp = Column(String(20))
    pmixgn = Column(Float)
    valiqprod = Column(Float)
    precoatacado = Column(Float)
    qtdeatacado = Column(Integer)

    categoriaproduto = relationship('Categoriaproduto')
    familiaproduto = relationship('Familiaproduto')
    marca1 = relationship('Marca')


class Recebimento(Base):
    __tablename__ = 'recebimento'

    codrecebimento = Column(Integer, primary_key=True)
    titulo = Column(String(18), nullable=False, index=True)
    emissao = Column(Date, index=True)
    codcliente = Column(ForeignKey('clientes.codcliente'), nullable=False, index=True)
    datavencimento = Column(Date)
    datarecebimento = Column(Date, index=True)
    caixa = Column(SmallInteger)
    contadebito = Column(Integer)
    contacredito = Column(Integer)
    status = Column(Text(2), nullable=False, index=True)
    via = Column(Text(4), nullable=False)
    formarecebimento = Column(Text(1), nullable=False)
    databaixa = Column(Date)
    historico = Column(String(150))
    codvenda = Column(Integer, index=True)
    codalmoxarifado = Column(SmallInteger, index=True)
    codvendedor = Column(SmallInteger, index=True)
    codusuario = Column(SmallInteger)
    n_documento = Column(String(20))
    datasistema = Column(DateTime)
    valorrecebido = Column(Float, server_default=text("0.00"))
    juros = Column(Float, server_default=text("0.00"))
    desconto = Column(Float, server_default=text("0.00"))
    perda = Column(Float, server_default=text("0.00"))
    troca = Column(Float, server_default=text("0.00"))
    funrural = Column(Float, server_default=text("0.00"))
    valor_prim_via = Column(Float)
    valor_resto = Column(Float)
    valortitulo = Column(Float, index=True)
    outro_credito = Column(Float)
    outro_debito = Column(Float)
    parcelas = Column(Integer)
    dup_rec_nf = Column(String(15))
    nf = Column(Integer, index=True)
    dp = Column(Integer, index=True)
    bl = Column(Integer, index=True)
    codorigem = Column(Integer)
    codigo_de_barras = Column(String(54))
    image_cod_barras = Column(LargeBinary)
    dv = Column(Text(2))
    nomearquivoretorno = Column(String(80))
    dataconsolida = Column(Date)
    banco = Column(String(60))
    agencia = Column(String(10))
    conta = Column(String(10))
    situacao = Column(Integer)
    selecionou = Column(Text(1))
    descontado = Column(Text(1))
    situacaocheque = Column(String(15))
    gerarqrem = Column(Integer)
    datagerarqrem = Column(Date)
    valst = Column(Float)
    valor_resto_sst = Column(Float)
    userid = Column(Integer)
    codigoboleto = Column(String(20))
    codigobanco = Column(Integer)
    codconciliacao = Column(String(50))

    cliente = relationship('Cliente')


class RecebimentoHist(Base):
    __tablename__ = 'recebimento_hist'

    codrecebimento = Column(Integer, primary_key=True, nullable=False)
    id_hist = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String(20))
    caixa = Column(Integer)
    tipo = Column(String(30), nullable=False)
    data_hist = Column(Date)
    historico = Column(String(200))
    usuario = Column(Integer)


class Remessa(Base):
    __tablename__ = 'remessa'

    titulo = Column(String(18), primary_key=True)
    numerobordero = Column(SmallInteger, nullable=False)
    codagencia = Column(SmallInteger, nullable=False)
    dataremessa = Column(Date)
    tipooperacao = Column(SmallInteger, nullable=False)


class Remessacartorio(Base):
    __tablename__ = 'remessacartorio'

    codcartorio = Column(Integer, primary_key=True)
    titulo = Column(String(18), nullable=False)
    dataremessa = Column(Date)
    dataprotesto = Column(Date)
    datebaixa = Column(Date)


class ReprCliente(Base):
    __tablename__ = 'repr_cliente'

    cod_cliente = Column(Integer)
    cod_reprcli = Column(Integer, primary_key=True)
    fone = Column(String(13))
    fone1 = Column(String(13))
    fone2 = Column(String(13))
    endereco = Column(String(60))
    numero = Column(String(10))
    complemento = Column(String(30))
    bairro = Column(String(50))
    cidade = Column(String(60))
    uf = Column(String(2))
    cep = Column(String(10))
    email = Column(String(40))
    nome_reprcli = Column(String(60))
    funcao = Column(String(60))


class ReprFornecedor(Base):
    __tablename__ = 'repr_fornecedor'

    cod_fornecedor = Column(ForeignKey('fornecedor.codfornecedor'), nullable=False, index=True)
    cod_reprfor = Column(Integer, primary_key=True)
    fone = Column(String(13))
    fone1 = Column(String(13))
    fone2 = Column(String(13))
    endereco = Column(String(60))
    numero = Column(String(10))
    complemento = Column(String(30))
    bairro = Column(String(50))
    cidade = Column(String(60))
    uf = Column(String(2))
    cep = Column(String(10))
    email = Column(String(40))
    nome_reprfor = Column(String(60))
    funcao = Column(String(60))

    fornecedor = relationship('Fornecedor')


class Responsavel(Base):
    __tablename__ = 'responsavel'

    cod_responsavel = Column(Integer, primary_key=True)
    responsavel = Column(String(200), nullable=False)
    endereco = Column(String(200))
    bairro = Column(String(50))
    cep = Column(Text(10))
    cidade = Column(String(50))
    uf = Column(Text(2))
    tipo_responsavel = Column(Text(1))
    cpf = Column(Text(14))
    rg = Column(String(20))
    telefone = Column(String(14))
    telefone1 = Column(String(14))
    email = Column(String(50))
    localtrabalho = Column(String(100))
    caixapostal = Column(String(20))
    telefone_comercial = Column(String(14))


class RetornoBanco(Base):
    __tablename__ = 'retorno_banco'

    codretorno = Column(Integer, primary_key=True)
    arquivo = Column(String(100), nullable=False)
    dataarquivo = Column(Date)
    nossonumero = Column(String(50), nullable=False)
    valorrecebido = Column(Float)
    valorjuros = Column(Float)
    valordesconto = Column(Float)
    titulobaixado = Column(String(30))
    situacao = Column(String(30))
    codrecebimento = Column(Integer)


class RomaneioF(Base):
    __tablename__ = 'romaneio_f'

    codromaneio_f = Column(Integer, primary_key=True)
    codromaneio = Column(Integer, nullable=False)
    codcliente = Column(Integer, nullable=False)
    pedido = Column(String(20), nullable=False)
    km = Column(String(20))
    hora = Column(DateTime)
    obs = Column(String(50))
    valor = Column(Float)
    tipo = Column(String(10))
    codrecebimento = Column(Integer)


class RomaneioPai(Base):
    __tablename__ = 'romaneio_pai'

    codromaneio = Column(Integer, primary_key=True)
    data = Column(Date)
    tipo = Column(String(1))


class Semana(Base):
    __tablename__ = 'semana'

    data = Column(Date, primary_key=True)
    ano = Column(SmallInteger)
    semana = Column(SmallInteger)
    mes = Column(SmallInteger)


class Series(Base):
    __tablename__ = 'series'

    serie = Column(String(20), primary_key=True)
    ultimo_numero = Column(Integer, nullable=False)
    codserie = Column(Text(3))
    notafiscal = Column(SmallInteger)
    icms_destacado = Column(Float)
    modelo = Column(String(2))


class Situaco(Base):
    __tablename__ = 'situacoes'

    situac_codigo = Column(String(2), primary_key=True)
    situac_descricao = Column(String(30), nullable=False)


class Spedicm(Base):
    __tablename__ = 'spedicms'

    dt_ini = Column(Date, primary_key=True)
    dt_fim = Column(Date)
    ind_mov_difal = Column(Text(1))
    vl_sld_cred_ant_difal = Column(Float)
    vl_tot_debitos_difal = Column(Float)
    vl_out_deb_difal = Column(Float)
    vl_tot_deb_fcp = Column(Float)
    vl_tot_creditos_difal = Column(Float)
    vl_tot_cred_fcp = Column(Float)
    vl_out_cred_difal = Column(Float)
    vl_sld_dev_ant_difal = Column(Float)
    vl_deducoes_difal = Column(Float)
    vl_sld_cred_transportar = Column(Float)
    deb_esp_difal = Column(Float)


class Spedpiscofin(Base):
    __tablename__ = 'spedpiscofins'

    codsped = Column(Integer, primary_key=True)
    dataini = Column(Date)
    datafim = Column(Date)
    datagerado = Column(Date)
    dataenviado = Column(Date)
    empresa = Column(String(100))
    empresa_cnpj = Column(Text(14))
    empresa_codigo = Column(Integer)
    codfinalidade = Column(SmallInteger)
    indicadormovimento = Column(SmallInteger)
    perfil = Column(SmallInteger)
    atividade = Column(SmallInteger)
    versaoleiaute = Column(SmallInteger)
    tipoescrituracao = Column(SmallInteger)
    indicadornaturezapj = Column(SmallInteger)
    indicadoratividade = Column(SmallInteger)
    codindinctributaria = Column(SmallInteger)
    indaprocred = Column(SmallInteger)
    codindtipocon = Column(SmallInteger)
    codindcritescrit = Column(SmallInteger)
    indcodincidencia = Column(SmallInteger)
    indcta = Column(SmallInteger)
    indescrituracao = Column(SmallInteger)
    basecalculocredito = Column(SmallInteger)
    indaj = Column(SmallInteger)
    codaj = Column(SmallInteger)
    indnatrec = Column(SmallInteger)
    natcreddesc = Column(SmallInteger)
    codcred = Column(SmallInteger)
    indtipcoop = Column(SmallInteger)
    indcredori = Column(SmallInteger)
    indrec = Column(SmallInteger)
    inddesccred = Column(SmallInteger)
    codcont = Column(SmallInteger)
    indnatretfonte = Column(SmallInteger)
    indorigemdiversas = Column(SmallInteger)
    indnatdeducao = Column(String(50))
    indtpoperacaoreceita = Column(SmallInteger)
    contador = Column(String(100))
    contador_cpf = Column(Text(11))
    contador_cnpj = Column(Text(14))
    contador_cep = Column(Text(8))
    contador_end = Column(String(100))
    contador_num = Column(Text(7))
    contador_compl = Column(String(80))
    contador_bairro = Column(String(80))
    contador_fone = Column(Text(14))
    contador_fax = Column(Text(14))
    contador_email = Column(String(100))
    contador_codmun = Column(Text(10))


class Spedpiscofinsdet(Base):
    __tablename__ = 'spedpiscofinsdet'

    codspeddet = Column(Integer, primary_key=True)
    codsped = Column(ForeignKey('spedpiscofins.codsped'), nullable=False)
    dataini = Column(Date)
    datafim = Column(Date)
    datagerado = Column(Date)
    dataenviado = Column(Date)
    empresa = Column(String(100))
    empresa_cnpj = Column(Text(14))
    empresa_codigo = Column(Integer)
    tipoitem = Column(String(30))
    tipooperacao = Column(String(30))
    emitente = Column(String(30))
    tipopagamento = Column(String(30))
    tipofrete = Column(String(30))
    tipofreteredespacho = Column(String(30))
    origemprocesso = Column(String(30))
    doctoarrecada = Column(String(30))
    tipotransporte = Column(String(30))
    doctoimporta = Column(String(30))
    tipotitulo = Column(String(30))
    movimentacaofisica = Column(String(10))
    apuracaoipi = Column(String(10))
    naturezafrete = Column(String(30))
    naturezafrtcontratado = Column(String(30))
    movimentost = Column(String(30))

    spedpiscofin = relationship('Spedpiscofin')


t_tab_cest = Table(
    'tab_cest', metadata,
    Column('cest', String(7), nullable=False),
    Column('ncm', String(8)),
    Column('descricao', String(512))
)


class Tabboletim(Base):
    __tablename__ = 'tabboletim'

    ra = Column(String(10))
    serieletra = Column(String(4))
    idmaterias = Column(Integer)
    idboletim = Column(String(20), primary_key=True)
    notaper1 = Column(String(4))
    notaper2 = Column(String(4))
    notaper3 = Column(String(4))
    notaper4 = Column(String(4))
    notaper5 = Column(String(4))
    notaper6 = Column(String(4))
    faltaper1 = Column(SmallInteger)
    faltaper2 = Column(SmallInteger)
    faltaper3 = Column(SmallInteger)
    faltaper4 = Column(SmallInteger)
    faltaper5 = Column(SmallInteger)
    faltaper6 = Column(SmallInteger)
    auladadaper1 = Column(SmallInteger)
    auladadaper2 = Column(SmallInteger)
    auladadaper3 = Column(SmallInteger)
    auladadaper4 = Column(SmallInteger)
    auladadaper5 = Column(SmallInteger)
    auladadaper6 = Column(SmallInteger)
    anoletivo = Column(Integer)
    notaper7 = Column(String(4))
    notaper8 = Column(String(4))
    notaper9 = Column(String(4))
    notaper10 = Column(String(4))
    notaper11 = Column(String(4))
    notaper12 = Column(String(4))
    faltaper7 = Column(SmallInteger)
    faltaper8 = Column(SmallInteger)
    faltaper9 = Column(SmallInteger)
    faltaper10 = Column(SmallInteger)
    faltaper11 = Column(SmallInteger)
    faltaper12 = Column(SmallInteger)
    auladadaper7 = Column(SmallInteger)
    auladadaper8 = Column(SmallInteger)
    auladadaper9 = Column(SmallInteger)
    auladadaper10 = Column(SmallInteger)
    auladadaper11 = Column(SmallInteger)
    auladadaper12 = Column(SmallInteger)
    dataenvio = Column(Date)


class Tabclassealuno(Base):
    __tablename__ = 'tabclassealuno'

    serieletra = Column(String(4))
    ra = Column(String(10))
    idclassealuno = Column(Integer, primary_key=True)
    serie = Column(String(4))
    numero = Column(SmallInteger)


class Tabensinotipo(Base):
    __tablename__ = 'tabensinotipo'

    tiposerie = Column(String(4), primary_key=True)
    tipoensino = Column(String(20), nullable=False)
    curso = Column(String(50))
    mensalidade = Column(Float)
    anuidade = Column(Float)
    serie = Column(String(50))


class Tabmateria(Base):
    __tablename__ = 'tabmaterias'

    materias = Column(String(50))
    idmaterias = Column(Integer, primary_key=True)
    tipoensino = Column(String(15))


class Tabmovnotasfreq(Base):
    __tablename__ = 'tabmovnotasfreq'

    idnotafrequencia = Column(Integer, primary_key=True)
    serieletra = Column(String(4))
    idmaterias = Column(Integer)
    turno = Column(String(7))
    ra = Column(String(10))
    nota = Column(String(4))
    frequencia = Column(SmallInteger)
    anoletivo = Column(Integer)
    serie = Column(String(4))
    idperiodo = Column(Integer)
    aulasdadas = Column(SmallInteger)


class Tabperiodo(Base):
    __tablename__ = 'tabperiodo'

    idperiodo = Column(Integer, primary_key=True)
    periodo = Column(String(15))
    notafinal = Column(Text(3))


class Tabsery(Base):
    __tablename__ = 'tabseries'

    serieletra = Column(String(4), primary_key=True)
    turno = Column(String(7))
    tipoensino = Column(String(15))
    serie = Column(String(4))
    desc_classe = Column(String(30))


class TbIbge(Base):
    __tablename__ = 'tb_ibge'

    nm_localidade = Column(String(40), nullable=False)
    cd_ibge = Column(String(10), nullable=False)
    nm_municipio = Column(String(40))
    nm_tipo_localidade = Column(String(20))
    sq_ibge = Column(Integer, primary_key=True)
    cd_uf = Column(Text(2))


class Tema(Base):
    __tablename__ = 'temas'

    texto = Column(String(100), primary_key=True)
    imagem = Column(LargeBinary)
    caminho = Column(String(200))
    texto1 = Column(String(100))
    texto2 = Column(String(100))


class TipoFiscal(Base):
    __tablename__ = 'tipo_fiscal'

    codfiscal = Column(Text(1), primary_key=True)
    descricao = Column(String(60), nullable=False)


class TipoVisita(Base):
    __tablename__ = 'tipo_visitas'

    codtipovisita = Column(Integer, primary_key=True)
    visita = Column(String(60))


class Transportadora(Base):
    __tablename__ = 'transportadora'

    codtransp = Column(Integer, primary_key=True)
    nometransp = Column(String(50))
    placatransp = Column(String(8))
    cnpj_cpf = Column(String(20))
    end_transp = Column(String(80))
    cidade_transp = Column(String(50))
    uf_veiculo_transp = Column(Text(2))
    uf_transp = Column(Text(2))
    frete = Column(Text(1))
    inscricaoestadual = Column(String(20))
    corponf1 = Column(String(75))
    corponf2 = Column(String(75))
    corponf3 = Column(String(75))
    corponf4 = Column(String(75))
    corponf5 = Column(String(75))
    corponf6 = Column(String(75))
    fone = Column(String(15))
    fone2 = Column(String(15))
    fax = Column(String(15))
    contato = Column(String(40))
    bairro = Column(String(40))
    cep = Column(String(15))
    fantasia = Column(String(50))
    email = Column(String(100))


t_uclog = Table(
    'uclog', metadata,
    Column('applicationid', String(250)),
    Column('iduser', Integer),
    Column('msg', String(250)),
    Column('data', String(14)),
    Column('nivel', Integer)
)


t_ucpmsg = Table(
    'ucpmsg', metadata,
    Column('idmsg', Integer),
    Column('usrfrom', Integer),
    Column('usrto', Integer),
    Column('subject', String(50)),
    Column('msg', String(255)),
    Column('dtsend', String(12)),
    Column('dtreceive', String(12))
)


t_uctabhistory = Table(
    'uctabhistory', metadata,
    Column('applicationid', String(250)),
    Column('userid', Integer),
    Column('eventdate', Text(10)),
    Column('eventtime', Text(8)),
    Column('form', String(250)),
    Column('formcaption', String(100)),
    Column('event', String(50)),
    Column('obs', Text),
    Column('tname', String(50))
)


t_uctabrights = Table(
    'uctabrights', metadata,
    Column('uciduser', Integer),
    Column('ucmodule', String(50)),
    Column('uccompname', String(50)),
    Column('uckey', String(255))
)


t_uctabrightsex = Table(
    'uctabrightsex', metadata,
    Column('uciduser', Integer),
    Column('ucmodule', String(50)),
    Column('uccompname', String(50)),
    Column('ucformname', String(50)),
    Column('uckey', String(255))
)


class Uctabuser(Base):
    __tablename__ = 'uctabusers'

    uciduser = Column(Integer, primary_key=True)
    ucusername = Column(String(30))
    uclogin = Column(String(30))
    ucpassword = Column(String(250))
    ucemail = Column(String(150))
    ucprivileged = Column(Integer)
    uctyperec = Column(Text(1))
    ucprofile = Column(Integer)
    uckey = Column(String(255))
    ucpassexpired = Column(Text(10))
    ucuserexpired = Column(Integer, server_default=text("0"))
    ucuserdayssun = Column(Integer)
    ucinative = Column(Integer)


t_uctabuserslogged = Table(
    'uctabuserslogged', metadata,
    Column('ucidlogon', Text(38)),
    Column('uciduser', Integer),
    Column('ucapplicationid', String(50)),
    Column('ucmachinename', String(50)),
    Column('ucdata', String(14))
)


class Unidademedida(Base):
    __tablename__ = 'unidademedida'

    codun = Column(Text(3), primary_key=True)
    descricao = Column(String(50))


class UsoProduto(Base):
    __tablename__ = 'uso_produto'

    cod_uso = Column(Integer, primary_key=True)
    cod_produto = Column(ForeignKey('produtos.codproduto'), nullable=False, index=True)
    descricao = Column(String(150))
    ano_de = Column(Integer)
    ano_ate = Column(Integer)
    uso_venda = Column(Text(1))
    grupo = Column(String(30))
    quantidade = Column(Float, server_default=text("0"))
    uso_orcamento = Column(Text(1))
    aumentaacima = Column(Float)
    aumentaacimaqtde = Column(Float)
    reduzabaixo = Column(Float)
    reduzabaixoqtde = Column(Float)

    produto = relationship('Produto')


class Usuario(Base):
    __tablename__ = 'usuario'

    codusuario = Column(SmallInteger, primary_key=True)
    nomeusuario = Column(String(30), nullable=False)
    status = Column(SmallInteger, nullable=False)
    perfil = Column(String(15))
    senha = Column(String(50))
    codbarra = Column(String(13))


class Veiculo(Base):
    __tablename__ = 'veiculo'

    cod_veiculo = Column(Integer, primary_key=True)
    cod_cliente = Column(ForeignKey('clientes.codcliente'), nullable=False)
    placa = Column(String(10))
    marca_modelo = Column(String(60))
    tipo = Column(String(20))
    combustivel = Column(String(20))
    ano_fab = Column(String(4))
    ano_mod = Column(String(4))
    cor = Column(String(20))
    chassis = Column(String(30))

    cliente = relationship('Cliente')


class Venda(Base):
    __tablename__ = 'venda'

    codvenda = Column(Integer, primary_key=True)
    codmovimento = Column(ForeignKey('movimento.codmovimento'), nullable=False)
    codcliente = Column(ForeignKey('clientes.codcliente'), nullable=False)
    datavenda = Column(Date, nullable=False)
    datavencimento = Column(Date, nullable=False)
    numerobordero = Column(Integer)
    banco = Column(SmallInteger)
    codvendedor = Column(ForeignKey('usuario.codusuario'))
    status = Column(SmallInteger)
    codusuario = Column(SmallInteger)
    datasistema = Column(Date)
    valor = Column(Float)
    notafiscal = Column(Integer)
    serie = Column(ForeignKey('series.serie'))
    desconto = Column(Float)
    codccusto = Column(SmallInteger)
    n_parcela = Column(SmallInteger)
    operacao = Column(Text(1))
    formarecebimento = Column(Text(1))
    n_documento = Column(String(20))
    caixa = Column(SmallInteger)
    multa_juros = Column(Float)
    apagar = Column(Float)
    valor_pagar = Column(Float)
    entrada = Column(Float)
    n_boleto = Column(String(30))
    status1 = Column(Text(1))
    controle = Column(String(15))
    obs = Column(String(500))
    valor_icms = Column(Float)
    valor_frete = Column(Float)
    valor_seguro = Column(Float)
    outras_desp = Column(Float)
    valor_ipi = Column(Float)
    prazo = Column(String(40))
    porcentagendesc = Column(Float)
    codorigem = Column(Integer)
    troco = Column(Float)
    comissao = Column(Float)
    caixinha = Column(Float)
    rateio = Column(Float)
    valor_st = Column(Float)
    xmlnfe = Column(LargeBinary)
    nomexml = Column(String(60))
    protocoloenv = Column(String(20))
    numrecibo = Column(String(20))

    cliente = relationship('Cliente')
    movimento = relationship('Movimento')
    usuario = relationship('Usuario')
    series = relationship('Series')


t_view_compra = Table(
    'view_compra', metadata,
    Column('codfornecedor', Numeric(scale=0)),
    Column('nomefornecedor', String(50)),
    Column('razaosocial', String(50)),
    Column('cidade', String(40)),
    Column('uf', Text(2)),
    Column('codproduto', Numeric(scale=0)),
    Column('produto', String(300)),
    Column('descproduto', String(300)),
    Column('qtde', Float),
    Column('preco_bruto', Float),
    Column('desconto', Float),
    Column('preco_liquido', Float),
    Column('valorcompra', Float),
    Column('codccusto', Numeric(scale=0)),
    Column('nomeccusto', String(200)),
    Column('codvendedor', Numeric(scale=0)),
    Column('nomevendedor', String(30)),
    Column('tipoproduto', String(10)),
    Column('codmovimento', Numeric(scale=0)),
    Column('coddetalhe', Numeric(scale=0)),
    Column('codcompra', Numeric(scale=0)),
    Column('datamovimento', Date),
    Column('datacompra', Date),
    Column('notafiscal', Numeric(scale=0)),
    Column('codpro', String(15))
)


t_view_venda = Table(
    'view_venda', metadata,
    Column('codcliente', Numeric(scale=0)),
    Column('nomecliente', String(60)),
    Column('razaosocial', String(60)),
    Column('cidade', String(40)),
    Column('uf', Text(2)),
    Column('codproduto', Numeric(scale=0)),
    Column('produto', String(300)),
    Column('descproduto', String(300)),
    Column('qtde', Float),
    Column('preco_bruto', Float),
    Column('desconto', Float),
    Column('preco_liquido', Float),
    Column('valorvenda', Float),
    Column('codccusto', Numeric(scale=0)),
    Column('nomeccusto', String(200)),
    Column('codvendedor', Numeric(scale=0)),
    Column('nomevendedor', String(30)),
    Column('tipoproduto', String(10)),
    Column('codmovimento', Numeric(scale=0)),
    Column('coddetalhe', Numeric(scale=0)),
    Column('codvenda', Numeric(scale=0)),
    Column('datamovimento', Date),
    Column('datavenda', Date),
    Column('notafiscal', Numeric(scale=0)),
    Column('codpro', String(15)),
    Column('cod_caixa', Numeric(scale=0))
)


class Visita(Base):
    __tablename__ = 'visitas'

    codvisita = Column(Integer, primary_key=True)
    codcliente = Column(Integer, nullable=False)
    visita = Column(String(60))
    dataultima = Column(Date)
    dataproxima = Column(Date)
    dias = Column(Integer)
