from flask import Flask, render_template
import psycopg2


app = Flask(__name__)


DB_CONFIG = {
    'dbname': 'Fruit Baskets',
    'user': 'postgres',
    'password': 'Pokemon',
    'host': 'localhost',
    'port': '5432'
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

@app.route('/api/update_basket_a')
def update_basket_a():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO basket_a (a, fruit_a) VALUES (%s, %s)", (5, 'Cherry'))
        conn.commit()
        cur.close()
        conn.close()
        return "Success!"
    except Exception as e:
        return str(e)

@app.route('/api/unique')
def unique_fruits():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        
        cur.execute("SELECT DISTINCT fruit_a FROM basket_a")
        fruits_a = [row[0] for row in cur.fetchall()]
        
        cur.execute("SELECT DISTINCT fruit_b FROM basket_b")
        fruits_b = [row[0] for row in cur.fetchall()]
        
        cur.close()
        conn.close()
        
        
        return render_template('unique_fruits.html', fruits_a=fruits_a, fruits_b=fruits_b)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
