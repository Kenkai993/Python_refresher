dict_of_pat = [
    {"Name": "Milos", "Godine": 32, "Dijagnoza": "Anksioznost"},
    {"Name": "Stefan", "Godine": 40, "Dijagnoza": "Pneumonija"},
    {"Name": "Boris", "Godine": 21, "Dijagnoza": "Tuberkuloza"},
    {"Name": "Sara", "Godine": 19, "Dijagnoza": "HIV"},
    {"Name": "Snjezana", "Godine": 46, "Dijagnoza": "Dijabetes"},

def remove_patient(pat_list, name):
    return [p for p in pat_list if p["Name"] != name]

dict_of_pat=remove_patient(dict_of_pat,"Stefan")
print(dict_of_pat)
