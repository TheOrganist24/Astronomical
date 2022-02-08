from datetime import timedelta
import unittest
from astronomical.model.custom_types import (
  real_time
)
from astronomical.model.physics import (
    angular_velocity,
    a_sin_theta,
    gravitational_force,
    law_of_orbits,
    law_of_periods,
    right_ascension,
    declination,
    equatorial_coordinates,
    solar_hour_angle,
    altitude,
    azimuth,
    elevation
)


class TestAngularVelocity(unittest.TestCase):
    def test_angular_velocity_returns_right_value(self):
        """RBICEP: Right"""
        test_period = timedelta(minutes=12)
        test_velocity = 0.5
        
        velocity = angular_velocity(test_period)
        
        assert velocity == test_velocity


class TestASinThetaVelocity(unittest.TestCase):
    def test_asintheta_returns_right_value(self):
        """RBICEP: Right"""
        test_a = 1
        test_theta = 0.25
        test_magnitude = test_a
        
        magnitude = a_sin_theta(test_a, test_theta)
        
        assert magnitude == test_magnitude


class TestGravitationalForce(unittest.TestCase):
    def test_gravitational_force_returns_right_value(self):
        """RBICEP: Right"""
        test_M = 5.972*10**24
        test_m = 100
        test_r = 6371*10**3
        test_f = 981
        
        f = gravitational_force(test_M, test_m, test_r)
        
        assert int(f) == int(test_f)  # round to integers


class TestLawOfOrbits(unittest.TestCase):
    def test_law_of_orbits_returns_right_value(self):
        """RBICEP: Right"""
        test_a = 2
        test_e = 0.1
        test_R_aphelion = 2.2
        test_R_perihelion = 1.8
        
        R_aphelion, R_perihelion = law_of_orbits(test_a, test_e)
        
        assert R_aphelion == test_R_aphelion \
            and R_perihelion == test_R_perihelion


class TestLawOfPeriods(unittest.TestCase):
    def test_law_of_periods_returns_right_value(self):
        """RBICEP: Right"""
        test_M = 1.989*10**30
        test_m = 5.972*10**24
        test_a = 149.598*10**9
        test_T = timedelta(days=365)
        
        T = law_of_periods(test_M, test_m, test_a)
        
        assert T.days == test_T.days  # round to days


class TestEquatorialCoordinates(unittest.TestCase):
    def test_right_ascension_returns_right_value(self):
        """RBICEP: Right"""
        test_angle_from_vernal_equinox = timedelta(days=100, hours=16)
        test_synodic_day = timedelta(hours=30)
        test_ra = timedelta(hours=16)
        
        ra = right_ascension(test_angle_from_vernal_equinox,
                             test_synodic_day)
                             
        assert ra == test_ra

    def test_declination_returns_right_value(self):
        """RBICEP: Right"""
        test_angle_from_vernal_equinox = timedelta(days=100, hours=16)
        test_synodic_day = timedelta(hours=30)
        test_ra = timedelta(hours=16)
        test_orbittal_obliquity = 45.0
        test_sidereal_period = timedelta(days=4)
        test_time_since_march_equinox = timedelta(days=3)
        test_dec = -45.0
        
        dec = declination(test_orbittal_obliquity,
                          test_sidereal_period,
                          test_time_since_march_equinox)
                             
        assert dec == test_dec

    def test_equatorial_coordinates_returns_right_value(self):
        """RBICEP: Right"""
        test_angle_from_vernal_equinox = timedelta(days=100, hours=16)
        test_synodic_day = timedelta(hours=30)
        test_ra = timedelta(hours=16)
        test_orbittal_obliquity = 45.0
        test_sidereal_period = timedelta(days=4)
        test_time_since_march_equinox = timedelta(days=3)
        test_dec = -45.0
        
        ra, dec = equatorial_coordinates(test_angle_from_vernal_equinox,
                                         test_synodic_day,
                                         test_orbittal_obliquity,
                                         test_sidereal_period,
                                         test_time_since_march_equinox)
                             
        assert ra == test_ra \
            and dec == test_dec


class TestSolarHourAngle(unittest.TestCase):
    def test_solar_hour_angle_returns_right_value(self):
        """RBICEP: Right"""
        test_synodic_day = real_time(hours=24)
        test_time_since_midnight = timedelta(hours=13)
        test_sha: float = 15.0
        
        sha = solar_hour_angle(test_synodic_day,
                                            test_time_since_midnight)
        
        assert sha == test_sha


class TestElevationCoordinates(unittest.TestCase):
    def test_altitude_returns_right_value(self):
        """RBICEP: Right"""
        test_latitude = 45.0
        test_declination = 20.0
        test_hour_angle = 0.0
        test_alt = 65
        
        alt = altitude(test_latitude,
        	       test_declination,
        	       test_hour_angle)
                             
        assert int(alt) == int(test_alt)

    def test_azimuth_returns_right_value(self):
        """RBICEP: Right"""
        test_latitude = 45.0
        test_declination = 20.0
        test_hour_angle = 0.0
        test_altitude = 65
        test_az = 180
        
        az = azimuth(test_latitude,
        	      test_declination,
        	      test_hour_angle,
        	      test_altitude)
                             
        assert int(az) == int(test_az)

    def test_elevation_returns_right_value(self):
        """RBICEP: Right"""
        test_latitude = 45.0
        test_declination = 20.0
        test_hour_angle = 0.0
        test_azimuth = 180
        test_altitude = 65
        
        azimuth, altitude = elevation(test_latitude,
        				test_declination,
        				test_hour_angle)
                             
        assert int(azimuth) == int(test_azimuth) \
            and int(altitude) == int(test_altitude)
