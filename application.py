from flask import *
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import datetime
import boto3


def contact_customer(list, customerid, total_price):
    email = "imnotarobotlol1234@gmail.com"
    password = "imnotarobot"
    send_to_email = "imnotarobotlol1234@gmail.com"
    subject = 'Thank you for ordering! Your Customer ID: {}'.format(customerid)
    string = ""
    date = datetime.datetime.today()
    for i in list:
        string += """<tr style="color: black">"""
        for x in i:
            string += """<th style="color: black; border: 2px solid black; text-align: center; padding: 8px;">""" + str(x) + "</th>"
        string += "</tr>"
    table = """<table style="border-collapse: collapse; width: 100%">
    <tr style="color: black">
        <th style="color: black; border: 2px solid black; text-align: center; padding: 8px;">Items</th>
        <th style="color: black; border: 2px solid black; text-align: center; padding: 8px;">Total Prices</th>
        <th style="color: black; border: 2px solid black; text-align: center; padding: 8px;">Customer ID</th>
    </tr>
    {}
    <tr style="color: black">
        <th style="color: black; border: 2px solid black; text-align: center; padding: 8px;">Delivery Charge</th>
        <th style="color: black; border: 2px solid black; text-align: center; padding: 8px;">2.00</th>
        <th style="color: black; border: 2px solid black; text-align: center; padding: 8px;">{}</th>
    </tr>
    <tr style="color: black">
        <th style="color: black; border: 2px solid black; text-align: center; padding: 8px;">Total Price:</th>
        <th style="color: black; border: 2px solid black; text-align: center; padding: 8px;">{}</th>
    </tr>
</table>""".format(string, customerid, total_price)
    message = """<html>
    <head></head>
    <body>
    <h3 style="color: black">Date: {}</h3>
    <h3 style="color: black">Your Receipt:</h3>
    {}
    <br>
    <h4 style="color: black">Approximate Delivery Time: 30-60 min</h4>
    </body>
    </html>""".format(date, table)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'html'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
        return 1
    except:
        return render_template('404.html')


application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        with sqlite3.connect("Order2") as conn:
            command1 = "INSERT INTO address VALUES (?, ?, ?, ?)"
            address_list = []
            if request.form['submit_button'] == 'Submit':
                address_list.append(request.form['name'])
                address_list.append(request.form['address'])
                address_list.append(request.form['phone'])
                address_list.append(customer_id)
                conn.execute(command1, address_list)
                conn.commit()
                return render_template('home.html')
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
                conn.echazchxecute(command, data_list)
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
    return render_template('home.html')


@application.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == "POST":
        with sqlite3.connect("Order2") as conn:
            command3 = "DELETE FROM orders where customerID = " + str(customer_id)
            conn.execute(command3)
            conn.commit()
        return render_template('home.html')
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
    with sqlite3.connect("Order2") as conn:
        command1 = "SELECT * FROM orders where customerID = " + str(customer_id)
        cursor1 = conn.execute(command1)
        orders_made = cursor1.fetchall()
        total = 0
        for items in orders_made:
            total = total + items[1]
            totals = round(total, 2)
            print(totals)
            totals += 2.00
            total_price1 = totals
    if request.method == "POST":
        result = contact_customer(orders_made, customer_id, total_price1)
        if result == 1:
            client = boto3.client(
                "sns",
                aws_access_key_id="ASIAWUAF4F6SH3ATK4XE",
                aws_secret_access_key="RFJ05j2wrVAI9sBcGXWUFAlRJ8zHsmXC+nVTn8Cw",
                aws_session_token="FwoGZXIvYXdzECAaDKsgQxwQcy6yqPlC7CLTAZcLFE6KJ2FAroX5ZA+WqWHdL9nXST74I3V1fphtqNfmzXRhW59PlqbbGL+largIUn0bly/FxwXIaotoSx1FKeDCx+7+eiPq3LYvtfA/NSgXC0I1ilYHp4bW3UsF0aXnQmaKGkyK/qfmvhWkkbmJAyjzu8q95zDtCfQRGk4ua199xmv2mxzmN7VniPHImp8PoWKSpLQ0A5crteJaQNLYb+RQsv3m6sKbQWRn8Hg350KiC3RJvxje64dkdXv/hN+GrSw0Kgp0mIEL81CimaSqj5pP4uwogb7k8gUyLQ4b0JDxZqUBqjon+Pme81jkXO/XJiGoAKXyAn2Xbi5w4bq0sstUrtSFyLCXXg==",
                region_name="us-east-1"
            )

            client.publish(
                PhoneNumber="16142865517",
                Message="Thank you for ordering! Your customer id: 1337 Approximate Delivery Time: 30-60 minutes"
            )
            with sqlite3.connect("Order2") as conn:
                command3 = "DELETE FROM orders where customerID = " + str(customer_id)
                conn.execute(command3)
                conn.commit()
            return render_template('orderplaced.html', customer_id=customer_id, result="Your order has been placed!", customer_message="Your Customer ID is: ")
        elif result == 0:
            return render_template('orderplaced.html', customer_id=customer_id, result="There was an error, please reorder.")
    else:
        return render_template('end.html', orders_made=orders_made, total_price1=total_price1, customer_id=customer_id)


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    tyler = random.randint(1, 100000)
    customer_id = tyler
    application.run(debug=True)
