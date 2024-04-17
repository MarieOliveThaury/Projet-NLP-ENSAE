import numpy as np
import pandas as pd
from unidecode import unidecode
#----------------------------------------------------------------------------------------------------------------


def find_index0(string, pattern) : 
    if (pattern + ': ') in string:
        return str.find(string, pattern + ': ') + len(pattern)
    else:
        return -1

#----------------------------------------------------------------------------------------------------------------


def find_information(pattern, string, df, liste):
    row = list(np.where(df['groundtruth'] == string)[0])[0] #on récupère le numéro de la ligne 
    index0 = df[pattern + '1'][row] #on récupère la position du début l'information pour le pattern 
    i = liste[row].index(index0) + 1 
    if i >= len(liste[row]) : 
        index1 = len(string)
    else :      
        index1 = liste[row][i] #on récupère la position de la fin de l'information pour le pattern
    if index0 == index1 :
        return ''
    else : 
        return unidecode(string[index0 + 2 : index1].lower().strip()) #on récupère l'information pour le pattern 


#----------------------------------------------------------------------------------------------------------------


def transform_sp(string) : 
    if string in ['s.p.', 'sp', 'sans prof', 'sans prof.', 's.p', 'sans p.', 'sans p', 's p', 'sans profession'] :
        return 'sans_profession'
    else :
        return string


#----------------------------------------------------------------------------------------------------------------