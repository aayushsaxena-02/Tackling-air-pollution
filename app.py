from flask import Flask,render_template,request
import pickle
app = Flask(__name__)

model = pickle.load(open('model.pk1'.'rb'))
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    print(request.form)
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.preduct_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if output > str(0.5):
        return render_template('air.html', pred = 'Your air quality is not up to the mark\n The probability of air being polluted is {}'.format(output))
    else:
        return render_template('air.html', pred = 'Your air quality is safe for breathing\n The probability of air being polluted is {}'.format(output))

if __name__ == '__main__':
    app.run()