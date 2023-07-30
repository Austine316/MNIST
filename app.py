from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import torch
import torch.nn.functional as F
import torchvision.transforms as transforms
import os
from datetime import datetime
from model import Net

app = Flask(__name__)


PATH = '/home/user/Documents/Hand_Written_Model_Testing/model.pt'

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Resize((28, 28)),
                                transforms.Normalize((0.5,), (0.5,))])


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        # Generate unique filename by prepending timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = timestamp + "_" + secure_filename(file.filename)

        file.save(os.path.join('static/uploads', filename))

        image = Image.open(file).convert('L')
        image = transform(image)
        image = image.unsqueeze(0)  # Add batch dimension, Batch_size, Channel, Height, Width (1, 1 28, 28)

        # instantiate the model
        model = Net()
   
        # load the state dictionary into the model
        model.load_state_dict(torch.load(PATH, map_location='cpu'))

        # switch the model to evaluation mode
        model.eval()

        with torch.no_grad():
            output = model(image)
            prob   = F.softmax(output, 1)
            probability, prediction  = torch.max(prob, 1)

        res = {'prediction': prediction.item(), 'probability': probability.item()}
        
        return render_template('index.html', result=res, filename=filename)
        
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
