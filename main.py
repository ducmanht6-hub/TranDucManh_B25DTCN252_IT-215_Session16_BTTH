from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, get_db
from model import Base
import schema
import service

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ride Booking API")


@app.get("/")
def home():
    return {"message": "Ride Booking API is running"}


# Fleet
@app.post("/fleets", response_model=schema.FleetResponse)
def create_fleet(fleet: schema.FleetCreate, db: Session = Depends(get_db)):
    return service.create_fleet(db, fleet)


@app.get("/fleets", response_model=list[schema.FleetResponse])
def get_fleets(db: Session = Depends(get_db)):
    return service.get_all_fleets(db)


# Driver
@app.post("/drivers", response_model=schema.DriverResponse)
def create_driver(driver: schema.DriverCreate, db: Session = Depends(get_db)):
    return service.create_driver(db, driver)


@app.get("/drivers", response_model=list[schema.DriverResponse])
def get_drivers(db: Session = Depends(get_db)):
    return service.get_all_drivers(db)


# Car
@app.post("/cars", response_model=schema.CarResponse)
def create_car(car: schema.CarCreate, db: Session = Depends(get_db)):
    return service.create_car(db, car)


@app.get("/cars", response_model=list[schema.CarResponse])
def get_cars(db: Session = Depends(get_db)):
    return service.get_all_cars(db)


# Booking
@app.post("/bookings", response_model=schema.BookingResponse)
def create_booking(booking: schema.BookingCreate, db: Session = Depends(get_db)):
    return service.create_booking(db, booking)


@app.get("/bookings", response_model=list[schema.BookingResponse])
def get_bookings(db: Session = Depends(get_db)):
    return service.get_all_bookings(db)
