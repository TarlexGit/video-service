import re


def check_on_match(pattern, data) -> bool:
    if re.match(pattern, data) is not None:
        return True
    else:
        return False


def data_verification(df):
    timecodes = df
    for row in timecodes.itertuples(index=False):
        pattern = "(\d+)[.]{1}(\d+)"
        check = check_on_match(pattern, str(row.Time))
        if check == True:
            continue
        else:
            return False
    return True
