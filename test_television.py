import pytest
from television import Television

@pytest.fixture
def television():
    return Television()

def test_init(television):
    assert str(television) == "Power = False, Channel = 0, Volume = 0"

def test_power(television):
    assert str(television) == "Power = False, Channel = 0, Volume = 0"
    television.power()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
    television.power()
    assert str(television) == "Power = False, Channel = 0, Volume = 0"

def test_mute(television):
    assert str(television) == "Power = False, Channel = 0, Volume = 0"
    television.power()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
    television.volume_up()
    assert str(television) == "Power = True, Channel = 0, Volume = 1"
    television.mute()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
    television.volume_up()
    assert str(television) == "Power = True, Channel = 0, Volume = 2"
    television.mute()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
    television.volume_down()
    assert str(television) == "Power = True, Channel = 0, Volume = 1"
    television.mute()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
    television.volume_down()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"

def test_channel_up(television):
    assert str(television) == "Power = False, Channel = 0, Volume = 0"
    television.power()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
    television.channel_up()
    assert str(television) == "Power = True, Channel = 1, Volume = 0"
    television.channel_up()
    assert str(television) == "Power = True, Channel = 2, Volume = 0"
    television.channel_up()
    assert str(television) == "Power = True, Channel = 3, Volume = 0"
    television.channel_up()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down(television):
    television.power()
    television.channel_down()
    assert str(television) == "Power = True, Channel = 3, Volume = 0"
    television.channel_down()
    assert str(television) == "Power = True, Channel = 2, Volume = 0"

def test_volume_up(television):
    assert str(television) == "Power = False, Channel = 0, Volume = 0"
    television.power()
    television.volume_up()
    assert str(television) == "Power = True, Channel = 0, Volume = 1"
    television.volume_up()
    assert str(television) == "Power = True, Channel = 0, Volume = 2"
    television.volume_up()
    assert str(television) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down(television):
    assert str(television) == "Power = False, Channel = 0, Volume = 0"
    television.power()
    television.volume_up()
    television.volume_up()
    television.volume_down()
    assert str(television) == "Power = True, Channel = 0, Volume = 1"
    television.volume_down()
    television.volume_down()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
    television.volume_down()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
    
