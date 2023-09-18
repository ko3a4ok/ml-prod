# Model training
The model training can be found in the file `commonlitreadabilityprize.ipynb`
The training process stores some artifacts: model weights and dictionary for the vectorization layer.

# Inference
Code is in file `main.py`.
It's a web server that runs the prediction.
To run it:
```
python main.py
```

To test it, run from the command line:
```
curl -H "Content-Type: application/json" -d '{"instances": [ "Hello world" ]}' -X POST http://localhost:5000
```
