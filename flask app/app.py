from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
# api = Api(app)  
# swagger = Swagger(app)

model_file = "model/model_file_v1.bin" 
with open(model_file, "rb") as in_file:
    model, dv, dmatrix = pickle.load(in_file)


@app.route('/', methods=["POST", "GET"])
def home():
    return render_template("index.html")

def resultPredictor(to_predict_list):

    features = {}
    features['Product'] = to_predict_list[0]
    features['Issue'] = to_predict_list[1]
    features['Consumer_consent_provided'] = to_predict_list[2]
    features['Submitted_via'] = to_predict_list[3]
    features['Company_response_to_consumer'] = to_predict_list[4]
    features['Timely_response'] = to_predict_list[5]
    features['Year'] = to_predict_list[6]

    scaled_features = dv.transform(features)

    to_predict = dmatrix(scaled_features, feature_names=dv.feature_names_, enable_categorical=True)
    # print('VAL DATA', val_data)

    prediction = (model.predict(to_predict)) >= 0.5

    return prediction[0]

@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
            
        form_data = [i for i in request.form.values()]
        prediction = resultPredictor(form_data)

    return render_template("index.html", prediction_text=prediction)

@app.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        features = request.get_json()
        scaled_features = dv.transform(features)
        to_predict = dmatrix(scaled_features, feature_names=dv.feature_names_, enable_categorical=True)
        prediction = model.predict(to_predict).round(2)
        will_dispute = (prediction >= 0.5)[0]
        print(prediction)
        print(will_dispute)
        result = {
            "dispute_probability": float(prediction),
            "will dispute": bool(will_dispute) 
        }

        return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)