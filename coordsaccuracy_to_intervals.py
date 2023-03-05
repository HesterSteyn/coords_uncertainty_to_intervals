#place accuracy in BRAHMS classes
def accuracy_to_intervals(val):
   
    if val <= 10 and val > 0:
        interval = '10m'
    elif val <= 50 and val > 10:
        interval = '50m'
    elif val <= 100 and val > 50:
        interval = '100m'
    elif val <= 250 and val > 100:
        interval = '250m'
    elif val <= 500 and val > 250:
        interval = '500m'
    elif val <= 1000 and val > 500:
        interval = '1000m'
    elif val <= 2000 and val > 1000:
        interval = '2k'
    elif val <= 5000 and val > 2000:
        interval = '5k'
    elif val <= 10000 and val > 5000:
        interval = '10k'
    elif val <= 50000 and val > 10000:
        interval = '50k'
    elif val >50000:
        interval = '100k'
        

    return interval