#from flask import Flask, render_template, request, redirect,*
from flask import *
from files import *
from werkzeug.utils import secure_filename
import os
from werkzeug.contrib.fixers import ProxyFix
import sys
from config import config


app=Flask(__name__)
app.config['UPLOAD_FOLDER']=config['upload_folder']
app.config['MAX_CONTENT_PATH']=100000000000000000000
files = Files(100)
app.wsgi_app = ProxyFix(app.wsgi_app)
@app.route('/')
def index():
	return render_template('index.html',files=files.getFiles())

@app.route('/uploader', methods=['GET','POST'])
def uploader():
	if request.method=='POST':
		f = request.files['file']
		f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
		files.notifyUploaded(f.filename)
		return redirect("/")
		#return render_template("index.html")


@app.route('/uploads/<string:file>',methods=['GET','POST'])
def download(file):
	print("cwd: " + os.getcwd())
	upload= app.config['UPLOAD_FOLDER'] + file
	#upload=os.path.join(os.getcwd(),'/uploads/')
	#upload=os.path.join(upload,file)
	print("upload: " + upload)
	return send_file(upload)

@app.route('/ajax/files',methods=['GET','POST'])
def ajax_sendfiles():
	temp=jsonify(files.getFiles())
	print(temp)
	return temp


#api refrence
#  /ajax/ = ajax request directory
# /ajax/files get files
# response = files array

#  [
# 	{
# 		name: whatever.jpg
#		extension: icons/jpg.svg
# 	}
#	{
# 		name: whatever2.jpg
#		extension: icons/jpg.svg
# 	}
# ]
temp_args=""
if len(sys.argv)==1:
	temp_args=sys.argv[0]

if __name__ == '__main__': 
	if temp_args=="debug":
		app.debug=True
		app.run(host='0.0.0.0',port=5000,debug=True)
	else:
		app.wsgi_app = ProxyFix(app.wsgi_app)
		app.run()


	


