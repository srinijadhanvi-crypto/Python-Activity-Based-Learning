capacity, level, threshold = 100, 40, 80
intervals = [(50, 5), (30, 10), (0, 120), (80, 0)]
first = 0
total_overflow = 0
total_shortage = 0
if capacity <= 0 or level < 0 or level > capacity or threshold < 0 or threshold > capacity:
    print("Invalid tank settings")
else:
    interval_number = 0
    for inflow, outflow in intervals:
        interval_number += 1
        if inflow < 0 or outflow < 0:
            print("Invalid interval; skipped")
        else:
            level += inflow
            overflow = 0
            if level > capacity:
                overflow = level - capacity
                level = capacity
            shortage = 0
            if outflow > level:
                shortage = outflow - level
                level = 0
            else:
                level -= outflow
            total_overflow += overflow
            total_shortage += shortage
            print("In {}, out {}: level {}, overflow {}, shortage {}".format(inflow, outflow, level, overflow, shortage))
            if first == 0 and level >= threshold:
                first = interval_number
    if first == 0:
        print("Threshold: not reached")
    else:
        print("First threshold interval:", first)
    print("Total overflow: {}; total shortage: {}".format(total_overflow, total_shortage))
