import pandas as pd

data = pd.DataFrame({'frontage':[20,23,42],'width':[21,22,24]})

data['area'] = data['frontage'] * data['width']

print(data)