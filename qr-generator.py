from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['qrdata']
        img = qrcode.make(data)
        img.save("generated_qr.png")
        return render_template('index.html', qr_generated=True)
    return render_template('index.html', qr_generated=False)

@app.route('/qr')
def qr():
    return send_file("generated_qr.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
