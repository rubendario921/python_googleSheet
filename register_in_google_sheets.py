# Importación de Librerías
# Credenciales de Google
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime
import time


# Registro en Google Sheets
# Ingresar al link https://console.cloud.google.com/ y realizar la configuración en las APIs de Google Sheets.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# Descargar el archivo JSON de la Api de Google colocar en el mismo directorio donde funcionara el programa
KEY = "python-registro-masivo-shet.json"

# De todo el URl de la hoja de Google Sheet debemos copiar desde /d/................./edit y eso colocar en SPREADSHEET_ID para que identifique e ingrese los datos
#  https://docs.google.com/spreadsheets/d/................/edit#gid=XXXXXXXXX

SPREADSHEET_ID = "...................................."
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()

# Ingreso de datos
# nombre_completo = ['nombre1','nombre2']
# registro_unico =['numero1','numero2']
# f_emision = ['fecha1','fecha2']

nombre_completo = ["nombre1", "nombre2"]
registro_unico = ["numero1", "numero2"]
f_emision = ["fecha1", "fecha2"]

# Contador de registros
sent_count = 0

for i in range(len(nombre_completo)):
    # Toma la fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ingreso de datos en Sheet
    values = [[nombre_completo[i]], [[registro_unico]][f_emision[i]]]
    values = list(map(list, zip(*values)))
    range_ = "A{0}:L{0}".format(i + 1)
    result = (
        sheet.values()
        .append(
            spreadsheetId=SPREADSHEET_ID,
            range=range_,
            valueInputOption="USER_ENTERED",
            body={"values": values},
        )
        .execute()
    )
    sent_count += 1

    # Confirmacion de registro ingresado
    print(
        f"Dato ingresado {registro_unico[i]} --> {nombre_completo[i]}"
        + " "
        + fecha_actual
        + " --> "
        + str(sent_count)
    )
    time.sleep(5)


# Resultado de los registro enviados en total
print(f"Total de registros en Google Sheet: {sent_count}")
