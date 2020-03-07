from flask import render_template, request, Flask, flash, url_for, redirect
from werkzeug.utils import secure_filename
import os
import time
from predict import prediction, detect_eyes
import sys

UPLOAD_FOLDER = './static/temp'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
IMAGE_FILE = ''

# App definition
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST','GET'])
def predict():

	if request.method == 'GET':
		return render_template("index.html")

	if request.method == 'POST':


		if 'imageUpload' not in request.files:
			#flash('No file part')
			return redirect(request.url)

		file = request.files['imageUpload']

		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':

			#print("YES")
			return redirect(request.url)

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)

			for files in os.listdir('static/temp/'):
				os.remove('static/temp/' + files)

			new_filename = "temp" + str(time.time()) + '.jpg'

			file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))

			pink_eye = prediction(new_filename, 1, 0, 0)

			print("yes")

			print("again")

			print(pink_eye)

			return ("yesyyys")

			#return redirect(url_for('predict_details', img=new_filename))



if __name__ == "__main__":
	app.run(threaded=False)
