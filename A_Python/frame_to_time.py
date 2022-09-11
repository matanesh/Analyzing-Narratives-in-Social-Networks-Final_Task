import csv
import difflib
from datetime import datetime



SRT_FILE = "../The_Italian_Job/srt_script.csv"

def main(): 

    with open(SRT_FILE , newline='') as f , open("../The_Italian_Job/srt-script_MiliSec.csv", "w", newline='') as f_time:
        srt_arr = []
        r = csv.reader(f)
        
        csvwriter = csv.writer(f_time)
        for res in r: 
            start_time = res[0]
            end_time = res[1]

            # MATH
            # 01:54:59,859
            mili_start = int(start_time[0:2])*60*60*1000 + int(start_time[3:5])*60*1000 + \
                int(start_time[6:8])*1000 + int(start_time[9:])
            
            mili_end = int(end_time[0:2])*60*60*1000 + int(end_time[3:5])*60*1000 + \
            int(end_time[6:8])*1000 + int(end_time[9:])

            res.insert(2, mili_start)
            res.insert(3, mili_end)

            csvwriter.writerow(res)


if __name__ == "__main__":
    main()