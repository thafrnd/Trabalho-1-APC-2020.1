import math
import copy

k=int(input()) #recebe k
ntrain,ntest=(input().split(' ')) #recebe ntrain e ntest
ntrain=int(ntrain)
ntest=int(ntest)

contador_ntrain=0
lista_ntrain=[]

#loop que cria uma lista com as linhas da matriz train aninhadas em forma de listas
while contador_ntrain<ntrain: 
    lista = (input().split(' '))
    lista_ntrain.append(lista)
    contador_ntrain=contador_ntrain+1
#loop que armazeza os rotulos de train em uma lista
lista_rotulos_train=[]
contador_ntrain=0
while contador_ntrain<ntrain: 
    rotulos=input()   
    lista_rotulos_train.append(rotulos)
    contador_ntrain=contador_ntrain+1
contador_ntest=0
lista_ntest=[]    
#loop que cria uma lista com as linhas da matriz test aninhadas em forma de listas
while contador_ntest<ntest: 
    lista2 = (input().split(' '))
    lista_ntest.append(lista2)
    contador_ntest=contador_ntest+1

    
####################################dicionarios################################################
dicio_cap_shape= {'b': 0, 'c': 1, 'x': 2, 'f': 3, 'k': 4, 's': 5}
dicio_cap_surface= {'f': 0, 'g': 1, 'y': 2, 's': 3}
dicio_cap_color={'n': 0, 'b': 1, 'c': 2, 'g': 3, 'r': 4, 'p': 5, 'u': 6, 'e': 7, 'w': 8, 'y': 9}
dicio_bruises= {'t': 0, 'f': 1}
dicio_odores={'a': 0, 'l': 1, 'c': 2, 'y': 3, 'f': 4, 'm': 5, 'n': 6, 'p': 7, 's': 8}
dicio_gill_attachement= {'a': 0, 'd': 1, 'f': 2, 'n': 3}
dicio_gill_spacing={'c': 0, 'w': 1, 'd': 2}
dicio_gill_size={'b': 0, 'n': 1}
dicio_gill_color={'k': 0, 'n': 1, 'b': 2, 'h': 3, 'g': 4, 'r': 5, 'o': 6, 'p': 7, 'u': 8, 'e': 9, 'w': 10, 'y': 11}
dicio_stalk_shape={'e': 0, 't': 1}
dicio_stalk_root={'b': 0, 'c': 1, 'u': 2, 'e': 3, 'z': 4, 'r': 5, '?': 6}
dicio_stalk_surface_above_ring={'f': 0, 'y': 1, 'k': 2, 's': 3}
dicio_stalk_surface_below_ring={'f': 0, 'y': 1, 'k': 2, 's': 3}
dicio_stalk_color_above_ring= {'n': 0, 'b': 1, 'c': 2, 'g': 3,'o': 4, 'p': 5, 'e': 6, 'w': 7, 'y': 8}
dicio_stalk_color_below_ring= {'n': 0, 'b': 1, 'c': 2, 'g': 3, 'o': 4, 'p': 5, 'e': 6, 'w': 7, 'y': 8}
dicio_veil_type={'p': 0, 'u': 1}
dicio_veil_color={'n': 0, 'o': 1, 'w': 2, 'y': 3}
dicio_ring_number={'n': 0, 'o': 1, 't': 2}
dicio_ring_type= {'c': 0, 'e': 1, 'f': 2, 'l': 3, 'n': 4, 'p': 5, 's': 6, 'z': 7}
dicio_spore_print_color={'k': 0, 'n': 1, 'b': 2, 'h': 3, 'r': 4, 'o': 5, 'u': 6, 'w': 7, 'y': 8}
dicio_population={'a': 0, 'c': 1, 'n': 2, 's': 3, 'v': 4, 'y': 5}
dicio_habitat={'g': 0, 'l': 1, 'm': 2, 'p': 3, 'u': 4, 'w': 5, 'd': 6}
lista_dicionarios=[dicio_cap_shape,dicio_cap_surface,dicio_cap_color,dicio_bruises,dicio_odores,dicio_gill_attachement,dicio_gill_spacing,dicio_gill_size,dicio_gill_color,dicio_stalk_shape,dicio_stalk_root,dicio_stalk_surface_above_ring,dicio_stalk_surface_below_ring,dicio_stalk_color_above_ring,dicio_stalk_color_below_ring,dicio_veil_type,dicio_veil_color,dicio_ring_number,dicio_ring_type,dicio_spore_print_color,dicio_population,dicio_habitat]

