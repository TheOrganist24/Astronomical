from datetime import timedelta
import unittest

from astronomical.model.configuration import sun
from astronomical.model.mechanics import (
    RotationalMechanicsService,
    OrbittalMechanicsService
)


class TestRotationalMechanicsServiceClass(unittest.TestCase):
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


class TestOrbittalMechanicsServiceClass(unittest.TestCase):
    def test_calculate_gravitational_force_returns_right_value(self):
        """RBICEP: Right"""
        test_name = "Earth"
        test_mass = 5.972*10**24
        test_radius = 6371*10**3
        test_semimajor_axis = 149.598*10**9
        test_eccentricity = 0.014710219
        test_orbittal_obliquity = 23.44
        test_parent = sun
        test_f = 3.53*10**22
        
        orbitting_body = OrbittalMechanicsService(test_name,
                                                  test_mass,
                                                  test_radius,
                                                  test_semimajor_axis,
                                                  test_eccentricity,
                                                  test_orbittal_obliquity,
                                                  test_parent)
        f = orbitting_body._calculate_gravitational_force()
        
        assert round(f, -21) == round(test_f, -21)  # round to 2sf

    def test_calculate_orbittal_period_returns_right_value(self):
        """RBICEP: Right"""
        test_name = "Earth"
        test_mass = 5.972*10**24
        test_radius = 6371*10**3
        test_semimajor_axis = 149.598*10**9
        test_eccentricity = 0.014710219
        test_orbittal_obliquity = 23.44
        test_parent = sun
        test_T = timedelta(days=365)
        
        orbitting_body = OrbittalMechanicsService(test_name,
                                                  test_mass,
                                                  test_radius,
                                                  test_semimajor_axis,
                                                  test_eccentricity,
                                                  test_orbittal_obliquity,
                                                  test_parent)
        T = orbitting_body._calculate_orbittal_period()
        
        assert T.days == test_T.days  # round to days
