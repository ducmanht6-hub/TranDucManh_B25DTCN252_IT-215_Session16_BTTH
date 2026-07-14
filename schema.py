from pydantic import BaseModel

class FleetCreate(BaseModel):
    name: str

class FleetResponse(FleetCreate):
    id: int

    class Config:
        from_attributes = True

class DriverCreate(BaseModel):
    full_name: str
    status: str
    fleet_id: int


class DriverResponse(DriverCreate):
    id: int

    class Config:
        from_attributes = True

class CarCreate(BaseModel):
    license_plate: str
    status: str


class CarResponse(CarCreate):
    id: int

    class Config:
        from_attributes = True

class BookingCreate(BaseModel):
    driver_id: int
    car_id: int


class BookingResponse(BookingCreate):
    id: int

    class Config:
        from_attributes = True
