!pip install kaggle

#Upload kaggle.json file
#configuring the path of kaggle.json file
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

#Importing Earthquake Dataset
#API to fetch the dataset from Kaggle
!kaggle competitions download -c LANL-Earthquake-Prediction

#Extracting the compressed dataset
from zipfile import ZipFile
dataset = '/content/LANL-Earthquake-Prediction.zip'

with ZipFile(dataset,'r') as zip:
  zip.extractall();
  print('The dataset is extracted')
