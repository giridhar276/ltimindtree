


org_list = ["oracle","google","microsoft","lti"]
rev_list=[]
for item in org_list:
    rev_list=[item]+rev_list
print("Reversed list:",rev_list)


#

["oracle"] + []   = ["oracle"]
["google"] + ["oracle"]    = ["google","oracle"]
["microsoft"] + ["google","oracle"] = ["microsoft","google","oracle"]
