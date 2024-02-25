from flask import Flask, render_template, redirect, request
import psycopg2
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(
        host="org-hrconnect-inst-textbook.data-1.use1.tembo.io",
        database="postgres",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    return conn

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('login.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Process the form data here if needed
        return redirect('/thankyou')  # Redirect to the thank you page after processing

    return render_template('employee_form.html')

@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    if request.method == 'POST':
        # Access form data using request.form
        employee_satisfaction = request.form['employee_satisfaction']
        work_life_balance = request.form['work_life_balance']
        relation_with_manager = request.form['relation_with_manager']
        eff = request.form['eff']
        personal_interests = request.form['personal_interests']
        # ... (get other form data)
        print(employee_satisfaction, work_life_balance, relation_with_manager)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        # Process the data as needed, for example, store it in a database
        # You can also pass the data to the template if you want to display it
        return render_template('thankyou.html')
    else:
        # Redirect to the home page if accessed directly without form submission
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
