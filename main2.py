import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models.widgets import Tabs, Panel
import requests
import os

# Membaca dataset dari Covid_19.csv
df = pd.read_csv('Covid_19.csv', parse_dates=['Date'])

# Untuk menyimpan baris-baris tiap index di variabel jabar, jatim dan jateng
# ini tuh buat bikin garis2 buat grafiknya, jadi ntar di grafiknya ada 3 baris
# yaitu jabar, jatim dan jateng
jabar = df[df.Location == 'Jawa Barat']
jatim = df[df.Location == 'Jawa Timur']
jateng = df[df.Location == 'Jawa Tengah']

# Untuk menampilkan source data jabar, jatim, jateng
# ColumnDataSource adalah DataFrame versi Bokeh
source_jabar = ColumnDataSource(data=jabar)
source_jatim = ColumnDataSource(data=jatim)
source_jateng = ColumnDataSource(data=jateng)

source_jabar1 = ColumnDataSource(data=jabar)
source_jatim1 = ColumnDataSource(data=jatim)
source_jateng1 = ColumnDataSource(data=jateng)

source_jabar2 = ColumnDataSource(data=jabar)
source_jatim2 = ColumnDataSource(data=jatim)
source_jateng2 = ColumnDataSource(data=jateng)

# Membuat Figure untuk menampilkan New Cases
# ini untuk buat figure nya alias buat gambarnya atau visualisasinya
fig1 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='New Cases',
    title='New Cases',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot New Cases dari Jabar
a = fig1.line(
    x='Date',
    y='New Cases',
    source=source_jabar2,
    color='blue',
    legend_label='Jawa Barat'
)

# Untuk menampilkan line plot New Cases dari Jatim
b = fig1.line(
    x='Date',
    y='New Cases',
    source=source_jatim2,
    color='red',
    legend_label='Jawa Timur'
)

# Untuk menampilkan line plot New Cases dari Jateng
c = fig1.line(
    x='Date',
    y='New Cases',
    source=source_jateng2,
    color='yellow',
    legend_label='Jawa Tengah'
)

# Bokeh Library
tooltips = [
            ('Index','@Location'), # ini index isinya nama lokasi
            ('New Cases', '@{New Cases}{f}') # ini New Cases isinya jumlah/angka yg ada di kolom new cases
                                             # maksud dari {f} itu untuk format angka nya
                                             # kalo {f} nya dihapus ntar gakan keluar angkanya
]

# Menambahkan HoverTool untuk membuat fig
# ini HoverTool dari library bokeh
# HoverTool digunakan untuk menampilkan data saat kita mengarahkan penunjuk mouse ke titik plot
fig1.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Membuat Figure untuk menampilkan New Deaths
fig2 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='New Deaths',
    title='New Deaths',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot New Deaths dari Jabar
a = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_jabar2,
    color='blue',
    legend_label='Jawa Barat'
)

# Untuk menampilkan line plot New Deaths dari Jatim
b = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_jatim2,
    color='red',
    legend_label='Jawa Timur'
)

# Untuk menampilkan line plot New Deaths dari Jateng
c = fig2.line(
    x='Date',
    y='New Deaths',
    source=source_jateng2,
    color='yellow',
    legend_label='Jawa Tengah'
)

# Bokeh Library
tooltips = [
            ('Index','@Location'),
            ('New Deaths', '@{New Deaths}{f}') #ini penjelasannya udah ya diatas
]

# Menambahkan HoverTool untuk membuat fig
# ini juga sama kaya yg diatas
fig2.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Membuat Figure untuk menampilkan Total Active Cases
fig3 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Total Active Cases',
    title='Total Active Cases',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot Total Active Cases dari Jabar
a = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_jabar2,
    color='blue',
    legend_label='Jawa Barat'
)

# Untuk menampilkan line plot Total Active Cases dari Jatim
b = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_jatim2,
    color='red',
    legend_label='Jawa Timur'
)

# Untuk menampilkan line plot Total Active Cases dari Jateng
c = fig3.line(
    x='Date',
    y='Total Active Cases',
    source=source_jateng2,
    color='yellow',
    legend_label='Jawa Tengah'
)

# Bokeh Library
tooltips = [
            ('Index','@Location'), # ini penjelasannya udah ada diatas juga
            ('Total Active Cases', '@{Total Active Cases}{f}')
]

# Menambahkan HoverTool untuk membuat fig
# ini juga udah ada diatas
fig3.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Menampilkan ke plot HTML
# jadi ini kita build aplikasi ke web kan? nah kita build ke html jadi ntar 
# outputnya bakalan kebuka versi html
output_file('StatistikCovid.html', title='Statistik Covid')

# ini menambahkan aspek interaktif yang memungkinkan user untuk menyembunyikan data untuk indeks tertentu
# jadi ntar kan dipojok kanan atas kan ada tuh keterangan jawa barat, jawa tengah, jawa timur
# nah kalo diklik salah satunya itu ntar jadinya bakalan hilang garis grafiknya
# silahkan dicoba aja ya
fig1.legend.click_policy = 'hide'
fig2.legend.click_policy = 'hide'
fig3.legend.click_policy = 'hide'

# Membuat tiga panel yaitu New Cases, New Deaths, Total Active Cases
# ini buat panel beserta tabs yang diatas ya
New_Cases = Panel(
    child=fig1,
    title='New Cases'
)
New_Deaths = Panel(
    child=fig2,
    title='New Deaths'
)
Total_Active_Cases = Panel(
    child=fig3,
    title='Total Active Cases'
)

tabs = Tabs(tabs=[
                  New_Cases, New_Deaths, Total_Active_Cases
                ])

show(tabs)

# jadi kita tuh punya 2 fitur interaktif 
# yang pertama yaitu 3 panel untuk memilih parameter yang ingin dibuka (New Cases, New Deaths, Total Active Cases)
# yang kedua yaitu user dapat menyembunyikan data untuk indeks tertentu dengan mengklik legend index 
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})