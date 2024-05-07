# create series with numpy array
import pandas as pd
import numpy as np
np.random.seed(1)
A = np.random.randint(1,76,4)
C = pd.Series(A)
print(C)
