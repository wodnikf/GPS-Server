from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'USER',
    'password': 'PASSWORD TO DATABASE',
    'database': 'NAME OF DATABASE'
}

@app.route('/NAME OF DATABASE', methods=['POST'])
def gps_data():
    data = request.json
    timestamp = data.get('timestamp')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    altitude = data.get('altitude')
    satellites = data.get('satellites')
    speed_kmh = data.get('speed_kmh')
    fix_quality = data.get('fix_quality')

    if not latitude or not longitude:
        return jsonify({'error': 'Invalid data'}), 400

    try:
        conn = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database'],
    ssl_disabled=True 
)

        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO gps_coordinates 
            (timestamp, latitude, longitude, altitude, satellites, speed_kmh, fix_quality) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (timestamp, latitude, longitude, altitude, satellites, speed_kmh, fix_quality)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Data saved successfully'}), 200
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({'error': 'Database error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)