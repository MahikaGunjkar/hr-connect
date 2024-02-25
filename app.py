from flask import Flask, render_template, redirect, request

app = Flask(__name__)

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
    if request.method == 'GET':
        # Access form data using request.form
        employee_satisfaction = request.form['employee_satisfaction']
        work_life_balance = request.form['work_life_balance']
        relation_with_manager = request.form['relation_with_manager']
        # ... (get other form data)
        print(employee_satisfaction, work_life_balance, relation_with_manager)
        # Process the data as needed, for example, store it in a database
        # You can also pass the data to the template if you want to display it
        return render_template('thankyou.html', employee_satisfaction=employee_satisfaction,
                               work_life_balance=work_life_balance, relation_with_manager=relation_with_manager)
    else:
        # Redirect to the home page if accessed directly without form submission
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
