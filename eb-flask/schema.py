from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Study(DB.Model):
    """Clinical Study data."""

    id = DB.Column(DB.Integer, primary_key=True)
    agency = DB.Column(DB.VARCHAR(100), nullable=True)
    brief_title = DB.Column(DB.VARCHAR(100), nullable=True)
    official_title = DB.Column(DB.VARCHAR(100), nullable=True)
    brief_summary = DB.Column(DB.VARCHAR(100), nullable=True)
    city = DB.Column(DB.VARCHAR(20), nullable=True)
    state = DB.Column(DB.VARCHAR(20), nullable=True)
    country = DB.Column(DB.VARCHAR(20), nullable=True)
    detailed_description = DB.Column(DB.VARCHAR(1500), nullable=True)
    eligibility = DB.Column(DB.VARCHAR(500), nullable=True)
    gender = DB.Column(DB.VARCHAR(20), nullable=True)
    condition = DB.Column(DB.VARCHAR(20), nullable=True)
    keyword = DB.Column(DB.VARCHAR(20), nullable=True)
    mesh_term = DB.Column(DB.VARCHAR(20), nullable=True)
    overall_status = DB.Column(DB.VARCHAR(20), nullable=True)
    phase = DB.Column(DB.VARCHAR(20), nullable=True)
    url = DB.Column(DB.VARCHAR(50), nullable=True)

    def __repr__(self):
        return f'<Title: {self.brief_title}>\n'
