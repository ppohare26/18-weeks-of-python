rd_km = 10
tm_min = 43
tm_sec = 30
km_mi = 1 / 1.61
rd_mi = rd_km * km_mi
tt_sec = (tm_min * 60) + tm_sec
at_pm_sec = tt_sec / rd_mi
at_pm_min = at_pm_sec // 60
at_pm_rem_sec = at_pm_sec % 60
as_mph = rd_mi / (tt_sec / 3600)
at_pm = f"{int(at_pm_min)}:{int(at_pm_rem_sec):02d} (min:sec)"
as_mph = round(as_mph, 2)
print("Average time per mile:", at_pm)
print("Average speed in mph:", as_mph)

