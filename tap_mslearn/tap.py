"""mslearn tap class."""
from typing import List
from singer_sdk import Tap, Stream

from tap_mslearn.streams import LearnCatalogs

PLUGIN_NAME = "tap-mslearn"

STREAM_TYPES = [LearnCatalogs]


class TapMSLearn(Tap):
    """mslearn tap class."""

    name = "tap-mslearn"

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        streams = [stream_class(tap=self) for stream_class in STREAM_TYPES]
        return streams


# CLI Execution:
cli = TapMSLearn.cli
