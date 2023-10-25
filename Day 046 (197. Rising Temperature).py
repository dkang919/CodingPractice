import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    
    dic = {"id":[]}
    ptemp = 99999
    weather.sort_values(["recordDate"], inplace=True)
    if len(weather) == 0:
        return weather[["id"]]

    count = 0
    for rdate in weather.index:
        ctemp = weather[weather.recordDate==rdate]["temperature"]
        if count == 0:
            pass
        
        elif str(rdate - pdate)[0] == "1":
            
            if ctemp > ptemp:
                dic["id"].append(weather[weather.recordDate==rdate].index)
        
        pdate = rdate
        ptemp = ctemp

    return pd.DataFrame(dic)



### BEST ANSWER

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')
    return weather[(weather.temperature.diff()>0) & (weather.recordDate.diff().dt.days==1)][['id']]