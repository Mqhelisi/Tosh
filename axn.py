import pandas as pd
import numpy as np
from dash import html
import plotly.express as px
from pg1 import side2side,makeRow,labelDict,labelDict2

def controlAvgs(row):
#     get xbar
    avg = Avrg(row)
    rge = rnge(row)
#     print(avg,rge)
    return avg
# get range
def controlRange(row):
#     get xbar
    rge = rnge(row)
    return rge
# UCL xbar
def Meandf(dfm):
#     get xbar
    dfm['avg_xbar']=dfm['xbar'].mean()
    return dfm
# UCL range
def findUCL(avgxbr,avgrng,a2=0.577):
    return avgxbr+(a2*avgrng)
# LCL range
def findLCL(avgxbr,avgrng,a2=0.577):
    return avgxbr-(a2*avgrng)
# return values
def UCLRange(avgrng,d4=2.11):
    return d4*avgrng
def LCLRange(avgrng,d2=0):
    return d2*avgrng
# testarr
def Avrg(lst):
    return sum(lst)/len(lst)

def rnge(lst):
    return max(lst)-min(lst)

def ProCap(dfr,specVal,maxmin):
    usl = specVal+maxmin
    lsl = specVal-maxmin
    dayta = np.array(dfr.to_list())
    sampleMean = np.mean(dayta)
    print(sampleMean)
    sampleStdev = np.std(dayta)
    print(sampleStdev)

    cp = (usl-lsl)/(6*sampleStdev)
    cpu = (usl-sampleMean)/(3*sampleStdev)
    cpl = (sampleMean-lsl)/(3*sampleStdev)
    val = makeRow([
        side2side(
            html.Label("Process Capability",style=labelDict),
            html.Label(str(cp),style=labelDict2,id='proc_cp'),
        ),
        side2side(
            html.Label("Process Capability Upper",style=labelDict),
            html.Label(str(cpl),style=labelDict2,id='proc_lower'),
        ),
        side2side(
            html.Label("Process Capability Lower",style=labelDict),
            html.Label(str(cpu),style=labelDict2,id='proc_upper'),
        )]
    )
    return val

def makeCtrlData(dfrm,qty_item):
    fdf = dfrm.copy()[[qty_item]]

    fdf['xbar']=fdf[qty_item].apply(controlAvgs)
    fdf['range']=fdf[qty_item].apply(controlRange)
    fdf = Meandf(fdf)
    fdf['avg_range'] = fdf['range'].max()-fdf['range'].min()
    avgrg  = fdf['avg_range'].iloc[0]
    avgxbr  = fdf['avg_xbar'].iloc[0]

    fdf['UCL Bar'] = findUCL(avgxbr,avgrg)
    fdf['LCL Bar']= findLCL(avgxbr,avgrg)

    fdf['UCLRange'] = UCLRange(avgrg)
    fdf['LCLRange'] = LCLRange(avgrg)
    sampleData = np.array(fdf[qty_item].to_list())
    sampleMean = np.mean(sampleData)
    sampleStdDev = np.std(sampleData)
    return fdf, sampleData, sampleMean,sampleStdDev

def makeCharts(dfm,qlt):
    xbarCtrl = dfm[['xbar','avg_xbar','UCL Bar','LCL Bar']]
    rngeCtrl = dfm[['range','avg_range','UCLRange','LCLRange']]
    figg1 = px.line(rngeCtrl,markers=True,title="Range Control Chart for "+qlt)
    figg = px.line(xbarCtrl,markers=True,title="Mean Control Chart for "+qlt)
    return figg1, figg