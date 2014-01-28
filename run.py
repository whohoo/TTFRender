#-*- coding: utf-8 -*-

from TTFRender import generate, get_token_list

# read content.txt file
txtFile = open('content.txt')
str = txtFile.read()
print(str)
token_list = get_token_list(str)
src_ttf_file = "新蒂小丸子小学版"
out_ttf_file   = "xindixiaowanzhi.ttf"

# generate new font file
generate(token_list, src_ttf_file, out_ttf_file)
