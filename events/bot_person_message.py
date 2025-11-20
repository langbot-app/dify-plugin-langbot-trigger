from collections.abc import Mapping
from typing import Any

from werkzeug import Request

from dify_plugin.entities.trigger import Variables
from dify_plugin.errors.trigger import EventIgnoreError
from dify_plugin.interfaces.trigger import Event


class BotPersonMessageEvent(Event):
    """
    Basic example trigger handler that emits the raw incoming payload.
    Replace the logic here with your integration specific processing.
    """

    def _on_event(self, request: Request, parameters: Mapping[str, Any], payload: Mapping[str, Any]) -> Variables:
        payload = request.get_json(silent=True) or {}

        print("bot_person_message payload: ", payload)

        # sample_filter = parameters.get("sample_filter")
        # if sample_filter and sample_filter not in str(payload):
        #     raise EventIgnoreError()

        plain_text = ""

        for message in payload.get("data", {}).get("message", []):
            if message.get("type") == "Plain":
                plain_text += message.get("text")

        return Variables(
            variables={
                "message": payload.get("data", {}).get("message", {}),
                "bot_uuid": payload.get("data", {}).get("bot_uuid", ""),
                "adapter_name": payload.get("data", {}).get("adapter_name", ""),
                "sender": payload.get("data", {}).get("sender", {}),
                "sender_id": payload.get("data", {}).get("sender", {}).get("id", ""),
                "sender_name": payload.get("data", {}).get("sender", {}).get("name", ""),
                "plain_text": plain_text,
                "timestamp": payload.get("data", {}).get("timestamp", ""),
                "raw_event": payload,
            }
        )
