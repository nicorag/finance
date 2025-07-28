#USE in GOOGLE COLAB
!pip install yfinance
#PANEL LIDER
import yfinance as yf
import os

# Tickers argentinos
tickers = ['ALUA.BA','BBAR.BA','BMA.BA','BYMA.BA','CEPU.BA','COME.BA','CRES.BA','EDN.BA','GGAL.BA','IRSA.BA','LOMA.BA','METR.BA','PAMP.BA', 'SUPV.BA','TECO2.BA','TGNO4.BA','TGSU2.BA','TRAN.BA','TXAR.BA','VALO.BA','YPFD.BA']
# Carpeta de salida
output_folder = "panel_lider_hasta_2024"
os.makedirs(output_folder, exist_ok=True)


# Guardar CSVs individuales
for ticker in tickers:
        df_ticker = yf.download(ticker, period='max')
        df_fil=df_ticker[df_ticker.index<='2024-12-30']
        output_path = os.path.join(output_folder, f"{ticker}_hasta2024.csv")
        df_fil.to_csv(output_path)
        print(f"{ticker} guardado en: {output_path}")
  
import shutil
from google.colab import files

# Carpeta que querés descargar (tu carpeta de CSVs)
carpeta = 'panel_lider_hasta_2024'
archivo_zip = carpeta + '.zip'

# Comprimir la carpeta
shutil.make_archive(carpeta, 'zip', carpeta)

# Descargar el archivo ZIP
files.download(archivo_zip)
#PANEL GENERAL
import yfinance as yf
import os

# Tickers argentinos
tickers = ['AGRO.BA','AUSO.BA','BHIP.BA','BOLT.BA','BPAT.BA','CADO.BA','CAPX.BA','CARC.BA','CECO2.BA','CELU.BA','CGPA2.BA','CTIO.BA','DGCU2.BA','FERR.BA','FIPL.BA','GAMI.BA','GBAN.BA','HARG.BA','INVJ.BA','LEDE.BA','LONG.BA','MIRG.BA','MOLA.BA','MOLI.BA','MORI.BA','OEST.BA','RICH.BA','RIGO.BA','SAMI.BA','SEMI.BA']
# Carpeta de salida
output_folder = "panel_general_hasta_2024"
os.makedirs(output_folder, exist_ok=True)


# Guardar CSVs individuales
for ticker in tickers:
        df_ticker = yf.download(ticker, period='max')
        df_fil=df_ticker[df_ticker.index<='2024-12-30']
        output_path = os.path.join(output_folder, f"{ticker}_hasta2024.csv")
        df_fil.to_csv(output_path)
        print(f"{ticker} guardado en: {output_path}")

import shutil
from google.colab import files

# Carpeta que querés descargar (tu carpeta de CSVs)
carpeta = 'panel_general_hasta_2024'
archivo_zip = carpeta + '.zip'

# Comprimir la carpeta
shutil.make_archive(carpeta, 'zip', carpeta)

# Descargar el archivo ZIP
files.download(archivo_zip)
