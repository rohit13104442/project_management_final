from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask

from sqlalchemy import create_engine,String, Table, Integer, MetaData, Column, ForeignKey,Date,TEXT
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///proj_man.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)




engine= create_engine("sqlite:///proj_man.db")
# meta = MetaData()
# employees = Table("client_partner", meta,
#
#                   Column("client_partner_id", Integer, primary_key= True),
#                   Column("cp_name", String),
#                   Column("cp_address", String),
#                   Column("cp_details", String),
#
#
#                   )
#
#
# meta.create_all(engine)