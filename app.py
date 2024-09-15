from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

model = load_model('skin_disease_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    img_file = request.files['image']

    temp_file_path = "temp.jpg"
    img_file.save(temp_file_path)

    img = image.load_img('./temp.jpg', target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)

    conditions = ['Acne and Rosacea Photos', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions', 'Atopic Dermatitis Photos',
    'Bullous Disease Photos','Cellulitis Impetigo and other Bacterial Infections','Eczema Photos','Exanthems and Drug Eruptions','Hair Loss Photos Alopecia and other Hair Diseases',
    'Herpes HPV and other STDs Photos','Light Diseases and Disorders of Pigmentation','Lupus and other Connective Tissue diseases',
    'Melanoma Skin Cancer Nevi and Moles','Nail Fungus and other Nail Disease','Poison Ivy Photos and other Contact Dermatitis',
    'Psoriasis pictures Lichen Planus and related diseases','Scabies Lyme Disease and other Infestations and Bites','Seborrheic Keratoses and other Benign Tumors',
    'Systemic Disease','Tinea Ringworm Candidiasis and other Fungal Infections','Urticaria Hives','Vascular Tumors','Vasculitis Photos',
    'Warts Molluscum and other Viral Infections']
   
    return jsonify({'condition': conditions[predicted_class[0]]})
    # return jsonify({'condition': conditions[predicted_class[0]]})

if __name__ == '__main__':
    app.run(debug=True)
