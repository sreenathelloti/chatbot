import pandas as pd
import numpy as np
import configparser
import UsefulFunctions

configParser = configparser.RawConfigParser()
configFilePath = r'C:\Users\Admin\Desktop\code-09-02\configfile.txt'
configParser.read(configFilePath)
data_path = configParser.get('file-config', 'data-path')
save_matrix_path = configParser.get('file-config', 'sparse-matrix-path')


#Reading Training data 
df = pd.read_csv(data_path)
question,response=UsefulFunctions.columnstoList(df)

#Datacleaning and spell check
question = UsefulFunctions.tokenization_spellcheck(question)

#Saving Tfidf matrix into disk
qmatrix = UsefulFunctions.createTfidfVectorizer(question)
np.save(save_matrix_path,qmatrix)







