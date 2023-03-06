import plotly.graph_objects as go
import plotly
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def plotChart(data):
    x=[i for i in range(1,len(data)+1)]
    ys=[ i["SGPA"] for i in data.values() ]
    yg=[ i["CGPA"] for i in data.values() ]

    ytp =[ i["totalPoints"] for i in data.values() ]
    ytc =[ i["totalCredit"] for i in data.values() ]
    df = pd.DataFrame( {'totalPoints': ytp, 'totalCredit':ytc})

    scaler = MinMaxScaler()

    # Scale the values between 0 and 1
    df["topo"] = scaler.fit_transform(df[["totalPoints"]])
    df["toco"] = scaler.fit_transform(df[["totalCredit"]])


    ytp=[ i*10 for i in df["topo"].to_list()]
    ytc=[ i*10 for i in df["toco"].to_list()]

    


    fig = go.Figure(
        data=[go.Line(x=x,y=ys,name="SGPA"),go.Line(x=x,y=yg,name="CGPA"),
              go.Line(x=x,y=ytp,name="Total Points"),go.Line(x=x,y=ytc,name="Total Credits")],
        
        layout_title_text="Your SGPA and CGPA with time",
        layout_yaxis_range=[0,11],
        layout_xaxis_range=[0,11],

    )

    fig.update_layout(xaxis_title="Semesters", yaxis_title="Pointers",template="plotly_dark")
    graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
    return graph_div