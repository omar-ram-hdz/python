import os
from openpyxl import *

RUTA = r"C:\Users\omarr\OneDrive\Documentos\CursoPython\datos.xlsx"
if not os.path.exists(RUTA):
    libro = Workbook()
    libro.save(RUTA)
