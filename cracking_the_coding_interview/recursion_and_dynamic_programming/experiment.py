# class AudioFile:
# 	def __init__(self, filename):
# 		if not filename.endswith(self.ext):
# 			raise Exception("Invalid file format")
			
# 		self.filename = filename

# class MP3File(AudioFile):
# 	ext = "mp3"

# 	def play(self):
# 		print("playing {} as mp3".format(self.filename))

# class WavFile(AudioFile):
# 	ext = "wav"
    
# 	def play(self):
# 		print("playing {} as wav".format(self.filename))


# # a = AudioFile("abc")
# b = MP3File("d.mp3")
# b.play()

# star = int(1)
# num = 4
# strstar = ("%s"%(star)) # Not in use yet

# temp = ' '

# print((temp*(num+1)),1) #worthless code used only for the "1" on top of triangle

# for x in range(0,num):
# 	print((temp*(num-x)),1,(x+1),int((x*(x+1))/2)) 
# #This piece of coding is for the triangle structure.    

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/lists', methods=['POST'])
def add_entry():
	print("p0")
	content = request.get_json()
	appname = content.get('title')
	return str(appname)
	# appname = content.get('title')

