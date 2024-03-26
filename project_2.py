from ast import Index
import json
from operator import index
from mysqlx import Column
import pandas as pd
import math
def read_json():
    with open("D:/Semester-6/DAV/Project dataset/encrypted_vpn_dataset/Non VPN/mail.json") as mails:
        mails_data=json.load(mails,)
    mails_df=pd.DataFrame(mails_data)
    # print(mails_df.head())
    protocol_lst=set(mails_df["ip_proto"])
    # print(type(protocol_lst))
    for protocol in protocol_lst:

        temp_protocol_df=mails_df[mails_df["ip_proto"]==protocol]
        # print(temp_protocol_df.index)
        protocol_df_col=list(temp_protocol_df.columns)
        # print(protocol_df_col)
        protocol_attr=list(list(temp_protocol_df["x_packets"])[0][0].keys())
        removed_element=protocol_df_col.pop(protocol_df_col.index("x_packets"))
        protocol_df=pd.DataFrame(columns=protocol_df_col+protocol_attr)
        protocol_df_col.append(removed_element)
        
        for row in temp_protocol_df.index:
            protocol_values=[]
            val_list=[]
            # print(list(temp_protocol_df.loc[row,list(temp_protocol_df.columns)]))
            for lst in list(temp_protocol_df.loc[row,list(temp_protocol_df.columns)]):
                if  isinstance(lst,list):
                    for dictnry in lst:
                        if isinstance(dictnry,dict):
                            dict_val_lst=[]
                            print(protocol_df.columns)
                            for val in range(len(list(dictnry.keys()))):

                                if protocol_attr[val] in list(dictnry.keys()):
                                    print(val)
                                    print(list(protocol_df.columns)[val])
                                    print(len(list(dictnry.values())))
                                    print(list(dictnry.values()))
                                    dict_val_lst.append(list(dictnry.values())[val])
                                else:
                                    dict_val_lst.append(math.nan)
                                    dict_val_lst.append(list(dictnry.values())[val])

                            protocol_values=val_list+dict_val_lst 
                            data={}
                            print(data)
                            removed_element=protocol_df_col.pop(protocol_df_col.index("x_packets"))
                            print(list(protocol_df.columns))
                            print(protocol_values)
                            print(len(list(protocol_df.columns)),len(protocol_values)) 
                            print("hi",protocol_df.shape) 
                            for index in range(len(list(protocol_df.columns))):
                                # if  list(protocol_df.columns)[index] in list((dictnry.keys()):
                                data[list(protocol_df.columns)[index]]=[protocol_values[index]]
                                # else:
                                #     data[list(protocol_df.columns)[index]]=[math.nan]



                            print(data)
                            temp_df=pd.DataFrame(data)  
                            protocol_df=pd.concat([protocol_df,temp_df])
                            protocol_df_col.append(removed_element)
                else:
                    val_list.append(lst)        
            # print(protocol_df)
            # print(protocol_values)
            # print(len(list(protocol_df_col)+protocol_attr))
            # print(protocol_df_col+protocol_attr)
        file_name=protocol +".csv"
        protocol_df.to_csv(file_name,index=False)       
                         
    

read_json()
# def read_csv():
#     mails_df=pd.read_csv("D:/Semester-6/DAV/Project dataset/mails.csv")    
#     col_lst=mails_df.columns
#     # mails_df.info()
#     protocol_lst=set(list(mails_df["ip_proto"]))
#     # print(protocol_lst)
#     udp_df=mails_df[mails_df["ip_proto"]=="udp"]
#     col_lst=mails_df["x_packets"]
#     first_row_data = mails_df.iloc[0]  # Access the first row as a Series
#     list_of_dicts =first_row_data["x_packets"]  # Replace "your_column_name" with the actual column name
#     list_of_dicts = [eval(dict_str) for dict_str in list_of_dicts]

#     print(list_of_dicts)

    # for dictnr in col_lst.split(","):
    #     print(dictnr)
      
        
    # col_dict=dict(col_lst[0])
    # print(col_dict.keys())
    # print(udp_df)

    
# read_csv()
# def protocol_filter(proto_df):
    