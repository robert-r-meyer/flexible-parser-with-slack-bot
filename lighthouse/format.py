import json

import pandas as pd
from pandas.io.json import json_normalize


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

        # result = pd.read_json(data, typ="records")
        df = pd.DataFrame(blob)

        return df.to_csv(index=False)
