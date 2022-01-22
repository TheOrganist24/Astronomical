from datetime import timedelta
from astronomical.model.physics import (
    angular_velocity,
    a_sin_theta,
    gravitational_force,
    law_of_orbits,
    law_of_periods,
    right_ascension
)


class TestAngularVelocity:
    def test_angular_velocity_returns_right_value(self):
        """RBICEP: Right"""
        test_period = timedelta(minutes=12)
        test_velocity = 0.5
        
        velocity = angular_velocity(test_period)
        
        assert velocity == test_velocity


class TestASinThetaVelocity:
    def test_asintheta_returns_right_value(self):
        """RBICEP: Right"""
        test_a = 1
        test_theta = 0.25
        test_magnitude = test_a
        
        magnitude = a_sin_theta(test_a, test_theta)
        
        assert magnitude == test_magnitude


class TestGravitationalForce:
    def test_gravitational_force_returns_right_value(self):
        """RBICEP: Right"""
        test_M = 5.972*10**24
        test_m = 100
        test_r = 6371*10**3
        test_f = 981
        
        f = gravitational_force(test_M, test_m, test_r)
        
        assert int(f) == int(test_f)  # round to integers


class TestLawOfOrbits:
    def test_law_of_orbits_returns_right_value(self):
        """RBICEP: Right"""
        test_a = 2
        test_e = 0.1
        test_R_aphelion = 2.2
        test_R_perihelion = 1.8
        
        R_aphelion, R_perihelion = law_of_orbits(test_a, test_e)
        
        assert R_aphelion == test_R_aphelion \
            and R_perihelion == test_R_perihelion


class TestLawOfPeriods:
    def test_law_of_periods_returns_right_value(self):
        """RBICEP: Right"""
        test_M = 1.989*10**30
        test_m = 5.972*10**24
        test_a = 149.598*10**9
        test_T = timedelta(days=365)
        
        T = law_of_periods(test_M, test_m, test_a)
        
        assert T.days == test_T.days  # round to days


class TestEquatorialCoordinates:
    def test_right_ascension_returns_right_value(self):
        """RBICEP: Right"""
        test_angle_from_vernal_equinox = timedelta(days=100, hours=16)
        test_synodic_day = timedelta(hours=30)
        test_ra = timedelta(hours=16)
        
        ra = right_ascension(test_angle_from_vernal_equinox,
                             test_synodic_day)
                             
        assert ra == test_ra
