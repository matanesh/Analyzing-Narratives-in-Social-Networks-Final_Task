

import csv

THIEF_WORDS = [
"burglarize", "knock over", "rob"
"loot", "pillage", "plunder" ,"sack"
"carjack", "hijack",
"pick", "rifle",
"poach", "rustle", "shoplift",
"collar", "grab", "grasp", "nail" ,"seize", "snatch" ,"take",
"mooch", "sponge",
"abduct", "kidnap", "spirit", "heist", "thief",

"officer's",
"despoil","loot","pillage","plunder","ravish","sack","spoil","strip",
"bleed","break in","cheat","chisel","cozen","defraud","exploit","fleece","hustle","mulct","pluck","rook","shortchange"",""skin","squeeze","stick","sting","swindle",
"hold up","mug","roll","stick up",

"crime",
"felony", "misconduct", "misdemeanor", "misfeasance",
"fault", 'foible', "peccadillo",
'break', 'infringement',
'immorality', 'iniquitousness', 'iniquity', 'sinfulness', 'vice', 'wickedness',
'corruption', 'debauchery', 'depravity', 'licentiousness',
'abuse', 'criminality', 'illegality', 'lawlessness', 'unlawfulness',
'descent', 'downfall', 'fall',
]

def get_lines():
    with open("The_Italian_Job/CSV_files/srt_script.csv", "rb") as f:
        return csv.reader(f)

def main():
    with open("The_Italian_Job/CSV_files/filtered.csv","w") as filtered, open("The_Italian_Job/CSV_files/srt_script.csv", "r") as f:
        csvwriter = csv.writer(filtered)
        mycsv = csv.reader(f)
        for row in mycsv:
            start_time, end_time, content, speaker = row
            clean_content = content.replace(',', '').replace('?','').replace('!', '').replace('.','').split(' ')
            new_content = list(filter(lambda word: word in THIEF_WORDS, clean_content))
            if new_content:
                content = " ".join(new_content)
            else:
                content = " "
            csvwriter.writerow([start_time, end_time, content, speaker])


if __name__ == "__main__":
    main()