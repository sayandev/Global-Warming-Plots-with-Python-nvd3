# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 21:51:24 2015

@author: Neel
"""

from nvd3 import multiBarChart
from nvd3 import lineChart
from nvd3 import linePlusBarChart
from nvd3 import lineWithFocusChart
from nvd3 import linePlusBarWithFocusChart
import random
import datetime
import time
import csv
import numpy as np


header=[]
data=[]
count=0
with open('ExcelFormattedGISTEMPDataCSV.csv') as f:
    reader = csv.reader(f)
    for row in reader:    
        print row
        if count==0:
            header.append(row)
        else:
            data.append(row)
        count=count+1
data_mat=np.array(data)
data_mat=data_mat.transpose()
data_trnsps=data_mat.tolist()

for i in range (0,len(data_trnsps)):
    for j in range (0,len(data_trnsps[i])):
        try:
            data_trnsps[i][j]=int(data_trnsps[i][j])
        except ValueError:
            data_trnsps[i][j]=np.nan
    
    
xdata1=[]
for i in range (0,len(data_trnsps[0])):
    xdata1.append(datetime.datetime.strptime(str(data_trnsps[0][i]), '%Y'))

start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
nb_element = 100
#Open File for test
output_file = open('tryd3.html', 'w')
#---------------------------------------

html_open = """
<!DOCTYPE html>
<html lang="en">
<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<link media="all" href="./bower_components/nvd3/src/nv.d3.css" type="text/css" rel="stylesheet" />
<script src="./bower_components/d3/d3.min.js" type="text/javascript"></script>
<script src="./bower_components/nvd3/nv.d3.min.js" type="text/javascript"></script>
</head>
"""

output_file.write(html_open)
type = "Line Chart of Monthly Temeprature from 1880-2015, Displaying Global Warming"
#chart = lineChart(name="lineChart-With-Interactive-Guideline",
#                  height=350, x_is_date=True, x_axis_format="%d %b %Y %H",
#                  jquery_on_ready=True, use_interactive_guideline=True)
                  
chart = lineChart(name="lineChart-With-Interactive-Guideline",
  height=1000,x_is_date=False,x_axis_format= '',
  jquery_on_ready=True, use_interactive_guideline=True)


chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
#xdata = list(range(nb_element))
#xdata = [start_time + x * 1000000000 for x in xdata]
#ydata = [i + random.randint(1, 10) for i in range(nb_element)]
#ydata2 = [x * 2 for x in ydata]

#data_trnsps[0]=map(int,data_trnsps[0])
#data_trnsps[1]=map(int,data_trnsps[1])
#data_trnsps[18]=map(int,data_trnsps[18])
xdata=data_trnsps[0]
for x in range(1, 13):
    kwargs1 = {'color': 'green'}
    extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}               
    chart.add_serie(name=header[0][x], y=data_trnsps[x], x=xdata, extra=extra_serie, **kwargs1)

#ydata =data_trnsps[1]
#ydata2 = data_trnsps[2]
#
#
##Configure a color for a specific serie
#kwargs1 = {'color': 'green'}
#kwargs2 = {'color': 'red'}
#
##extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"},
##               "date_format": "%d %b %Y %I:%M:%S %p"}
#               
#extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}               
#chart.add_serie(name="Jan", y=ydata, x=xdata, extra=extra_serie, **kwargs1)
#extra_serie = {"tooltip": {"y_start": "", "y_end": " calls"}}
#chart.add_serie(name="Feb", y=ydata2, x=xdata, extra=extra_serie, **kwargs1)

chart.buildcontent()

output_file.write(chart.htmlcontent)

#---------------------------------------

type = "MultiBarChart of Mean temperature of Meteorological seasons from 1880-2015, Displaying Global Warming "
chart = multiBarChart(height=350, jquery_on_ready=True,x_axis_format= '')
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
nb_element = 10

xdata=data_trnsps[0]
for x in range(13, 19):
    extra_serie = {"tooltip": {"y_start": "For year ", "y_end": " calls"}}               
    chart.add_serie(name=header[0][x], y=data_trnsps[x], x=xdata)

#xdata = list(range(nb_element))
#ydata = [random.randint(1, 10) for i in range(nb_element)]
#ydata2 = [x * 2 for x in ydata]
#
#extra_serie = {"tooltip": {"y_start": "", "y_end": " call"}}
#chart.add_serie(name="Count", y=ydata, x=xdata, extra=extra_serie)
#extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
#chart.add_serie(name="Duration", y=ydata2, x=xdata, extra=extra_serie)


chart.buildcontent()

output_file.write(chart.htmlcontent)
#---------------------------------------

html_close = """</body></html>"""
output_file.write(html_close)

#close Html file
output_file.close()