from python_ask_service.backend import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    answer_text = db.Column(db.Text)

    def __repr__(self):
        return f'<Question {self.id}: {self.question_text}>'
