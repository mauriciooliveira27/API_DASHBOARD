from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Query:
    ...

class DashBoard(db.Model, Query):
    id = db.Column(db.Integer, primary_key = True, auto_increment = True)
    tensao = db.Column(db.Float(), nullable = False)
    tensao_f1 = db.Column(db.Float(), nullable = False)
    tensao_f2 = db.Column(db.Float(), nullable = False)
    tensao_f3 = db.Column(db.Float(), nullable = False)
    corrente = db.Column(db.Float(), nullable = False) 
    corrente_f1 = db.Column(db.Float(), nullable = False) 
    corrente_f2 = db.Column(db.Float(), nullable = False)
    potencia_ativa = db.Column(db.Float(), nullable = False)
    potencia_ativa_f1 = db.Column(db.Float(), nullable = False)
    potencia_ativa_f2 = db.Column(db.Float(), nullable = False)
    potencia_ativa_f3 = db.Column(db.Float(), nullable = False)
    potencia_reativa = db.Column(db.Float(), nullable = False)
    potencia_reativa_f1 = db.Column(db.Float(), nullable = False)
    potencia_reativa_f2 = db.Column(db.Float(), nullable = False)
    potencia_reativa_f3 = db.Column(db.Float(), nullable = False)
    potencia_aparente = db.Column(db.Float(), nullable = False)
    potencia_aparente_f1 = db.Column(db.Float(), nullable = False)
    potencia_aparente_f2 = db.Column(db.Float(), nullable = False)
    potencia_aparente_f3 = db.Column(db.Float(), nullable = False)
    fp_circuito = db.Column(db.Float(), nullable = False)
    fP_fase1 = db.Column(db.Float(), nullable = False)
    fP_fase2 = db.Column(db.Float(), nullable = False)
    fP_fase3 = db.Column(db.Float(), nullable = False)
    frequencia = db.Column(db.Float(), nullable = False)
    data = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class Calculate:
    ...