from flask import Flask, request, redirect, url_for, render_template_string
from sqlalchemy import create_engine, Column, Integer, String, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Configuration de la base de données SQLite
engine = create_engine('sqlite:///messages.db', connect_args={'check_same_thread': False})
Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    content = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

# Template HTML
template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Message Board</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: #f0f8ff;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            background: #fff;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 20px;
        }
        .message-box {
            max-height: 300px;
            overflow-y: auto;
            margin-top: 20px;
            border-top: 1px solid #dee2e6;
            padding-top: 10px;
        }
        .message {
            background: #e9ecef;
            border: 1px solid #ced4da;
            border-radius: 4px;
            padding: 10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-4">Message Board</h1>
        <form method="post" class="d-flex">
            <input type="text" name="message" class="form-control me-2" placeholder="Votre message" required>
            <button type="submit" class="btn btn-primary">Envoyer</button>
        </form>
        <div class="message-box">
            {% for msg in messages %}
            <div class="message">
                {{ msg.content }}
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_msg = request.form.get('message')
        if new_msg:
            message = Message(content=new_msg)
            db_session.add(message)
            db_session.commit()
        return redirect(url_for('index'))
    # Récupérer les 10 derniers messages dans l'ordre décroissant
    messages = db_session.query(Message).order_by(desc(Message.id)).limit(10).all()
    return render_template_string(template, messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
