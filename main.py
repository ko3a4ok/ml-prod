from flask import Flask, request
from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten, TextVectorization, \
  GlobalAveragePooling1D

vectorize_layer = TextVectorization(
    max_tokens=10000,
    output_mode='int',
    output_sequence_length=5000)
vectorize_layer._load_assets('')
model = Sequential([
    vectorize_layer,
    Embedding(50000, 128),
    GlobalAveragePooling1D(),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.load_weights('weights')

app = Flask(__name__)


@app.route('/', methods=["POST"])
def root():
  print(request.json)
  return {
      'predictions': model.predict(request.json['instances']).tolist()
  }


if __name__ == '__main__':
  app.run(host='0.0.0.0')
