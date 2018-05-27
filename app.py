# 

from flask import Flask, render_template, request
import os

app = Flask(__name__)
hash_id = 1

def go_hash(hash):
	global hash_id
	f = open('hash/%d.hash'%hash_id,'w')
	f.write(hash)
	f.close()
	hash_id += 1
	return

def go_crack(id,format):
	os.system('hashcat -a 3 -m 0 --outfile-format 3 -o out/%d.out --potfile-disable hash/%d.hash %s' % (hash_id,hash_id,format))
	return

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/post', methods=['GET','POST'])
def pass_post():
	if request.method == 'GET':
		return render_template('post.html')
	else:
		my_hash = request.form['hash']
		my_format = request.form['format']
		print(my_hash,my_format)
		global hash_id
		go_hash(my_hash)
		go_crack(hash_id,my_format)
		# go_post(hash_id)
		return '''
		<script>alert('POST success');window.location.href='/';</script> '''

if __name__ == '__main__':
	app.run()