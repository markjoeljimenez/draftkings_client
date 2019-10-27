from datetime import datetime
import pytz


def identity(value):
    return value


def from_unix_milliseconds_to_datetime(unix_milliseconds):
    return datetime.fromtimestamp(unix_milliseconds / 1e3, tz=pytz.UTC)


def translate_formatted_datetime(formatted_datetime):
    return datetime.fromtimestamp(int(formatted_datetime[6:-2]) / 1e3, tz=pytz.utc)


def dig(data, *key_path, transformer=identity, fallback=None):
    try:
        nested_data = data
        for key in key_path:
            nested_data = nested_data[key]

        return transformer(nested_data)
    except KeyError:
        return fallback

def translate_team(num):
    teams = [
        {
            "id": 1,
            "team": "ATL"
        },
        {
            "id": 2,
            "team": "BOS"
        },
        {
            "id": 3,
            "team": "NOP"
        },
        {
            "id": 4,
            "team": "CHI"
        },
        {
            "id": 5,
            "team": "CLE"
        },
        {
            "id": 6,
            "team": "DAL"
        },
        {
            "id": 7,
            "team": "7"
        },
        {
            "id": 8,
            "team": "DET"
        },
        {
            "id": 9,
            "team": "9"
        },
        {
            "id": 10,
            "team": "HOU"
        },
        {
            "id": 11,
            "team": "IND"
        },
        {
            "id": 12,
            "team": "LAC"
        },
        {
            "id": 13,
            "team": "LAL"
        },
        {
            "id": 14,
            "team": "MIA"
        },
        {
            "id": 15,
            "team": "15"
        },
        {
            "id": 16,
            "team": "MIN"
        },
        {
            "id": 17,
            "team": "BKN"
        },
        {
            "id": 18,
            "team": "NYK"
        },
        {
            "id": 19,
            "team": "ORL"
        },
        {
            "id": 20,
            "team": "PHI"
        },
        {
            "id": 21,
            "team": "PHO"
        },
        {
            "id": 22,
            "team": "POR"
        },
        {
            "id": 23,
            "team": "SAC"
        },
        {
            "id": 24,
            "team": "SAS"
        },
        {
            "id": 25,
            "team": "25"
        },
        {
            "id": 26,
            "team": "UTA"
        },
        {
            "id": 27,
            "team": "WAS"
        },
        {
            "id": 28,
            "team": "TOR"
        },
        {
            "id": 29,
            "team": "MEM"
        },
        {
            "id": 30,
            "team": "30"
        },
        {
            "id": 5312,
            "team": "CHA"
        }
    ]

    return next(filter(lambda x: x.get("id") == num, teams))["team"]
