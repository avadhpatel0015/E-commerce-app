from sqlalchemy.orm import Session
from models.user import User
from schemas.users import UserCreate, UserUpdate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        role=user.role,
        shop_ids=user.shop_ids
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.userId == user_id).first()


def update_user(db: Session, user_id: str, user: UserUpdate):
    db_user = db.query(User).filter(User.userId == user_id).first()
    if not db_user:
        return None

    update_data = user.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: str):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return True
