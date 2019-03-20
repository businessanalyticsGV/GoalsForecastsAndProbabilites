### I.- EXTRATING FILES FROM JULITOOOOOOO

import os
import numpy as np
import pandas as pd

path = '//nvocorpfileshare/inventory management/FRANCISCO JARAMILLO/REPORTES/Diario-INNSIST vs MATRIX/Base/2019/Marzo'
ls_files = [file for file in os.listdir(path) if file[-len('.xlsx'):] == '.xlsx']


