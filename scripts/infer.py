from feature_extractor import extract_features
from joblib import load
import sys, os

cwd = os.getcwd()
root_dir = "/".join(cwd.split('/')[:-1])

sys.path.append(root_dir)

# Load model and scaler object
clf = load(os.path.join(root_dir, 'models/random_forest_clf_all.joblib'))
scaler = load(os.path.join(root_dir, 'models/scaler.joblib'))

def inference(features):

    x_features = features[1:-1]
    y_label = features[-1]

    # transform features
    x_test = scaler.transform([x_features])

    # predict the class
    y_pred = clf.predict(x_test)
    
    print(f'Actual: {y_label}')

    if y_pred[0] == 0:
        print('Predicted: legitimate')
    else:
        print('Predicted: phishing')


def main():

    URL = 'http://www.malwaredomainlist.com/forums/index.php?PHPSESSID=505129431572df4552d91501d09b5767&topic=3270.msg11613#msg11613'

    # URL = 'https://uniswappro.llc/#/pages/login/index'
    STATUS = 'phishing' # legitimate, phishing

    # URL = 'https://data.mendeley.com/datasets/c2gw7fy2j4/3'

    # URL = 'https://medium.com/@lovishchopra/how-i-got-into-stanford-ms-in-cs-application-experience-tips-and-tricks-4ba1772bb9b'
    # STATUS = 'legitimate'

    features = extract_features(URL, STATUS)

    print(features)

    inference(features)


if __name__ == '__main__':
    main()


