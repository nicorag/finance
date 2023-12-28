#----------------------------------------------------------------------------#
def gap(start,end):

  '''

  Install yfinance
  Date Format YYYY-MM-DD
  USD_CCL with GGAL y GGAL.BA
  Definition of global variable: ccl_ggal

  '''
  global ccl_ggal
##Import Packages##
  import pandas as pd 
  import yfinance as yf
  import matplotlib.pyplot as plt
  ###################
  name= 'GGAL'
  ggal_p=yf.download(name+'.BA',start=start, end=end)
  ggal_usd=yf.download(name,start=start, end=end)

#Change the date forma
  ggal_p.index=ggal_p.index.strftime('%Y-%m-%d') 
  ggal_usd.index=ggal_usd.index.strftime('%Y-%m-%d') 


  ccl_ggal= 10*ggal_p['Close']/ggal_usd['Close']
  ccl_ggal=ccl_ggal.dropna()
  usdars=yf.download('ARS=X',start=start, end=end)

  usdars.index=usdars.index.strftime('%Y-%m-%d') 
  print('#-----------------------------------------#')
  print('   GAP USD_CCL/USDARS using ' +name+'   ')
  print('#-----------------------------------------#')

  brecha=100*(ccl_ggal-usdars['Close'])/usdars['Close']
  brecha=brecha.dropna()
  brecha=pd.DataFrame(brecha)
  brecha.set_index(brecha.index)
  brecha.index=pd.to_datetime(brecha.index)


  fig, axs = plt.subplots( figsize=(20,10))
  plt.axes().set_facecolor('silver')
  plt.plot(brecha.index.values, brecha,color='black',linestyle='-')
  plt.hlines([50,80,100,120,150],brecha.index[0],brecha.index[-1],color='red',linestyle='-',linewidth=1) 
#ticks in x-axis each six month
  plt.xticks(rotation=45)
  axs.set_xticks(brecha.index[0:-1:180])
  plt.grid(True)
  plt.ylabel('% USD_CCL/USDARS')
  plt.xlabel('Date')
#----------------------------------------------------------------------------#
gap?
!pip install investpy
!pip install yfinance
#----------------------------------------------------------------------------#
start1='2019-01-01'
end1='2022-10-28'
gap(start1,end1)
#----------------------------------------------------------------------------#
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
IMV_P=yf.download('M.BA',start=start1,end=end1)
IMV_P.index=IMV_P.index.strftime('%Y-%m-%d') 

IMV_USD=(IMV_P['Close']/ccl_ggal).dropna()
IMV_USD.index=pd.to_datetime(IMV_USD.index)


fig, axs = plt.subplots( figsize=(20,10))
plt.axes().set_facecolor('silver')
plt.plot(IMV_USD.index.values[IMV_USD.index!='2022-07-14'], IMV_USD[IMV_USD.index!='2022-07-14'],color='black',linestyle='-')
#ticks in x-axis each six month
plt.xticks(rotation=45)
axs.set_xticks(IMV_USD.index[0:-1:180])
plt.grid(True)
plt.ylabel('IMV (USD_CCL)')
plt.xlabel('Date')
#----------------------------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt

ccl_ggal.index=pd.to_datetime(ccl_ggal.index)

correlation=np.zeros(len(ccl_ggal)-19)
for i in range(20,len(ccl_ggal)):
  correlation[i-20]=IMV_USD[i-20:i].corr(ccl_ggal[i-20:i])



plt.figure(figsize=(15,5))
plt.plot(ccl_ggal.index.values[0:len(correlation)],correlation,'k.')

print('#'*50)
print('The mean between '+start1+' and '+end1+' is:')
print(round(np.mean(correlation),2))
print('#'*50)

plt.savefig('correlation.png')
