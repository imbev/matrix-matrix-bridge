import toml
import pytest


EXAMPLE_CONFIG_PATH = "./config.toml.example"
with open(EXAMPLE_CONFIG_PATH, "r") as f:
    example_config = toml.loads(f.read())

def test_creds() -> None:
    assert example_config["homeserver"] == "https://example.com"
    assert example_config["username"] == "example_user"
    assert example_config["password"] == "example_password"
    assert example_config["admin_user_id"] == []

def test_bridge() -> None:
    bridges = example_config["bridge"]
    assert len(bridges) == 2
    
    if bridges[0]["name"] == "example_bridge":
        bridge_1 = bridges[0]
    elif bridges[1]["name"] == "example_bridge":
        bridge_1 = bridges[1]
    else:
        assert False
    
    if bridges[0]["name"] == "another_bridge":
        bridge_2 = bridges[0]
    elif bridges[1]["name"] == "another_bridge":
        bridge_2 = bridges[1]
    else:
        assert False

    assert len(bridge_1["input"]) == 1
    assert bridge_1["input"][0]["room_id"] == "!yRjNdMVvyeIgpYRBit:example.com"
    assert bridge_1["input"][0]["required_prefix"] == ""
    assert bridge_1["input"][0]["required_sender_user_id"] == []

    assert len(bridge_1["output"]) == 1
    assert bridge_1["output"][0]["room_id"] == "!OGEhHVWSdvArJzumhm:example.com"

    assert len(bridge_2["input"]) == 2
    bridge_2_input_1, bridge_2_input_2 = {}, {}
    for i in bridge_2["input"]:
        if i["room_id"] == "!ovGZXReQuDFezAaAfr:example.com":
            bridge_2_input_1 = i
        elif i["room_id"] == "!jxlRxnrZCsjpjDubDX:example.com":
            bridge_2_input_2 = i
        else:
            assert False
    assert bridge_2_input_1["required_prefix"] == "b!"
    assert bridge_2_input_1["required_sender_user_id"] == ["@user:example.com"]
    with pytest.raises(KeyError):
        bridge_2_input_2["required_prefix"]
    with pytest.raises(KeyError):
        bridge_2_input_2["required_sender_user_id"]

    assert len(bridge_2["output"]) == 2
    bridge_2_output_1, bridge_2_output_2 = {}, {}
    for i in bridge_2["output"]:
        if i["room_id"] == "!HRNVeGThDQRMYdGzLD:example.com":
            bridge_2_output_1 = i
        elif i["room_id"] == "!JiiOHXrIUCtcOJsZCa:example.com":
            bridge_2_output_2 = i
        else:
            assert False
    assert bridge_2_output_1
    assert bridge_2_output_2

