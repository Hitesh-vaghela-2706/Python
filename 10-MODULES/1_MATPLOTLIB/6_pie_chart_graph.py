# pie charts

# given 1 day and working hours with work

# sleeping = 7
# eating = 2
# study = 5
# homework = 1
# wandering = 3
# relextime = 2

import matplotlib.pyplot as plt
import numpy as np

x = np.array([7,2,5,1,4,3,2]) #always first is numpy array in plt
y = np.array(['sleeping','eating','study','homework','phoneuse','wandering','relextime'])
c = np.array(['b','g','c','r','pink','orange','magenta'])
plt.pie(x,labels=y,startangle=90,shadow=True,colors=c,autopct='%1.3f%%')
plt.legend()
plt.show()