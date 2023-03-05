from os import path
import pandas as pd
from coordsaccuracy_to_intervals import accuracy_to_intervals


#SCRIPT
filepath = r'C:\NSCF\Ian\GeorefToolToBODATSA' #empty string if local directory
filename = "PRE Senecio Marinda_georeferences2022-11-21T14_53_13.368Z_QDSUpdates.csv"
fieldname = 'dwc:coordinateUncertaintyInMeters'
file = path.join(filepath,filename)
df = pd.read_csv(file)
df["llRes"] = None

for index, row in df.iterrows(): 
    accuracy = row.loc[fieldname]
    
    if accuracy:
        try:
            interval = accuracy_to_intervals(accuracy)
            df.loc[index, "llRes"] = interval
        except:
            i = 0 #do nothing

newfilename = filename.replace('.csv', '_llResUpdates.csv')
df.to_csv(path.join(filepath, newfilename), index = False)