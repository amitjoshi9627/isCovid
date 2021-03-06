# isCovid
### By Amit Joshi
isCovid is a Deep Learning model which predicts COVID-19 based on chest X-ray.

<img src="src/img/screeneshot1.jpg?raw=true" width="1000">
<img src="src/img/screenshot2.jpg?raw=true" width="1000">

### How to Run:
1. Install necessary modules with `sudo pip3 install -r requirements.txt` command.
2. Go to __src__ folder (if you want to change paths of files and folders, go to _**src/config.py**_).
3. Run `python3 train.py` to train and save the machine learning model.
4. To run this app from **Streamlit**. Run `streamlit run streamlitapp.py`.
5. Upload your X-ray Image or you can upload the sample images provided (__data/val/__) and then check the result.

### Data
Covid-19 chest X-ray images can be downloaded from [here](https://github.com/ieee8023/covid-chestxray-dataset) and Normal chest X-ray images can be downloaded from [here](https://www.qmenta.com/covid-19-kaggle-chest-x-ray-normal/)

> Web App was made using [__Streamlit__](https://www.streamlit.io/)

__Please Give a :star2: if you :+1: it.__
