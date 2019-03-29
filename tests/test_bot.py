import pytest

from lighthouse import bot


class TestBot():
    def setup(self):
        self.test_bot = bot.Bot()

    @pytest.mark.vcr()
    def test_bot_id_found(self):
        assert self.test_bot.bot_id == '<@WBWJANHH7>'

    @pytest.mark.vcr()
    def test_bot_is_valid(self):
        assert self.test_bot.valid
