import matplotlib as plt
import pandas as pd
import OpenBlender
import json

#data 
action = 'API_getObservationsFromDataset'
      
parameters = { 
        'token':'5ec160ba9516291bc83ffd36pxpx4duSekHkWh10f0s92I3Oi960bF',
	    'id_user':'5ec160ba9516291bc83ffd36',
	    'id_dataset':'5e7a0d5d9516296cb86c6263',
        'drop_features':["lat","long","province_state"],
        'filter_select':{'feature':'country_region', 'values':['Brazil', 'Canada', 'United States']},
	    'consumption_confirmation':'on',
	    'date_filter':{"start_date":"2020-04-15T05:00:00.000Z","end_date":"2020-05-17"},
	    'add_time':{"treatment":"date"} 
}
        
df_data = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df_data.reset_index(drop=True, inplace=True)
df_data.head()
print(df_data.head())