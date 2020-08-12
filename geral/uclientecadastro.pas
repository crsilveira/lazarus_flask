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
    BitBtn2: TBitBtn;
    btnCidade3: TButton;
    btnCidade4: TButton;
    btnGravar: TBitBtn;
    btnGravar1: TBitBtn;
    btnGravar2: TBitBtn;
    btnGravar3: TBitBtn;
    BufDataset1: TBufDataset;
    ComboBox1: TComboBox;
    ComboBox2: TComboBox;
    ComboBox3: TComboBox;
    ComboBox4: TComboBox;
    ComboBox5: TComboBox;
    ComboBox6: TComboBox;
    ds: TDataSource;
    edtcodcliente: TDBEdit;
    DBEdit10: TDBEdit;
    DBEdit11: TDBEdit;
    DBEdit12: TDBEdit;
    DBEdit13: TDBEdit;
    DBEdit14: TDBEdit;
    DBEdit15: TDBEdit;
    DBEdit16: TDBEdit;
    DBEdit18: TDBEdit;
    DBEdit19: TDBEdit;
    DBEdit20: TDBEdit;
    DBEdit21: TDBEdit;
    DBEdit22: TDBEdit;
    DBEdit23: TDBEdit;
    edtrazaosocial: TDBEdit;
    edtcnpj: TDBEdit;
    DBEdit40: TDBEdit;
    DBEdit41: TDBEdit;
    DBEdit42: TDBEdit;
    DBEdit43: TDBEdit;
    DBEdit44: TDBEdit;
    DBEdit45: TDBEdit;
    DBEdit46: TDBEdit;
    DBEdit47: TDBEdit;
    DBEdit48: TDBEdit;
    DBEdit49: TDBEdit;
    DBEdit5: TDBEdit;
    DBEdit50: TDBEdit;
    DBEdit51: TDBEdit;
    DBEdit52: TDBEdit;
    DBEdit53: TDBEdit;
    DBEdit54: TDBEdit;
    DBEdit55: TDBEdit;
    DBEdit6: TDBEdit;
    DBEdit7: TDBEdit;
    DBEdit8: TDBEdit;
    DBEdit9: TDBEdit;
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
    RadioGroup1: TRadioGroup;
    RadioGroup2: TRadioGroup;
    RadioGroup3: TRadioGroup;
    TabSheet1: TTabSheet;
    TabSheet3: TTabSheet;
    TabSheet6: TTabSheet;
    procedure btnGravar2Click(Sender: TObject);
    procedure btnGravar3Click(Sender: TObject);
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

procedure TfClienteCadastro.btnGravar3Click(Sender: TObject);
begin
  Close;
end;

procedure TfClienteCadastro.btnGravar2Click(Sender: TObject);
begin
  Close;
end;

end.

