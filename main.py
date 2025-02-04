from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"


pipe = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def mainfuction():
    if request.method=='POST':
        if "file" not in request.files:
            return "No file uploaded", 400

        file = request.files['file']

        if file.filename == "":
            return "No file selected", 400

        if file:
            filepath=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            #read file content
            with open(filepath, "r", encoding="utf-8") as f:
                email_text = f.read()
          

            prediction = pipe.predict([email_text])[0]

            return render_template('show.html', prediction=prediction, email_content=email_text)

    else:
        return render_template('index.html')





if __name__ == '__main__':
    if not os.path.exists("uploads"): # create a folder if it doesn't exist
        os.mkdir("uploads")
    app.run(debug=True)