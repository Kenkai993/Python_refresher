dict_of_pat = [
    {"Ime": "Milos", "Godine": 32, "Dijagnoza": "Anksioznost"},
    {"Ime": "Stefan", "Godine": 40, "Dijagnoza": "Pneumonija"},
    {"Ime": "Boris", "Godine": 21, "Dijagnoza": "Tuberkuloza"},
    {"Ime": "Sara", "Godine": 19, "Dijagnoza": "HIV"},
    {"Ime": "Snjezana", "Godine": 46, "Dijagnoza": "Dijabetes"},
]

def remove_patient(patient_list, name):
    return [p for p in patient_list if p.get("Ime") != name]

if __name__ == "__main__":
    print("Prvobitna lista:", dict_of_pat)
    dict_of_pat = remove_patient(dict_of_pat, "Stefan")
    print("Bez Stefana:", dict_of_pat)
