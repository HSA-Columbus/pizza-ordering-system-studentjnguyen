from flask import *
import sqlite3
import random
import pdfkit


application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        with sqlite3.connect("Order2") as conn:
            command1 = "INSERT INTO address VALUES (?, ?, ?)"
            address_list = []
            if request.form['submit_button'] == 'Submit':
                address_list.append(request.form['name'])
                address_list.append(request.form['address'])
                address_list.append(customer_id)
                conn.execute(command1, address_list)
                conn.commit()
    if request.method == "POST":
        with sqlite3.connect("Order2") as conn:
            command = "INSERT INTO orders VALUES (?, ?, ?)"
            data_list = []
            if request.form['submit_button'] == 'Add Sicilian':
                data_list.append('Sicilian')
                data_list.append(11.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Marine':
                data_list.append('Marine')
                data_list.append(11.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Mixed':
                data_list.append('Mixed')
                data_list.append(11.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Neapolitan':
                data_list.append('Neapolitan')
                data_list.append(11.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Hot Dog':
                data_list.append('Hot Dog')
                data_list.append(4.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Meatball Dog':
                data_list.append('Meatball Dog')
                data_list.append(5.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Water Dog':
                data_list.append('Water Dog')
                data_list.append(0.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Green Pepper':
                data_list.append('Green Pepper')
                data_list.append(0.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Tomato':
                data_list.append('Tomato')
                data_list.append(0.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Banana Pepper':
                data_list.append('Banana Pepper')
                data_list.append(0.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Mushroom':
                data_list.append('Mushroom')
                data_list.append(0.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
            if request.form['submit_button'] == 'Add Olive':
                data_list.append('Olive')
                data_list.append(0.99)
                data_list.append(customer_id)
                conn.execute(command, data_list)
                conn.commit()
    return render_template('home.html')


@application.route('/cart', methods=['GET', 'POST'])
def cart():
    try:
        with sqlite3.connect("Order2") as conn:
            command1 = "SELECT * FROM orders where customerID = " + str(customer_id)
            cursor1 = conn.execute(command1)
            orders_made = cursor1.fetchall()
            total = 0
            command2 = "SELECT * FROM address where customerID = " + str(customer_id)
            cursor2 = conn.execute(command2)
            address_made = cursor2.fetchall()
            for items in orders_made:
                total = total+items[1]
                totals = round(total, 2)
                print(totals)
                totals += 2.00
                total_price1 = totals
            return render_template('cart.html', orders_made=orders_made, total_price1=total_price1, address_made=address_made, customer_id=customer_id)
    except:
        return render_template('401.html')


@application.route('/orderplaced', methods=['GET', 'POST'])
def orderplaced():
    return render_template('end.html', customer_id=customer_id)


if __name__ == "__main__":
    tyler = random.randint(1, 100000)
    customer_id = tyler
    application.run(debug=True)
