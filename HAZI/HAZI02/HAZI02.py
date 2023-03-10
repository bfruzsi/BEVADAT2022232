# %%
import numpy as np

#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()


def column_swap(array: np.array) -> np.array:
    array[:, [0, 1]] = array[:, [1, 0]]

    return array

# Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön


def compare_two_array(array1: np.array, array2: np.array) -> np.array:
    return np.where(array1 == array2)

# Készíts egy olyan függvényt, ami vissza adja string-ként a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!, 


def get_array_shape(array: np.array) -> np.array:

    row = 1
    column = 1
    depth = 1

    if np.ndim(array) == 3:
        column = array.shape[0]
        row = array.shape[1]
        depth = array.shape[2]
        return "sor: {}, oszlop: {}, melyseg: {}".format(row, column, depth)
    elif np.ndim(array) == 2:
         column = array.shape[0]
         row = array.shape[1]
         return "sor: {}, oszlop: {}, melyseg: {}".format(column, row, depth)
    else:
        column = array.shape[0]
        return "sor: {}, oszlop: {}, melyseg: {}".format(row, column, depth)

# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges pred-et egy numpy array-ből. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()


def encode_Y(array: np.array, classes: int) -> np.array:
    result = np.zeros((len(array), classes))
    result[np.arange(len(array)), array] = 1

    return result

# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()


def decode_Y(twoDarray: np.array) -> np.array:
    result = np.where(twoDarray == 1)[1]
    return result

# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy listát és egy array-t és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()


def eval_classification(mylist: list, array: np.array):
    max_index = np.argmax(array)
    return mylist[max_index]


# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()


def replace_odd_numbers(array: np.array) -> np.array:
    result = np.where(array % 2 == 1, -1, array)
    return result


# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb 
# vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()


def replace_by_value(array: np.array, number) -> np.array:  
    return np.where(array < number, -1, 1)

# Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza


def array_multi(arr):
    return np.prod(arr)

# Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az 
# elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()


def array_multi_2d(arr):
    mul = np.prod(arr, axis=1)
    return list(mul)

# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()


def add_border(array: np.array) -> np.array:
    row, column = np.array(array).shape
    new_array = np.zeros((row+2, column+2))
    new_array[1:-1, 1:-1] = array

    return new_array

# A KÖTVETKEZŐ FELADATOKHOZ NÉZZÉTEK MEG A NUMPY DATA TYPE-JÁT!

# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot és ezt adja vissza egy numpy array-ben. A fgv ként str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettő paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()


def list_days(start_date: str, end_date: str)-> np.array:
    #start = np.datetime64(start_date+"-01")
    #end = np.datetime64(end_date+"-01")
    #array = np.array(np.arange(start,end),np.datetime64)
    array = np.arange(start_date, end_date, dtype='datetime64[D]')
    return array

list_days('2023-03', '2023-04')

# Írj egy fügvgényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD. Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24


def get_act_date():
    act_date = np.datetime64('now')
    return np.datetime_as_string(act_date, unit='D')

# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta. Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()


def sec_from_1970() -> int: 
    time1 = np.datetime64('now')
    time2 = '1970-01-01 00:02:00'    
    dt = np.datetime64(time1) - np.datetime64(time2)
    seconds = dt.item().total_seconds()

    return int(seconds)