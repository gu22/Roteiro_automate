# -*- coding: utf-8 -*-
"""
TIRA AS ROTAS DO TXT

"""
import os.path
import easygui
import sys
import glob
import shutil
import os
import easygui
import re
from shutil import copyfile
from unidecode import unidecode



cd = easygui.enterbox("Nome Cd")


# cidade dt
# index= easygui.fileopenbox("Escolha o arquivo de orientacao",default="*.txt")

# rotas para extrair
#index2= easygui.fileopenbox(default="*.txt")


# if 'SECO' in index:
#     material = "SECO"
# else:
#     material = "LIQUIDO"
    
user_dir = easygui.diropenbox("escolha pasta com os txt de rotas")

Path_name = user_dir
Path_file = os.listdir(Path_name)
# user_dir = easygui.diropenbox()
# Path_name = user_dir
# Path_file = os.listdir(Path_name)

# index_open = open(index,'r',encoding='utf8')


# ----------------------------------------------------------------------






# index_busca=[]
# for i in index_open:
#     index_busca.append(i)

# catalogo = {}
# catalogo = []
# for i in index_busca:
#     cidade = unidecode(i)
#     cidade = (((" ").join(re.findall("[A-Za-z]\w+",cidade))))
# # for i in index_busca:
# #     cidade = unidecode(i)
# #     cidade = (((" ").join(re.findall("[A-Za-z]\w+",cidade))))
# #     catalogo.append(cidade)
    
#     dt = re.findall("[0-9]{10}",i)
#     dt = dt[0]+".txt"
#     catalogo.update({cidade:dt})
    # catalogo.append(cidade)

#------------------------------------------------------------------------------
    
   
material = "EXTRACT"    
c=0
a=0   

# arquivos= []
# for data in Path_file:
#     file = os.path.join(Path_name,data)
#     arquivos.append(file)


# veriq = []    
# for cy in index_busca: 
#     cidadeu = (" ").join(re.findall("[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]\w+",cy))
#     cidadeu = unidecode(cidadeu)
#     veriq.append(cidadeu)

# controlesystem = [] 


# texto_raw = []

# viagem =[ ]
out = []
ea = 0
eu = 0
testador =0
contador = 0
explicito=[]
#=============================================================================
for item in Path_file:
    
    # for i in catalogo:
    #     if item in catalogo[i]:
    #         cidade = i
    #     else:
    #         pass
    remessa = (item.split("."))[0]
    
    
    file = os.path.join(Path_name,item)
    
    # arquivo_txt = os.path.join(Path_name,catalogo[item])
    # try:
    #     arquivo_open = open (arquivo_txt,"r",encoding='utf-8')
    # except:
    #     out.append(arquivo_txt)
    #     testador+=1
    #     continue
#---------- abrindo arquivo 
    arquivo_open = open (file,"r",encoding='utf-8')
    
## ---------------- pegando linhas do arquivo    
    trajeto = []
    
    for linha in arquivo_open:
        trajeto.append(unidecode(linha))
        
    name_arquivo = (trajeto[-1].split(","))[1]
    name_arquivo = (" ").join(( re.findall("[A-Za-z]\w+",name_arquivo)))        
   
##-----------------------
        
     
        
     
    # roteiro=[]
           
    # for caminho in trajeto:
    #     for t in catalogo:
    #         if t in caminho:
    #             roteiro.append(caminho)
    #             cidade = t
    #         else:
    #             roteiro.append(caminho)
   
    
    
    roteiro = []       
    for caminho in trajeto:
      roteiro.append(caminho)
          
                
    
    contador+=1
    arquivo_open.close()
    
    rotas =[]
    adeq = []
    rodovias = []
    
    for i in roteiro:
        check1 = re.findall("[BR\s]+[0-9]{5}",i)
        check2 = re.findall("(([A-Z]{2})+[0-9]{3})",i)
        check3 = re.findall("(([A-Z]{2})+[0-9]{2})",i)
        
        if not check1:
            if not check2:
                if check3:
                    rotas.append(check3)
                    adeq.append(check3[0][0])
                    #print (check2)
                    with open(("{}-{}_Extract.txt".format(remessa,name_arquivo)),"a",encoding="utf-8") as escritor:
                        escritor.write(check3[0][0])
                        escritor.write("\n")
            else:
                rotas.append(check2)
                adeq.append(check2[0][0])
                 #print (check2)
                with open(("{}-{}_Extract.txt".format(remessa,name_arquivo)),"a",encoding="utf-8") as escritor:
                    escritor.write(check2[0][0])
                    escritor.write("\n")
                
    else:
        rotas.append(check1)
        #print (check1)
        with open(("{}-{}_Extract.txt".format(remessa,name_arquivo)),"a",encoding="utf-8") as escritor:
            escritor.write(check1[0])
            escritor.write("\n")

# organizando as rotas
    for item in adeq:
        text = item[0:2]+"-"+item[2:5]
        if text in rodovias:
            pass
        else:
            # text = item[0:2]+"-"+item[2:5]
            rodovias.append(text)
    
    with open((".ROTAS_{} - final.txt".format(cd)),"a",encoding="utf-8") as escritor:
        escritor.write((remessa+":"+name_arquivo+";"))
        escritor.write(",".join(rodovias))
        escritor.write("\n")
   
    
    
    
