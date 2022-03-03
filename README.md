# matrix-matrix-bridge
A bridge for the Matrix Protocol that connects Matrix rooms to each other. 

Made with [![](https://img.shields.io/badge/simplematrixbotlib-2.6.2-brightgreen)](https://github.com/i10b/simplematrixbotlib)

## Setup
- Install python 3.8 or higher
- Install git
- Install python-poetry
```bash
python -m pip install poetry
```
- Clone repository
```bash
git clone https://github.com/KrazyKirby99999/matrix-matrix-bridge
```
- Install dependencies
```bash
cd matrix-matrix-bridge
python -m poetry install
```

## Usage
- Create configuration file
```toml
# config.toml
homeserver = "https://example.com"
username = "username" 
password = "password"
[[bridge]]
    name = "bridge"
    [[bridge.input]]
        room_id = "!aRAWUKZyBETGiwvoRh:matrix.org"
    [[bridge.output]]
        room_id = "!AUweUQXCxcVfFOaOIU:matrix.org"
```
A more detailed example can be found at https://github.com/KrazyKirby99999/matrix-matrix-bridge/blob/master/config.toml.example
- Run program
```bash
python -m poetry python run main.py
```

## Notes
- GPL-3.0 License
- Each bridge supports multiple input rooms and multiple output rooms with more options for configuration.
