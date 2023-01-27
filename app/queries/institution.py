from config.database import db_session
from models import Institution
from schemas.institution import InstitutionFullGetSchema


@db_session
def add_institution(db, institution: Institution) -> Institution:
    db.add(institution)
    db.commit()
    db.refresh(institution)
    return institution


@db_session
def get_all_institutions(db):
    return db.query(Institution).all()


@db_session
def get_institution_by_id(db, _id: int, is_dump: bool = False):
    institution = db.query(Institution).filter(Institution.id == _id).one()

    if is_dump:
        schema = InstitutionFullGetSchema()
        institution = schema.dump(institution)

    return institution


@db_session
def update_institution(db, _id: int, institution: Institution):
    institution.id = _id
    db.merge(institution)
    db.commit()


@db_session
def delete_product(db, _id: int):
    db.query(Institution).filter(Institution.id == _id).delete()
    db.commit()
    db.flush()
