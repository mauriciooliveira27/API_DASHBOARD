from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class QueryDB:

    def __repr__(self) -> str:

        return f'{ self.id}'

    @classmethod
    def get_last_record_by_id(cls):
        return cls.query.order_by(db.desc(cls.id)).first()




class DashBoard(db.Model, QueryDB):

    __tablename__ = 'dash'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    tensao = db.Column(db.Float(), nullable = True)
    tensao_f1 = db.Column(db.Float(), nullable = True)
    tensao_f2 = db.Column(db.Float(), nullable = True)
    tensao_f3 = db.Column(db.Float(), nullable = True)
    corrente = db.Column(db.Float(), nullable = True) 
    corrente_f1 = db.Column(db.Float(), nullable = True) 
    corrente_f2 = db.Column(db.Float(), nullable = True)
    potencia_ativa = db.Column(db.Float(), nullable = True)
    potencia_ativa_f1 = db.Column(db.Float(), nullable = True)
    potencia_ativa_f2 = db.Column(db.Float(), nullable = True)
    potencia_ativa_f3 = db.Column(db.Float(), nullable = True)
    potencia_reativa = db.Column(db.Float(), nullable = True)
    potencia_reativa_f1 = db.Column(db.Float(), nullable = True)
    potencia_reativa_f2 = db.Column(db.Float(), nullable = True)
    potencia_reativa_f3 = db.Column(db.Float(), nullable = True)
    potencia_aparente = db.Column(db.Float(), nullable = True)
    potencia_aparente_f1 = db.Column(db.Float(), nullable = True)
    potencia_aparente_f2 = db.Column(db.Float(), nullable = True)
    potencia_aparente_f3 = db.Column(db.Float(), nullable = True)
    fp_circuito = db.Column(db.Float(), nullable = True)
    fP_fase1 = db.Column(db.Float(), nullable = True)
    fP_fase2 = db.Column(db.Float(), nullable = True)
    fP_fase3 = db.Column(db.Float(), nullable = True)
    frequencia = db.Column(db.Float(), nullable = True)
    data = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)


class Calculate:
    ...