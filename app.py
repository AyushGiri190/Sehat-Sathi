from flask import Flask, render_template, request,url_for,jsonify
import os
import autenticate as at
from chest_cancer import chest
from brain_tumor import brain_tumor
from Breast_cancer import breast_cancer as breast
from Skin_cancer import skin
import symptom as s


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/login',methods=["GET","POST"])
def login():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    print(email,password)
  # Process the registration data (e.g., store in database, send confirmation email)
    #return render_template('index.html',mesage="Please enter the correct crediantials")  
    
    if name =="":
        if at.signin(email,password):
            return render_template('card.html')
           
        else:
            return render_template('index.html',mesage="Please enter the correct crediantials")
    else :
        if at.check_mail(email):
             return render_template('index.html',mesage="Crediantials already exist")
        else:
            return render_template('card.html')
    

@app.route("/home",methods=["GET","POST"])
def home():
    return render_template('card.html')

@app.route("/symp",methods=["GET","POST"])
def symp():
    return render_template('symptom.html')


@app.route("/brain_tumour",methods=["GET","POST"])
def brain_tumour():
    return render_template('braintumour.html')


@app.route("/breast_cancer",methods=["GET","POST"])
def breast_cancer():
    return render_template('breastcancer.html')


@app.route("/lung_cancer",methods=["GET","POST"])
def lung_cancer():
    return render_template('lungcancer.html')

@app.route("/skin_cancer",methods=["GET","POST"])
def skin_cancer():
    return render_template('skincancer.html')

@app.route("/symptom",methods=["GET","POST"])
def symptom():
    if request.method == 'POST':
        symptoms = request.form.get('symptoms')
        # mysysms = request.form.get('mysysms')
        # print(mysysms)
        print(symptoms)
        if symptoms =="Symptoms":
            message = "Please either write symptoms or you have written misspelled symptoms"
            return render_template('symptom.html', message=message)
        else:
            # Split the user's input into a list of symptoms (assuming they are comma-separated)
            
            user_symptoms = [s.strip() for s in symptoms.split(',')]
            
            # Remove any extra characters, if any

            user_symptoms = [symptom.strip("[]' ") for symptom in user_symptoms]
            
            predicted_disease = s.get_predicted_value(user_symptoms)
            dis_des, precautions, medications, rec_diet, workout = s.helper(predicted_disease)

            my_precautions = []
            for i in precautions[0]:
                my_precautions.append(i)

            return render_template('symptom.html', predicted_disease=predicted_disease, dis_des=dis_des,
                                   my_precautions=my_precautions, medications=medications, my_diet=rec_diet,
                                   workout=workout)

    return render_template('symptom.html')


@app.route("/predictbrain",methods=["GET","POST"])
def predictbrain():
    image_file = request.files['image']
    if(image_file):
        im = image_file.read()
        with open("saved_image1.png", "wb") as f:
            f.write(im)
        predicted = brain_tumor('./saved_image1.png')
        
        if(predicted=="Tumour"):
            extra = """Environmental hazards
                    Avoid smoking, excessive radiation exposure, pesticides, insecticides, and carcinogenic chemicals. Limit exposure to chemicals in your living and working spaces, and ensure proper ventilation.
                    Lifestyle
                    Maintain a healthy weight through a balanced diet and regular exercise. Avoid processed foods and sugars, limit alcohol consumption, and reduce stress levels. Get adequate sleep, and use hands-free devices and reduce screen time.
                    Family history
                    If you have a first-degree biological relative who has been diagnosed with a brain tumor, it's important to tell your healthcare provider."""
        else:
            extra='''
Looks like you are free from brain tumor. Nonetheless, maintaining brain health involves various proactive measures. A balanced diet rich in antioxidants, omega-3 fatty acids, and vitamins supports overall brain function and may reduce the risk of tumors. Regular physical activity promotes blood flow to the brain, potentially lowering the risk of certain brain conditions. Avoiding tobacco and excessive alcohol consumption is crucial, as they may increase the risk of brain tumors. Regular cognitive stimulation, such as puzzles or learning new skills, helps maintain brain health and function. Additionally, practicing good sleep hygiene and managing stress effectively contribute to overall brain health. While there are no guarantees, adopting these lifestyle habits may help reduce the risk of brain tumors and promote long-term well-being.'''
        return jsonify({'prediction':predicted ,'extra':extra})
    else:
        
        return jsonify({'error': 'No image uploaded'}), 400


