from datetime import timedelta
from astronomical.services.mechanics import (
    RotationalMechanicsService,
    OrbittalMechanicsService
)


class TestRotationalMechanicsServiceClass:
    def test_calculate_axial_velocity_returns_right_value(self):
        """RBICEP: Right"""
        test_name = "Test"
        test_mass = 2
        test_radius = 3
        test_sidereal_period = timedelta(minutes=30)
        test_velocity = 0.2
        
        spinning_body = RotationalMechanicsService(test_name,
                                                   test_mass,
                                                   test_radius,
                                                   test_sidereal_period)
        
        velocity = spinning_body._calculate_axial_velocity()
        
        assert velocity == test_velocity
