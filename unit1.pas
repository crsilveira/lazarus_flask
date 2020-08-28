unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, Buttons, StdCtrls,
  DBGrids, fphttpclient, fpjson, jsonparser, memds, db, BufDataset;



type

  { TForm1 }

  TForm1 = class(TForm)
    BitBtn1: TBitBtn;
    btnBuscaTudo1: TBitBtn;
    btnCadastroCliente: TBitBtn;
    btnBuscaTudo: TBitBtn;
    btnBuscaUmRegistro: TBitBtn;
    btnCarregaTodaTabela: TBitBtn;
    btnEstruturaGrid: TBitBtn;
    btnEnviar: TBitBtn;
    BufDataset1: TBufDataset;
    DataSource1: TDataSource;
    DBGrid1: TDBGrid;
    edtPagina: TEdit;
    edtcaminho: TEdit;
    edtcodcliente: TEdit;
    edtnomecliente: TEdit;
    Edit3: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Memo1: TMemo;
    Memo2: TMemo;
    procedure BitBtn1Click(Sender: TObject);
    procedure btnBuscaTudo1Click(Sender: TObject);
    procedure btnBuscaTudoClick(Sender: TObject);
    procedure btnBuscaUmRegistroClick(Sender: TObject);
    procedure btnCadastroClienteClick(Sender: TObject);
    procedure btnCarregaTodaTabelaClick(Sender: TObject);
    procedure btnEstruturaGridClick(Sender: TObject);
    procedure btnEnviarClick(Sender: TObject);
    procedure DBGrid1CellClick(Column: TColumn);
  private
    const url = 'http://127.0.0.1:5000/';
    function CarregarJson(tabela, uso: String): String;

  public

  end;

var
  Form1: TForm1;

implementation

uses uClienteCadastro, JsonTools;

{$R *.lfm}

{ TForm1 }

procedure TForm1.btnBuscaTudoClick(Sender: TObject);
var L: TStringList;
  jData : TJSONData;
  jItem : TJSONData;
  object_name, field_name, field_value: String;
  i, j: integer;
begin
  btnEstruturaGrid.Click;
  try
    L := TStringList.Create;
    with tfphttpclient.create(nil) do
    begin
      // BUSCA OS CLIENTE - else do hello.py
      Get(edtcaminho.Text, L);

      Memo1.Lines.Assign(L);

      jData := GetJSON(Memo1.Text);
      for i := 0 to jData.Count - 1 do
      begin
        jItem := jData.Items[i];
        BufDataset1.Append;
        for j := 0 to jItem.Count - 1 do
        begin
          //jObject := TJSONObject(jItem);
          field_name := TJSONObject(jItem).Names[j];
          field_value := jItem.FindPath(TJSONObject(jItem).Names[j]).AsString;
          BufDataset1.FieldByName(field_name).Value := field_value;
          if field_name = 'codcliente' then
            edtcodcliente.Text := field_value;
          if field_name = 'nomecliente' then
            edtnomecliente.Text := field_value;
        end;
        BufDataset1.Post;
      end;
      free;
    end;
    BufDataSet1.SaveToFile('cliente.bds');
  finally
    l.Free;
  end;
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
var
  N: TJsonNode;
  v : string;
  C : TJsonNode;
begin
  N := TJsonNode.Create;
  N.Value := Memo1.Text;

  for C in N do
  begin
      v := C.Value;
      v := C.Find('codcliente').Value;
  end;
  //v := N.Value;

end;

procedure TForm1.btnBuscaTudo1Click(Sender: TObject);
var
  N: TJsonNode;
  v : string;
  C : TJsonNode;
  L: TStringList;
  field_name, field_value: String;
begin
  // Busca usando o JsonTools
  btnEstruturaGrid.Click;
  try
    L := TStringList.Create;
    with tfphttpclient.create(nil) do
    begin
      // BUSCA OS CLIENTE - else do hello.py
      Get(edtcaminho.Text, L);
      free;
    end;
    Memo1.Lines.Assign(L);
    N := TJsonNode.Create;
    N.Value := Memo1.Text;

    for C in N do
    begin
      BufDataset1.Append;
      field_name := C.Find('codcliente').Name;
      field_value := C.Find('codcliente').Value;
      edtcodcliente.Text := field_value;
      BufDataset1.FieldByName(field_name).Value := field_value;
      field_name := C.Find('nomecliente').Name;
      field_value := C.Find('nomecliente').AsString;
      edtnomecliente.Text := field_value;
      BufDataset1.FieldByName(field_name).Value := field_value;
      field_name := C.Find('razaosocial').Name;
      field_value := C.Find('razaosocial').AsString;
      BufDataset1.FieldByName(field_name).Value := field_value;
      field_name := C.Find('cnpj').Name;
      field_value := C.Find('cnpj').AsString;
      BufDataset1.FieldByName(field_name).Value := field_value;
    end;
    BufDataset1.Post;

    BufDataSet1.SaveToFile('cliente.bds');
  finally
    l.Free;
  end;
