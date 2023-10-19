import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:

    dic = {"Email":[]}

    d = person.groupby(["email"]).count()
    #print(d.loc[d.id >= 2])

    dic["Email"] = list(d.loc[d.id >= 2].index)

    return pd.DataFrame(dic)



## Best runtime answer

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    d = defaultdict(int)
    for e in person["email"].values:
        d[e] += 1
    return pd.DataFrame({"Email": [k for k, v in d.items() if v > 1]})