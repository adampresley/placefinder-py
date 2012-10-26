import unittest
from placefinder import PlaceFinder, InvalidSearchQueryException

KEY = "YOUR KEY"
SECRET = "YOUR SECRET"
APP_ID = "YOUR APP ID"

class PlaceFinderTests(unittest.TestCase):
	def setUp(self):
		self.placefinder = PlaceFinder(KEY, SECRET, APP_ID)

	def test_geocode_valid_freeform_returns_single_match(self):
		response, content, results = self.placefinder.geocode(q = "80 Delancey Street, New York, NY 10002")
		self.assertEqual(1, len(results), "One record was expected to match. %s match(es) came back instead." % len(results))

	def test_geocode_address_only_returns_single_match(self):
		response, content, results = self.placefinder.geocode(line1 = "Spring Street")
		self.assertEqual(1, len(results), "One record was expected to match. %s match(es) came back instead" % len(results))

	def test_geocode_invalid_address_returns_no_matches(self):
		response, content, results = self.placefinder.geocode(line1 = "9u523u4biwhbdfuwfwejb")
		self.assertEqual(0, len(results), "No records were expected to match. %s match(es) came back instead" % len(results))

	def test_geocode_invalid_search_query_raises_exception(self):
		self.assertRaises(InvalidSearchQueryException, self.placefinder.geocode)

	def test_geocode_getQualityDescription_99_returns_Coordniate(self):
		result = self.placefinder.getQualityDescription(99)
		self.assertEqual("Coordinate", result, "getQualityDescription(99) expected to return 'Coordinate'. Returned %s instead" % result)

	def test_geocode_getQualityDescription_62_returns_Airport(self):
		result = self.placefinder.getQualityDescription(62)
		self.assertEqual("Airport", result, "getQualityDescription(62) expected to return 'Airport'. Returned %s instead" % result)

	def test_geocodeFreeform_valid_address_returns_single_match(self):
		response, content, results = self.placefinder.geocodeFreeform("80 Delancey Street, New York, NY 10002")
		self.assertEqual(1, len(results), "One record was expected to match. %s match(es) came back instead." % len(results))

	def test_geocodeMultiline_valid_address_returns_single_match(self):
		response, content, results = self.placefinder.geocodeMultiline("80 Delancey Street", "New York", "NY", "10002")
		self.assertEqual(1, len(results), "One record was expected to match. %s match(es) came back instead." % len(results))

		
def suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(PlaceFinderTests))

	return suite


if __name__ == "__main__":
	unittest.main(verbosity = 2)
