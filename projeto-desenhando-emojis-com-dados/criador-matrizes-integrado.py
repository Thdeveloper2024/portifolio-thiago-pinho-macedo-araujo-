import matplotlib.pyplot as plt
 
 
emoji_data = {
    "nome": "Smile",
    "grade": [
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)], # Linha 0
        [(255,255,0), (0,0,0),     (255,255,0), (0,0,0),     (255,255,0)], # Linha 1 (Olhos)
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)], # Linha 2
        [(255,255,0), (0,0,0),     (0,0,0),     (0,0,0),     (255,255,0)], # Linha 3 (Boca)
        [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)]  # Linha 4
    ]
}
 
new_emoji = {}
 
for chave, valor in emoji_data.items():
    if chave == "nome":
        new_emoji[chave] = valor
    elif chave == "grade":
        new_grade = []
 
        for linha in valor:
            nova_linha = []
 
            for pixel in linha:
                if pixel == (255, 255, 0):
                    novo_pixel = (pixel[0] // 2, pixel[1] // 2, pixel[2] // 2)
                else:
                    novo_pixel = pixel
 
                nova_linha.append(novo_pixel)
 
            new_grade.append(nova_linha)
 
            new_emoji[chave] = new_grade
 
print(new_emoji)
 
plt.imshow(new_emoji["grade"])
plt.show()
 
#Desafio 2: Matrizes Musicais (Transposição)
 
 
biblioteca_musical = {
    "Toques": [
        {"Alegre": ([440, 480], [520, 560])},
        {"Triste": ([200, 150], [100, 50])}
    ]
}
 
 
for chave, lista_musicas in biblioteca_musical.items():
 
 
    for musica in lista_musicas:
        for nome, matriz in musica.items():
            linha1, linha2 = matriz
            nova_matriz = []
 
            for i in range(len(linha1)):
                nova_linha = []
 
 
                nova_linha.append(linha1[i])
                nova_linha.append(linha2[i])
 
                nova_matriz.append(nova_linha)
 
            musica.update({nome: nova_matriz})
 
print(biblioteca_musical)
 
playlist = {
    "imagens": [
        {
            "nome": "Sol",
            "pixels": [(255, 255, 0), (255, 255, 0), (0, 0, 0)]
        },
        {
            "nome": "Noite",
            "pixels": [(0, 0, 0), (255, 255, 0), (0, 0, 0)]
        }
    ]
}
 
#Desafio 3: O Integrador (Criação Livre)
 
 
for chave in playlist.keys():
 
    for imagem in playlist[chave]:
 
        imagem["pixels"].pop()
 
        novos_pixels = []
 
        for pixel in imagem["pixels"]:
            novo_pixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
 
            novos_pixels.append(novo_pixel)
 
        novos_pixels.insert(0, (128, 128, 128))
 
        imagem.update({"pixels": novos_pixels})

print(playlist)