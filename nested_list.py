#my_list = ["hi", 6, 6.0, ["i", 7, 7.0], ("a", 77, 77.7),{"key" : "value"}]
# dict = { 
#     "key" : "value",
#     "name" : "msd",
#     "no" : "07"
# }
# tuple_1 = tuple(dict.keys())
# tuple_10 = tuple(dict.values())
# print(tuple_1,tuple_10,sep='\n')

def nested_list():

    my_list=[10, "a", 30, "c", 2.0, ["hi", 2], 5.77, 'b', 100, (1, 20), 110, 'msd', [500],False , True ,{"key" : "value"}]

    list_1=[my_list[5],my_list[12]]
    tuple_1=(my_list[9])
    boolean=(my_list[13],my_list[14])
    numeric= (my_list[0],my_list[2],my_list[5][1],my_list[9][0],my_list[9][1],my_list[12][0],my_list[8],my_list[10])
    float_1=(my_list[4],my_list[6])
    string_1=(my_list[1],my_list[3],my_list[5][0],my_list[7],my_list[11])
    dict_1=[my_list[15]["key"]]
    print(list_1,tuple_1,boolean,numeric,float_1,string_1,dict_1,sep='\n')