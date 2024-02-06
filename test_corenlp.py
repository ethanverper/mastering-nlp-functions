from nlplogic.corenlp import get_tags, get_phrases


def test_get_phrases():
    assert "10th-most-populous country" in get_phrases("Mexico")


def test_get_tags():
    assert "Spanish" in get_tags("Mexico")[1]
