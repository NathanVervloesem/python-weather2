from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')   # Home page
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    
    # Check for empty strings or string with only spaces
    if not bool(city.strip()):       # strip() strips aways spaces
        city = "Antwerpen"

    data = get_current_weather(city)

    # Check if city is not found
    if not data['cod'] == 200:
        return render_template("city-not-found.html")
    
    return render_template(
        "weather.html",
        title=data["name"],
        status=data["weather"][0]["description"].capitalize(),
        temp = f"{data['main']['temp']:.1f}",
        feels_like = f"{data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5001)