end;

procedure TForm1.btnBuscaUmRegistroClick(Sender: TObject);
var L: TStringList;
  jData : TJSONData;
  jItem : TJSONData;
  //jObject : TJSONObject;
  //jArray : TJSONArray;
  //s: String;
  i, j, k: integer;
  field_name, field_value: String;
  postJson: TJSONObject;
  dadosJson: TJSONObject;
  responseData: String;
begin
  if (Edit3.Text = '') then
  begin
    BufDataset1.Filtered:=False;
    exit;
  end;
  Memo2.Lines.Clear;
  postJson := TJSONObject.Create;
  dadosJson := TJSONObject.Create;
  postJson.Add('title', 'Consulta Cliente');
  postJson.Add('body', 'Corpo Consulta');
  dadosJson.Add('codcliente', Edit3.text);
  postJson.Add('cliente', dadosJson);
  postJson.Add('userId', 1);
  With TFPHttpClient.Create(Nil) do
    try
      AddHeader('Content-Type', 'application/json');
      RequestBody := TStringStream.Create(postJson.AsJSON);
      responseData := Post(edtcaminho.Text);
    finally
      Free;
    end;
  Memo2.Lines.Add(responseData);

  jData := GetJSON(Memo2.Text);
  dadosJson := TJSONObject(jData);
  for i := 0 to jData.Count - 1 do
  begin
    jItem := jData.Items[i];
    for j := 0 to jItem.Count - 1 do
    begin
      field_name := TJSONObject(jItem).Names[j];
      begin
        for k:=0 to ComponentCount-1 do
           if (Components[k] is TEdit) then
             if (Components[k] as TEdit).Name = 'edt' + field_name then
             begin
                field_value := jItem.FindPath(field_name).AsString;
                (Components[k] as TEdit).Text := field_value;
                Break;
             end;
      end;
    end;
  end;
  BufDataset1.Filtered:=False;
  BufDataset1.Filter:='codcliente='+edit3.Text;
  BufDataset1.Filtered:=True;
end;

procedure TForm1.btnCadastroClienteClick(Sender: TObject);
begin
  fClienteCadastro.caminho_server := edtcaminho.Text;
  //fClienteCadastro.BufDataset1.BeforeInsert';
  if fileExists('cliente.bds') then
  begin
    fClienteCadastro.BufDataset1.LoadFromFile('cliente.bds');
    fClienteCadastro.BufDataset1.Filtered:=False;
    fClienteCadastro.BufDataset1.Filter:='codcliente='+edit3.Text;
    fClienteCadastro.BufDataset1.Filtered:=True;
  end;
  fClienteCadastro.ShowModal;
end;

procedure TForm1.btnCarregaTodaTabelaClick(Sender: TObject);
var
  jData : TJSONData;
  jItem : TJSONData;
  jObject : TJSONObject;
  postJson: TJSONObject;
  dadosJson: TJSONObject;
  responseData: String;
  i  : integer;
  c: String;
  t: String;
  s: String;
begin
  // CARREGA TODOS OS CAMPOS DA TABELA
  Memo2.Lines.Clear;
  postJson := TJSONObject.Create;
  dadosJson := TJSONObject.Create;
  postJson.Add('title', 'Pegando Estrutura Tabela');
  postJson.Add('body', 'Estrutura Tabela Cliente');
  dadosJson.Add('nometabela', 'Cliente');
  postJson.Add('cliente_tabela', dadosJson);
  postJson.Add('userId', 1);
  With TFPHttpClient.Create(Nil) do
    try
      AddHeader('Content-Type', 'application/json');
      RequestBody := TStringStream.Create(postJson.AsJSON);
      responseData := Post(edtcaminho.Text);
    finally
     Free;
    end;
  Memo2.Lines.Add(responseData);
  jData := GetJSON(Memo2.Text);
  for i := 0 to jData.Count - 1 do
  begin
    jItem := jData.Items[i];
    jObject := TJSONObject(jItem);
    c := jObject.Get('campo');
    t := jObject.Get('tipo');
    s := jObject.Get('tam');
    t := Copy(t, 1, 7);
    if Copy(t, 1, 4) = 'TEXT' then
       t := Copy(t, 1, 4);
    if t = 'INTEGER' then
      BufDataset1.FieldDefs.Add(c,ftInteger);
    if t = 'SMALLIN' then
      BufDataset1.FieldDefs.Add(c,ftInteger);
    if t = 'VARCHAR' then
      BufDataset1.FieldDefs.Add(c,ftString, StrToInt(s));
    if t = 'DATE' then
      BufDataset1.FieldDefs.Add(c,ftDate);
    if t = 'DATETIM' then
      BufDataset1.FieldDefs.Add(c,ftDateTime);
    if t = 'TEXT' then
      BufDataset1.FieldDefs.Add(c,ftString, StrToInt(s));
  end;
  BufDataset1.CreateDataSet;
  BufDataset1.Open;
