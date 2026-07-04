from flask import Flask, request, jsonify , render_template
import pickle

app = Flask(__name__)

# Load the trained model 
crop_model = pickle.load(open('model/Crop_recom_model.pkl', 'rb'))
crop_encoder = pickle.load(open('model/crop_recom_encoder.pkl', 'rb'))
crop_scaler = pickle.load(open('model/crop_recom_scaler.pkl', 'rb'))

fertilizer_model = pickle.load(open('model/fertilizer_model.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))
le_soil = pickle.load(open('model/le_soil.pkl', 'rb'))
le_crop = pickle.load(open('model/le_crop.pkl', 'rb'))
le_target = pickle.load(open('model/le_target.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crop")
def crop():
     return render_template(
        "crop.html",)


@app.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")


@app.route("/crop_predict", methods=["POST"])
def crop_predict():
    # Get the input data from the form
    nitrogen = int(request.form["N"])
    phosphorus = int(request.form["P"])
    potassium = int(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    # Prepare the input data for prediction
    input_data = [[
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    ]]

    # Scale the input data
    input_data_scaled = crop_scaler.transform(input_data)

    # Make the prediction
    prediction = crop_model.predict(input_data_scaled)[0]

    # Decode the predicted crop label
    predicted_crop = crop_encoder.inverse_transform([prediction])[0]

    return render_template(
        "result.html",
        crop=predicted_crop
    )
 

@app.route("/fertilizer_predict", methods=["POST"])
def fertilizer_predict():

    temperature = float(request.form["temperature"])
    moisture = float(request.form["moisture"])
    rainfall = float(request.form["rainfall"])
    ph = float(request.form["ph"])
    nitrogen = float(request.form["nitrogen"])
    phosphorus = float(request.form["phosphorus"])
    potassium = float(request.form["potassium"])
    carbon = float(request.form["carbon"])

    soil = request.form["soil"]
    crop = request.form["crop"]

    # Encode categorical values
    soil = le_soil.transform([soil])[0]
    crop = le_crop.transform([crop])[0]

    # Create input
    features = [[
        temperature,
        moisture,
        rainfall,
        ph,
        nitrogen,
        phosphorus,
        potassium,
        carbon,
        soil,
        crop
    ]]

    # Scale features
    features = scaler.transform(features)

    # Predict
    prediction = fertilizer_model.predict(features)

    # Decode prediction
    fertilizer = le_target.inverse_transform(prediction)[0]

    return render_template(
        "result.html",
        fertilizer=fertilizer
    )

if __name__ == '__main__':
    app.run(debug=True)