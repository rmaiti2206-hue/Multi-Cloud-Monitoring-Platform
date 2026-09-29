from datetime import datetime,timedelta,timezone
from jose import jwt
from passlib.context import CryptContext
from app.config import settings
pwd=CryptContext(schemes=['bcrypt'],deprecated='auto')
def hash_password(x):return pwd.hash(x)
def verify_password(x,h):return pwd.verify(x,h)
def create_token(sub,uid,role):return jwt.encode({'sub':sub,'uid':uid,'role':role,'exp':datetime.now(timezone.utc)+timedelta(hours=12)},settings.secret_key,algorithm='HS256')
def decode_token(t):return jwt.decode(t,settings.secret_key,algorithms=['HS256'])
