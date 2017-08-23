from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
count = 0
@app.route('/')
def main_route():
    return render_template('index.html')

@app.route('/request-counter', methods=['GET', 'POST'])
def request_route():
    global count
    count += 1
    print(count)
    return render_template('index.html', name='count')


if __name__ == "__main__":
    app.secret_key = 'jhklpoiuztsacvadw'  # Change the content of this string
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )

