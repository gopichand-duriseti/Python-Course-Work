#INT Type_Conversions
int_a = 2
float(int_a) and str(int_a) and boola(int_a) are valid
#FLOAT Type_Conversions
float_b=2.3
int(float_b) and str(float_b) and bool(float_b) are valid
#STRING Type_Conversions
string_c = 'power'
int(string_c) #only for numeric strings similarly float(string_c)
bool(string_c),list(string_c),tuple(string_c),set(string_c) are valid
#LIST Type_Conversions
list_d = [1, 2, 3, 4]
str(list_d) "[1, 2, 3, 4]" ,bool(list_d),tuple(list_d),set(list_d) are valid
#TUPLE Type_Conversions
tuple=(1,2,3,4)
set(tuple_f),str(tuple_f),list(tuple_f),bool(tuple_f)
#SET Type_Conversions
set_e = {3, 4, 5, 6}
str(set_e),tuple(set_e),list(set_e),bool(set_e) are valid
#DICTIONARY Type_Conversions
dict_g = {1: 1, 2: 4, 3: 9}
str(dict_g),bool(dict_g),list(dict_g),tuple(dict_g),set(dict_g) are valid 
#BOOLEAN Type_Conversions
boolean = False
int(boolean),float(boolean),str(boolean) are valid
#LIST TO DICTIONARY
d = [('name', 'teja'), ('batch', '22'), ('subject', 'python')]
dict(d) #{'name': 'teja', 'batch': '22', 'subject': 'python'}
