from flask import Flask, render_template, request

app = Flask(__name__)
user_data_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data = {
            'name': request.form.get('name'),
            'city': request.form.get('city'),
            'hobby': request.form.get('hobby'),
            'age': request.form.get('age')
        }
        user_data_list.append(user_data)
    return render_template('index.html', user_data_list=user_data_list)

if __name__ == '__main__':
    app.run(debug=True)
