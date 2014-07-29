#-*- coding: utf-8 -*-

from TTFRender import generate, get_token_list

# read content.txt file
txtFile = open('content.txt')
str = txtFile.read()
token_list = get_token_list(str)
src_ttf_file = "MComicPRC-Medium"
out_ttf_file   = "MComicPRC-Medium"
print(out_ttf_file)
# generate new font file
generate(token_list, src_ttf_file, out_ttf_file)
