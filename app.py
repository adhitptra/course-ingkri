import requests

# URL model di Google Cloud Storage
model_url = 'https://storage.googleapis.com/submissionmlgc-adhitya/model.json'

# Nama file lokal tempat Anda menyimpan model
local_model_path = 'model.json'

# Unduh model dari URL dan simpan sebagai file lokal
response = requests.get(model_url)
with open(local_model_path, 'wb') as f:
    f.write(response.content)

print("Model downloaded successfully")

# Sekarang muat model menggunakan TensorFlow
model = tf.keras.models.load_model(local_model_path)
print("Model loaded successfully")