#################################################################################################################
#traduzir
lista_ntrain_traduzida=[]
for lista in lista_ntrain:
    lista=[dicio_cap_shape[lista[0]],dicio_cap_surface[lista[1]],dicio_cap_color[lista[2]],dicio_bruises[lista[3]],dicio_odores[lista[4]],dicio_gill_attachement[lista[5]],dicio_gill_spacing[lista[6]],dicio_gill_size[lista[7]],dicio_gill_color[lista[8]],dicio_stalk_shape[lista[9]],dicio_stalk_root[lista[10]],dicio_stalk_surface_above_ring[lista[11]],dicio_stalk_surface_below_ring[lista[12]],dicio_stalk_color_above_ring[lista[13]],dicio_stalk_color_below_ring[lista[14]],dicio_veil_type[lista[15]],dicio_veil_color[lista[16]],dicio_ring_number[lista[17]],dicio_ring_type[lista[18]],dicio_spore_print_color[lista[19]],dicio_population[lista[20]],dicio_habitat[lista[21]]]
    lista_ntrain_traduzida.append(lista)

lista_ntest_traduzida=[]
for lista in lista_ntest:
    lista=[dicio_cap_shape[lista[0]],dicio_cap_surface[lista[1]],dicio_cap_color[lista[2]],dicio_bruises[lista[3]],dicio_odores[lista[4]],dicio_gill_attachement[lista[5]],dicio_gill_spacing[lista[6]],dicio_gill_size[lista[7]],dicio_gill_color[lista[8]],dicio_stalk_shape[lista[9]],dicio_stalk_root[lista[10]],dicio_stalk_surface_above_ring[lista[11]],dicio_stalk_surface_below_ring[lista[12]],dicio_stalk_color_above_ring[lista[13]],dicio_stalk_color_below_ring[lista[14]],dicio_veil_type[lista[15]],dicio_veil_color[lista[16]],dicio_ring_number[lista[17]],dicio_ring_type[lista[18]],dicio_spore_print_color[lista[19]],dicio_population[lista[20]],dicio_habitat[lista[21]]]
    lista_ntest_traduzida.append(lista)

###############normalizar os dados do conjunto train########################################
#criar uma lista com as medias referenteas a cada caracteristica
lista_cap_shape=[]
lista_cap_surface=[]
lista_cap_color=[]
lista_bruises=[]
lista_odores=[]
lista_gill_attachement=[]
lista_gill_spacing=[]
lista_gill_size=[]
lista_gill_color=[]
lista_stalk_shape=[]
lista_stalk_root=[]
lista_stalk_surface_above_ring=[]
lista_stalk_surface_below_ring=[]
lista_stalk_color_above_ring=[]
lista_stalk_color_below_ring=[]
lista_veil_type=[]
lista_veil_color=[]
lista_ring_number=[]
lista_ring_type=[]
lista_spore_print_color=[]
lista_population=[]
lista_habitat=[]
medias=[]
for lista in lista_ntrain_traduzida:
    lista_cap_shape.append(lista[0])
media_cap_shape=sum(lista_cap_shape)/len(lista_cap_shape)
medias.append(media_cap_shape)

for lista in lista_ntrain_traduzida:
    lista_cap_surface.append(lista[1])
media_cap_surface=sum(lista_cap_surface)/len(lista_cap_surface)
medias.append(media_cap_surface)

for lista in lista_ntrain_traduzida:
    lista_cap_color.append(lista[2])
media_cap_color=sum(lista_cap_color)/len(lista_cap_color)
medias.append(media_cap_color)
    
for lista in lista_ntrain_traduzida:
    lista_bruises.append(lista[3])
media_bruises=sum(lista_bruises)/len(lista_bruises)
medias.append(media_bruises)    

for lista in lista_ntrain_traduzida:
    lista_odores.append(lista[4])
media_odores=sum(lista_odores)/len(lista_odores)
medias.append(media_odores)

for lista in lista_ntrain_traduzida:
    lista_gill_attachement.append(lista[5])
media_gill_attachement=sum(lista_gill_attachement)/len(lista_gill_attachement)
medias.append(media_gill_attachement)    

for lista in lista_ntrain_traduzida:
    lista_gill_spacing.append(lista[6])
media_gill_spacing=sum(lista_gill_spacing)/len(lista_gill_spacing)
medias.append(media_gill_spacing)

for lista in lista_ntrain_traduzida:
    lista_gill_size.append(lista[7])
