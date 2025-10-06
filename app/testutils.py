from utils import process_data

def test_process_data():
    sample = [{"userId": 1, "id": 101, "title": "abc"}]
    df = process_data(sample)
    assert df.loc[0, "UserID"] == 1
    assert df.loc[0, "PostCount"] == 1