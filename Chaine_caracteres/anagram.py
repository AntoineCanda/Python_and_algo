# w = liste de mot
def anagrams(w):
    # On retire les doublons avec un set
        w = list(set(w))
    # Structure qui va grouper les mots de meme signature
        d = {}
        
        for i in range(len(w)):
        # Calcul de la signature
                s = ''.join(sorted(w[i]))
                if s in d:
                        d[s].append(i)
                else:
                        d[s] = [i]      
    # Extrait les anagrames
        reponse = []
        for s in d:
                # On ne considere que les mots avec au moins une anagramme
                if len(d[s]) > 1:
                        reponse.append([w[i] for i in d[s]])
        return reponse
