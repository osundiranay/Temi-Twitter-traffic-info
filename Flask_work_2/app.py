from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/send', methods=['GET', 'POST'])
def send():
  if request.method == 'POST':
    print(request.form)
    location = request.form['location']

    return render_template('location.html', location=location)

  return render_template('index.html')

if __name__ == "__main__":
  app.run()
