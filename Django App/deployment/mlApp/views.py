from django.shortcuts import render
from .forms import form_inputs
import pickle
import xgboost as xgb
import pandas as pd
# Create your views here.
def home(request):
    return render(request, "home.html")

def predict(request):
    context = {}
    context['form'] = form_inputs()
    return render(request, "predict.html", context)

def get_result(Product,Issue,Consumer_consent_provided,Submitted_via,Company_response_to_consumer,Timely_response,Year):
    input_file = "mlApp/model_file_v1.bin" 
    with open(input_file, "rb") as in_file:
        model, dv, dmatrix = pickle.load(in_file)

    features = {}
    features['Product'] = Product
    features['Issue'] = Issue
    features['Consumer_consent_provided'] = Consumer_consent_provided
    features['Submitted_via'] = Submitted_via
    features['Company_response_to_consumer'] = Company_response_to_consumer
    features['Timely_response'] = Timely_response
    features['Year'] = Year
    
    data = dv.transform(features)
    # print("dict vectorized data", data)
    # print("dict vectorized data", type(data))

    val_data = dmatrix(data, feature_names=dv.feature_names_, enable_categorical=True)
    # print('VAL DATA', val_data)
    

    prediction = (model.predict(val_data)) >= 0.5
    # print(prediction[0])

    return prediction[0]



def result(request):
    if request.method == 'POST':
        form = form_inputs(request.POST)
        if form.is_valid():
            Product = form.cleaned_data["product_type"]
            # print("PRODUCT", Product)
            # print("PRODUCT", type(Product))

            Issue = form.cleaned_data.get("issue_type")
            Consumer_consent_provided = form.cleaned_data.get("consent_type")
            Submitted_via = form.cleaned_data.get("submitted_via")
            Company_response_to_consumer = form.cleaned_data.get("company_response")
            Timely_response = bool(form.cleaned_data.get("timely_response"))
            Year = int(form.cleaned_data.get("year"))

            result = get_result(Product,Issue,Consumer_consent_provided,Submitted_via,Company_response_to_consumer,Timely_response,Year)
            # print(result)

            
    return render(request, "result.html", {'result': result})