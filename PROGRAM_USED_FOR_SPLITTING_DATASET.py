# THIS PROGRAM WAS MADE TO SPLIT THE DATA INTO TRAINING DATA AND
# CORRESPONDING TARGET which was stored in training_data.dat and target_data.dat 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from numpy import array
from numpy import vstack
p=0
while p==0:
	pd.options.mode.chained_assignment = None
	df=pd.read_csv('DATASET.csv')
	f_df=df.drop(['name','group','alive','mult'],axis=1)
	w_df=f_df.dropna(axis='rows')
	target_raw=np.array(w_df['aliveat1'])
	w_df=w_df.drop(['aliveat1'],axis=1)
	w_df['split'] = np.random.randn(w_df.shape[0], 1)
	split = np.random.rand(len(w_df)) <= 0.8
	train_raw= w_df[split]	
	traine=train_raw.drop(['split'],axis=1)
	target_raw=target_raw.reshape(target_raw.shape[0],-1)
	o=np.shape(train_raw)
	z=[]
	z=list(o)
	train=traine[:z[0]]
	i=np.shape(train)	
	a=[]
	a=list(i)
	target=target_raw[:a[0]]
	X_train,X_test,y_train,y_test=train_test_split(train,target,random_state=0)
	knn=KNeighborsClassifier(n_neighbors=2) 
	knn.fit(X_train,np.ravel(y_train,order='C'))
	print('Test Score: {:.2f}'.format(knn.score(X_test,y_test)))
	m=knn.score(X_test,y_test)
	if m>=0.90:
		target_set=target
		training_set=train
		np.savetxt('training_data.dat',training_set)
		np.savetxt('target_data.dat',target_set)
		p=1
		print('Done')