# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['pdf.fonttype'] = 42

font1 = dict(family='Kaiti', color='darkred', weight='normal', size=16)

ts = pd.read_csv('1.csv', index_col=0, parse_dates=True)

plt.figure(figsize=[10, 12])

ts1 = ts[(ts['ITEMID'] == 3411) & (ts['STATIONID'] == 370222)]
ax = plt.subplot(411)
ts1['OBSVALUE'].plot()
ax.set_title('邹城地电场', fontdict=font1)

plt.subplot(412)
ts1['OBSVALUE'].plot.kde()

plt.subplot(413)
ts1 = ts[(ts['ITEMID'] == 3411) & (ts['STATIONID'] == 370271)]
ts1['OBSVALUE'].plot()
ax.set_title('邹城地电场', fontdict=font1)

plt.subplot(414)
ts1['OBSVALUE'].plot.kde()

plt.subplots_adjust(hspace=0.6)
plt.savefig('1.pdf')
