# by using this method we able to give own indexes and also able to
# put some NAN values like bellow...
import pandas as pd
A = {

"hin"  :{
            "0":40,
            "1":50,
            "2":60,
            "3":70,
            "4":80
        } ,

"eng"  :{   "0":41,
            "1":51,
            "2":61,
            "3":71,
            "4":81
        } ,

"guj"  :{   "0":42,
            "1":52,
            "2":62,
            "3":72,
            "4":82
        } ,

"san"  :{   "0":43,
            "1":53,
            "3":73,
            "4":83
        }

}
B = pd.DataFrame(A)
print(B)