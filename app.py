from flask import render_template, request, Flask, flash, url_for, redirect
from werkzeug.utils import secure_filename
import os
import time
from predict import prediction, detect_eyes

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

			return redirect(url_for('predict_details', img=new_filename))


@app.route('/details/<img>', methods=['POST','GET'])
def predict_details(img):

	if request.method == 'GET':
		valid = detect_eyes('./static/temp/'+img)
			#print("\n\n\n", valid)
		return render_template("intermediate.html", img_src='temp/'+img, validity=valid)


	if request.method == 'POST':
		for files in os.listdir('static/temp/'):
			image = files
		return ('Yeah')
		itching = int(request.form['itching'])
		discharge = int(request.form['discharge'])
		pain_blur_eye = int(request.form['pain_blur'])

		pink_eye = prediction(image, itching, discharge, pain_blur_eye)
#		print("\n\n\n\n", type(pink_eye))
#		print(request.form['itching'])

		return render_template('output.html', img_src='temp/'+image, result=pink_eye)


if __name__ == "__main__":
	app.run(threaded=False)
