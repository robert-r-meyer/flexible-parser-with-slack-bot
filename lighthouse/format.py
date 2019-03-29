import json

class FormatFor():
    """
    Provides formatting options for many outputs
    Currently Slack
        - code blob wrapped with ```
    """

    @classmethod
    def slack_json_as_code_blob(cls, blob):
        return "```" + json.dumps(blob, indent=4, sort_keys=True) + '```'
