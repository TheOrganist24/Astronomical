from datetime import timedelta
from astronomical.services.physics import (angular_velocity,
    angular_velocity,
    a_sin_theta,
    gravitational_force,
    law_of_orbits_aphelion,
    law_of_orbits_perihelion,
    law_of_orbits,
    law_of_periods
)

class TestAngularVelocity:
    def test_angular_velocity_returns_right_value(self):
        test_period = timedelta(minutes=12)
        test_velocity = 0.5
        
        velocity = angular_velocity(test_period)
        
        assert velocity == test_velocity
