from flask import Flask, Response, request
import requests
import io

app = Flask(__name__)

@app.route('/')
def index():
	s = requests.Session()
	cookies = {'role': 'guest'}

	output = io.StringIO()
	output.write("<html><body>")
	output.write("<h1>Welcome to Toko Cake</h1>")
	output.write("<p>Usage: Look at the code ;-)</p>")

	try:
		output.write("<p><strong>Overwriting cookies with default value! This must be secure!</strong></p>")
		cookies = {**dict(request.cookies), **cookies}
		headers = {**dict(request.headers)}

		if cookies['role'] != 'guest':
			raise Exception("Illegal access!")

		r = requests.Request("GET", "http://backend:8086/whoami", cookies=cookies, headers=headers)
		prep = r.prepare()

		output.write("<p>Prepared request cookies are: ")
		output.write(str(prep._cookies.items()))
		output.write("</p>")
		output.write("<p>Sending request...</p>")
		
		resp = s.send(prep, timeout=2.0)
		
		output.write("<p>Request cookies are: ")
		output.write(str(resp.request._cookies.items()))
		output.write("</p>")
		if 'Admin' in resp.content.decode():
			output.write("<p>Someone's drunk oO</p>")
		output.write("<p>Response is: ")
		output.write(resp.content.decode())
		output.write("</p>")
	except Exception as e:
		print(e)
		output.write("<p>Error :-/ " + str(e) + "</p>")

	output.write("</body></html>")

	return Response(output.getvalue(), mimetype='text/html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='8085', debug=False)
