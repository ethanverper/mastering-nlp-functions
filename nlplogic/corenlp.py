from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search wikipedia"""
    print(f"Searching for name: {name}")
    return wikipedia.summary(name, sentences=2, auto_suggest=False, redirect=True)


def summarize_wikipedia(name):
    """Summarize wikipedia"""

    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Gets text blob object and returns"""

    blob = TextBlob(text)
    return blob


def get_tags(name):
    """Find wikipedia name and return back tags"""

    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    tags = blob.tags
    return tags


def get_phrases(name):
    """Find wikipedia name and return back phrases"""

    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
