class Location:
    """Location on the globe."""
    
    def __init__(self, name, longitude, latitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.location = (longitude, latitude)
