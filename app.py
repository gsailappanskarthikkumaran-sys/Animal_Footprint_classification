from flask import *
import os
from werkzeug.utils import secure_filename
import label_image

def load_image(image):
    text = label_image.main(image)
    return text

app = Flask(__name__)

@app.route('/first')
def first():
    return render_template('first.html')

 
  
    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result = load_image(file_path)
        result = result.title()
        d = {'Bear':" -> Detected Animal was Bear, Keep Safe", 
        'Cat':" -> Detected Animal was cat, there is No Risk",
        'Horse':" -> Detected Animal was wild Horse, Keep Safe",
        'Bongo':" -> Detected Animal was Bongo, Keep Safe",
        'Cheetah':" -> Detected Animal was Cheetah, Keep Safe",
        'Rat':"-> Detected Animal was Rat, there is No Risk",
        'Squirrel':" -> Detected Animal was Squirrel, there is No Risk",
        'Rabbit':" -> Detected Animal was Rabbit, there is No Risk",
        'Duck':" -> Detected Animal was Duck, there is No Risk",
        'Chicken':" -> Detected Animal was Chicken, there is No Risk", 
        'Cow':" -> Detected Animal was wild, Cow Keep Safe",
        'Dog':" -> Detected Animal was Hunting, Dog Keep safe",
        'Not_Found' : " -> Pleace Chack The Image"}
        result = result+d[result]
        #result2 = result+d[result]
        #result = [result]
        #result3 = d[result]        
        print(result)
        #print(result3)
        os.remove(file_path)
        return result
        #return result3
    return None 

if __name__ == '__main__':
    app.run()
