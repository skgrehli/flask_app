import os
from app import app

# app seems to break without following, consider adding ', debug=True' after 'port=port'
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)