end;

procedure TForm1.btnEstruturaGridClick(Sender: TObject);
var
  jData : TJSONData;
  jItem : TJSONData;
  jObject : TJSONObject;
  postJson: TJSONObject;
  dadosJson: TJSONObject;
  responseData: String;
  i  : integer;
  c: String;
  t: String;
  s: String;
begin
  // TODO tenho q separar o buffdataset do GRID .... ???!!!!
  // em um preciso todos os campos o outro nao, nao quero estrever a
  // estrutura toda da tabela no ats_cliente

  // CARREGA OS CAMPOS PARA O GRID
  Memo2.Lines.Clear;
  BufDataset1.Clear;
  postJson := TJSONObject.Create;
  dadosJson := TJSONObject.Create;
  postJson.Add('title', 'Pegando Estrutura Tabela');
  postJson.Add('body', 'Estrutura Tabela Cliente');
  dadosJson.Add('nometabela', 'Cliente');

  // CHAMO A FUNCAO  =  estrutura_grid (hello.py)
  postJson.Add('cliente_filtro', dadosJson);

  postJson.Add('userId', 1);
  With TFPHttpClient.Create(Nil) do
    try
      AddHeader('Content-Type', 'application/json');
      RequestBody := TStringStream.Create(postJson.AsJSON);
      responseData := Post(edtcaminho.Text);
    finally
     Free;
    end;
  Memo2.Lines.Add(responseData);
  jData := GetJSON(Memo2.Text);
  for i := 0 to jData.Count - 1 do
  begin
    jItem := jData.Items[i];
    jObject := TJSONObject(jItem);
    //object_name := TJSONObject(jData).Names[i];
    c := jObject.Get('campo');
    t := jObject.Get('tipo');
    s := jObject.Get('tam');
    t := Copy(t, 1, 7);
    if Copy(t, 1, 4) = 'TEXT' then
       t := Copy(t, 1, 4);
    if t = 'INTEGER' then
      BufDataset1.FieldDefs.Add(c,ftInteger);
    if t = 'SMALLIN' then
      BufDataset1.FieldDefs.Add(c,ftInteger);
    if t = 'VARCHAR' then
      BufDataset1.FieldDefs.Add(c,ftString, StrToInt(s));
    if t = 'DATE' then
      BufDataset1.FieldDefs.Add(c,ftDate);
    if t = 'DATETIM' then
      BufDataset1.FieldDefs.Add(c,ftDateTime);
    if t = 'TEXT' then
      BufDataset1.FieldDefs.Add(c,ftString, StrToInt(s));
  end;
  BufDataset1.CreateDataSet;
  BufDataset1.Open;
  with DBGrid1 do
    for i := 0 to jData.Count - 1 do
    begin
      jItem := jData.Items[i];
      jObject := TJSONObject(jItem);
      t := jObject.Get('titulo');
      Columns[i].Title.Caption := t;
      s := jObject.Get('tam');
      if StrToInt(s) > 0 then
        Columns[i].Width := StrToInt(s);
    end;
end;

procedure TForm1.btnEnviarClick(Sender: TObject);
var
  postJson: TJSONObject;
  dadosJson: TJSONObject;
  responseData: String;
begin
  postJson := TJSONObject.Create;
  dadosJson := TJSONObject.Create;
  postJson.Add('title', 'Titulo Teste');
  postJson.Add('body', 'Corpo Envio');
  dadosJson.Add('codcliente', edtcodcliente.text);
  dadosJson.Add('nomecliente', edtnomecliente.text);
  postJson.Add('dados', dadosJson);
  postJson.Add('userId', 1);

  With TFPHttpClient.Create(Nil) do
    try
      AddHeader('Content-Type', 'application/json');
      RequestBody := TStringStream.Create(postJson.AsJSON);
      responseData := Post(edtcaminho.Text);
    finally
     Free;
    end;
  Memo2.Lines.Add(responseData);
end;

procedure TForm1.DBGrid1CellClick(Column: TColumn);
begin
  edtcodcliente.Text := IntToStr(BufDataset1.FieldByName('codcliente').AsInteger);
  edtnomecliente.Text := BufDataset1.FieldByName('nomecliente').AsString;
end;

function TForm1.CarregarJson(tabela, uso: String): String;
var
  postJson: TJSONObject;
  dadosJson: TJSONObject;
  responseData: String;
begin
  postJson := TJSONObject.Create;
  dadosJson := TJSONObject.Create;
  postJson.Add('title', uso);
  postJson.Add('body', tabela);
  dadosJson.Add(tabela, tabela);
  postJson.Add(uso, dadosJson);
  postJson.Add('userId', 1);
  With TFPHttpClient.Create(Nil) do
    try
      AddHeader('Content-Type', 'application/json');
      RequestBody := TStringStream.Create(postJson.AsJSON);
      responseData := Post(edtcaminho.Text);
      result := responseData;
    finally
     Free;
    end;
end;

end.

