import simplematrixbotlib as botlib


def setup_handlers(bot, config) -> None:

    @bot.listener.on_startup
    async def join_bridged_rooms():
        """Join rooms specified in config if not already joined."""
        joined_rooms = (await bot.async_client.joined_rooms())
        for bridge in config["bridge"]:
            for bridge_input in bridge["input"]:
                if not bridge_input["room_id"] in joined_rooms:
                    await bot.async_client.join(bridge_input["room_id"])
            for bridge_output in bridge["output"]:
                if not bridge_output["room_id"] in joined_rooms:
                    await bot.async_client.join(bridge_output["room_id"])
    join_bridged_rooms # Satisfy Pyright type checker

