bibliothèque= [{'titre': 'gum a jemea' , 'auteur':'brenda' , 'etat':'lu'},{'titre': 'les larmes du bonheur' , 'auteur':'larissa' , 'etat':'non lu'}, {'titre': "vers l'allemagne" , 'auteur':'michel' , 'etat':'non lu'} ]
while True:
    print(('MENU').center(50))
    print('1.', ' ' "Afficher tous les livres de la bibliothèque.")
    print('2.', ' ' "Ajouter un nouveau livre.")
    print('3.', ' ' "Rechercher un livre par son titre.")
    print('4.', ' ' "Modifier le statut d'un livre (passer de à lire à lu).")
    print('5.', ' ' "Supprimer un livre.")
    print('6.', ' ' "Quitter")
    
    try: 
        choix=int(input('entrez le numero de votre choix'))
    except: 
        print("merci de saisir un entier")
        continue
    if choix == 6 :
        print("merci d'avoir utiliser notre programme")
        break
    if choix <1 or choix > 6:
        print("invalide saisir un entier compris entre 1 et 6")
        continue
    if choix == 1:
        for index, livre in enumerate(bibliothèque, 1):
            print(index,':', livre)
    elif choix == 2:
       while True:
        titre= input("entrez le titre du livre").lower().strip()
        auteur=input("entrez l'auteur du livre").lower().strip()
        if titre.strip() =='' or auteur.strip()== '':
            print("donner le titre du livre et le nom de l'auteur")
            continue
        else:
            new_livre = {'titre': titre, 'auteur': auteur, 'etat': 'non lu'}
            bibliothèque.append(new_livre)
            print("le livre a bien été rangé sur l'étagère")
            print(bibliothèque)
            break
    elif choix==3:
        trouve = False
        livre_r = input("entrez le nom du livre que vous rechercher").strip().lower()
        for i, livre in enumerate(bibliothèque):
            if livre['titre'].strip().lower()== livre_r:
                indice =i
                print(bibliothèque[indice])
                trouve = True
        if not trouve:
            print("Ce livre est introuvable.")

    elif choix==4:
        for index, livre in enumerate(bibliothèque, 1):
            print(index, ':', livre)
        try: 
            mod_livre = int(input('entrez le numero du livre a modifier'))
        except:
            print('entrez un le numero du livre a modifier')
            continue
        if mod_livre > len(bibliothèque):
            print('il ya pas autant de livre entrez le numero du livre')
            continue
        if mod_livre < 1:
            print('entrez un le numero du livre a modifier superieur a 1')
            continue
        num = mod_livre-1
        bibliothèque[num]['etat']= 'lu'
        print(bibliothèque)
    else:
        for index, livre in enumerate(bibliothèque, 1):
            print(index, ':', livre)
        try: 
            mod_livre = int(input('entrez le numero du livre a supprimer'))
        except:
            print('entrez un le numero du livre a supprimer')
            continue
        if mod_livre > len(bibliothèque):
            print('il ya pas autant de livre entrez le numero du livre')
            continue
        if mod_livre < 1:
            print('entrez un le numero du livre a supprimer superieur a 1')
            continue
        num = mod_livre-1
        bibliothèque.pop(num)
        print(bibliothèque)
       



            
            


    


       
        



        
