## TTFRender Module ##

TTFRender Module 是中文 WebFont && WebFont Loader 的解决方案。WebFont 作为 css3
中比较好的技术被国外广为应用，配合 google webfont loader 方案能很好的实现页面字
体动态加载，并且脱离了终端字体库的限制。

WebFont 纵然很好，但是目前没有较好的中文解决方案。一是 google 等其他 WebFont 厂
商没有支持。二来是因为中文字库太大，影响 UE。

TTFRender 就是为了解决这一问题而出现的。我们只需要提供特定字体和需要支持的字列
表，然后便可以生成符合应用的字符，有效的节省了带宽与时间，并提升了 UE。

#### How To Use ####

    #-*- coding: utf-8 -*-
    
    from TTFRender import generate
    
    token_list = ["一","三","测","A","B","C","D","E"]
    ttf_file = "new_kai.ttf"
    
    generate(token_list, "kai", ttf_file)

这样就生成了符合应用的字体，之后便可以通过 WebFont && WebFont Loader 引入。


#### API ####

* TTFRender/__init__.py
导出模块功能。

* TTFRender/helper.py 
模块 Helper Functions.

    * _unicode

    返回 string 的 unicode 值。

    * get_ttf_file

    根据字体返回指定的字体文件。

    * get_token_list

    返回字列表

* TTFRender/parser.py

TTFRender Core Module.
