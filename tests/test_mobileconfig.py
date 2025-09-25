import plistlib
from pathlib import Path


def load_mobileconfig():
    config_path = Path(__file__).resolve().parents[1] / "AppleDNS-DoT.mobileconfig"
    with config_path.open("rb") as handle:
        return plistlib.load(handle)


def test_payload_uuids_are_unique():
    config = load_mobileconfig()
    top_uuid = config["PayloadUUID"]
    child_payloads = config["PayloadContent"]
    assert child_payloads, "PayloadContent should not be empty"
    child_uuid = child_payloads[0]["PayloadUUID"]
    assert top_uuid != child_uuid, "Top level and child payload UUIDs must differ"


def test_dns_settings_enable_dot():
    config = load_mobileconfig()
    dns_settings = config["PayloadContent"][0]["DNSSettings"]
    assert dns_settings["DNSProtocol"] == "TLS"
    assert dns_settings["ServerName"] == "dot.114dns.com"
    assert dns_settings["ServerAddresses"] == ["114.114.114.114"]
