unit uClienteCadastro;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, db, BufDataset, Forms, Controls, Graphics, Dialogs,
  ExtCtrls, DBCtrls, StdCtrls, ComCtrls, Buttons, Types,
  fphttpclient, fpjson, jsonparser;

type

  { TfClienteCadastro }

  TfClienteCadastro = class(TForm)
    btnProcCidade: TBitBtn;
    btnCidade3: TButton;
    btnCidade4: TButton;
    btnGravar: TBitBtn;
    btnExcluir: TBitBtn;
    btnProcurar: TBitBtn;
    btnSair: TBitBtn;
    BufDataset1: TBufDataset;
    edtcodfiscal: TComboBox;
    edt_cfop: TComboBox;
    edtregiao: TComboBox;
    edtcodusuario: TComboBox;
    edtcodtransp: TComboBox;
    edtnomelista: TComboBox;
    ds: TDataSource;
    edtcodcliente: TDBEdit;
    edtcodlista: TDBEdit;
    edtlimitecredito: TDBEdit;
    edtprazorecebimento: TDBEdit;
    edtdesconto: TDBEdit;
    edtdadosadicionais: TDBEdit;
    edtlogradouro: TDBEdit;
    edtnumero: TDBEdit;
    edtbairro: TDBEdit;
    edtcomplemento: TDBEdit;
    edtcidade: TDBEdit;
    edtcep: TDBEdit;
    edtcd_ibge: TDBEdit;
    edtuf: TDBEdit;
    edtrazaosocial: TDBEdit;
    edtcnpj: TDBEdit;
    edtlogradouro2: TDBEdit;
    edtbairro2: TDBEdit;
    edtcidade2: TDBEdit;
    edtcep2: TDBEdit;
    edtcomplemento2: TDBEdit;
    edtcd_ibge2: TDBEdit;
    edtuf2: TDBEdit;
    edtnumero2: TDBEdit;
    edtlogradouro1: TDBEdit;
    edtbairro1: TDBEdit;
    edtinscestadual: TDBEdit;
    edtcidade1: TDBEdit;
    edtcep1: TDBEdit;
    edtcomplemento1: TDBEdit;
    edtcd_ibge1: TDBEdit;
    edtuf1: TDBEdit;
    edtnumero1: TDBEdit;
    edtcontato: TDBEdit;
    edttelefone: TDBEdit;
    edttelefone1: TDBEdit;
    edte_mail: TDBEdit;
    dsCliente: TDataSource;
    Label13: TLabel;
    Label14: TLabel;
    Label15: TLabel;
    Label16: TLabel;
    Label17: TLabel;
    Label18: TLabel;
    Label19: TLabel;
    Label20: TLabel;
    Label21: TLabel;
    Label22: TLabel;
    Label23: TLabel;
    Label24: TLabel;
    Label25: TLabel;
    Label26: TLabel;
    Label27: TLabel;
    Label28: TLabel;
    Label29: TLabel;
    Label30: TLabel;
    Label31: TLabel;
    Label32: TLabel;
    Label33: TLabel;
    Label34: TLabel;
    Label4: TLabel;
    Label42: TLabel;
    Label43: TLabel;
    Label44: TLabel;
    Label45: TLabel;
    Label46: TLabel;
    Label47: TLabel;
    Label49: TLabel;
    Label50: TLabel;
    Label51: TLabel;
    Label52: TLabel;
    Label53: TLabel;
    Label54: TLabel;
    Label55: TLabel;
    Label56: TLabel;
    Label57: TLabel;
    Label58: TLabel;
    Label59: TLabel;
    Label6: TLabel;
    Label60: TLabel;
    Label61: TLabel;
    Label62: TLabel;
    Label63: TLabel;
    Label7: TLabel;
    Label8: TLabel;
    edtnomecliente: TDBEdit;
    PageControl1: TPageControl;
    Panel1: TPanel;
    Panel2: TPanel;
    Panel3: TPanel;
    Panel4: TPanel;
    Panel5: TPanel;
    edttipofirma: TRadioGroup;
    edttem_ie: TRadioGroup;
    edtstatus: TRadioGroup;
    TabSheet1: TTabSheet;
    TabSheet3: TTabSheet;
    TabSheet6: TTabSheet;
    procedure btnProcurarClick(Sender: TObject);
    procedure btnSairClick(Sender: TObject);
    procedure btnGravarClick(Sender: TObject);
    procedure dsDataChange(Sender: TObject; Field: TField);
    procedure FormShow(Sender: TObject);
    procedure PageControl1Change(Sender: TObject);
    procedure Panel2Click(Sender: TObject);
    procedure TabSheet1ContextPopup(Sender: TObject; MousePos: TPoint;
      var Handled: Boolean);
    procedure TabSheet5ContextPopup(Sender: TObject; MousePos: TPoint;
      var Handled: Boolean);
  private

  public
    caminho_server: String;
  end;

var
  fClienteCadastro: TfClienteCadastro;

implementation

{$R *.lfm}

{ TfClienteCadastro }

procedure TfClienteCadastro.TabSheet1ContextPopup(Sender: TObject;
  MousePos: TPoint; var Handled: Boolean);
begin

end;

procedure TfClienteCadastro.TabSheet5ContextPopup(Sender: TObject;
  MousePos: TPoint; var Handled: Boolean);
