from flask import Flask
import subprocess
from datetime import datetime
import pytz
import getpass  # ✅ safer than os.getlogin()

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        username = getpass.getuser()  # ✅ use this instead of os.getlogin()
        ist = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
        top_lines = '\n'.join(top_output.splitlines()[:10])
        
        return f"""
        <h1>HTOP Status Page</h1>
        <p><b>Name:</b> Rahul Pradhan</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {current_time}</p>
        <pre>{top_lines}</pre>
        """
    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