####------------------------------------------------------------------------    
# for item in catalogo:
    
#     arquivo_txt = os.path.join(Path_name,catalogo[item])
#     try:
#         arquivo_open = open (arquivo_txt,"r",encoding='utf-8')
#     except:
#         out.append(arquivo_txt)
#         break
    
    
#     trajeto = []
    
#     for linha in arquivo_open:
#         trajeto.append(unidecode(linha))
        
#     roteiro=[]
    
        
#     for caminho in trajeto:
#         if item in caminho:
#             roteiro.append(caminho)
#             explicito.append(item)
#             ea +=1
#             break
        
#         elif  "Trimble" in caminho:
#             break
        
#         else:
#             roteiro.append(caminho)
#             eu +=1
     
#     arquivo_open.close()

















# index_open.close()

# # XXX - Teste2 Mais uma tentativi
# for itens in nomedata:
#      index_ex = open(itens,'r',encoding='utf8')
     
#      for texto in index_ex:
#          texto_raw.append(unidecode(texto))
         
     
#      roteiro = []
#      destino = []
     
#      for cidade in veriq:   
#          for caminho in texto_raw:
#              if cidade in caminho:
#                  viagem.append(cidade)
#                  destino.append(cidade)
#                  print(cidade+"   +++++++++++++\n")
#                  veriq.remove(cidade)
#                  break
     
#      for cidades in destino:
#         roteiro=[]
#         for caminho in texto_raw:
#             if cidades in caminho:
#                 roteiro.append(caminho)
#                 break
#             else:
#                 roteiro.append(caminho)
#                 if "Trimble" in caminho:
#                     break
                
#         print(cidades+'   ^^^^^^^^^^^^^\n')        
    
#         with open((cidades+".txt"),"w",) as wr:
#             for dado in roteiro:
#                 wr.write(dado)
#                 wr.write("\n")
#             roteiro=[]
                     
         
   













   
# for nome in nomedata:   
#     index_ex = open(nome,'r',encoding='utf8')
        
#     index_acha=[]
#     for i in index_ex:
#         index_acha.append(i) 
    
#     indexr = []
    
#     rota = []
   
#     #HINT adicionar um loop for verificando arquivo de orientação
    
            
#         # Pega o nome da cicade 
#     # veriq = (" ").join(re.findall("[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]\w+",cy))
        
#     cidadecontrole=[]
        
#     for cc in veriq:
#                                 # extraido os textos
#         for idx in index_acha:
#             if cc in idx:
#                 if not cc in controlesystem:
#                     cidadecontrole.append(cc)
                
#                     break
#             else:
#                 pass
#         print(cidadecontrole)
            
#     for itemi in cidadecontrole:
#       if not itemi in controlesystem:   
#         for add in index_acha:
#             if itemi in add:
#                 indexr.append(add)
#                 break
#             else:
#                 indexr.append(add)
#         # print(indexr)    
                
#                 # indexr.append(idx)
#                 # break
#         # if index_acha[a] in indexr:
#         #     break
            
#         # else:
#     #     a+=1
#     # c+=1
        
#         adeq =[]
        
#         #nome arquivo
#         cidade= itemi
#         arq_city = cidade +".txt"
        
#         # extaindo as rotas
#         for i in indexr:
#             check1 = re.findall("[BR\s]+[0-9]{5}",i)
#             check2 = re.findall("(([A-Z]{2})+[0-9]{3})",i)
#             if not check1:
#                 if check2:
#                     rota.append(check2)
#                     adeq.append(check2[0][0])
#                     #print (check2)
#                     with open(arq_city,"a",encoding="utf-8") as escritor:
#                         escritor.write(check2[0][0])
#                         escritor.write("\n")
                    
#             else:
#                 rota.append(check1)
#                 #print (check1)
#                 with open(arq_city,"a",encoding="utf-8") as escritor:
#                     escritor.write(check1[0])
#                     escritor.write("\n")
        
                
#         # print(rota)
#         # print
#         rotas =[]
    
#     # organizando as rotas
#         for item in adeq:
#             text = item[0:2]+"-"+item[2:5]
#             rotas.append(text)
        
#         with open((".ROTAS_{}.txt".format(material)),"a",encoding="utf-8") as escritor:
#             escritor.write((cidade+";"))
#             escritor.write(",".join(rotas))
#             escritor.write("\n")
   
#         controlesystem.append(itemi)



            
                
# print(a)
# ex = len(index_acha)-a
# a+=1
# for i in range (ex):
  
#TIP re.findall("[BR\s]+[0-9]{5}",index_acha[1])
#TIP >>> desconsiderar >> re.findall("[BR]+[0-9]{3}",index_acha[9])
#TIP re.findall("([A-Z]{2})+[0-9]{3}",index_acha[9])
    
  
    
# for item in Path_file:
#     file = os.path.join(Path_name,item)
#     rota = open(file,'r',encoding='utf8')