@app.route("/predictbreast",methods=["GET","POST"])
def predictbreast():
    image_file = request.files['image']
    if(image_file):
        im = image_file.read()
        with open("saved_image2.png", "wb") as f:
            f.write(im)
        predicted = breast('./saved_image2.png')
        print(predicted)
        if(predicted=="normal"):
            extra='''
Looks like you are free from breast cancer. However, maintaining breast health involves several proactive measures. A diet abundant in fruits, vegetables, and lean proteins, coupled with limited processed foods, aids in overall well-being and potentially lowers breast cancer risk. Regular physical activity, such as brisk walking or cycling, for at least 150 minutes per week helps maintain a healthy weight, crucial for reducing breast cancer risk. Moderating alcohol intake and avoiding tobacco products are paramount, as they significantly impact breast cancer risk. Self-exams and regular screenings, including mammograms as recommended by healthcare providers, facilitate early detection and treatment if necessary. Effective stress management through mindfulness practices and sufficient sleep, along with good hygiene habits, further contribute to breast health. Staying informed about risk factors and proactive in lifestyle choices empowers individuals in reducing the risk of breast cancer and promoting long-term well-being.'''
        else:
            extra='''Limit or stay away from alcohol. It's safest not to drink alcohol. But if you do drink it, enjoy it in moderation. The more alcohol you have, the greater your risk of getting breast cancer. In general, women should have no more than one drink a day. Even small amounts raise the risk of breast cancer. One drink is about 12 ounces of beer, 5 ounces of wine, or 1.5 ounces of 80-proof distilled spirits.
Stay at a healthy weight. Ask a member of your health care team whether your weight is healthy. If it is, work to maintain that weight. If you need to lose weight, ask your health care professional how to do so. Simple steps may help. Watch your portion sizes. Try to eat fewer calories. And slowly build up the amount of exercise you do.
Get active. Physical activity can help you stay at a healthy weight, which helps prevent breast cancer. So try to move more and sit less. Most healthy adults should aim for at least 150 minutes a week of moderate aerobic exercise. Or try to get at least 75 minutes of vigorous aerobic exercise a week. Aerobic exercise gets your heart pumping. Some examples are walking, biking, running and swimming. Also aim to do strength training at least twice a week.
Breastfeed. If you have a baby, breastfeeding might play a role in helping prevent breast cancer. The longer you breastfeed, the greater the protective effect.'''
        
        return jsonify({'prediction':predicted,'extra':extra})
    else:
        
        return jsonify({'error': 'No image uploaded'}), 400


@app.route("/predictchest",methods=["GET","POST"])
def predictchest():
    image_file = request.files['image']
    if(image_file):
        im = image_file.read()
        with open("saved_image3.png", "wb") as f:
            f.write(im)
        predicted = chest('./saved_image3.png')
        print(predicted)
        if(predicted=="Normal"):
            extra='''
Looks like you are free from lung cancer. However, maintaining lung health involves several proactive measures. Avoiding tobacco products and minimizing exposure to secondhand smoke are paramount, as they are the leading causes of lung cancer. Additionally, reducing exposure to environmental pollutants and chemicals can further lower the risk. Regular physical activity supports lung function and overall health, while a balanced diet rich in fruits, vegetables, and antioxidants may help protect against lung cancer. Regular screenings for individuals at high risk, such as current or former smokers, can aid in early detection and treatment if necessary. Effective stress management, sufficient sleep, and good hygiene habits also contribute to lung health. By staying informed and proactive in lifestyle choices, individuals can reduce the risk of lung cancer and promote long-term well-being.'''
        else:
            extra='''Don’t smoke. Cigarette smoking causes about 80% to 90% of lung cancer deaths in the United States. The most important thing you can do to prevent lung cancer is to not start smoking, or to quit if you smoke.
Avoid secondhand smoke. Smoke from other people’s cigarettes, cigars, or pipes is called secondhand smoke. Make your home and car smoke-free.
Limiting exposure to radon is another prevention strategy. Surprisingly, exposure to radon is the second most common cause of lung cancer in the nation, after smoking. Radon comes from the ground and can seep into groundwater and into homes, through cracks in the foundation.'''
        return jsonify({'prediction':predicted,'extra':extra})
                       
    else:
        
        return jsonify({'error': 'No image uploaded'}), 400


@app.route("/predictskin",methods=["GET","POST"])
def predictskin():
    image_file = request.files['image']
    if(image_file):
        im = image_file.read()
        with open("saved_image4.png", "wb") as f:
            f.write(im)
        predicted = skin('./saved_image4.png')
        print(predicted)
      
        extra = '''Avoid the sun between 10 a.m. and 4 p.m., which are the peak hours of sun strength in North America, even in the winter and on cloudy days.
Wear sunscreen — at least sun protection factor (SPF) 30 — throughout the entire year. Reapply sunscreen every two hours or more frequently if you're swimming or sweating.
Wear sun-protective clothing with ultraviolet protection factor (UPF) of 50+, which blocks 98% of the sun's rays. Hats with wide brims and sun-protective clothing that covers your arms and legs are helpful to protect your skin from harmful UV damage. Sunscreen doesn't block all UV rays, which cause skin cancer.
Avoid tanning beds. Tanning beds operate with UV lights, damaging your skin and potentially leading to cancer.
Self-check your skin. If you notice differences, talk with your health care team.'''
        return jsonify({'prediction':predicted,'extra':extra})
                        
    else:
        
        return jsonify({'error': 'No image uploaded'}), 400


if __name__=='__main__':
    app.run(debug=True)