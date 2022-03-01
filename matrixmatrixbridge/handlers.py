import simplematrixbotlib as botlib


def setup_handlers(bot, config) -> None:

    @bot.listener.on_startup
    async def join_bridged_rooms(room):
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

    @bot.listener.on_message_event
    async def bridge(room, event):
        for bridge in config["bridge"]:
            matched = False

            for bridge_input in bridge["input"]: 
                if not room.room_id == bridge_input["room_id"]:
                    break

                try:
                    required_prefix = bridge_input["required_prefix"]
                except KeyError:
                    required_prefix = ""

                match = botlib.MessageMatch(room, event, bot, required_prefix)

                try:
                    required_sender_user_id = bridge_input["required_sender_user_id"]
                except KeyError:
                    required_sender_user_id = []

                if required_prefix and (not match.prefix()):
                    break
                if required_sender_user_id and (
                        not event.sender in required_sender_user_id):
                    break

                matched = True

            if not matched:
                break

            for bridge_output in bridge["output"]:

                room_id = bridge_output["room_id"]
                try:
                    response_format = bridge_output["format"]
                except KeyError:
                    response_format = "(%user_id): %message"

                response = response_format.replace(
                        "%user_id", event.sender).replace(
                        "%message", event.body)
                await bot.api.send_text_message(room_id, response)

    bridge # Satisfy Pyright type checker
