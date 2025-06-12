import datetime

def easter_date(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return (year, month, day)

def print_easter(year=None):
    if year is None:
        year = datetime.datetime.now().year
    elif not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer.")
    easter = easter_date(year)
    print(f"Easter in {year} falls on {easter[1]}/{easter[2]}/{easter[0]}")

if __name__ == "__main__":  
    print_easter()