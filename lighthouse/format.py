import json

import pandas as pd


class FormatFor:
    """
    Provides formatting options for many outputs
    Currently Slack
        - code blob wrapped with ```
    """

    @classmethod
    def slack_json_as_code_blob(cls, blob):
        return "```" + json.dumps(blob, indent=4, sort_keys=True) + "```"

    @classmethod
    def slack_csv_blob(cls, blob):
        # Blob is the json back from the server
        # data_strucutre tells us how to format it

        df = pd.DataFrame(blob)

        if type(blob) is list:
            return df.to_csv(index=False)

        return None
