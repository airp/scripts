#----------------------------------------
# 常用脚本描述文档
#----------------------------------------
1.cdscuts_glob_echo, cdscuts_list_echo脚本(辅助cdg命令进入项目书签).
    配合fzf, ~/.cdg_paths, ~/.zshrc使用.
    ln -s 到/usr/bin/目录下.
    赋予755权限.
    zsh中, cd命令进入不了目录名后面带空白字符的路径,fzf列表显示则无法包含空格以及#注释内容,后面再优化.
