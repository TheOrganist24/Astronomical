# Data classes only hold data so only test that data exist and that incorrect data causes errors
# this is overkill - remove in future as only example

import pytest
import unittest
from astronomical.model import celestials

class TestBodyClass(unittest.TestCase):
    def test_when_body_is_instatiated_that_values_are_returned(self):
        test_name = "Not the Earth"
        test_mass = 2
        test_radius = 3
        
        body = celestials.Body(test_name, test_mass, test_radius)
        
        assert body.name == test_name \
            and body.mass == test_mass \
            and body.radius == test_radius

    def test_when_body_is_instatiated_without_args_that_failure(self):
        with pytest.raises(TypeError):
            body = celestials.Body()
