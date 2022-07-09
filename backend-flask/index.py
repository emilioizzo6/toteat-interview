from flask import Flask, jsonify, request
from flask_cors import CORS
import functions as fs

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/general-data", methods=["GET"])
def load_data():
    mean_table_time, mean_table_bill, mean_table_diners, categories, products, waiters, zones = fs.means()
    return jsonify({ 'mtt': mean_table_time, 'mtb': mean_table_bill, 'mtd': mean_table_diners, 'categories': categories, 'products': products, 'waiters': waiters, 'zones': zones})

@app.route("/waiter-info")
def waiter_info():
    waiter = request.args.get('name')
    total_orders, total_billing = fs.waiter_info(waiter)
    return jsonify({ 'total_orders': total_orders, 'total_billing': total_billing})

@app.route("/zone-info")
def zone_info():
    zone = request.args.get('zone')
    mean_billing, mean_time = fs.zone_info(zone)
    return jsonify({ 'mean_billing': mean_billing, 'mean_time': mean_time})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)