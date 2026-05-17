import pandas as pd
import json
import pickle 

with open('DATA/shl_catalog.json','r') as f:            #loading the data from the json file which we fetched in the previous step
    data = json.load(f)

df = pd.DataFrame(data)                                  #converting the data into a pandas dataframe for easier manipulation and analysis
df= df.fillna(" ")

df["doc"] = df.apply( lambda row: f"""
                    Assessment Name: {row.get('name', '')}
                    Description:{row.get('description', '')}
                    Job Levels:{", ".join(row.get('job_levels', []))}
                    Languages:{", ".join(row.get('languages', []))}
                    Duration:{row.get('duration', '')}
                    Remote:{row.get('remote', '')}
                    Adaptive:{row.get('adaptive', '')}
                    Assessment Categories:{", ".join(row.get('keys', []))}
                    Assessment URL:{row.get('link', '')}""",
                    axis=1)

docs = df["doc"].tolist()
metadata = df[["name","link","desciption","job_levels","languages","duration","remote","adaptive","keys"]].to_dict(orient="records")

with open('DATA/documents.pkl',"wb") as f:
    pickle.dump(docs,f)

with open('DATA/metadata.pkl',"wb") as f:
    pickle.dump(metadata,f)

df.to_csv('DATA/shl_catalog.csv',index=False)

print("Data preprocessed and saved successfully in pickle and csv formats!")    
print(f"total documents created:{len(docs)}")

print("\nSample Document:\n")
print(docs[0])