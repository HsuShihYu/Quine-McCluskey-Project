# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:11:02 2018

@author: lenovo
"""
import sys

def p_dic(new_list,subnumber):
    p_dict = {}    
    for i in range(6,6+subnumber):
        if new_list[i][1] not in p_dict:
            p_dict[new_list[i][1]] = [new_list[i][3]]
        else:
            p_dict[new_list[i][1]].append(new_list[i][3])
    if int(new_list[2][1]) > 1:
        for i in p_dict:
            for j in range(len(p_dict[i])):
                p_dict[i][j] = int(p_dict[i][j],2)
    return p_dict 

def list2decimal(p_list):
    ans = 0
    length = len(p_list)
    for i in range(length):
        ans = ans + int(p_list[length-i-1])*pow(2,i)
    return ans

def tables(new_list,subnumber):
    table = {}
    for i in range(6,6+subnumber):
        if new_list[i][1] not in table:
            table[new_list[i][1]] = [new_list[i][2]]
        else:
            table[new_list[i][1]].append(new_list[i][2])
    return table

def p_next(p_list,table):
    temp_table = table.copy()
    for x in p_list:
        for i in x:
            length = len(table[i])
            for j in range(length):
                for k in p_list:
                    element = table[i][j]
                    if element in k:
                        temp_table[i][j] = k
    p_next_list = []
    temp = -1
    temp_list = []
    while len(temp_list)!=len(temp_table.keys()):
        for x in p_list:
            for i in x:
                if i not in temp_list:
                    p_next_list.append([])
                    temp = temp+1
                    temp_list.append(i)
                    p_next_list[temp].append(i)
                    for j in x:
                        if j not in temp_list:
                            if i!=j:
                                if temp_table[i] == temp_table[j]:
                                    p_next_list[temp].append(j)
                                    temp_list.append(j)
    return p_next_list

############# The following is Main, and I use Partition method to solve the question ###############

################# read file and transfer to new_list ##########################
stg_file = open(sys.argv[1],'r')        
stg_list = stg_file.read().splitlines()
new_list =[]
for line in stg_list:
    line = line.split()
    new_list.append(line)    
subnumber = (2**int(stg_list[1][3]))*int(stg_list[4][3])
p_dict = p_dic(new_list,subnumber)
init_dict = {}
for x in p_dict:
    for i in range(10000):
        if list2decimal(p_dict[x]) == i and i not in init_dict:
            init_dict[i] = [x]
        elif list2decimal(p_dict[x]) == i:
            init_dict[i].append(x)
############ find p0_list #####################################################
p0_list = []                      
for i in init_dict:
    p0_list.append(init_dict[i])

########## create table to find next_list #####################################
table = tables(new_list,subnumber)
p_before_list = p0_list.copy()
p_next_list = p_next(p0_list,table)


while p_next_list != p_before_list:
    table = tables(new_list,subnumber)
    p_before_list = p_next_list
    p_next_list = p_next(p_before_list,table)
    
########## complete p_next_list ###############################################
temp_p_list = []
trans_list = []
for i in p_next_list:
    temp_p_list.append(i[0])
for i in range(6,6+subnumber):
    if new_list[i][1] in temp_p_list:
        trans_list.append(new_list[i])
for i in p_next_list:
    if len(i) >= 2:
        for x in trans_list:
            if i[1] in x:
                x[2] = i[0]
########### trans_list is done ################################################

temp_state_list = []
for i in trans_list:
    if i[1] not in temp_state_list:
        temp_state_list.append(i[1])

final_list = []
for i in range(3):
    final_list.append((new_list[i]))
final_list.append(['.p',str(len(temp_state_list)*(2**int(stg_list[1][3])))])
final_list.append(['.s',str(len(temp_state_list))])
final_list.append(['.r',str(temp_state_list[0])])
for i in trans_list:
    final_list.append(i)
final_list.append(['.end_kiss'])

dot_dic = {}
for i in trans_list:
    if i[1]+ '->' + i[2] not in dot_dic:
        dot_dic[i[1]+ '->' + i[2]] = [i[0] + "/" + i[3]]
    else:
        dot_dic[i[1]+ '->' + i[2]].append(i[0] + '/' + i[3])
        
output_file_kiss = open(sys.argv[2], 'w')
for i in final_list:
    i = " ".join(i)
    output_file_kiss.write(i+"\n")

output_file_dot = open(sys.argv[3], 'w')
output_file_dot.write("digraph STG {" +"\n"+"  rankdir = LR;"+"\n"+"\n"+"INIT [shape = point]"+"\n")
for i in temp_state_list:
    output_file_dot.write(i+"[label=\"" + i + "\"];" +"\n" )
output_file_dot.write('INIT ->' + temp_state_list[0] + "\n" )
for i in dot_dic:
    output_file_dot.write(i +"[label=\"")
    dot_dic[i] = ",".join(dot_dic[i])
    output_file_dot.write(dot_dic[i] + "\"];" + "\n")
output_file_dot.write("}")


"""
ex: exe input output.kiss output.dot = argv[0] argv[1] argv[2] argv[3]
"""
    

        
        
        
