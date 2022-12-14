import datetime
from time import gmtime, localtime

def now():
    # current UTC as string
    return datetime.datetime.utcnow().strftime("%Y/%m/%dT%H:%M:%S")

def date_to_nid(d):
    """date_to_nid.
    Converts date string yyyymmdd to ZTF night id (nid)
    Args:
        d:
    """
    try:
        year  = int(d[0:4])
        month = int(d[4:6])
        day   = int(d[6:8])
    except:
        print("Date %s not in format yyyymmdd" % d)
        return -1
    d0 = datetime.date(2017, 1, 1)
    d1 = datetime.date(year, month, day)
    nid = (d1 - d0).days
    return nid

def nid_now():
    """nid_now.
    Converts date string yyyymmdd (in UTC) to ZTF night id (nid)
    """
    g = gmtime()
    return date_to_nid("%4s%2s%2s" % (g.tm_year, g.tm_mon, g.tm_mday))

def nid_to_date(nid):
    """nid_to_date.
    Converts ZTF night id (nid) to date string yyyymmdd (in UTC)
    Args:
        nid
    """
    d0 = datetime.date(2017, 1, 1)
    d1 = d0 + datetime.timedelta(days=nid)
    return d1.strftime("%Y%m%d")

if __name__ == "__main__":
    print(now())

    is_market_open()


    nid = nid_now()
    print("nid now is: %d" % nid)

    date = nid_to_date(nid)
    print("date now is: %s" % date)

    nid = date_to_nid(date)
    print("nid is: %d" % nid)
