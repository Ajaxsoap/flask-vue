from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/portfolio')
def portfolio():
  return render_template('portfolio.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/test')
def test():
  my_dict = {
    "myJSON" :
      {
        "mainTitle": "This are my portfolio",
        "portfolioTitle": "Portfolio",
        "aboutTitle": "About",
        "contactTitle": "Contact"
      }
    }
  return json.dumps(my_dict)

if __name__ == "__main__":
  print("The server is running on localhost")
  app.run(debug=True)