# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import line
from data import getdata

menu_string = "  1. ข้าวผัดกระเพา\n  2. ข้าวบะหมี่ผัดใส่กรอก"

new_msg: str = "\n\nสวัสดี, เราหิวมากๆเลยย \nTonnee Hiww Khaw Mak Lei" \
               f'\n\nเมนูอยากกินน\n{menu_string}' \
               "\n\nFak ma rub nee hai noii\nhttps://goo.gl/maps/s3vH2rN6nnCYfPCB6"

API_reply_msg: str = "สวัสดี, เราหิวมากๆเลยย \nTonnee Hiww Khaw Mak Lei" \
               f'\n\nเมนูอยากกินน\n{menu_string}' \
               "\n\nFak ma rub nee hai noii\nhttps://goo.gl/maps/s3vH2rN6nnCYfPCB6"



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    line.sendline(msg=new_msg)
    getdata().places_API(['13.184983, 100.933544'], radius=50000)
    #  ได้โลแล้วไงต่อ
    # ปุ่มอับเดทโลในไลน์?




    # import plotly.express as px
    # import pandas
    # import html
    # import pandas as pd
    #
    #
    # df = pandas.DataFrame({
    #     'Name' : [restaurant["name"] for restaurant in restaurant_data],
    #     'Latitude' : [restaurant["latitude"] for restaurant in restaurant_data],
    #     'Longitude' : [restaurant["longitude"] for restaurant in restaurant_data],
    #     'Magnitude': [1 for x in range(len(restaurant_data))],
    #
    # })
    # df = pandas.DataFrame(df)
    # fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', hover_name='Name', radius=10,
    #                         center=dict(lat=0, lon=180), zoom=0, mapbox_style="stamen-terrain")
    # fig.data[0].hovertemplate += html.Button('Button 1', id='btn-nclicks-1', n_clicks=0)
    # fig.update_layout(mapbox_style="carto-darkmatter")
    # fig.update_layout(margin=dict(b=0, t=0, l=0, r=0))
    #
    # fig.show()