media_gill_size=sum(lista_gill_size)/len(lista_gill_size)
medias.append(media_gill_size)

for lista in lista_ntrain_traduzida:
    lista_gill_color.append(lista[8])
media_gill_color=sum(lista_gill_color)/len(lista_gill_color)
medias.append(media_gill_color)

for lista in lista_ntrain_traduzida:
    lista_stalk_shape.append(lista[9])
media_stalk_shape=sum(lista_stalk_shape)/len(lista_stalk_shape)
medias.append(media_stalk_shape)

for lista in lista_ntrain_traduzida:
    lista_stalk_root.append(lista[10])
media_stalk_root=sum(lista_stalk_root)/len(lista_stalk_root)
medias.append(media_stalk_root)

for lista in lista_ntrain_traduzida:
    lista_stalk_surface_above_ring.append(lista[11])
media_stalk_surface_above_ring=sum(lista_stalk_surface_above_ring)/len(lista_stalk_surface_above_ring)
medias.append(media_stalk_surface_above_ring)

for lista in lista_ntrain_traduzida:
    lista_stalk_surface_below_ring.append(lista[12])
media_stalk_surface_below_ring=sum(lista_stalk_surface_below_ring)/len(lista_stalk_surface_below_ring)
medias.append(media_stalk_surface_below_ring)

for lista in lista_ntrain_traduzida:
    lista_stalk_color_above_ring.append(lista[13])
media_stalk_color_above_ring=sum(lista_stalk_color_above_ring)/len(lista_stalk_color_above_ring)
medias.append(media_stalk_color_above_ring)

for lista in lista_ntrain_traduzida:
    lista_stalk_color_below_ring.append(lista[14])
media_stalk_color_below_ring=sum(lista_stalk_color_below_ring)/len(lista_stalk_color_below_ring)
medias.append(media_stalk_color_below_ring)

for lista in lista_ntrain_traduzida:
    lista_veil_type.append(lista[15])
media_veil_type=sum(lista_veil_type)/len(lista_veil_type)
medias.append(media_veil_type)

for lista in lista_ntrain_traduzida:
    lista_veil_color.append(lista[16])
media_veil_color=sum(lista_veil_color)/len(lista_veil_color)
medias.append(media_veil_color)

for lista in lista_ntrain_traduzida:
    lista_ring_number.append(lista[17])
media_ring_number=sum(lista_ring_number)/len(lista_ring_number)
medias.append(media_ring_number)

for lista in lista_ntrain_traduzida:
    lista_ring_type.append(lista[18])
media_ring_type=sum(lista_ring_type)/len(lista_ring_type)
medias.append(media_ring_type)

for lista in lista_ntrain_traduzida:
    lista_spore_print_color.append(lista[19])
media_spore_print_color=sum(lista_spore_print_color)/len(lista_spore_print_color)
medias.append(media_spore_print_color)

for lista in lista_ntrain_traduzida:
    lista_population.append(lista[20])
media_population=sum(lista_population)/len(lista_population)
medias.append(media_population)

for lista in lista_ntrain_traduzida:
    lista_habitat.append(lista[21])
media_habitat=sum(lista_habitat)/len(lista_habitat)
medias.append(media_habitat)
#calcular a diferen??a entre cada atributo a media de tal atributo e elevar ao quadrado
lista_variancias=[]
diferen??as_cap_shape=[]
for i in lista_cap_shape:
    diferen??as_cap_shape.append((i- media_cap_shape)**2)
variancia_cap_shape=math.sqrt((sum(diferen??as_cap_shape))/ntrain)
lista_variancias.append(variancia_cap_shape)

diferen??as_cap_surface=[]
for i in lista_cap_surface:
    diferen??as_cap_surface.append((i- media_cap_surface)**2)
variancia_cap_surface=math.sqrt((sum(diferen??as_cap_surface))/ntrain)
lista_variancias.append(variancia_cap_surface)

diferen??as_cap_color=[]
for i in lista_cap_color:
    diferen??as_cap_color.append((i- media_cap_color)**2)
variancia_cap_color=math.sqrt((sum(diferen??as_cap_color))/ntrain)
lista_variancias.append(variancia_cap_color)

diferen??as_bruises=[]
for i in lista_bruises:
    diferen??as_bruises.append((i- media_bruises)**2)
variancia_bruises=math.sqrt((sum(diferen??as_bruises))/ntrain)
lista_variancias.append(variancia_bruises)

diferen??as_odores=[]
for i in lista_odores:
    diferen??as_odores.append((i- media_odores)**2)
