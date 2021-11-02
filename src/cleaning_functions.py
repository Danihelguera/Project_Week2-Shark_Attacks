import pandas as ps

def number_of_nans_in_each_row(df):
    """
    Esta función nos devuelve una lista con la cantidad de NaNs que hay en cada fila del data frame Pandas argumentado.
    Input:
        df --> class pandas dataframe
    Output:
        number_of_nans --> class list
    """
    nans_en_cada_fila = []
    for row in df.values:
        i = 0
        for el in row:
            if el != el :
                i += 1
        nans_en_cada_fila.append(i)
    return nans_en_cada_fila


def cambiarseparadorfechaapunto(x) :
    if type(x) == str :
        return x.replace( "/" , "." ).replace("-",".").replace(",",".")
    return x



def extraer_año_y_mes_de_case_number(fecha_fea):
    import re
    
    if fecha_fea != 0 :
        if re.search("\d{4}.\d{2}",fecha_fea) != None :
            return re.search("\d{4}.\d{2}" , fecha_fea ).group()
        else :
            return None
    else :
        return None



def separar_año(año_mes):
    return año_mes.split(".")[0]

def separar_mes(año_mes):
    return año_mes.split(".")[1]



def extraer_fecha_de_date(fecha_fea):
    import re
    print(fecha_fea)
    if re.search("\d\d-\w\w\w-\d{4}",fecha_fea) != None :
        date  = re.search("\d\d-\w\w\w-\d{4}",fecha_fea).group()
        year  = re.search("\d{4}"   , date ).group()
        month = re.search("\w\w\w"  , date ).group()
        day   = re.search("\d{2}"   , date ).group()
        
    elif re.search("\d\d-\w\w\w-\d{2}",fecha_fea) != None :
        date = re.search("\d\d-\w\w\w-\d{2}",fecha_fea).group()
        year  = "19" + re.search("-\d{2}"   , date ).group().split("-")[1]
        month = re.search("\w\w\w"  , date ).group()
        day   = re.search("\d{2}"   , date ).group()
        
    else :
        year = "0000"
        month = "00"
        day = "00"
    
    date = year + "-" + month + "-" + day
    print(date)
    return date



def crear_dicc_con_freq_de_palabras( serie_texto , num_min_repeticiones=1 ) :
    import re
    Freq_of_words = {}
    for elemento in serie_texto :
        if type(elemento) == str :
            for word in re.findall("[a-zA-Z]{3,}" , elemento.lower()) :
                if word in Freq_of_words :
                    Freq_of_words[word] +=1
                else :
                    Freq_of_words.setdefault(word, 1)
    import operator
    sorted_words = sorted(Freq_of_words.items(), key=operator.itemgetter(1) , reverse=True)
    word_freq = {}
    word_freq.clear()
    for i in sorted_words :
        if i[1] >= num_min_repeticiones:
            word_freq.update({i})
    return word_freq