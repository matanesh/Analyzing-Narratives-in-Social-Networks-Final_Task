

import csv


THIEF_WORDS = [
"burglarize", "knock over", "rob",
"loot", "pillage", "plunder" ,"sack",
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

PLAN_WORDS =["arranging", "blueprinting", "budgeting", "calculating", "charting", "choreographing", "designing",
 "framing", "laying", "out", 
"", "mapping", "(out)", "organizing", "preparing", "projecting", "scheming", "(out)", "shaping", "strategizing",
 "(about)", "", "conspiring", "contriving", "devising", "intriguing", "machinating", "plotting", "putting", "up", "",
  "concerting", "getting", "up", "", "drafting", "outlining", "sketching", "", "aiming", "figuring", "having", "on", "intending", "meaning", "", "contemplating", "meditating", "premeditating", "", "aiming", "allowing", " chiefly", "Southern", "", "Midland", "aspiring", "calculating", "contemplating", "designing", "going", " chiefly", "Southern", "", "Midland", "", "intending", "looking", "meaning", "meditating", "proposing", "purporting", "purposing", "", "dreaming", "hoping", "wishing", "considering", "debating", "mulling", "(over)", "pondering", "attempting", "endeavoring", "striving", "struggling", "trying", "plotting", "scheming", "accomplishing", "achieving", "effecting", "executing", "performing", "", "replenishment", "recapture", "reclamation", "recoupment", "recovery", "repossession", "retrieval", "redemption", "rescue", "loss", "misplacement", "appointment", "assignment", "conscription", "enlistment", "employ", "employment", "engagement", "hire", "incumbency", "tenure", "occupation", "place", "position", "post", "situation", "work", "joblessness", "nonemployment", "unemployment", "boot", "discharge", "dismissal", "firing", "removal", "sack", "severance", "demotion", "suspension", "furlough", "layoff", "leave", "liberty", "retirement", "gang", "army", "band", "brigade", "company", "crew", "outfit", "party", "platoon", "squad", "team", "battalion", "corps", "troop", "force", "host", "posse", "stable", "troupe", "administration", "department", "help", "personnel", "staff", "body", "bunch", "circle", "clan", "clique", "community", "coterie", "coven", "crowd", "fold", "galère", "klatch", "(also", "klatsch)", "lot", "network", "pack", "ring", "set", "charmed", "circle", "elite", "in-group", "closed", "shop", "club", "college", "fellowship", "guild", "(also", "gild)", "league", "organization", "society", "camp", "faction", "sect", "side", "tribe", "mess", "squad", "brotherhood", "fraternity", "order", "sisterhood", "sodality", "sorority", "commune", "alliance", "bloc", "coalition", "confederation", "congress", "council", "federation", "union", "loner", "individualist", "cabal", "conspiracy", "crew", "Mafia", "mob", "ring", "syndicate", "", "", "bunch", "circle", "clan", "clique", "coterie", "coven", "crowd", "galère", "lot", "network", "pack", "set", "junta", "oligarchy", "affiliate", "ally", "attach", "band", "bond", "club", "collaborate", "collude", "confederate", "conjoin", "connect", "cooperate", "couple", "get", "along", "get", "on", "group", "interrelate", "join", "knot", "league", "link", "mingle", "mix", "rally", "relate", "side", "socialize", "team", "tie", "wed", "associate", "chum", "company", 
"consociate", "consort", "fraternize", "hang", "(around", "or", "out)", "hobnob", "hook", "up", "mess"
, "around", "pal", "(around)", "run", "sort", "travel", "befriend", "friend", "avoid", "cold-shoulder", "shun", "snub", "alienate", "estrange", "break", "up", "disband", "disperse", "split", "(up)", "disjoin", "dissociate", "disunite", "divorce", "sever", "split", "sunder", "", "bread", " slang", "bucks", "cabbage", " slang", "cash", "change", "chips", "coin", "currency", "dough", "gold", "green", "jack", " slang", "kale", " slang", "legal", "tender", "lolly", " British", "long", "green", " slang", "loot", "lucre", "moola", "(or", "moolah)", " slang", "needful", "pelf", "scratch", " slang", "", "shekels", "(also", "sheqels", "or", "shekelim", "or", "shekalim", "or", "sheqalim)", "tender", "wampum", "", "coinage", "specie", "dead", "presidents", " slang", "folding", "money", "paper", "money", "scrip", "banknote", "cashier's", "check", "check", "draft", "money", "order", "note", "promissory", "note", "bill", "dollar", "greenback", "bankroll", "capital", "finances", "funds", "roll", " slang", "wad", "wallet", "chump", "change", "dibs", " slang", "dime", "mite", "peanuts", "pittance", "shoestring", "big", "bucks", "bomb", " British", "boodle", "bundle", "earth", "fortune", "king's", "ransom", 
"megabucks", "mint", "packet", " chiefly", "British", "pile", "pot", "abundance", "means", "opulence",
 "riches", "treasure", "wealth", "resources", "wherewithal", "mad", "money", "petty", "cash", "pin", "money", "pocket", "money", "spending", "money", "moneymaker", "money-spinner", " chiefly", "British", "magnate", "nabob", "tycoon", "billionaire", "gazillionaire", "millionaire", "multibillionaire", "multimillionaire", "multimillionairess", "zillionaire", "bankrupt", "beggar", "have-not", "pauper", "distress", "endangerment", "harm's", "way", "imperilment", "jeopardy", "peril", "risk", "trouble", "exposure", "liability", "openness", "vulnerability", "precariousness", "threat", "susceptibility", "susceptibleness", "defenselessness", "helplessness", "weakness", "preservation", 
"salvation", "defense", "protection", "exemption", "immunity", "impunity", "inviolability",
 "invulnerability", "safeness", "safety", "secureness", "security", "hazard", "imminence",
  "menace", "peril", "pitfall", "risk", "threat", "trouble", "snare", "trap", "booby", "trap",
   "guard", "protection", "safeguard", "shield", "ward", "asylum", "harbor", "haven", "refuge", "retreat", "shelter"]


def get_lines():
    with open("../The_Italian_Job/CSV_files/srt_script.csv", "rb") as f:
        return csv.reader(f)

def main():
    with open("../The_Italian_Job/CSV_files/filtered_P.csv","w") as filtered, open("../The_Italian_Job/CSV_files/srt_script.csv", "r") as f:
        csvwriter = csv.writer(filtered)
        mycsv = csv.reader(f)
        for row in mycsv:
            start_time, end_time, content, speaker = row
            clean_content = content.replace(',', '').replace('?','').replace('!', '').replace('.','').split(' ')
            new_content = list(filter(lambda word: word in PLAN_WORDS, clean_content))
            if new_content:
                content = " ".join(new_content)
            else:
                content = " "
            csvwriter.writerow([start_time, end_time, content, speaker])


if __name__ == "__main__":
    main()