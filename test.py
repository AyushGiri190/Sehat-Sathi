from flask import Flask, render_template, request,url_for,jsonify
import os
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_choice = request.form.get("disease-history")
    if user_choice == "Yes":
        return render_template("detail2.html") 
    elif user_choice == "No":
        return render_template("carding.html")
    else:
        return render_template("index.html") 

@app.route("/brain")
def brain():
    # Add logic or content specific to page1
    return render_template("brain.html")

@app.route("/breastcancer")
def breastcancer():
    # Add logic or content specific to page1
    return render_template("breastcancer.html")


@app.route("/predict", methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'})

    image_file = request.files['image']
    #image = request.form.get('imageInput')
    print(type(image_file))
    image_bytes = image_file.read()
    filename = "up.jpg"
    # Create the uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    # Save the image to the uploads folder
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(image_path, 'wb') as f:
      f.write(image_bytes)

    print(type(image_bytes))
    print("hello")
    prediction = "hello"
    return jsonify({'prediction': prediction})
if __name__ == "__main__":
    app.run(debug=True)
