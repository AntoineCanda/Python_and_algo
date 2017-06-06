# Representation du fonctionnement du T9 comme on peut trouver dans les anciens portables


t9="22233344455566677778889999"
#   abcdefghijklmnopqrstuvwxyz les corresppondances

# conversion d'une lettre dans le chiffre associe
def lettre_to_chiffre(x):
    # On verifie que c'est bien une lettre definie dans le codage
    assert 'a' <= x and x <= 'z'
    return t9[ord(x) - ord('a')]

# conversion d'un mot dans le code t9 associe
def mot_to_code(mot):
    # fonctionnel quand tu nous tiens...
    return ''.join(map(lettre_to_chiffre,mot))

def predictive_text(dictionnaire):
    # nombre de mot avec le prefixe p = freq[p]
    freq = {}
    for mot, poids in dictionnaire:
        prefixe = ""
        for x in mot:
            prefixe += x
            if prefixe in freq:
                freq[prefixe] += poids
            else:
                freq[prefixe] = poids
    prop = {}
    for prefixe in freq:
        code = mot_to_code(prefixe)
        if code not in prop or freq[prop[code]] < freq[prefixe]:
            prop[code] = prefixe
    return prop

def propose(prop, seq):
    if seq in prop:
        return prop[seq]
    else:
        return "None"

def test_predictive_text(self):
    dico = [("another", 5), ("contest", 6), ("follow", 3), ("give", 13), ("integer", 6), ("new", 14), ("program", 4)]
    prop = predictive_text(dico)
    A = ""
    for seq in ["7764726", "639", "468", "2668437", "7777"]:
        for i in range(len(seq)):
            A += propose(prop, seq[:i + 1]) + " "
            self.assertEqual( A, "p pr pro prog progr progra program n ne new g "\
                    "in int c co con cont anoth anothe another p pr None None ")
