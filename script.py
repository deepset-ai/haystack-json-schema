import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

sys.path.append(".")
from haystack.nodes._json_schema import update_json_schema

update_json_schema(destination_path=Path("/haystack-json-schema") / "json-schema")
