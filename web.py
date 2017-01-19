from flask import Flask, render_template, request
import weather2
app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get('address') # returns dict with any params passed to it (? in url)
	forecast = None # this fixes the server error you'll get by not defining forecast 1st
	if address:
		forecast = weather2.get_weather(address) # add the filename.function to call an import
	return render_template('index.html', forecast=forecast)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run()