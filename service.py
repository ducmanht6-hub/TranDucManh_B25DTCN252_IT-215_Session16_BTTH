from sqlalchemy.orm import Session
import model
import schema

def create_fleet(db: Session, fleet: schema.FleetCreate):
    new_fleet = model.Fleet(**fleet.model_dump())
    db.add(new_fleet)
    db.commit()
    db.refresh(new_fleet)
    return new_fleet


def get_all_fleets(db: Session):
    return db.query(model.Fleet).all()

def create_driver(db: Session, driver: schema.DriverCreate):
    new_driver = model.Driver(**driver.model_dump())
    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)
    return new_driver


def get_all_drivers(db: Session):
    return db.query(model.Driver).all()

def create_car(db: Session, car: schema.CarCreate):
    new_car = model.Car(**car.model_dump())
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car


def get_all_cars(db: Session):
    return db.query(model.Car).all()

def create_booking(db: Session, booking: schema.BookingCreate):
    new_booking = model.Booking(**booking.model_dump())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

def get_all_bookings(db: Session):
    return db.query(model.Booking).all()
