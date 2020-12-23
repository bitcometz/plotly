import pandas as pd
import plotly

# chr     start   end     gene    depth   n1      n2
# 7       193149  193384  FAM20C  143.379 0.103597        0.702483

df = pd.read_table('N008903.final.cnr.chr7')
df1 = pd.DataFrame({'id':df['chr'].map(str) + ':' + df['start'].map(str)})
df2 = pd.DataFrame({'id':df['chr'].map(str) + ':' + df['start'].map(str)})
df3 = pd.DataFrame({'id':df['chr'].map(str) + ':' + df['start'].map(str)})

df1['pos'] = df['start']
df1['depth'] = df['depth']
df2['pos'] = df['end']
df2['depth'] = df['depth']
df3['pos'] = df['end']+1
df3['depth'] = 'None'

df0 = pd.concat([df1,df2,df3])
df0.sort_values("pos",inplace=True)
df0
#df3
fig = px.line(df0, x="pos", y="depth", title='Depth coverage line')
#fig.show()
plotly.offline.plot(fig, filename='chr7.html')

