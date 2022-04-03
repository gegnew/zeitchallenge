from app.util import count_letters


class TestUtil:
    def test_gets_expected_letter_counts(self):
        text = "Zeit Medical"
        result = count_letters(text)

        assert isinstance(result, dict)
        assert result["a"] == 1
        assert result["c"] == 1
        assert result["d"] == 1
        assert result["e"] == 2
        assert result["i"] == 2
        assert result["l"] == 1
        assert result["m"] == 1
        assert result["t"] == 1
        assert result["z"] == 1
        assert result["Z"] == 0  # only lowercase letters
        assert result["x"] == 0  # no nonexistent letters, no error

    def test_strips_non_characters(self):
        text = "Zeit Medical"
        result = count_letters(text)

        assert result[" "] == 0
