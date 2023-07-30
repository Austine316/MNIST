# MNIST Handwritten Digit Classifier Web App

This web application uses a trained PyTorch model to classify uploaded images of handwritten digits.

![web](https://github.com/Austine316/MNIST/assets/77448406/6356fe15-8bc2-412b-a0c4-dd595258f3a2)




## Installation
1. Install Python 3.6 or later.

2. Clone this repository to your local machine.


```git clone https://github.com/<your-github-username>/handwritten-digit-classifier.git```

3. (Optional) Create a virtual environment.

```python3 -m venv env```

```source env/bin/activate```

4. Install the required packages.
```pip install -r requirements.txt```

## Running the App
To run the app, navigate to the repository directory and type the following command:

```python app.py```

Then, open a web browser and go to http://localhost:5000.


## Using the App

To use the app, click the "Choose File" button and select an image of a handwritten digit from your computer (test images are in the image folder in this repo). Then, click "Classify" to submit the image. The web app will display the model's classification of the digit, along with the associated probabilities.
