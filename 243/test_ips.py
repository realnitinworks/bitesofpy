import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import ServiceIPRange, parse_ipv4_service_ranges, get_aws_service_range

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network("192.0.2.8/29")


@pytest.fixture(scope="module")
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


@pytest.fixture(scope="module")
def service_ranges():
    service = "CLOUD9"
    region = "eu-west-1"
    CIDRS = [
        "10.1.18.0/24",
        "192.168.1.0/27",
        "192.0.2.8/29",
        "192.168.1.0/24"
    ]

    return [
        ServiceIPRange(
            service=service,
            region=region,
            cidr=IPv4Network(cidr)
        )
        for cidr in CIDRS
    ] 


def test_parse_ip4_service_ranges(json_file):
    service_ranges = parse_ipv4_service_ranges(json_file)
    assert len(service_ranges) == 1886
    assert isinstance(service_ranges, list)
    assert isinstance(service_ranges[0], ServiceIPRange)


def test_ServiceIPRange_string_representaiton():
    service = "CLOUD9"
    region = "eu-west-1"
    cidr = IP

    expected = f"{cidr} is allocated to the {service} service in the {region} region"
    assert str(ServiceIPRange(service, region, cidr)) == expected


def test_invalid_ip_address():
    service = "CLOUD9"
    region = "eu-west-1"
    cidr = IP
    invalid_ip = "192.0.2.9/24"  # Invalid IP. This is a valid CIDR

    service_ranges = [ServiceIPRange(service, region, cidr)]
    with pytest.raises(ValueError) as exc:
        get_aws_service_range(invalid_ip, service_ranges)

    assert str(exc.value) == "Address must be a valid IPv4 address"


def test_ipv4_address_in_service_ranges(service_ranges):
    actual = get_aws_service_range("10.1.18.15", service_ranges)
    expected = [service_ranges[0]]
    assert actual == expected

    # 192.168.1.16 is in the subnect of both
    # 192.168.1.0/27 and 192.168.1.0/24
    actual = get_aws_service_range("192.168.1.16", service_ranges)
    expected = [service_ranges[1], service_ranges[3]]
    assert actual == expected


def test_ip4_address_not_in_service_ranges(service_ranges):
    # 192.0.2.16 is outside 192.0.2.8/29
    # 192.0.2.8/29 : 192.0.2.8 - 192.0.2.7
    assert not get_aws_service_range("192.0.2.16", service_ranges)

    # 192.168.1.33/27 is outside 192.168.1.0/27
    # 192.168.1.0/27 : 192.168.1.0 - 192.168.1.31
    assert not get_aws_service_range("192.168.2.33", service_ranges)