begin

end;

procedure TfClienteCadastro.Panel2Click(Sender: TObject);
begin

end;

procedure TfClienteCadastro.PageControl1Change(Sender: TObject);
begin

end;

procedure TfClienteCadastro.FormShow(Sender: TObject);
var
  jData : TJSONData;
  jItem : TJSONData;
  jObject : TJSONObject;
  postJson: TJSONObject;
  dadosJson: TJSONObject;
  responseData: String;
  i, k  : integer;
  c: String;
  t: String;
  s: String;
begin
  // Carregar o BufDataSet e ligar os dbedit nele
    // CARREGA OS CAMPOS PARA O GRID
    //Memo2.Lines.Clear;
    {
    BufDataset1.Clear;
    postJson := TJSONObject.Create;
    dadosJson := TJSONObject.Create;
    postJson.Add('title', 'Pegando Tabela');
    postJson.Add('body', 'Tabela Cliente');
    dadosJson.Add('nometabela', 'Cliente');

    // CHAMO A FUNCAO  =  cliente_tabela (hello.py)
    postJson.Add('cliente_tabela', dadosJson);

    postJson.Add('userId', 1);
    With TFPHttpClient.Create(Nil) do
      try
        AddHeader('Content-Type', 'application/json');
        RequestBody := TStringStream.Create(postJson.AsJSON);
        responseData := Post(caminho_server);
      finally
       Free;
      end;
    //Memo2.Lines.Add(responseData);
    jData := GetJSON(responseData);
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
    }
    {
    for k:=0 to ComponentCount-1 do
       if (Components[k] is TDBEdit) then
         if (Components[k] as TDBEdit).Name = 'edt' + field_name then
         begin
            field_value := jItem.FindPath(field_name).AsString;
            (Components[k] as TEdit).Text := field_value;
            Break;
         end;
    }
    {
    edtnomecliente.DataSource := ds;
    edtnomecliente.DataField := 'nomecliente';
    edtrazaosocial.DataSource := ds;
    edtrazaosocial.DataField := 'razaosocial';
    edtcodcliente.DataSource := ds;
    edtcodcliente.DataField := 'codcliente';
    edtcnpj.DataSource := ds;
    edtcnpj.DataField := 'cnpj';}
    i := BufDataset1.FieldDefs.Count;
    //c := BufDataset1.FieldDefs.Items[0].DisplayName;
    c := BufDataset1.FieldDefs.Items[0].Name;
    for i:=0 to BufDataset1.FieldDefs.Count-1 do
    begin
      c := BufDataset1.FieldDefs.Items[i].Name;
      for k:=0 to ComponentCount-1 do
       if (Components[k] is TDBEdit) then
         if (Components[k] as TDBEdit).Name = 'edt' + c then
         begin
            //field_value := jItem.FindPath(field_name).AsString;
            (Components[k] as TDBEdit).DataSource := ds;
            (Components[k] as TDBEdit).DataField := c;
            Break;
         end;
    end;


    BufDataset1.Open;
end;

procedure TfClienteCadastro.dsDataChange(Sender: TObject; Field: TField);
begin

end;

procedure TfClienteCadastro.btnSairClick(Sender: TObject);
begin
  Close;
end;

procedure TfClienteCadastro.btnGravarClick(Sender: TObject);
var i: Integer;
  postJson: TJSONObject;
  dadosJson: TJSONObject;
  responseData: String;
  comDados: String;
  ver: string;
begin
  comDados := 'N';
  postJson := TJSONObject.Create;
  dadosJson := TJSONObject.Create;
  BufDataset1.Post;
  // gravando alteracoes ou inclusões
  if edtcodcliente.Text = '0' then
  begin
    // inclusao
    postJson.Add('title', 'Insert');
    postJson.Add('body', 'Insert');
    postJson.Add('cliente_insert', dadosJson);
    postJson.Add('userId', 1);
    for i:=0 to BufDataset1.FieldDefs.Count-1 do
    begin
      comDados := 'S';
      ver := BufDataset1.FieldDefs.Items[i].Name;
      ver := BufDataset1.Fields[i].Value;
      dadosJson.Add(BufDataset1.FieldDefs.Items[i].Name, BufDataset1.Fields[i].Value);
    end;
  end
  else begin
    // atualizacao
    postJson.Add('title', 'Update');
    postJson.Add('body', 'Corpo Update');
    postJson.Add('cliente_update', dadosJson);
    postJson.Add('userId', 1);
    for i:=0 to BufDataset1.FieldDefs.Count-1 do
    begin
      comDados := 'S';
      ver := BufDataset1.FieldDefs.Items[i].Name;
      ver := BufDataset1.Fields[i].Value;
      dadosJson.Add(BufDataset1.FieldDefs.Items[i].Name, BufDataset1.Fields[i].Value);
    end;
  end;
  if (comDados = 'S') then
    begin

      With TFPHttpClient.Create(Nil) do
        try
          AddHeader('Content-Type', 'application/json');
          RequestBody := TStringStream.Create(postJson.AsJSON);
          responseData := Post(caminho_server);
          ShowMessage(responseData);
        finally
         Free;
        end;
    end;
end;

procedure TfClienteCadastro.btnProcurarClick(Sender: TObject);
begin
  Close;
end;

end.

