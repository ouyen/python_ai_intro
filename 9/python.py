# 读取文件，如有报错，可根据报错信息安装xlrd或者openpyxl
import pandas as pd
# table = pd.read_excel('poem.xlsx')
word_list_df = pd.read_excel('wordlist.xlsx')

word_list=set(word_list_df.word)

# 实现前向最大匹配分词算法
# string: 待分词的串
# word_list: 词表
# max_length: 词表中词语的最大长度
def cut(string, word_list, max_length):
    # TODO
    rlt=[]
    end_pos=min(max_length,len(string))
    start_pos=0
    while 1:
        if(start_pos==end_pos):
            start_pos+=1
            end_pos=min(start_pos+max_length,len(string))
        if(string[start_pos:end_pos] in word_list):
            rlt.append(string[start_pos:end_pos])
            start_pos=end_pos
            end_pos=min(start_pos+max_length,len(string))
        else:
            end_pos-=1
        if(start_pos==len(string)):
            break
    return rlt

print(cut('洛陽舊有( 一作出) 神明宰',word_list,3))