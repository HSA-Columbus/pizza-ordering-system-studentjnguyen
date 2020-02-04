from flask import *
import sqlite3
application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        with sqlite3.connect("Order2") as conn:
            command = "INSERT INTO orders VALUES (?, ?)"
            data_list = []
            if request.form['submit_button'] == 'Add Sicilian':
                data_list.append('Sicilian')
                data_list.append('11.99')
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Marine':
                data_list.append('Marine')
                data_list.append('11.99')
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Mixed':
                data_list.append('Mixed')
                data_list.append('11.99')
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Napoliten':
                data_list.append('Napoliten')
                data_list.append('11.99')
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Hot Dog':
                data_list.append('Hot Dog')
                data_list.append('4.99')
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Meatball Dog':
                data_list.append('Meatball Dog')
                data_list.append('5.99')
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Water Dog':
                data_list.append('Water Dog')
                data_list.append('0.99')
                conn.execute(command, data_list)
                conn.commit()
    return render_template('home.html')


@application.route('/cart', methods=['GET', 'POST'])
def cart():
    with sqlite3.connect("Order2") as conn:
        command1 = "SELECT * FROM orders"
        cursor1 = conn.execute(command1)
        orders_made = cursor1.fetchall()
    if request.form['jeremiah'] == 'Place order':
    return render_template('cart.html', orders_made=orders_made)


if __name__ == "__main__":
    application.run(debug=True)
