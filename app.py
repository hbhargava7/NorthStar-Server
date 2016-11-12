from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


# @app.route('/calculateRoute/', methods = ['POST'])
# def hello(): 
# 	data = request.form
# 	dataJson = request.data
# 	dataDict = json.loads(dataJson)
# 	print(data)
# 	print(dataJson)
# 	print(dataDict)
# 	return "hello world"

# print(hello())

# if __name__ == '__main__':



@app.route('/', methods = ['POST'])
def hello(): 
	data = request.form
	print(data)
	print("TEST")
	return "hello world"

app.run(
	host="0.0.0.0",
	port=int("80")
)



