def generate_html(input_file, output_file, image_url):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            links = [line.strip() for line in infile if line.strip()]
            print(f"{len(links)} liens trouvés dans le fichier d'entrée.")
        
        if not links:
            print("Aucun lien valide trouvé dans le fichier d'entrée.")
            return

        html_content = '<p id="giveaways" align="left">\n'
        counter = 1  # Compteur pour la numérotation des sections

        for i, link in enumerate(links, start=1):
            html_content += f'''    <a class="giveaway" href="{link}" target="_blank" rel="noreferrer">
        <img src="{image_url}" alt="Giveaway Image" width="76" height="76" />
    </a>\n'''

            # Ajouter un séparateur tous les 10 liens avec numérotation et délimitation visuelle
            if i % 10 == 0:
                html_content += f'<br><h1>Paragraph {counter}</h1>\n'  # Ajouter le titre en grand avec <h1>
                html_content += '<br>\n'  # Ajouter un saut de ligne avant la délimitation
                counter += 1  # Incrémenter le compteur

        html_content += '</p>'

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(html_content)
            print(f"Le contenu HTML a été écrit dans le fichier {output_file}")

    except Exception as e:
        print(f"Erreur : {e}")

def main():
    input_file = input("Veuillez entrer l'emplacement du fichier contenant les liens (ex: C:/chemin/vers/fichier.txt) : ").strip(' "')
    output_file = input("Veuillez entrer l'emplacement du fichier de sortie (ex: C:/chemin/vers/fichier_sortie.txt) : ").strip(' "')
    image_url = 'https://gaming-cdn.com/images/avatars/16693760-1689603180.jpg'  # URL de l'image mise à jour

    generate_html(input_file, output_file, image_url)

if __name__ == "__main__":
    main()
