


执行 :PluginInstall


提示 不是编辑器命令

检查
```
$ git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

2. 安装Vundle
首先，如果你的Linux系统上还没有Git，安装它（http://ask.xmodulo.com/install-git-linux.html）。

下一步，创建一个目录，Vim插件下载后将安装到该目录下。默认情况下，该目录位于~/.vim/bundle。

$ mkdir -p ~/.vim/bundle
现在安装Vundle，如下所示。请注意：Vundle本身是另一种Vim插件。因而，我们将Vundle安装在之前创建的~/.vim/bundle下。

$ git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

3. 配置Vundle
现在设置你的.vimrc文件，如下所示：

```
set nocompatible              " 这是必需的
filetype off                  " 这是必需的

" 你在此设置运行时路径
set rtp+=~/.vim/bundle/Vundle.vim  

" vundle初始化
call vundle#begin()  

" 这应该始终是第一个
Plugin 'gmarik/Vundle.vim'

" 该例子来自https://github.com/gmarik/Vundle.vim README
Plugin 'tpope/vim-fugitive'  

" 来自http://vim-scripts.org/vim/scripts.html的插件
Plugin 'L9'  

"未托管在GitHub上的Git插件
Plugin 'git://git.wincent.com/command-t.git'  

"本地机器上的git软件库（即编写自己的插件时）
Plugin 'file:///home/gmarik/path/to/plugin'  

" sparkup vim脚本在名为vim的该软件库子目录下。
" 传递路径，合理设置运行时路径。
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}

" 与L9避免名称冲突
Plugin 'user/L9', {'name': 'newL9'}  

"每个插件都应该在这一行之前  

call vundle#end()            " required
```


4. Vundle命令用法
一旦你用Vundle设置好了插件，就可以使用几个Vundle命令，用Vundle来安装、更新、搜索和清理闲置未用的插件。

- 4.1  安装一个新的插件

PluginInstall命令会安装在你的.vimrc文件中列出来的所有插件。你还可以只安装某一个特定的插件，只要传递其名称。

:PluginInstall
:PluginInstall <plugin-name>
- 4.2 清理闲置未用的插件

如果你有任何闲置未用的插件，只要使用PluginClean命令，就可以清理它。

:PluginClean
- 4.3搜索插件

如果你想从所提供的插件列表安装一个插件，搜索功能就很有用。

:PluginSearch <text-list>
在搜索过程中，你可以在交互式分屏上安装、清理、研究或重新装入同一列表。安装插件不会自动装入你的插件。想自动装入插件，将插件添加到你的.vimrc文件。

这个功能也经常用，比如:PluginSearch taglist，完成搜索后，可以按下'i'进行安装


https://www.cnblogs.com/aaronLinux/p/6798898.html