variancia_odores=math.sqrt((sum(diferen??as_odores))/ntrain)
lista_variancias.append(variancia_odores)

diferen??as_gill_attachement=[]
for i in lista_gill_attachement:
    diferen??as_gill_attachement.append((i- media_gill_attachement)**2)
variancia_gill_attachement=math.sqrt((sum(diferen??as_gill_attachement))/ntrain)
lista_variancias.append(variancia_gill_attachement)

diferen??as_gill_spacing=[]
for i in lista_gill_spacing:
    diferen??as_gill_spacing.append((i- media_gill_spacing)**2)
variancia_gill_spacing=math.sqrt((sum(diferen??as_gill_spacing))/ntrain)
lista_variancias.append(variancia_gill_spacing)

diferen??as_gill_size=[]
for i in lista_gill_size:
    diferen??as_gill_size.append((i- media_gill_size)**2)
variancia_gill_size=math.sqrt((sum(diferen??as_gill_size))/ntrain)
lista_variancias.append(variancia_gill_size)

diferen??as_gill_color=[]
for i in lista_gill_color:
    diferen??as_gill_color.append((i- media_gill_color)**2)
variancia_gill_color=math.sqrt((sum(diferen??as_gill_color))/ntrain)
lista_variancias.append(variancia_gill_color)

diferen??as_stalk_shape=[]
for i in lista_stalk_shape:
    diferen??as_stalk_shape.append((i- media_stalk_shape)**2)
variancia_stalk_shape=math.sqrt((sum(diferen??as_stalk_shape))/ntrain)
lista_variancias.append(variancia_stalk_shape)

diferen??as_stalk_root=[]
for i in lista_stalk_root:
    diferen??as_stalk_root.append((i- media_stalk_root)**2)
variancia_stalk_root=math.sqrt((sum(diferen??as_stalk_root))/ntrain)
lista_variancias.append(variancia_stalk_root)

diferen??as_stalk_surface_above_ring=[]
for i in lista_stalk_surface_above_ring:
    diferen??as_stalk_surface_above_ring.append((i- media_stalk_surface_above_ring)**2)
variancia_stalk_surface_above_ring=math.sqrt((sum(diferen??as_stalk_surface_above_ring))/ntrain)
lista_variancias.append(variancia_stalk_surface_above_ring)

diferen??as_stalk_surface_below_ring=[]
for i in lista_stalk_surface_below_ring:
    diferen??as_stalk_surface_below_ring.append((i- media_stalk_surface_below_ring)**2)
variancia_stalk_surface_below_ring=math.sqrt((sum(diferen??as_stalk_surface_below_ring))/ntrain)
lista_variancias.append(variancia_stalk_surface_below_ring)

diferen??as_stalk_color_above_ring=[]
for i in lista_stalk_color_above_ring:
    diferen??as_stalk_color_above_ring.append((i- media_stalk_color_above_ring)**2)
variancia_stalk_color_above_ring=math.sqrt((sum(diferen??as_stalk_color_above_ring))/ntrain)
lista_variancias.append(variancia_stalk_color_above_ring)

diferen??as_stalk_color_below_ring=[]
for i in lista_stalk_color_below_ring:
    diferen??as_stalk_color_below_ring.append((i- media_stalk_color_below_ring)**2)
variancia_stalk_color_below_ring=math.sqrt((sum(diferen??as_stalk_color_below_ring))/ntrain)
lista_variancias.append(variancia_stalk_color_below_ring)

diferen??as_veil_type=[]
for i in lista_veil_type:
    diferen??as_veil_type.append((i- media_veil_type)**2)
variancia_veil_type=math.sqrt((sum(diferen??as_veil_type))/ntrain)
lista_variancias.append(variancia_veil_type)

diferen??as_veil_color=[]
for i in lista_veil_color:
    diferen??as_veil_color.append((i- media_veil_color)**2)
variancia_veil_color=math.sqrt((sum(diferen??as_veil_color))/ntrain)
lista_variancias.append(variancia_veil_color)

diferen??as_ring_number=[]
for i in lista_ring_number:
    diferen??as_ring_number.append((i- media_ring_number)**2)
variancia_ring_number=math.sqrt((sum(diferen??as_ring_number))/ntrain)
lista_variancias.append(variancia_ring_number)

diferen??as_ring_type=[]
for i in lista_ring_type:
    diferen??as_ring_type.append((i- media_ring_type)**2)
variancia_ring_type=math.sqrt((sum(diferen??as_ring_type))/ntrain)
lista_variancias.append(variancia_ring_type)

