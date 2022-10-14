import sys

# conda install -c conda-forge pandas
import pandas as pd

# conda install -c anaconda numpy
import numpy as np

import spacy
nlp = spacy.load("en_core_web_lg")


# Load boxoffice file
df_boxoffice = pd.read_csv('/datagrid/1/ktb/app/project/linkimdb/boxoffice_ex.csv',sep=",",low_memory=False)

# Load tconst id from 
dfcon = pd.read_csv('/datagrid/1/ktb/app/project/linkimdb/tconst_list.csv',sep=",",low_memory=False)

dlist = d_fboxoffice['title'].tolist()
grosslist = df_boxoffice['lifetime_gross'].tolist()
cc=0
tid=0
ntid=20
taskid=int(sys.argv[1])
#print(taskid)
dlsize = len(dlist)
if taskid > ntid:
	print("Error Check taskid!!")
	exit (1)

cci = 0	
for i in dlist:

	if tid != taskid:
		tid += 1
		if tid >= ntid:
			tid=0
		cci += 1
		continue
	else:
		pass

	ch=i[0]
	#print(i[0])
	d=int(len(i)*30/100)
	if d == 1:
		d=int(len(i)*50/100)

	gross=grosslist[cci]
	cci += 1
	ii = i[0:d]
	
    regex = f'{ii}.*'
	dd = dfcon.loc[(dfcon['originalTitle'].str.match(regex)),:]
	nn = dd['originalTitle'].count()
	doc1 = nlp(i)
	for j in range(nn):
		ff = dd['originalTitle'].iloc[j]
		doc2 = nlp(ff)
		percent = doc1.similarity(doc2)

		if percent >0.96:
			tc = dd['tconst'].iloc[j]
			if percent ==1.0:
				print(f"{cc}/{dlsize},{i}|{ff}|{percent}|{tc}|{gross}")
				break
			elif percent > 1.0:
				pass
			else:
				print(f"{cc}/{dlsize},{i}|{ff}|{percent}|{tc}|{gross}")
 



	tid += 1
	if tid >= ntid:
		tid=0
	
	cc += 1
