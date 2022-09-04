# webpage-phishing-detection
Machine Learning based spam website detection

--------------------------------------------

### Dataset

- **Mendeley Data:** [Web page phishing detection](https://data.mendeley.com/datasets/c2gw7fy2j4/3)
- **Kaggle:** [Dataset](https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset)

--------------------------------------------

### Installation

- Install [python3.10.4](https://www.python.org/downloads/release/python-3104/)
- Create environment
```
python3 -m venv phishing
source phishing/bin/activate
```
- Install packages
```
pip install -r requirements_full.txt
```
For heroku, use [requirements.txt](/requirements.txt) 

---------------------------------------------

### Run

- Check [infer.py](/scripts/infer.py) 

```
cd scripts
python infer.py
```

- Streamlit [app](/app.py)
```
streamlit run app.py
```

----------------------------------------------

### ML Part

- [main.ipynb](/main.ipynb) contains machine learning model generation and analysis code

----------------------------------------------

### Feature extraction

Feature extractor code is available [here](https://data.mendeley.com/datasets/c2gw7fy2j4/3), however some files are missing which included in this repository.

> In order to run [Feature extractor](/scripts/feature_extractor.py), some part of the code is commented and modified compare to the original work by author of the [paper](10.1016/j.engappai.2021.104347).

----------------------------------------------

### Citation

Hannousse, Abdelhakim; Yahiouche, Salima (2021), “[Web page phishing detection](https://data.mendeley.com/datasets/c2gw7fy2j4/3)”, Mendeley Data, V3, doi: 10.17632/c2gw7fy2j4.3

Thank you Abdelhakim Hannousse for your help.




