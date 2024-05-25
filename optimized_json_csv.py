from cProfile import label
import json
import pandas as pd
import datetime as dt
def read_json(json_data,saving_location):
    df=pd.DataFrame(json_data)
    protocol_lst=df["ip_proto"].unique()
    acutal_col=list(df.columns)
    acutal_col.pop(acutal_col.index('x_packets'))

    for protocol in protocol_lst:
        temp_protocol_df=df[df["ip_proto"]==protocol]
        protocol_attr=temp_protocol_df["x_packets"]
        actual_df=pd.DataFrame(columns=acutal_col)
        protocol_df=pd.DataFrame(columns=protocol_attr.iloc[0][0].keys())
        temp_df=pd.DataFrame(columns=acutal_col)

        for row in range(len(protocol_attr)):
            protocol_df=pd.concat([protocol_df,pd.DataFrame(protocol_attr.iloc[row])])
            temp_df=pd.concat([temp_df,pd.DataFrame(([temp_protocol_df.iloc[row,0:3]]*len(protocol_attr.iloc[row])))])
            protocol_df.reset_index(drop=True,inplace=True)
            temp_df.reset_index(drop=True,inplace=True)
        actual_df=pd.concat([temp_df,protocol_df],axis=1) 
        actual_df.to_csv(saving_location+"/"+protocol+".csv",index=False)
        
with open("D:/Semester-6/DAV/Project dataset/encrypted_vpn_dataset/Non VPN/meet.json") as non_streaming:
        non_streaming_data=json.load(non_streaming)
read_json(non_streaming_data,"D:/Semester-6/DAV/Project dataset/encrypted_vpn_dataset/Non VPN/sample")