diferen??as_spore_print_color=[]
for i in lista_spore_print_color:
    diferen??as_spore_print_color.append((i- media_spore_print_color)**2)
variancia_spore_print_color=math.sqrt((sum(diferen??as_spore_print_color))/ntrain)
lista_variancias.append(variancia_spore_print_color)

diferen??as_population=[]
for i in lista_population:
    diferen??as_population.append((i- media_population)**2)
variancia_population=math.sqrt((sum(diferen??as_population))/ntrain)
lista_variancias.append(variancia_population)

diferen??as_habitat=[]
for i in lista_habitat:
    diferen??as_habitat.append((i- media_habitat)**2)
variancia_habitat=math.sqrt((sum(diferen??as_habitat))/ntrain)
lista_variancias.append(variancia_habitat)
#subtrair a media e dividir pelo desvio padr??o para cada atributo
#se o desvio==0 atribuir o seu valor a 0
lista_ntrain_padronizada=[]
lista_testetrain=[]
for lista in lista_ntrain_traduzida:
    c=0
    for i in lista:
        if lista_variancias[c]!=0:
            lista_testetrain.append((i-medias[c])/lista_variancias[c])
            
        else:
            lista_testetrain.append(0)
        c=c+1
                 
    lista_ntrain_padronizada.append(lista_testetrain)
    lista_testetrain=[]
lista_ntest_padronizada=[]
lista_teste=[]
for lista in lista_ntest_traduzida:
    c=0
    for i in lista:
        if lista_variancias[c]!=0:
            lista_teste.append((i-medias[c])/lista_variancias[c])
            
        else:
            lista_teste.append(0)
        c=c+1
        
            
    lista_ntest_padronizada.append(lista_teste)
    lista_teste=[]
###################calcular a distancia euclediania de cada valor xtest em rela????o a todos os vetores xtrain################
def distancia(vetor1, vetor2):
  distancias_interna=[]
  lista_diferen??as=[]
  for x, i in zip(vetor1, vetor2):
    diferen??a=((x-i)**2)
    lista_diferen??as.append(diferen??a)
  distancias_interna.append(sum(lista_diferen??as))
  return distancias_interna
# def distancia(vetor1, vetor2):
#   dim, soma = len(vetor1), 0
#   for i in range(dim):
#       soma += math.pow(vetor1[i] - vetor2[i], 2)
#   return soma
distancias=[]
distancias_teste=[]
for lista in lista_ntest_padronizada:
    for listas in lista_ntrain_padronizada:
        distancias.append(distancia(lista,listas))

        
#achar os k mais proximos

# menores_distancias=[]
# indices=[]
# indices_separados=[] 
w=0
c=ntrain
diferen??as_separadas=[]
while w<len(distancias) and c<len(distancias)+1:
    diferen??as_separadas.append(distancias[w:c]) #ntest listas de ntrain elementos
    w=w+ntrain
    c=c+ntrain
menores_distancias=[]
##achar os menores valores
lista_menores_valores=[]
lista_sele????o=copy.deepcopy(diferen??as_separadas)
for lista in lista_sele????o:
    lista.sort()
    lista_menores_valores.append(lista[:k])
#achar o indice dos menores valores: acessar cada lista dentro diferen??as_separadas, acessar  cada valor dentro de lista_menores valores
# retornar o index para cada valor da lista_menores_valores dentro da lista interna de diferen??as_separadas
lista_indices=[]
for lista, x in zip(diferen??as_separadas,lista_menores_valores):
    for i in x:
        lista_indices.append (lista.index(i))


#separar em listas de k elementos
f=0
j=k
indices_separdos=[]
while f<len(lista_indices) and k<len(lista_indices)+1:
    indices_separdos.append(lista_indices[f:j]) #ntest listas de ntrain elementos
    f=f+k
    j=j+k

rotulos_interna=[]
rotulos_externa=[]
for lista in indices_separdos:
    for i in lista:
        rotulos_interna.append(lista_rotulos_train[i])
    rotulos_externa.append(rotulos_interna)
    rotulos_interna=[]

lista_rotulos_test=[]
for lista in rotulos_externa:
    contador_p=0
    contador_e=0
    for i in lista:
        if i=='p':
            contador_p=contador_p+1
        elif i=='e':
            contador_e=contador_e+1
    if contador_p>contador_e:
        lista_rotulos_test.append('p')
    elif contador_p<contador_e:
        lista_rotulos_test.append('e')
for i in lista_rotulos_test:
    print(i)