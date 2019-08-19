--------------------------- 环境 ---------------------------

1. CentOS系统
2. 到Maven仓库的路由需可达：route add default gw 172(192).31(168).179.99

--------------------------- 安装 ---------------------------

* 对于已经装好了Python3的环境可直接进行安装即可：

                     $python3 setup.py

* 对于未安装Python3的环境需要先安装Python3，大概10-15分钟：

            $python setup.py --install-python3
     （如果Python2也没安装的话，可以看代码按步骤手动安装Python3）

  然后再：

                      $python3 setup.py

--------------------------- 使用 ---------------------------

\path\to\generate\code$ seerengine

--------------------------- 注意 ---------------------------

1. 安装脚本不会更改~/.m2/settings.xml文件，H3C的Maven仓库URL将在生成的pom.xml文件中指定
2. 安装脚本会重置~/.pip/pip.conf文件，将PyPI仓库地址指向H3C内网代理，这样的好处是以后可以使用pip install一键安装Python依赖
3. 如果使用--install-python3安装Python3，脚本会修改系统yum源
4. ref文件夹里是官方示例代码供参考