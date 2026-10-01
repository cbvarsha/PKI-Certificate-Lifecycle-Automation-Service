from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import os

app=Flask(__name__); CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL','sqlite:///pki.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Approval(db.Model):
    id=db.Column(db.Integer,primary_key=True); title=db.Column(db.String(120)); common_name=db.Column(db.String(160)); requester=db.Column(db.String(80)); environment=db.Column(db.String(40)); cert_type=db.Column(db.String(60)); status=db.Column(db.String(30),default='PENDING'); created_at=db.Column(db.DateTime,default=lambda:datetime.now(timezone.utc))
class Audit(db.Model):
    id=db.Column(db.Integer,primary_key=True); event=db.Column(db.String(80)); detail=db.Column(db.String(240)); created_at=db.Column(db.DateTime,default=lambda:datetime.now(timezone.utc))

def seed():
    db.create_all()
    if not Approval.query.first():
        db.session.add(Approval(title='Certificate Signing Request',common_name='api.payment.internal',requester='requester',environment='Production',cert_type='TLS Server'))
        db.session.commit()

@app.get('/api/health')
def health(): return jsonify(status='ok',database='online',hsm='online',jobs='healthy')
@app.get('/api/approvals')
def approvals():
    return jsonify([{'id':a.id,'title':a.title,'commonName':a.common_name,'requester':a.requester,'environment':a.environment,'type':a.cert_type,'status':a.status,'date':'24 Sep 2026, 09:14'} for a in Approval.query.order_by(Approval.id.desc()).all()])
@app.post('/api/approvals/<int:i>/<action>')
def decision(i,action):
    if action not in ('approve','reject'): return jsonify(error='invalid action'),400
    a=Approval.query.get_or_404(i); a.status='APPROVED' if action=='approve' else 'REJECTED'; db.session.add(Audit(event='REQUEST_'+a.status,detail=f'{a.common_name} {a.status.lower()} by Security Admin')); db.session.commit(); return jsonify(ok=True,status=a.status)
@app.get('/api/search')
def search():
    q=request.args.get('q','').lower(); items=['api.payment.internal','web-app.internal','batch-service','monitoring.internal','deploy-agent','TLS Server Policy v2.0','Production HSM','Azure Key Vault (Dev)']; return jsonify([x for x in items if q in x.lower()][:8])
@app.get('/api/audit')
def audit(): return jsonify([{'event':x.event,'detail':x.detail,'time':x.created_at.isoformat()} for x in Audit.query.order_by(Audit.id.desc()).limit(30)])
if __name__=='__main__':
    with app.app_context(): seed()
    app.run(host='127.0.0.1',port=8000,debug=True)
