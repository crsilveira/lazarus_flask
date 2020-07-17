unit Unit2;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  DateTimePicker;

type

  { TForm2 }

  TForm2 = class(TForm)
    dtdatacadastro: TDateTimePicker;
    edtcodcliente: TEdit;
    edtnomecliente: TEdit;
    edtrazaosocial: TEdit;
    edtcnpj: TEdit;
    rgtipofirma: TRadioGroup;
    procedure FormShow(Sender: TObject);
  private

  public

  end;

var
  Form2: TForm2;

implementation

{$R *.lfm}

{ TForm2 }

procedure TForm2.FormShow(Sender: TObject);
begin

end;

end.

