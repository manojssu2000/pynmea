import unittest

from pynmea.utils import checksum_calc

class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_checksum_calc(self):
        nmea_str1 = 'GPGLL,3751.65,S,14507.36,E'
        nmea_str2 = '$GPGLL,3751.65,S,14507.36,E'
        nmea_str3 = 'GPGLL,3751.65,S,14507.36,E*77'
        nmea_str4 = '$GPGLL,3751.65,S,14507.36,E*77'
        nmea_str5 = '$GPGLL,3751.65,S,14507.36,E*'
        nmea_str6 = 'GPGLL,3751.65,S,14507.36,E*'
        nmea_str7 = '$GPHDT,227.66,T*02'

        result1 = checksum_calc(nmea_str1)
        result2 = checksum_calc(nmea_str2)
        result3 = checksum_calc(nmea_str3)
        result4 = checksum_calc(nmea_str4)
        result5 = checksum_calc(nmea_str5)
        result6 = checksum_calc(nmea_str6)
        result7 = checksum_calc(nmea_str7)

        self.assertEquals(result1, '77')
        self.assertEquals(result2, '77')
        self.assertEquals(result3, '77')
        self.assertEquals(result4, '77')
        self.assertEquals(result5, '77')
        self.assertEquals(result6, '77')
        self.assertEquals(result7, '02')

    def test_lat_nmea_to_deg(self):
        """ Test conversion from nmea formatted latitudes to degrees
        """
        self.assertTrue(False)

    def test_lat_deg_to_nmea(self):
        """ Test conversion from degrees to nmea formatted latitudes
        """
        self.assertTrue(False)

    def test_lon_nmea_to_deg(self):
        """ Test conversion from nmea formatted longitudes to degrees
        """
        self.assertTrue(False)

    def test_lon_deg_to_nmea(self):
        """ Test conversion from degrees to nmea formatted longitudes
        """
        self.assertTrue(False)
