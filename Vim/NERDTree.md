NERDTree

安装好后，命令行中输入vim，打开vim后，在vim中输入:NERDTree，你就可以看到NERDTree的效果了。

```
ctrl + w + h    光标 focus 左侧树形目录
ctrl + w + l    光标 focus 右侧文件显示窗口
ctrl + w + w    光标自动在左右侧窗口切换
ctrl + w + r    移动当前窗口的布局位置
o       在已有窗口中打开文件、目录或书签，并跳到该窗口
go      在已有窗口 中打开文件、目录或书签，但不跳到该窗口
t       在新 Tab 中打开选中文件/书签，并跳到新 Tab
T       在新 Tab 中打开选中文件/书签，但不跳到新 Tab
i       split 一个新窗口打开选中文件，并跳到该窗口
gi      split 一个新窗口打开选中文件，但不跳到该窗口
s       vsplit 一个新窗口打开选中文件，并跳到该窗口
gs      vsplit 一个新 窗口打开选中文件，但不跳到该窗口
!       执行当前文件
O       递归打开选中 结点下的所有目录
x       合拢选中结点的父目录
X       递归 合拢选中结点下的所有目录
e       Edit the current dif
双击    相当于 NERDTree-o
中键    对文件相当于 NERDTree-i，对目录相当于 NERDTree-e
D       删除当前书签
P       跳到根结点
p       跳到父结点
K       跳到当前目录下同级的第一个结点
J       跳到当前目录下同级的最后一个结点
k       跳到当前目录下同级的前一个结点
j       跳到当前目录下同级的后一个结点
C       将选中目录或选中文件的父目录设为根结点
u       将当前根结点的父目录设为根目录，并变成合拢原根结点
U       将当前根结点的父目录设为根目录，但保持展开原根结点
r       递归刷新选中目录
R       递归刷新根结点
m       显示文件系统菜单
cd      将 CWD 设为选中目录
I       切换是否显示隐藏文件
f       切换是否使用文件过滤器
F       切换是否显示文件
B       切换是否显示书签
q       关闭 NerdTree 窗口
?       切换是否显示 Quick Help


```

#下载和配置 NERDTree插件的官方地址如下，可以从这里获取最新的版本 https://github.com/scrooloose/nerdtree 下载zip安装包 或者使用下面官网源文件安装方法

我的实验环境是centos6.6,其他版本可能有些不同。 安装方法很简单，先把压缩文件下载下来，解压后将plugin目录下的NERD_tree.vim拷贝~/.vim/plugin以及doc目录下的NERD_tree.txt拷贝到~/.vim/doc. ~表示当前用户的目录，我的环境中没有~/.vim ~/.vim/plugin ~/.vim/doc ，待会会创建，如果你的版本有，那就更好了。
```
wget http://www.vim.org/scripts/download_script.php?src_id=17123 -O nerdtree.zip
unzip nerdtree.zip

mkdir -p ~/.vim/{plugin,doc}

cp plugin/NERD_tree.vim ~/.vim/plugin/
cp doc/NERD_tree.txt ~/.vim/doc/

```
安装好后，命令行中输入vim，打开vim后，在vim中输入:NERDTree，你就可以看到NERDTree的效果了。

为了方便起见，我们设置一下快捷键，在~/.vimrc 文件中添加下面内容， 我的centos6.6还是没有这个~/.vimrc，没关系，创建一个，直接 vim ~/.vimrc 然后添加 " NERDTree map <F10> :NERDTreeToggle<CR> 这样打开vim后，只要按键盘上的F10就可以显示和隐藏NERDTree的文件浏览了。

只会 F10, 那也太没技术含量了，下面又是一波快捷键，学习吧。

https://my.oschina.net/VASKS/blog/388907
