import os
from os.path import basename
from config import config
import json
import sys
import time
import flask
from werkzeug.utils import secure_filename
from PIL import Image
class Files:

	
	image_extensions=['bmp','eps','icns','ico','im','jpeg','jpg'
		'msp','pcx','ppm','png','sgi','spi','tga','tiff','webp','xbm']


	def is_extension(self,temp_ext):
		ret=False
		for i in range(0,len(self.extensions)):
			if self.extensions[i]==temp_ext:
				ret=True
		return ret
	def __init__(self,num):
		tempfiles=os.listdir(config['upload_folder'])
		self.extensions=[]
		self.files=[]
		temp_files=[]
		temp_extensions=os.listdir("static/file_type_icons")
		for i in range(0,len(temp_extensions)):
			temp = temp_extensions[i].split('.svg')
			self.extensions.append(temp[0])


		for i in range(0,len(tempfiles)):
			temp_file_name=tempfiles[i]
			#temp=tempfiles[i].split('.')
			if(temp_file_name!='files.json'):
				extension=self.return_extension(tempfiles[i])
				t_file={"name":temp_file_name, "thumbnail":"static/file_type_icons/"+ extension + ".svg","time":time.time(),
						"location":temp_file_name}
				t_file=self.gen_thumbnail(t_file)
				temp_files.append(t_file)
			#self.files.append({"name":temp_file_name, "extension":extension})
		self.files=temp_files

		#open json

		#file json at uploads/files.json
		try:
			file=open(config['upload_folder']+"files.json","r")
			file_contents=""
			while(0==0):
				temp_content=file.read(1)
				if temp_content !='':
					file_contents+=temp_content
				else:
					file.close()
					break
			# reading json
			json_files=[]
			try:
				json_files=json.loads(file_contents)
			except: 
				sys.exit("ERROR:  JSON files object tampered with")
			self.files=self.compare_files(temp_files,json_files)

		except:
			print("files.json not found")
			file=open(config['upload_folder']+"files.json","w")
			file.write(json.dumps(temp_files))


		#print("files: " + str(self.files))

	def getFiles(self):
		return self.files
	def notifyUploaded(self,file_name,file_saved):
		tempext=self.return_extension(file_name)
		
		tempfile={"name":file_name, "time":time.time(),
			"location":file_saved}
		tempfile=self.gen_thumbnail(tempfile)
		# setting files database
		self.files.append(tempfile)
	def return_extension(self,filename):
		temp=filename.split('.')
		if(self.is_extension(temp[1])):
			return temp[1]
		else:
			return "quest"


		#compares real files with json files and returns json with real files
	def compare_files(self,real_files,json_files):
		for i in range(0,len(real_files)):
			if i<len(json_files):
				if real_files[i]['name']==json_files[i]['name']:
					real_files[i]=json_files[i]
				else:
					real_files[i]['time']==time.time()
			else:
				real_files[i]['time']==time.time()
				break


		#print("TBA"
		return real_files
	def save_file(self,request,n):
		f = request.files['file']
		if(f.filename!='files.json'):
			filename=secure_filename(str(n) + f.filename)
			if(os.path.isfile(config["upload_folder"] + filename)):
				self.save_file(request,n+1)
			else:
				filename=str(n)+filename
				f.save(os.path.join(config['upload_folder'],secure_filename(filename)))
				self.notifyUploaded(f.filename,filename)
	def gen_thumbnail(self,file):
		#returns directory of thumbnail 
		# Note file has to be saved first
		extension=self.return_extension(file['name'])
		img_name=os.path.splitext(file['name'])
		#img_name=config["upload_folder"] + img_name[0]
		img_name=img_name[0]
		print("img_name: " + img_name)
		thumbnail="static/file_type_icons/" + extension + ".svg"
		file['thumbnail']=thumbnail
		print("thumbnail_generated")

	
		for i in self.image_extensions:

			print("i: " + i+ "	extension:" + extension)
			if extension==i:
				print("file['location']:   " + file['location'])
				image=Image.open(config['upload_folder']+
					file['location'])

				image.thumbnail(config['thumbnail_size'])
				thumbnail=self.save_thumbnail(image,img_name,0)
				file['thumbnail']=thumbnail
				print("exported image")
		return file


	def save_thumbnail(self,image,name,n):
		thumbnail_path=""
		thumbnail_name=""
		if os.path.isfile(config['thumbnail_folder']+str(n) +name + ".jpg"):
			thumbnail_name = self.save_thumbnail(image,name,n+1)
		else:
			image = image.convert('RGB')
			thumbnail_path=config['thumbnail_folder']+str(n) + name + ".jpg"
			image.save(thumbnail_path)
			thumbnail_name="thumbnails/" + str(n) + name + ".jpg"
		print("thumbnail name:"+ thumbnail_name)
		print("thumbnail path:"+ thumbnail_path)

		return thumbnail_name