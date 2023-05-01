import json
import os
import unittest
from jsonschema import validate, ValidationError


class TestEventsConfig(unittest.TestCase):
    def setUp(self):
        # Load the JSON schema
        with open(os.path.join(os.path.dirname(__file__), '..', 'events-config.schema.json'), 'r') as schema_file:
            self.schema = json.load(schema_file)

        # Load the events-config.json file
        with open(os.path.join(os.path.dirname(__file__), '..', 'config', 'events-config.json'), 'r') as events_file:
            self.events_config = json.load(events_file)

    def test_events_config_valid(self):
        try:
            # Validate the events-config.json file against the schema
            validate(instance=self.events_config, schema=self.schema)
        except ValidationError as e:
            self.fail(f"events-config.json validation failed: {e}")


if __name__ == '__main__':
    unittest.main()
