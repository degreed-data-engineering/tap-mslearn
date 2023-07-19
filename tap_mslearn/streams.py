"""Stream class for tap-mslearn."""

import logging

from singer_sdk.streams import RESTStream
from singer_sdk import typing as th

logging.basicConfig(level=logging.INFO)


class TapMSLearnStream(RESTStream):
    """Generic MSLearn stream class."""

    @property
    def url_base(self) -> str:
        """Base URL of source"""
        return "https://docs.microsoft.com/api"


class LearnCatalogs(TapMSLearnStream):
    name = "learn_catalogs"
    path = "/learn/catalog"
    primary_keys = ["uid"]
    records_jsonpath = "$.modules[0:]"
    schema = th.PropertiesList(
        th.Property("uid", th.StringType),
    ).to_dict()
