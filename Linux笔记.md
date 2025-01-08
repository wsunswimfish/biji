# Linux

GNU:GNU`s Not Unix

GPL:GNU通用公共许可证，GNU General Public License

> Linux应成为GNU/Linux
> 
> Linux一般指内核
> 
> Linux绝大多数都是无界面的

------

## 001 计算机硬件之冯诺依曼体系

+ 计算机处理的数据和指令都是二进制表示
+ 顺序执行程序
+ 计算机硬件是由运算器、控制器、存储器、输入设备、输出设备五部分组成

## 002 Linux系统的分支

- Redhat
  
  - 代表作：CentOS

- Debian
  
  - 代表作：Ubuntu
  
  **注：**版本选择一般用双不用单

## 003 Linux常用命令

+ type xxx
  
  返回命令类型，一般会有内部命令、关键字、脚本文件等。

+ help xxx
  
  显示内部命令的帮助

+ man xxx
  
  显示外部命令的帮助

+ whereis
  
  查询**命令**文件的位置

+ file
  
  查看文件的类型

+ who
  
  查看当前在线用户

+ whoami
  
  查看我是谁

+ pwd
  
  查看我在哪

+ uname -a
  
  查看内核信息

+ echo
  
  打印语句

+ clear
  
  清屏

+ history
  
  历史命令

## 004 Linux特殊符号

+ .
  
  文件名前有.代表是隐藏文件

+ $
  
  变量

+ *
  
  通配符

+ ~
  
  当前用户的家目录

## 005 Linux文件系统

> Linux万物万事皆文件

+ /
  
   根目录

+ bin
  
  脚本、命令目录

+ boot
  
  系统启动目录

+ dev
  
  设备目录

+ etc
  
  配置文件目录

+ home
  
  各用户家目录

+ lib
  
  库文件目录

+ lib64
  
  64位库文件目录

+ media
  
  多媒体

+ mnt
  
  设备挂接目录

+ opt
  
  软件安装目录

+ proc
  
  进程目录

+ root
  
  root用户家目录

+ run
  
  运行时系统变量目录

+ sbin
  
  增强型bin文件

+ srv
  
  系统启动需要数据

+ sys
  
  内核文件

+ tmp
  
  临时文件目录

+ usr
  
  用户共享

+ var
  
  系统变量、信息，区别于tmp，重启不丢失。

## 006 Linux文件操作命令

+ cd 

+ ll、ls

+ mkdir
  
  + mkdir a
  + mkdir -p a/b/c 
  + mkdir -p a/{b,c,d}

+ rmdir
  
  删除时文件夹必须为空
  
  + rmdir a

+ cp
  
  -r 一起拷贝其下的子目录

+ mv
  
  + 移动文件
  + 文件更名

+ rm
  
  + 删除文件。-f 强制删除
  + 删除文件夹。 -r

+ touch
  
  + 生成文件
  + 对于存在的文件，统一访问修改改变时间

+ stat
  
  查看文件基本信息

+ ln
  
  + ln     硬连接，源文件删除后改文件依然可用。
  + ln -s 软连接，源文件删除后连接无效。

+ cat / tac
  
  查看文件内容

+ more
  
  分页查看文件

+ head / tail
  
  从前后方向显示指定的行数 
  
  + -f 通过文件Inode获取
  + -F 通过文件名称获取

+ find
  
  搜索指定的文件
  
  + find /  -name xxx
  
  + **参数列表**
    
    | 参数                | 描述                                            |
    | ----------------- | --------------------------------------------- |
    | -name             | 匹配名称                                          |
    | -perm             | 匹配权限（mode为完全匹配，-mode为包含即可）                    |
    | -user             | 匹配所有者                                         |
    | -group            | 匹配所有组                                         |
    | -mtime -n +n      | 匹配修改内容的时间（-n指n天以内，+n指n天以前）                    |
    | -atime -n +n      | 匹配访问文件的时间（-n指n天以内，+n指n天以前）                    |
    | -ctime -n +n      | 匹配修改文件权限的时间（-n指n天以内，+n指n天以前）                  |
    | -nouser           | 匹配无所有者的文件                                     |
    | -nogroup          | 匹配无所有组的文件                                     |
    | -newer f1 !f2     | 匹配比文件f1新但比f2旧的文件                              |
    | -type b/d/c/p/l/f | 匹配文件类型（后面的字幕字母依次表示块设备、目录、字符设备、管道、链接文件、文本文件）   |
    | -size             | 匹配文件的大小（+50KB为查找超过50KB的文件，而-50KB为查找小于50KB的文件） |
    | -prune            | 忽略某个目录                                        |
    | -exec …… {}\;     | 后面可跟用于进一步处理搜索结果的命令                            |
    | -ok …… {}\;       | 后面可跟用于进一步处理搜索结果的命令（执行操作需确认）                   |

## 0007 Linux VIM

+ G
  
  转到最后一行

+ gg
  
  转到第一行

+ 6gg
  
  转到第6行，：set nu显示行号

+ a
  
  向右移动

+ A
  
  移到行尾

+ h
  
  向左移动

+ H
  
  移动到首行

+ dd
  
  删除当前行

+ 3dd
  
  删除3行

+ w
  
  下个单词

+ 3w
  
  下3个单词

+ dw
  
  删除一个单词

+ 3dw
  
  删除3个单词

+ u
  
  撤销前一个操作

+ .
  
  回退u执行的操作

+ yw
  
  复制1个词

+ 3yw
  
  复制3个词

+ yy
  
  复制1行

+ 3yy
  
  复制3行

+ p
  
  粘贴

+ 6p
  
  粘贴6次

+ x
  
  剪切1个词

+ 3x
  
  剪切3个词

+ hjkl
  
  方向键

### 光标移动

| 按键      | 说明                                  |
| ------- | ----------------------------------- |
| h、←     | 光标左移一个字符，配合n使用，可实现光标移动n个字符。         |
| j、↓     | 光标下移一个字符，配合n使用，可实现光标移动n个字符。         |
| k、↑     | 光标上移一个字符，配合n使用，可实现光标移动n个字符。         |
| l、→     | 光标右移一个字符，配合n使用，可实现光标移动n个字符。         |
| 数字0     | 光标移到本行开头                            |
| Shift+6 | 光标移动到本行第一个非空字符                      |
| Shift+4 | 光标移动到本行行尾                           |
| Ctrl+f  | 下翻页                                 |
| Ctrl+b  | 上翻页                                 |
| gg      | 光标移动到文件第一行行首                        |
| ngg     | 光标移动到指定行行首，如5gg，第5行行首。行号可用set nu设置。 |

### 基本编辑

+ 插入
  
  | 按键  | 说明                      |
  | --- | ----------------------- |
  | i   | 变为编辑模式，当前字符前插入。         |
  | a   | 变为编辑模式，当前字符后插入。         |
  | A   | 变为编辑模式，光标移动到当前行尾。       |
  | o   | 在当前行下方插入空行。可配合n使用，插入多行。 |
  | O   | 在当前行上方插入空行。可配合n使用，插入多行。 |

+ 删除
  
  | 按键                  | 说明                         |
  | ------------------- | -------------------------- |
  | x（del）、X（backspace） | 向后或向前删除一个字符，可配合n使用，删除多个字符。 |
  | dw                  | 删除当前单词                     |
  | d0                  | 删除当前单词到行首。                 |
  | d$                  | 删除当前单词到行尾。                 |
  | dd                  | 删除当前行整行。可配合n使用，删除当前行开始的n行。 |
  
  u：恢复
  
  ctrl+r：重复

+ 剪切、复制、粘贴与合并行
  
  | 按键  | 说明                       |
  | --- | ------------------------ |
  | yy  | 复制当前行。可配合n使用，复制当前行开始的n行。 |
  | yw  | 复制当前单词。                  |
  | y0  | 复制当前单词到行首。               |
  | y$  | 复制当前单词到行尾。               |
  | p、P | 将复制的内容粘贴到当前位置的下一行或上一行。   |
  | J   | 将当前行和下一行合并成一行。           |

+ 查找和替换
  
  | 按键  | 说明  |
  | --- | --- |
  |     |     |
  |     |     |
  |     |     |
  |     |     |
  |     |     |
  |     |     |

## 008 Linux文件传输

+ Linux与Windows/macOS互传

+ 安装lrzsz
  
    Yum install lrzsz -y
  
  + rz
    
    上传
  
  + sz 文件名
    
    下载

+ Linux与Linux互传
  
  + scp 源 目标
  + scp 文件  用户名@IP地址：/路径/
  + 拷贝文件夹，加 -r

## 009 Linux文件系统命令

+ df
  
  查看分区信息 df -h

+ du
  
  查看指定文件的大小 du -h --max-depth=1 

+ tar
  
  文件压缩和解压缩
  
  + tar -zx(解压)v(过程)f(文件)  xxx.tar
  + tar -zc(压缩)f(文件) xxx.tar(压缩后的名字)  xxx(源文件)

+ zip / unzip
  
  文件压缩和解压缩
  
  + unzip xxx.zip
  + zip -r xxx.zip xxx

## 010 Linux 网络命令

+ ifconfig
  
  + 新版本用IP代替

+ ip
  
  + ip addr show
  + ip addr add/del 10.0.2.10/24 dev enp0s3
  + ip link show
  + ip link set enp0s3 up/down
  + ip route show
  + ip route add  10.0.2.0/24 via 10.0.2.2 dev enp0s3
  + ip route add default  via 10.0.2.2 dev enp0s3
  + ip route del default 
  + Systemctl restart network 生效

+ 网络配置文件
  
  （4中方式：图形界面、配置文件、nmtui、nmcli）
  
  + /etc/sysconfig/network-scripts/ifc-网卡设备名
    + DEVICE= " 设备名"
    + ONBOOT ="yes"/"no"    开机是否启动
    + BOOTPROTO="static/dhcp/no"     若设置多网口绑定，则no
    + IPADDR="10.0.2.10"    ip地址
    + NETMASK="255.255.255.0"    子网掩码
    + PREFIX="24"    子网掩码，同上。
    + DNS1="8.8.8.8"    主DNS
    + DOMAIN="114.114.114.114"    辅助DNS
  + /etc/sysconfig/network-script/route-网卡设备名
    + 用于修改了默认路由
    + 添加 10.0.2.0/24 via 10.0.2.2 

+ netstat
  
  + netstat -anp 显示当前端口监听状态
  + netstat -r 显示核心路由表

+ ping 测试地址通断

+ telnet 测试端口通断

+ curl 获取网页内容
  
  + curl -X get http://www.baidu.com

## 011 Linux 防火墙

centos 7+中，使用firewall代替了iptables。

> Firewalld是一种提供了支持网络/防火墙区域(zone)定义网络链接以及接口安全等级的动态防火墙管理工具，它自身并不具备防火墙的功能，而是和iptables一样需要通过内核的netfilter来实现，也就是说firewalld和 iptables一样，他们的作用都是用于维护规则，而真正使用规则干活的是内核的netfilter，只不过firewalld和iptables的结构以及使用方法不一样罢了。

+ 配置文件
  
  + 系统配置文件
    
    /usr/lib/firewalld/ 尽量不要修改
  
  + 用户配置文件
    
    /etc/firewalld/ 
  
  + 服务配置文件
    
    /usr/lib/firewalld/services/ 
    
    与之对应的配置文件中记录了各项服务所使用的 tcp/udp 端口，在最新版本的 firewalld 中默认已经定义了 70+ 种服务供我们使用。

+ 控制端口/服务
  
  + 可以通过指定端口或指定服务两种方式控制端口的开放
  + 用端口开放的用端口方式关闭，用服务开放的用服务方式关闭。
  + 指定端口时需指定协议tcp或udp。

+ 区域规则
  
  | 区域       | 默认规则策略                                                                      |
  | -------- | --------------------------------------------------------------------------- |
  | trusted  | 允许所有的数据包                                                                    |
  | home     | 拒绝流入的数据包，除非与输出的数据包相关，或是ssh、mdns、ipp-client、samba-client与dhcpv6-client服务则允许。 |
  | internal | 等同于home区域                                                                   |
  | work     | 拒绝流入的数据包，除非与输出的数据包相关，或是ssh、ipp-client与dhcpv6-client服务则允许。                   |
  | public   | 拒绝流入的数据包，除非与输出的数据包相关，或是ssh、dhcpv6-client服务则允许。                              |
  | external | 拒绝流入的数据包，除非与输出的数据包相关，或是ssh服务则允许。                                            |
  | dmz      | 拒绝流入的数据包，除非与输出的数据包相关，或是ssh服务则允许。                                            |
  | block    | 拒绝流入的数据包，除非与输出的数据包相关服务则允许。                                                  |
  | drop     | 拒绝流入的数据包，除非与输出的数据包相关服务则允许。                                                  |

+ firewall-cmd
  
  
  
  | 参数                        | 作用                                              |
  | ------------------------- | ----------------------------------------------- |
  | --get-default-zone        | 查询默认的区域名称                                       |
  | --set-default-zone=<区域名称> | 设置默认区域，永久生效。                                    |
  | --get-zones               | 显示可用的区域                                         |
  | --get-services            | 显示预先定义的服务                                       |
  | --get-active-zones        | 显示当前正在使用的区域与网卡名称                                |
  | --add-source=             | 将来源于此IP或子网的流量导向指定的区域                            |
  | --remove-source=          | 不再将此IP或子网的流量导向指定的区域                             |
  | --add-interface=<网卡名称>    | 将来自于该网卡的所有流量都导向某个指定区域                           |
  | --change-interface=<网卡名称> | 将某个网卡与区域做关联                                     |
  | --list-all                | 显示当前区域的网卡配置参数、资源、端口以及服务等信息                      |
  | --list-all-zones          | 显示所有区域的网卡配置参数、资源、端口以及服务等信息                      |
  | --add-service=<服务名>       | 设置默认区域允许该服务的流量                                  |
  | --add-port=<端口号/协议>       | 设置默认区域允许该端口的流量                                  |
  | --remove-service=<服务名>    | 设置默认区域不再允许该服务的流量                                |
  | --remove-port=<端口号/协议>    | 设置默认区域不再允许该端口的流量                                |
  | --reload                  | 让永久生效的配置立即生效，不影响当前连接状态。--complete-reload 中断用户连接 |
  | --timeout=xx              | 临时设置指定的服务开放的秒数                                  |
  
  **注意：**firewall服务有两份规则策略配置记录：
  
  + **runtime**：当前生效的
  
  + **permanent**：永久生效

+ systemctl status firewalld.service
  
  查看防火墙的状态

+ systemctl start firewalld.service
  
  启动防火墙

+ systemctl stop firewalls.service
  
  停止防火墙

+ 

## 012 Linux 加密算法

+ 不可逆加密算法
  
  + hash
  + md5

+ 对称加密算法
  
  使用相同的密钥进行加密和解密
  
  + AES
  + DES

+ 非对称加密算法
  
  公开密钥和私有密钥，公钥和私钥是一对；公钥加密只能用私钥解密，同样，私钥加密只能用公钥解密。
  
  + RSA
  + ECC
  + DSA

Linux 相互面密钥

+ 公钥一般记录在用户目录下的.ssh/known_hosts

+ ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
  
  id_rsa中存放私钥
  
  id_rsa.pub中存放公钥

+ ssh-copy-id -i ~/.ssh/id_rsa.pub root@IP
  
  发送公钥到对方机器，再登录对方即可免密码。

+ 屏蔽系统的yes/no提示信息
  
  ssh -v -o GSSAPIAuthentication=no root@IP只保证当前一次不被系统信息中断
  
  /etc/ssh/ssh_config中添加
  
  + StricHostKeyChecking no
  + UserKnownHostsFile /dev/null

## 013 Linux 日期与时间

+ date
  
  + date -s "新时间"

+ cal

+ 时间同步
  
  + ntpdate cn.ntp.org.cn
  + service ntpd start
  + vi /etc/ntp.conf

+ timedatectl
  
  + timedatectl list-timezones
  + sudo timedatectl set-timezone Asia/Shanghai

## 014 Linux 用户、组

+ 新增用户
  
  useradd 用户名
  
  同时增加同名家目录和组

+ 设置密码
  
  passwd 用户名

+ 删除用户
  
  userdel 用户名
  
  + -f 强制删除用户，即使其处于登录状态，同时删除用户主目录。
  + -r 删除用户及用户主目录和所有文件及子目录。

+ 切换用户
  
  su 用户名

+ 修改用户信息
  
  + usermod -l 新用户名 原用户名
    
    但是家用户和组名称不变
  
  + usermod -L 用户名（passwd -l 用户名）
    
    锁定用户
  
  + usermod -U 用户名（passwd -u 用户名）
    
    解锁用户名
  
  + usermod -e yyyy-mm-dd 用户名
    
    设置用户到期时间
  
  + usermod -d 路径 用户名 
    
    修改用户主目录
  
  + usermod -s shell 用户名
    
    修改用户shell
  
  + usermod -u xxx 用户名
    
    修改用户id
  
  + usermod -g xxx 用户名
    
    修改用户组id

+ 用户信息文件
  
      + /etc/passwd
      + /etc/shadow
      + /etc/group

+ 创建组
  
  + groupadd 组名

+ 删除组
  
  + groupdel

+ 修改组信息
  
  + groupmod -n 新组名 原组名

+ chage 针对用户密码进行设定
  
  + -l：显示账户基本信息
  + -E：指定账户过期时间，yyyy-mm-dd
  + -I：指定密码过期后多少天锁定账户
  + -m：两次修改密码的最小间隔天数，0为不限定。
  + -M：修改密码的最大设定天数。
  + -W：密码过期前，提前多少天警告。

## 015 Linux 管道和重定向

+ 管道
  
  将前面命令的结果作为参数传递给后面的命令。

+ 输出重定向
  
  改变数据的输出位置和方向
  
  + 1> 输出正确信息
    
    ls / > a
  
  + 2>输出错误信息
    
    ls / 2> a
  
  + '>'替换 '>>'追加
  
  + 信息黑洞
    
    ls / >> /dev/null 2>&1
  
  + &代替所有
    
    ll -lh >a 2>b  正确结果输出到a，错误信息输出到b
    
    ll -lh &> a  ,  ll -lh >a 2>&1  所有结果输出到a

## 016 Linux 系统进程

| 参数  | 描述                     |
| --- | ---------------------- |
| a   | 列出带有终端的所有用户的进程         |
| x   | 列出当前用户的所有进程，包括没有终端的进程。 |
| u   | 面向用户友好的显示风格            |
| -e  | 列出所有进程                 |
| -u  | 列出某个用户关联的所有进程          |
| -f  | 显示完整格式的进程列表            |

+ 进程信息
  
  ps -ef  可查看进程父子关系
  
  ps  aux 查看系统中所有进程

+ &可将命令放入后台

+ nohup 可防止进程被挂起

+ kill 杀死进程
  
  -9  强迫进程立刻终止

+ 进程树
  
  pstree -p
  
  pstree -u

+ netstat 
  
  netstat -anp
  
  netstat -nlp
  
  | 参数  | 描述               |
  | --- | ---------------- |
  | -a  | 显示所有正在监听和未监听的套接字 |
  | -n  | 拒绝显示别名           |
  | -l  | 仅列出在监听的服务状态      |
  | -p  | 显示哪个进程在调用        |

## 017 Linux  软件安装

+ rpm安装
  
  + 安装软件
    
    rpm -ivh xxx.rpm
  
  + 查询软件
    
    rpm -qa | grep xxx
    
    rpm -q xxx
  
  + 卸载软件
    
    rpm -e xxxx

+ tar解压缩

+ 源码安装

+ 包管理器

## 018 Linux 三剑客

+ 普通剑客
  
  + cut -d ':' -f1,2,3,4 passed 
  
  + sort passwd
    
    sort -t ':' -k3 passwd
    
    sort -t ':' -k3 -r passwd
    
    sort -t ':' -k3 -n passwd
  
  + wc passwd
    
    wc -l passwd
    
    wc -w passwd
    
    wc -c passwd

+ grep
  
  + 可对文本进行搜索
  
  + 同时搜索多个文件
    
    grep 关键词 文件1 文件2
  
  + 显示匹配的行号
    
    grep -n 关键词 文件1
  
  + 搜索空行
    
    grep -c ^$ 文件
  
  + **参数列表**
  
  | 参数  | 描述                                           |
  | --- | -------------------------------------------- |
  | -i  | 忽略大小写                                        |
  | -c  | 只输出匹配行的数量                                    |
  | -l  | 只列出符合匹配的文件名，不列出具体的匹配行                        |
  | -n  | 列出所有的匹配行，显示行号                                |
  | -h  | 查询多文件时不显示文件名                                 |
  | -s  | 不显示不存在、没有匹配文本的错误信息                           |
  | -v  | 显示不包含匹配文本的所有行                                |
  | -w  | 匹配整词                                         |
  | -x  | 匹配整行                                         |
  | -r  | 递归搜索                                         |
  | -q  | 禁止输出任何结果，已退出状态表示搜索是否成功。0为包含，1为不包含，使用$?查询返回值。 |
  | -b  | 打印匹配行距文件头部的偏移量，以字节为单位                        |
  | -o  | 与-b结合使用，打印匹配的词据文件头部的偏移量，以字节为单位               |
  | -F  | 匹配固定字符串的内容                                   |
  | -E  | 支持扩展的正则表达式                                   |
  
  + 匹配符
    
    ^ : 匹配开头
    
    $ : 匹配结尾
    
    .  : 匹配任意一个字符
    
    *: 匹配前一字符任意次
    
    [] :匹配字符区间
    
    \ : 转义字符

+ sed
  
  + 字符流编辑器
  + sed从文件或管道中，读取一行处理一行输出一行；再读区一行处理一行输出一行...
  + 一次一行不多占内存
  + 对文本进行增删改查

+ awk
  
  + 目标也是操作文本
  + 是一门语言

## 019 Linux shell

### 1.shell 基本概念

> ### shell 名词解释

+ Kernel
  + 内核主要是和硬件打交道
+ shell
  + 命令解释器
  + 既是一种程序，也是一种语言
  + 提供用户界面，用户通过该界面访问操作系统内核服务
+ shell两大主流
  + sh
    + sh
    + bash
  + csh
    + csh
    + tcsh
+ #！声明所用的shell
  + #！/bin/bash

> shell 脚本执行

+ ./xx.sh
  
  该脚本必须具备执行权限，在子shell下执行。

+ sh xx.sh
  
  会启动新的子shell去执行，xx.sh当做新shell的参数。

+ source xx.sh（.  xx.sh）
  
  在当前shell执行，不会启动子进程 

+ export 变量名=xxx
  
  这样定义的变量会从父进程传递到子进程中去

### 2.shell基本入门

> shell 变量

+ 变量定义时，变量名前不加$，变量引用时变量名前加$
+ 变量名不能使用标点符号、空格和shell的保留字

> 变量类型

+ 全局变量
  
  ```
  env (只显示全局变量)
  printenv (只显示全局变量)
  set (显示所有变量)
  unset (取消自定义变量)
  ```

+ 局部变量
  
  在脚本或命令中定义，仅在当前shell实例中有效。

+ 只读变量
  
  ```
  readonly a=xx
  ```

+ 环境变量
  
  所有程序，包括shell的启动的程序，都能访问。

+ shell变量
  
  由shell程序设定的特殊变量，有环境变量也有局部变量。

```shell
name=libai
echo $name
echo ${name}
readonly name
unset name
```

> shell 字符串

+ shell中的字符串可以用单引号，也可以用双引号，也可以不用引号

+ 单引号
  
  + 单引号中的内容原样输出，其中的变量无效。

+ 成对使用

+ 双引号
  
  + 双引号中可以有变量
  + 双引号中可以有转义字符

> shell 数组

+ 伪数组，非连续空间。

+ bash支持一维数组，没限定数组的大小。

+ 数组元素的下表从0开始编号，下表可以是整数或数学表达式，其值应大于等于0。

+ @和*代表数组的所有元素。

> shell 注释

+ 以#开头解释器认为是注释
+ 通过每行加#设置多行注释

> shell 参数传递

+ 执行脚本时，向脚本传递参数，脚本内获取参数的格式为：$n，n代表一个数字。

+ 参数引用
  
  | 参数处理 | 参数说明                 |
  | ---- | -------------------- |
  | $#   | 传递到脚本的参数个数           |
  | $*   | 以字符串的形式返回传递到脚本的所有参数  |
  | $@   | 代表所有传入的参数，但是区别对待。    |
  | $$   | 脚本运行的当前进程ID          |
  | $!   | 后台运行的最后一个进程ID        |
  | $?   | 显示最后命令的退出状态，0表示没有错误。 |
  | $0   | 执行的文件名               |

> shell 运算符

运算符：expr 数值 运算符 数值

如：expr 2 + 3      expr 5 \\* 3

简化形式：$((运算式))  或者 $[运算式]

test 运算式    或者   [ 运算式 ]

+ 算数运算符
  + +加
  + -减
  + *乘
  + /除
  + %取余
  + =赋值
  + ==比较
  + ！=不相等
+ 关系运算符
  + -eq等于
  + -ne不等于
  + -gt大于
  + -lt小于
  + -ge大于等于
  + -le小于等于
+ 布尔运算符
  + ！=
  + ==
  + -a
  + -o
+ 逻辑运算符
  + &&逻辑与
  + ｜｜逻辑或
+ 字符串运算符
  + =
  + ！=
  + -z字符串长度为0
  + -n字符串长度不为0
+ 文件测试运算符
  + -r文件可读
  + -w文件可写
  + -x文件可执行
  + -f普通文件
  + -d目录
  + -s文件是否为空
  + -e文件是否存在
  + -b是否为块文件
  + -c文件存在且为字符特殊文件

> test命令

+ test用于检查某个条件是否成立，可进行数值、字符、文件3个方面的测试
+ 0 为真，1为假
+ 用$？测试   
+ 或者 [ 条件判断 ] 条件前后有空格，表达式内要有空格，省略test

> shell流程控制

+ if
  
  ```sh
  if 条件 
  then
      语句
  elif 条件
  then
        语句
  else
        语句
  fi
  ```

+ case
  
  ```sh
  case 变量 in
        1) 语句
             语句
             ;;
        2) 语句
             语句
             ;;     
        *) 语句
             语句
             ;;
  esac
  ```

+ for
  
  ```sh
  for 变量 in 列表
  do
        语句
  done
  ```
  
  ```
  for ((初始值;循环控制条件;变量变化))
  do
    语句
  done
  ```

+ while
  
  ```sh
  while 条件
  do
        语句
  done
  
  ** break 和 continue
  ```

> shell 函数

+ linux shell 可以用户定义函数，然后在shell脚本中调用。
+ 可以function fun() 定义，也可以直接fun()定义。
+ 参数返回，可以显示加return，如果不加，则以最后一条命令运行结果，作为返回值。

> 读取控制台输入

+ read （选项） （参数）
  
  + 选项
    
    -p：指定读取值时的提示符
    
    -t：指定读取时等待时间（秒）
  
  + 参数
    
    变量：指定读取值的变量名
  
  read -t 7 -p "输入你的名字："  name

### 3.函数

脚本和函数区别：主要在于返回值和调用方式

函数是简化版脚本

+ 系统函数
  
  + basename
    
    bansename [string/pathname] [suffix]
    
    得到不带路径的文件名称，包括去除后缀。
  
  + dirname 文件绝对路径
    
    得到文件路径，与basename相反。

+ 自定义函数
  
  [function] funname[()]
  
  {
  
  ​       Action;
  
  ​       [return int;]
  
  }

### 4.系统任务设置

> 系统启动流程

+ 启动计算机的硬件BIOS
  
  + 读取时间
  + 选择对应的启动模式（USB HDD EFI）

+ 如果是Linux系统，找/boot目录引导系统启动

+ 计算机读取初始配置文件
  
  + /etc/inittab
  
  + 启动时控制计算机的运行级别runlevel
    
    | 级别  | 描述                         |
    | --- | -------------------------- |
    | 0   | halt 关机                    |
    | 1   | Single user mod 单用户模式      |
    | 2   | Multi user 多用户无网络模式        |
    | 3   | Full muliuser mode 多用户完整模式 |
    | 4   | unused 保留模式                |
    | 5   | X11 图形界面模式                 |
    | 6   | reboot 重启模式                |

+ 开始引导默认组件或服务
  
  + /etc/rc.d/rc.sysint

+ 开始加载runlevel对应的服务
  
  + /etc/rc{n}.d/
    + K：关机时需要关闭的服务
    + S：启动时需要开启的服务
    + 数字代表开始或关闭的顺序
    + 所有文件都是软链接，链接地址是/etc/init.d

+ 启动完毕，所有的服务也被加载完成

> 系统服务

+ chkconfig查看当前的服务
+ 开机后，可通过service 或 systemctl命令控制服务的启动、关闭、重启。

> 开机自启动服务

+ rc.local

创建脚本，赋予执行权限，添加到rc.local中

+ chkconfig
  
  + 创建开机自启动脚本文件
    
    + 创建脚本，包含以下部分：
      
      #！/bin/bash
      
      #chkconfig 2345 88 99
      
      #description：auto_run 
      
      脚本正文
  
  + 脚本文件拷贝到/etc/init.d
  
  + 为脚本文件添加执行权限
    
    + chmod a+x 脚本文件
  
  + 添加到服务
    
    + chkconfig -add /etc/init.d/脚本文件
      
      2345里面放s开头，06里放k开头

> 定时任务

+ 在系统服务中心，crond负责周期性任务
  
  + systemctl status crond.service

+ 添加任务
  
  + crontab -e

+ 显示任务
  
  + crontab -l

+ 格式
  
  \*    *   *   *   *    command
  
  分 时 日 月 周 命令
  
  \*：代表任意时间都，实际上就是‘每’的意思
  
  -：表示区间，是一个范围。
  
  ,：是分隔时段。
  
  /n：表示分割，*/5 * * * * * cmd 表示每5分钟执行

+ 重启
  
  + systemctl restart corned.service

+ 清除任务
  
  + crontab -r

## 020 Linux 磁盘管理

### 1. du

查看文件和目录占用的磁盘空间

+ du 文件/目录

+ | 选项  | 功能             |
  | --- | -------------- |
  | -h  | 易读方式显示容量       |
  | -a  | 不仅查看目录大小，还包括文件 |
  | -s  | 只显示总和          |

### 2. df

查看磁盘占用

+ df 

+ | 选项  | 功能       |
  | --- | -------- |
  | -h  | 易读方式显示容量 |

### 3. lsblk

查看设备挂载情况

+ lsblk

+ 

+ | 选项  | 功能                |
  | --- | ----------------- |
  | -f  | 显示设备文件类型、挂载、UUID等 |

### 4. mount / umount

设备挂载、卸载

mount [-t vfstype] [-o option] device  dir

开机自动挂载

/etc/fstab

### 5. fdisk

硬盘分区和格式化

+ fdisk -l
  
  显示磁盘信息

### 6. mkfs

给新设备指定文件系统

+ mkfs -t  xfs /dev/sdc1

## 021 其他命令参考

### 《Linux从入门到精通》

> 获取用户相关信息

whoami：列出你目前登录的用户名

who am i：除了显示用户名，还显示登录终端，当前日期时间和IP地址

who ：列出当前都有哪些用户在系统上工作

w：与who列出的信息类似，但是所获取的信息更多

users：只列出所有登录用户的名字

tty：显示当前登录使用的终端

> 活下来的公司都是市场做的最好的，而不是技术做的最好的。

> 获取系统相关信息

uname：Unix name的缩写

+ -a, --all                print all information, in the following order,
  
                               except omit -p and -i if unknown:

+ -s, --kernel-name        print the kernel name

+ -n, --nodename           print the network node hostname

+ -r, --kernel-release     print the kernel release

+ -v, --kernel-version     print the kernel version

+ -m, --machine            print the machine hardware name

+ -p, --processor          print the processor type or "unknown"

+ -i, --hardware-platform  print the hardware platform or "unknown"

+ -o, --operating-system   print the operating system

+ ​      --help     display this help and exit

+ ​      --version  output version information and exit

> 获取系统日期时间相关信息

date：

cal：

clear：

> 查看命令信息/帮助

+ 命令 --help
+ man 命令
+ whatis 命令
+ info 命令
+ type 命令

## 022 其他相关参考

### Linux用户权限——sudoers的深入剖析

#### **一、sudo权限的配置**

root账号登录系统不会记录root账号做了什么操作。

su虽然不记录以root执行了哪些命令，但会创建一条日志记录谁在什么时候变成了root。而su切换为root身份，仍然有很大的无法受控的权限，因此sudo是一个更好的选择。

sudo命令的意思是以其他用户身份执行命令，用户是否拥有sudo权限？拥有哪些权限？sudo执行时是否需要输入密码？这些都是通过/etc/sudoers文件进行配置和控制的。普通用户我们可以通过su命令切换到其他用户，但是需要知道其他用户的密码，如果是需要执行管理员命令则需要知道root密码。但是如果普通用户拥有sudo权限则可以只需要输入自己密码或者不输入密码完成管理员命令的执行。既保证了超级管理员的密码的安全性，又满足了普通用户执行特殊命令的需求，这就是/etc/sudoers文件的作用。

sudoers文件包含 sudo 命令所需的所有配置信息。默认情况下，sudoers 文件只能由 root 用户编辑并修改。sudoers文件的默认位置是 /etc/sudoers。

**1.编辑 sudo权限命令**

```
visudo
```

命令实际修改的是 /etc/sudoers 文件

**2./etc/sudoers 配置文件说明**

```
[swimfish@amika-zhou ~]$ sudo cat  /etc/sudoers
## Sudoers allows particular users to run various commands as
## the root user, without needing the root password.
## 该文件允许特定用户像root一样执行命令，并且不需要root的口令
##
## Examples are provided at the bottom of the file for collections
## of related commands, which can then be delegated out to particular
## users or groups.
## 
## This file must be edited with the 'visudo' command.

## Host Aliases
## Groups of machines. You may prefer to use hostnames (perhaps using 
## wildcards for entire domains) or IP addresses instead.
## 主机别名，通过别名代表一组主机名称
# Host_Alias     FILESERVERS = fs1, fs2
# Host_Alias     MAILSERVERS = smtp, smtp2

## User Aliases
## These aren't often necessary, as you can use regular groups
## (ie, from files, LDAP, NIS, etc) in this file - just use %groupname 
## rather than USERALIAS
## 用户别名，通过别名代表一组用户
# User_Alias ADMINS = jsmith, mikem


## Command Aliases
## These are groups of related commands...
## 命令别名，通过别名代表一组相关命令

## Networking
## 网络操作别名，通过别名代表一组网络操作相关的命令
# Cmnd_Alias NETWORKING = /sbin/route, /sbin/ifconfig, /bin/ping, /sbin/dhclient, /usr/bin/net, /sbin/iptables, /usr/bin/rfcomm, /usr/bin/wvdial, /sbin/iwconfig, /sbin/mii-tool

## Installation and management of software
## 软件安装相关操作别名，通过别名代表一组软件安装相关的命令
# Cmnd_Alias SOFTWARE = /bin/rpm, /usr/bin/up2date, /usr/bin/yum

## Services
## 服务操作相关别名，通过别名代表一组服务操作命令
# Cmnd_Alias SERVICES = /sbin/service, /sbin/chkconfig, /usr/bin/systemctl start, /usr/bin/systemctl stop, /usr/bin/systemctl reload, /usr/bin/systemctl restart, /usr/bin/systemctl status, /usr/bin/systemctl enable, /usr/bin/systemctl disable

## Updating the locate database
# Cmnd_Alias LOCATE = /usr/bin/updatedb

## Storage
# Cmnd_Alias STORAGE = /sbin/fdisk, /sbin/sfdisk, /sbin/parted, /sbin/partprobe, /bin/mount, /bin/umount

## Delegating permissions
# Cmnd_Alias DELEGATING = /usr/sbin/visudo, /bin/chown, /bin/chmod, /bin/chgrp 

## Processes
# Cmnd_Alias PROCESSES = /bin/nice, /bin/kill, /usr/bin/kill, /usr/bin/killall

## Drivers
# Cmnd_Alias DRIVERS = /sbin/modprobe

# Defaults specification

#
# Refuse to run if unable to disable echo on the tty.
#
Defaults   !visiblepw

#
# Preserving HOME has security implications since many programs
# use it when searching for configuration files. Note that HOME
# is already set when the the env_reset option is enabled, so
# this option is only effective for configurations where either
# env_reset is disabled or HOME is present in the env_keep list.
#
Defaults    always_set_home
Defaults    match_group_by_gid

# Prior to version 1.8.15, groups listed in sudoers that were not
# found in the system group database were passed to the group
# plugin, if any. Starting with 1.8.15, only groups of the form
# %:group are resolved via the group plugin by default.
# We enable always_query_group_plugin to restore old behavior.
# Disable this option for new behavior.
Defaults    always_query_group_plugin

Defaults    env_reset
Defaults    env_keep =  "COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS"
Defaults    env_keep += "MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE"
Defaults    env_keep += "LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES"
Defaults    env_keep += "LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE"
Defaults    env_keep += "LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY"

#
# Adding HOME to env_keep may enable a user to run unrestricted
# commands via sudo.
#
# Defaults   env_keep += "HOME"

Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin

## Next comes the main part: which users can run what software on 
## which machines (the sudoers file can be shared between multiple
## systems).
## Syntax:
##
##      user    MACHINE=COMMANDS
##
## The COMMANDS section may have other options added to it.
##
## Allow root to run any commands anywhere 
root    ALL=(ALL)       ALL
swimfish        ALL=(ALL)  NOPASSWD: ALL

## Allows members of the 'sys' group to run networking, software, 
## service management apps and more.
## 允许用户组运行指定的命令组
# %sys ALL = NETWORKING, SOFTWARE, SERVICES, STORAGE, DELEGATING, PROCESSES, LOCATE, DRIVERS

## Allows people in group wheel to run all commands
## 允许用户组运行所有命令
%wheel  ALL=(ALL)       ALL

## Same thing without a password
## 允许用户组无密码运行所有命令
# %wheel        ALL=(ALL)       NOPASSWD: ALL

## Allows members of the users group to mount and unmount the 
## cdrom as root
## 允许用户组运行指定命令
# %users  ALL=/sbin/mount /mnt/cdrom, /sbin/umount /mnt/cdrom

## Allows members of the users group to shutdown this system
## 允许用户组在本地运行关机
# %users  localhost=/sbin/shutdown -h now

## Read drop-in files from /etc/sudoers.d (the # here does not mean a comment)
## 下面的#并不是注释
#includedir /etc/sudoers.d
[swimfish@amika-zhou ~]$ 
```

**为用户配置sudo权限**

```
用户名    [被管理主机的IP]=（[可以使用的身份]）    [nopasswd：/passwd：] [授权的命令]
```

[被管理主机的IP]、 [可以使用的身份]、 [授权的命令] 都可以使用 ALL 来表示不限制。

添加 [NOPASSWD: ] 选项可以使用户在使用sudo权限时不需要输入密码。

[授权的命令]要使用绝对路径，多条命令之间可用逗号（ ,）分隔。例：

```
swimfish        ALL=(ALL)  NOPASSWD: ALL
```

**为用户组配置sudo权限**

```
%组名    [被管理主机的IP]=（[可以使用的身份]）    [nopasswd：/passwd：] [授权的命令]
```

[被管理主机的IP]、 [可以使用的身份]、 [授权的命令] 都可以使用 ALL 来表示不限制。

添加 [NOPASSWD: ] 选项可以使用户在使用sudo权限时不需要输入密码。

用户组 与 用户 的唯一区别是用户组前有个 %，例：

```
%wheel        ALL=(ALL)       NOPASSWD: ALL
```

3.注意事项

1）赋予用户sudo权限时一定要谨慎，够用即可，不要赋予过高的权限

2）[授权的命令] 设置得越具体，用户获得的权限越小。

3）严禁赋予普通用户 /usr/bin/passwd、/usr/bin/vi、/usr/bin/su、/usr/bin/bash 命令的权限，拥此权限的用户可以修改root用户密码，然后为所欲为。

4）权力越大，责任越大。

#### 二、sudo 命令介绍

1.sudo [命令]：以 root 身份来执行命令

用户必须有相应命令的sudo权限例子普通用户使用 less 命令查看 root 用户的历史命令

2.sudo su：切换到root用户

用户必须有 /usr/bin/su命令的sudo权限一旦切换成功，用户可以以root身份执行任何命令例子普通用户使用 sudo su 命令切换到 root 用户，然后修改root用户的密码

3.sudo -s <shell>：切换到root用户的shell

可以不加 <shell>，会使用默认 shell用户必须有相应shell命令的sudo权限，例如 /usr/bin/bash一旦切换成功，用户可以以root身份执行任何命令

+ 普通用户使用 sudo -s /usr/bin/bash 命令切换到 root 的shell，然后修改root用户的密码

```
[swimfish@amika-zhou ~]$ sudo -s /usr/bin/bash
[root@amika-zhou swimfish]# passwd 
Changing password for user root.
New password: 
[root@amika-zhou swimfish]# exit
exit
[swimfish@amika-zhou ~]$ 
```

+ 可以不加 <shell>，会使用默认 shell

```
[swimfish@amika-zhou ~]$ sudo -s 
[root@amika-zhou swimfish]# exit
exit
[swimfish@amika-zhou ~]$ 
```

4.sudo -l：列出目前用户可用的sudo权限的指令

```
[swimfish@amika-zhou ~]$ sudo -l
Matching Defaults entries for swimfish on amika-zhou:
!visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin, env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE", env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES",
env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE", env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY",
secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

User swimfish may run the following commands on amika-zhou:
(ALL) NOPASSWD: ALL
[swimfish@amika-zhou ~]$ 
```

#### 三、sudo权限的应用

1.授权普通用户可以重启服务器

+ 执行 visudo， 然后添加如下内容切换到user1账号

```
user1  ALL=(ALL) /sbin/reboot -r  now
```

+ 查看user1可用的sudo权限的指令

```
[user1@amika-zhou ~]$ sudo -l
...

User swimfish may run the following commands on amika-zhou:
(ALL)  /sbin/reboot -r  now
[user1@amika-zhou ~]$ 
```

2.授权普通用户可以添加其他用户

要想添加其他用户，必须拥有添加用户和设置密码的权限，即 /usr/sbin/useradd 和 /usr/bin/passwd 两个命令的sudo权限。

若用户完全拥有 /usr/bin/passwd 的sudo权限，则可以通过 sudo passwd 命令或者 sudo passwd root 命令修改 root 密码，这样就会变得非常不安全。

因此，需要严格限制用户对 /usr/bin/passwd 的权限：

```
user1  ALL=(ALL) /usr/bin/passwd [A-Za-z]* ,!/usr/bin/passwd "",!/usr/bin/passwd root
```

/usr/bin/passwd [A-Za-z]* 表示 passwd 命令后附加的第一个字符只能是大小写字母。

!/usr/bin/passwd "" 表示 passwd 命令后不能什么都不加。

!/usr/bin/passwd root 表示 passwd 命令后不能加 root。

三条语句的缺一不可，且顺序不能颠倒。

#### 四、visudo命令简介

1、使用语法用法：#visudo [-chqsV] [-f sudoers]

2、参数说明

| 参数                 | 参数说明          |
| ------------------ | ------------- |
| -c, --check        | 检查sudoers配置文件 |
| -f, --file=sudoers | 修改sudoers配置文件 |
| -h, --help         | 获取命令帮助        |
| -q, --quiet        | 静默输出          |
| -s, --strict       | 严格语法检查        |
| -V, --version      | 查看命令版本        |

### 字符文字

+ figlet
  
  + -w：指定字符宽度，默认字符宽度80。
  + -l：字符左对齐，默认选项。
  + -c：字符居中，默认左对齐。
  + -r：字符右对齐。
  + -k：字距调整，每个字母独立占位。
  + -f：选字体，**showfigfonts**显示可用字体示例。
  + -d：选字体目录

+ toilet
  
  支持--gay和--metal两种色彩格式
  
  + 

### [超级详细的iptable教程文档 ](https://www.cnblogs.com/Dicky-Zhang/p/5904429.html)

Iptabels是与Linux内核集成的包过滤防火墙系统，几乎所有的linux发行版本都会包含Iptables的功能。如果 Linux 系统连接到因特网或 LAN、服务器或连接 LAN 和因特网的代理服务器， 则Iptables有利于在 Linux 系统上更好地控制 IP 信息包过滤和防火墙配置。

netfilter/iptables过滤防火墙系统是一种功能强大的工具，可用于添加、编辑和除去规则，这些规则是在做信息包过滤决定时，防火墙所遵循和组成的规则。这些规则存储在专用的信 息包过滤表中，而这些表集成在 Linux 内核中。在信息包过滤表中，规则被分组放在我们所谓的链（chain）中。

虽然netfilter/iptables包过滤系统被称为单个实体，但它实际上由两个组件netfilter 和 iptables 组成。

netfilter 组件也称为内核空间（kernelspace），是内核的一部分，由一些信息包过滤表组成，这些表包含内核用来控制信息包过滤处理的规则集。

iptables 组件是一种工具，也称为用户空间（userspace），它使插入、修改和除去信息包过滤表中的规则变得容易。

**优点**

netfilter/iptables的最大优点是它可以配置有状态的防火墙。有状态的防火墙能够指定并记住为发送或接收信息包所建立的连接的状态。防火墙可以从信息包的连接跟踪状态获得该信 息。在决定新的信息包过滤时，防火墙所使用的这些状态信息可以增加其效率和速度。这里有四种有效状态，名称分别为 ESTABLISHED 、 INVALID 、 NEW 和 RELATED 。

状态 ESTABLISHED指出该信息包属于已建立的连接，该连接一直用于发送和接收信息包并且完全有效。 INVALID 状态指出该信息包与任何已知的流或连接都不相关联，它可能包含错误的数据或头。状态 NEW 意味着该信息包已经或将启动新的连接，或者它与尚未用于发送和接收信息包的连接相关联。最后， RELATED 表示该信息包正在启动新连接，以及它与已建立的连接相关联。

netfilter/iptables的另一个重要优点是，它使用户可以完全控制防火墙配置和信息包过滤。您可以定制自己的规则来满足您的特定需求，从而只允许您想要的网络流量进入系统。

另外，netfilter/iptables是免费的，这对于那些想要节省费用的人来说十分理想，它可以代替昂贵的防火墙解决方案。

**原理**

iptables的原理主要是对数据包的控制，看下图：

![img](iptable0)

（1） 一个数据包进入网卡时，它首先进入PREROUTING链，内核根据数据包目的IP判断是否需要转发出去。

（2） 如果数据包就是进入本机的，它就会沿着图向下移动，到达INPUT链。数据包到了INPUT链后，任何进程都会收到它。本机上运行的程序可以发送数据包，这些数据包会经 过OUTPUT链，然后到达POSTROUTING链输出。

（3）如果数据包是要转发出去的，且内核允许转发，数据包就会如图所示向右移动，经过 FORWARD链，然后到达POSTROUTING链输出。

**规则、表和链**

**1.规则（rules）**

规则（rules）其实就是网络管理员预定义的条件，规则一般的定义为“如果数据包头符合这样的条件，就这样处理这个数据包”。规则存储在内核空间的信息包过滤表中，这些规则分别指定了源地址、目的地址、传输协议（如TCP、UDP、ICMP）和服务类型（如HTTP、FTP和SMTP）等。当数据包与规则匹配时，iptables就根据规则所定义的方法来处理这些数据包，如放行（accept）、拒绝（reject）和丢弃（drop）等。配置防火墙的主要工作就是添加、修改和删除这些规则。

**2.链（chains）**

链（chains）是数据包传播的路径，每一条链其实就是众多规则中的一个检查清单，每一条链中可以有一条或数条规则。当一个数据包到达一个链时，iptables就会从链中第一条规则开始检查，看该数据包是否满足规则所定义的条件。如果满足，系统就会根据该条规则所定义的方法处理该数据包；否则iptables将继续检查下一条规则，如果该数据包不符合链中任一条规则，iptables就会根据该链预先定义的默认策略来处理数据包。

**3.表（tables）**
表（tables）提供特定的功能，iptables内置了4个表，即raw表、filter表、nat表和mangle表，分别用于实现包过滤，网络地址转换和包重构的功能。

![img](IPTABLE)

（1）RAW表

只使用在PREROUTING链和OUTPUT链上,因为优先级最高，从而可以对收到的数据包在连接跟踪前进行处理。一但用户使用了RAW表,在 某个链上,RAW表处理完后,将跳过NAT表和 ip_conntrack处理,即不再做地址转换和数据包的链接跟踪处理了.

（2）filter表

主要用于过滤数据包，该表根据系统管理员预定义的一组规则过滤符合条件的数据包。对于防火墙而言，主要利用在filter表中指定的规则来实现对数据包的过滤。Filter表是默认的表，如果没有指定哪个表，iptables 就默认使用filter表来执行所有命令，filter表包含了INPUT链（处理进入的数据包），RORWARD链（处理转发的数据包），OUTPUT链（处理本地生成的数据包）在filter表中只能允许对数据包进行接受，丢弃的操作，而无法对数据包进行更改

（3）nat表

主要用于网络地址转换NAT，该表可以实现一对一，一对多，多对多等NAT 工作，iptables就是使用该表实现共享上网的，NAT表包含了PREROUTING链（修改即将到来的数据包），POSTROUTING链（修改即将出去的数据包），OUTPUT链（修改路由之前本地生成的数据包）

（4）mangle表

主要用于对指定数据包进行更改，在内核版本2.4.18 后的linux版本中该表包含的链为：INPUT链（处理进入的数据包），RORWARD链（处理转发的数据包），OUTPUT链（处理本地生成的数据包）POSTROUTING链（修改即将出去的数据包），PREROUTING链（修改即将到来的数据包）

**3、规则表之间的优先顺序：**

Raw——mangle——nat——filter

规则链之间的优先顺序（分三种情况）：

**第一种情况：入站数据流向
**

从外界到达防火墙的数据包，先被PREROUTING规则链处理（是否修改数据包地址等），之后会进行路由选择（判断该数据包应该发往何处），如果数据包 的目标主机是防火墙本机（比如说Internet用户访问防火墙主机中的web服务器的数据包），那么内核将其传给INPUT链进行处理（决定是否允许通 过等），通过以后再交给系统上层的应用程序（比如Apache服务器）进行响应。

**第二冲情况：转发数据流向**

来自外界的数据包到达防火墙后，首先被PREROUTING规则链处理，之后会进行路由选择，如果数据包的目标地址是其它外部地址（比如局域网用户通过网 关访问QQ站点的数据包），则内核将其传递给FORWARD链进行处理（是否转发或拦截），然后再交给POSTROUTING规则链（是否修改数据包的地 址等）进行处理。

**第三种情况：出站数据流向**

防火墙本机向外部地址发送的数据包（比如在防火墙主机中测试公网DNS服务器时），首先被OUTPUT规则链处理，之后进行路由选择，然后传递给POSTROUTING规则链（是否修改数据包的地址等）进行处理。

iptables是采用规则堆栈的方式来进行过滤，当一个封包进入网卡，会先检查 Prerouting，然后检查目的IP判断是否需要转送出去，接着就会跳到INPUT 或 Forward 进行过滤，如果封包需转送处理则检查 Postrouting，如果是来自本机封包，则检查 OUTPUT 以及Postrouting。过程中如果符合某条规则将会进行处理，处理动作除了 ACCEPT、REJECT、DROP、REDIRECT 和MASQUERADE 以外，还多出 LOG、ULOG、DNAT、SNAT、MIRROR、QUEUE、RETURN、TOS、TTL、MARK等，其中某些处理动作不会中断过滤程序，某些处理动作则会中断同一规则链的过滤，并依照前述流程继续进行下一个规则链的过滤（注意：这一点与ipchains不同），一直到堆栈中的规则检查完毕为止。透过这种机制所带来的好处是，我们可以进行复杂、多重的封包过滤，简单的说，iptables可以进行纵横交错式的过滤（tables）而非链状过滤（chains）。ACCEPT 将封包放行，进行完此处理动作后，将不再比对其它规则，直接跳往下一个规则链（nat:postrouting）。

那么如何使用iptables在以上流程中控制对数据包的处理行为呢？当然是使用iptables与其相关的参数了。

### 1、iptables命令格式

iptables的命令格式较为复杂，一般的格式如下：

**iptables [-t 表] -命令 匹配  操作**

说明

（1） -t 表

表选项用于指定命令应用于哪个iptables内置表。

（2）命令

命令选项用于指定iptables的执行方式，包括插入规则，删除规则和添加规则，如下表所示

**命令                     说明**

```
-P  --policy        <链名>  定义默认策略
-L  --list          <链名>  查看iptables规则列表
-A  --append        <链名>  在规则列表的最后增加1条规则
-I  --insert        <链名>  在指定的位置插入1条规则
-D  --delete        <链名>  从规则列表中删除1条规则
-R  --replace       <链名>  替换规则列表中的某条规则
-F  --flush         <链名>  删除表中所有规则
-Z  --zero          <链名>  将表中数据包计数器和流量计数器归零
-X  --delete-chain  <链名>  删除自定义链
-v  --verbose       <链名>  与-L他命令一起使用显示更多更详细的信息
```

（3） 匹配规则

匹配选项指定数据包与规则匹配所具有的特征，包括源地址，目的地址，传输协议和端口号，如下表所示

**匹配                                说明**

```
-i --in-interface    网络接口名>     指定数据包从哪个网络接口进入，
-o --out-interface   网络接口名>     指定数据包从哪个网络接口输出
-p ---proto          协议类型        指定数据包匹配的协议，如TCP、UDP和ICMP等
-s --source          源地址或子网>   指定数据包匹配的源地址
--sport           源端口号>       指定数据包匹配的源端口号
--dport           目的端口号>     指定数据包匹配的目的端口号
-m --match           匹配的模块      指定数据包规则所使用的过滤模块
```

iptables执行规则时，是从规则表中从上至下顺序执行的，如果没遇到匹配的规则，就一条一条往下执行，如果遇到匹配的规则后，那么就执行本规则，执行后根据本规则的动作(accept，reject，log，drop等)，决定下一步执行的情况，后续执行一般有三种情况。

- 一种是继续执行当前规则队列内的下一条规则。比如执行过Filter队列内的LOG后，还会执行Filter队列内的下一条规则。
- 一种是中止当前规则队列的执行，转到下一条规则队列。比如从执行过accept后就中断Filter队列内其它规则，跳到nat队列规则去执行
- 一种是中止所有规则队列的执行。

### 2、iptables规则的动作

前面我们说过iptables处理动作除了 ACCEPT、REJECT、DROP、REDIRECT 、MASQUERADE 以外，还多出 LOG、ULOG、DNAT、RETURN、TOS、SNAT、MIRROR、QUEUE、TTL、MARK等。我们只说明其中最常用的动作：

**REJECT**  拦阻该数据包，并返回数据包通知对方，可以返回的数据包有几个选择：ICMP port-unreachable、ICMP echo-reply 或是tcp-reset（这个数据包包会要求对方关闭联机），进行完此处理动作后，将不再比对其它规则，直接中断过滤程序。 范例如下：

```
iptables -A  INPUT -p TCP --dport 22 -j REJECT --reject-with ICMP echo-reply
```

**DROP** 丢弃数据包不予处理，进行完此处理动作后，将不再比对其它规则，直接中断过滤程序。

**REDIRECT**  将封包重新导向到另一个端口（PNAT），进行完此处理动作后，将会继续比对其它规则。这个功能可以用来实作透明代理 或用来保护web 服务器。例如：

```
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT--to-ports 8081
```

**MASQUERADE** 改写封包来源IP为防火墙的IP，可以指定port 对应的范围，进行完此处理动作后，直接跳往下一个规则链（mangle:postrouting）。这个功能与 SNAT 略有不同，当进行IP 伪装时，不需指定要伪装成哪个 IP，IP 会从网卡直接读取，当使用拨接连线时，IP 通常是由 ISP 公司的 DHCP服务器指派的，这个时候 MASQUERADE 特别有用。范例如下：

```
iptables -t nat -A POSTROUTING -p TCP -j MASQUERADE --to-ports 21000-31000
```

**LOG**  将数据包相关信息纪录在 /var/log 中，详细位置请查阅 /etc/syslog.conf 配置文件，进行完此处理动作后，将会继续比对其它规则。例如：

```
iptables -A INPUT -p tcp -j LOG --log-prefix "input packet"
```

**SNAT** 改写封包来源 IP 为某特定 IP 或 IP 范围，可以指定 port 对应的范围，进行完此处理动作后，将直接跳往下一个规则炼（mangle:postrouting）。范例如下：

```
iptables -t nat -A POSTROUTING -p tcp-o eth0 -j SNAT --to-source 192.168.10.15-192.168.10.160:2100-3200
```

**DNAT** 改写数据包包目的地 IP 为某特定 IP 或 IP 范围，可以指定 port 对应的范围，进行完此处理动作后，将会直接跳往下一个规则链（filter:input 或 filter:forward）。范例如下：

```
iptables -t nat -A PREROUTING -p tcp -d 15.45.23.67 --dport 80 -j DNAT --to-destination 192.168.10.1-192.168.10.10:80-100
```

**MIRROR** 镜像数据包，也就是将来源 IP与目的地IP对调后，将数据包返回，进行完此处理动作后，将会中断过滤程序。

**QUEUE**  中断过滤程序，将封包放入队列，交给其它程序处理。透过自行开发的处理程序，可以进行其它应用，例如：计算联机费用.......等。

**RETURN** 结束在目前规则链中的过滤程序，返回主规则链继续过滤，如果把自订规则炼看成是一个子程序，那么这个动作，就相当于提早结束子程序并返回到主程序中。

**MARK** 将封包标上某个代号，以便提供作为后续过滤的条件判断依据，进行完此处理动作后，将会继续比对其它规则。范例如下：

```
iptables -t mangle -A PREROUTING -p tcp --dport 22 -j MARK --set-mark 22
```

看了本文是不是对iptables参数有所了解了，下文我会使用实例来更详细的说明iptables的参数的用法。

**保存规则**

使用iptables程序建立的规则只会保存在内存中，通常我们在修改了iptables的规则重启 iptables 后，之前修改的规则又消失了。那么如何保存新建立的规则呢？

方法1、对于RHEL和ceontos系统可以使用service iptables save将当前内存中的规则保存到*/etc/sysconfig/iptables*文件中

```
[root@lampbo ~]# service iptables save
```

方法2、修改/etc/sysconfig/iptables-config 将里面的IPTABLES_SAVE_ON_STOP="no", 这一句的"no"改为"yes"这样每次服务在停止之前会自动将现有的规则保存在 /etc/sysconfig/iptables 这个文件中去。

### 规则示例

先回顾下iptables的格式：

```
iptables [-t table] command [match] [-j target/jump]
```

-t 参数用来指定规则表，内建的规则表有三个，分别是：nat、mangle 和 filter，当未指定规则表时，则一律视为是 filter。

各个规则表的功能如下：

**nat** 此规则表拥有 Prerouting 和 postrouting 两个规则链，主要功能为进行一对一、一对多、多对多等网址转换工作（SNAT，DNAT），由于转换的特性，需进行目的地网址转换的数据包，就不需要进行来源网址转换，反之亦然，因此为了提升改写封包的效率，在防火墙运作时，每个封包只会经过这个规则表一次。如果我们把数据包过滤的规则定义在这个数据表里，将会造成无法对同一包进行多次比对，因此这个规则表除了作网址转换外，请不要做其它用途。mangle 此规则表拥有 Prerouting、FORWARD 和 postrouting 三个规则链。

除了进行网址转译工作会改写封包外，在某些特殊应用可能也必须去改写数据包（TTL、TOS）或者是设定 MARK（将数据包作记号，以进行后续的过滤），这时就必须将这些工作定义在 mangle 规则表中。

**mangle**表主要用于对指定数据包进行更改，在内核版本2.4.18 后的linux版本中该表包含的链为：INPUT链（处理进入的数据包），RORWARD链（处理转发的数据包），OUTPUT链（处理本地生成的数据包）POSTROUTING链（修改即将出去的数据包），PREROUTING链（修改即将到来的数据包）LINUX教程 centos教程

**filter** 这个规则表是预设规则表，拥有 INPUT、FORWARD 和 OUTPUT 三个规则链，这个规则表顾名思义是用来进行封包过滤的动作（例如：DROP、 LOG、 ACCEPT 或 REJECT），我们会将基本规则都建立在此规则表中。

(一)、常用命令示例：

1、命令 -A, --append

范例：**iptables -A INPUT -p tcp --dport 80 -j ACCEPT**

说明 ：新增规则到INPUT规则链中，规则时接到所有目的端口为80的数据包的流入连接，该规则将会成为规则链中的最后一条规则。

2、命令 -D, --delete

范例：**iptables -D INPUT -p tcp --dport 80 -j ACCEPT**

或  ： **iptables -D INPUT 1**

说明： 从INPUT规则链中删除上面建立的规则，可输入完整规则，或直接指定规则编号加以删除。

3、命令 -R, --replace

范例： **iptables -R INPUT 1 -s 192.168.0.1 -j DROP**

说明 取代现行第一条规则，规则被取代后并不会改变顺序。

4、命令 -I, --insert

范例：**iptables -I INPUT 1 -p tcp --dport 80 -j ACCEPT**

说明： 在第一条规则前插入一条规则，原本该位置上的规则将会往后移动一个顺位。

5、命令 -L, --list

范例： **iptables -L INPUT**

说明：列出INPUT规则链中的所有规则。

6、命令 -F, --flush

范例： **iptables -F INPUT**

说明： 删除INPUT规则链中的所有规则。

7、命令 -Z, --zeroLINUX教程 centos教程

范例：**iptables -Z INPUT**

说明 将INPUT链中的数据包计数器归零。它是计算同一数据包出现次数，过滤阻断式攻击不可少的工具。

8、命令 -N, --new-chain

范例： **iptables -N denied**

说明： 定义新的规则链。

9、命令 -X, --delete-chain

范例： **iptables -X denied**

说明： 删除某个规则链。

10、命令 -P, --policy

范例 ：**iptables -P INPUT DROP**

说明 ：定义默认的过滤策略。 数据包没有找到符合的策略，则根据此预设方式处理。

11、命令 -E, --rename-chain

范例： **iptables -E denied disallowed**

说明： 修改某自订规则链的名称。

（二）常用封包比对参数：

1、参数 -p, --protocol

范例：**iptables -A INPUT -p tcpLINUX教程 centos教程**

说明：比对通讯协议类型是否相符，可以使用 ! 运算子进行反向比对，例如：-p ! tcp ，意思是指除 tcp 以外的其它类型，包含udp、icmp ...等。如果要比对所有类型，则可以使用 all 关键词，例如：-p all。

2、参数 -s, --src, --source

范例: **iptables -A INPUT -s 192.168.1.100**

说明：用来比对数据包的来源IP，可以比对单机或网络，比对网络时请用数字来表示屏蔽，例如：-s 192.168.0.0/24，比对 IP 时可以使用!运算子进行反向比对，例如：-s ! 192.168.0.0/24。

3、参数 -d, --dst, --destination

范例： **iptables -A INPUT -d 192.168.1.100**

说明：用来比对封包的目的地 IP，设定方式同上。

4、参数 -i, --in-interface

范例 **iptables -A INPUT -i lo**

说明:用来比对数据包是从哪个网卡进入，可以使用通配字符 + 来做大范围比对，如：-i eth+ 表示所有的 ethernet 网卡，也可以使用 ! 运算子进行反向比对，如：-i ! eth0。这里lo指本地换回接口。

5、参数 -o, --out-interface

范例：**iptables -A FORWARD -o eth0**

说明：用来比对数据包要从哪个网卡流出，设定方式同上。

6、参数 --sport, --source-port

范例：**iptables -A INPUT -p tcp --sport 22**

说明：用来比对数据的包的来源端口号，可以比对单一端口，或是一个范围，例如：--sport 22:80，表示从 22 到 80 端口之间都算是符合件，如果要比对不连续的多个端口，则必须使用 --multiport 参数，详见后文。比对端口号时，可以使用 ! 运算子进行反向比对。

7、参数 --dport, --destination-port

范例 **iptables -A INPUT -p tcp --dport 22**
说明 用来比对封包的目的地端口号，设定方式同上。

8、参数 --tcp-flags

范例：**iptables -p tcp --tcp-flags SYN,FIN,ACK SYN**

说明：比对 TCP 封包的状态标志号，参数分为两个部分，第一个部分列举出想比对的标志号，第二部分则列举前述标志号中哪些有被设，未被列举的标志号必须是空的。TCP 状态标志号包括：SYN（同步）、ACK（应答）、FIN（结束）、RST（重设）、URG（紧急）PSH（强迫推送） 等均可使用于参数中，除此之外还可以使用关键词 ALL 和 NONE 进行比对。比对标志号时，可以使用 ! 运算子行反向比对。

9、参数 --syn

范例：**iptables -p tcp --syn**

说明：用来比对是否为要求联机之TCP 封包，与 iptables -p tcp --tcp-flags SYN,FIN,ACK SYN 的作用完全相同，如果使用 !运算子，可用来比对非要求联机封包。

10、参数 -m multiport --source-port

范例： **iptables -A INPUT -p tcp -m multiport --source-port 22,53,80,110 -j ACCEPT**

说明 用来比对不连续的多个来源端口号，一次最多可以比对 15 个端口，可以使用 ! 运算子进行反向比对。

11、参数 -m multiport --destination-port

范例 ：**iptables -A INPUT -p tcp -m multiport --destination-port 22,53,80,110 -j ACCEPT**

说明：用来比对不连续的多个目的地端口号，设定方式同上。

12、参数 -m multiport --port

范例：**iptables -A INPUT -p tcp -m multiport --port 22,53,80,110 -j ACCEPT**

说明：这个参数比较特殊，用来比对来源端口号和目的端口号相同的数据包，设定方式同上。注意：在本范例中，如果来源端口号为 80，目的地端口号为 110，这种数据包并不算符合条件。

13、参数 --icmp-type

范例：**iptables -A INPUT -p icmp --icmp-type 8 -j DROP**

说明：用来比对 ICMP 的类型编号，可以使用代码或数字编号来进行比对。请打 iptables -p icmp --help 来查看有哪些代码可用。这里是指禁止ping如，但是可以从该主机ping出。

14、参数 -m limit --limit

范例：**iptables -A INPUT -m limit --limit 3/hour**

说明：用来比对某段时间内数据包的平均流量，上面的例子是用来比对：每小时平均流量是否超过一次3个数据包。 除了每小时平均次外，也可以每秒钟、每分钟或每天平均一次，默认值为每小时平均一次，参数如后： /second、 /minute、/day。 除了进行数据包数量的比对外，设定这个参数也会在条件达成时，暂停数据包的比对动作，以避免因洪水攻击法，导致服务被阻断。

15、参数 --limit-burst

范例：**iptables -A INPUT -m limit --limit-burst 5**

说明：用来比对瞬间大量封包的数量，上面的例子是用来比对一次同时涌入的封包是否超过 5 个（这是默认值），超过此上限的封将被直接丢弃。使用效果同上。

16、参数 -m mac --mac-source

范例：**iptables -A INPUT -m mac --mac-source 00:00:00:00:00:01 -j ACCEPT**

说明：用来比对数据包来源网络接口的硬件地址，这个参数不能用在 OUTPUT 和 Postrouting 规则链上，这是因为封包要送出到网后，才能由网卡驱动程序透过 ARP 通讯协议查出目的地的 MAC 地址，所以 iptables 在进行封包比对时，并不知道封包会送到个网络接口去。linux基础

17、参数 --mark

范例：**iptables -t mangle -A INPUT -m mark --mark 1**

说明：用来比对封包是否被表示某个号码，当封包被比对成功时，我们可以透过 MARK 处理动作，将该封包标示一个号码，号码最不可以超过 4294967296。linux基础

18、参数 -m owner --uid-owner

范例：**iptables -A OUTPUT -m owner --uid-owner 500**

说明：用来比对来自本机的封包，是否为某特定使用者所产生的，这样可以避免服务器使用 root 或其它身分将敏感数据传送出，可以降低系统被骇的损失。可惜这个功能无法比对出来自其它主机的封包。

19、参数 -m owner --gid-owner

范例：**iptables -A OUTPUT -m owner --gid-owner 0**

说明：用来比对来自本机的数据包，是否为某特定使用者群组所产生的，使用时机同上。

20、参数 -m owner --pid-owner

范例：**iptables -A OUTPUT -m owner --pid-owner 78**

说明：用来比对来自本机的数据包，是否为某特定行程所产生的，使用时机同上。

21、参数 -m owner --sid-owner

范例： **iptables -A OUTPUT -m owner --sid-owner 100**

说明： 用来比对来自本机的数据包，是否为某特定联机（Session ID）的响应封包，使用时机同上。

22、参数 -m state --state

范例： **iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT**

说明 用来比对联机状态，联机状态共有四种：INVALID、ESTABLISHED、NEW 和 RELATED。

23、iptables -L -n -v  可以查看计数器

INVALID 表示该数据包的联机编号（Session ID）无法辨识或编号不正确。ESTABLISHED 表示该数据包属于某个已经建立的联机。NEW 表示该数据包想要起始一个联机（重设联机或将联机重导向）。RELATED 表示该数据包是属于某个已经建立的联机，所建立的新联机。例如：FTP-DATA 联机必定是源自某个 FTP 联机。

（三）、常用的处理动作：

-j 参数用来指定要进行的处理动作，常用的处理动作包括：**ACCEPT、REJECT、DROP、REDIRECT、MASQUERADE、LOG、DNAT、SNAT、MIRROR、QUEUE、RETURN、MARK**。

分别说明如下：

**ACCEPT** 将数据包放行，进行完此处理动作后，将不再比对其它规则，直接跳往下一个规则链（natostrouting）。

**REJECT** 拦阻该数据包，并传送数据包通知对方，可以传送的数据包有几个选择：ICMP port-unreachable、ICMP echo-reply 或是tcp-reset（这个数据包会要求对方关闭联机），进行完此处理动作后，将不再比对其它规则，直接 中断过滤程序。 范例如下：

**iptables -A FORWARD -p TCP --dport 22 -j REJECT --reject-with tcp-reset**

**DROP** 丢弃包不予处理，进行完此处理动作后，将不再比对其它规则，直接中断过滤程序。

**REDIRECT** 将包重新导向到另一个端口（PNAT），进行完此处理动作后，将会继续比对其它规则。 这个功能可以用来实作通透式porxy 或用来保护 web 服务器。例如：

**iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 8080**

**MASQUERADE** 改写数据包来源 IP为防火墙 NIC IP，可以指定 port 对应的范围，进行完此处理动作后，直接跳往下一个规则（mangleostrouting）。这个功能与 SNAT 略有不同，当进行 IP 伪装时，不需指定要伪装成哪个 IP，IP 会从网卡直接读取，当使用拨号连接时，IP 通常是由 ISP 公司的 DHCP 服务器指派的，这个时候 MASQUERADE 特别有用。范例如下：linux基础

**iptables -t nat -A POSTROUTING -p TCP -j MASQUERADE --to-ports 1024-31000**

**LOG** 将封包相关讯息纪录在 /var/log 中，详细位置请查阅 /etc/syslog.conf 配置文件，进行完此处理动作后，将会继续比对其规则。例如：

**iptables -A INPUT -p tcp -j LOG --log-prefix "INPUT packets"**

**SNAT** 改写封包来源 IP 为某特定 IP 或 IP 范围，可以指定 port 对应的范围，进行完此处理动作后，将直接跳往下一个规则（mangleostrouting）。范例如下：

**iptables -t nat -A POSTROUTING -p tcp-o eth0 -j SNAT --to-source 194.236.50.155-194.236.50.160:1024-32000**

**DNAT** 改写封包目的地 IP 为某特定 IP 或 IP 范围，可以指定 port 对应的范围，进行完此处理动作后，将会直接跳往下一个规炼（filter:input 或 filter:forward）。范例如下：

**iptables -t nat -A PREROUTING -p tcp -d 15.45.23.67 --dport 80 -j DNAT --to-destination
192.168.1.1-192.168.1.10:80-100**

**MIRROR** 镜像数据包，也就是将来源 IP 与目的地 IP 对调后，将数据包送回，进行完此处理动作后，将会中断过滤程序。

**QUEUE** 中断过滤程序，将数据包放入队列，交给其它程序处理。透过自行开发的处理程序，可以进行其它应用，例如：计算联机费.......等。

**RETURN** 结束在目前规则链中的过滤程序，返回主规则链继续过滤，如果把自订规则链看成是一个子程序，那么这个动作，就相当提早结束子程序并返回到主程序中。

**MARK** 将数据包标上某个代号，以便提供作为后续过滤的条件判断依据，进行完此处理动作后，将会继续比对其它规则。范例如下：

**iptables -t mangle -A PREROUTING -p tcp --dport 22 -j MARK --set-mark 2**

# 杂项

## TTY、PTS、PTMX

+ tty（终端设备的统称）
  
  终端是一种字符设备，tty用来简称各种终端设备

+ pty（虚拟终端）
  
  远程telnet或者xterm连接主机即虚拟终端。

+ pts/ptmx（pts/ptmx结合使用，实现pty）
  
  pts是pty的实现方法，与ptmx配合实现pty。

## Linux下的终端

​    linux系统设备均在/dev/下

+ 串行端口终端（/dev/ttySn）
  
  它是使用计算机端口连接的终端设备，并将每个串行口都看作是一个字符设备。如果要向一个端口发送数据，可以在命令行上把标准输出重定向到这些特殊文件名上即可。

+ 伪终端（/dev/pty/）
  
  是成对的逻辑终端设备，例如/dev/ptyp3和/dev/ttyp3，它们与实际物理设备并不直接相关。

+ 控制终端（/dev/tty）
  
  如果当前进程有控制终端的话，那么/dev/tty就是当前进程的控制终端的设备特殊文件。可以使用命令”ps –ax”来查看进程与哪个控制终端相连。假如你登录的是shell，那么/dev/tty就是你使用的终端，使用命令”tty”可以查看它 具体对应哪个实际终端设备。

+ 控制台终端（/dev/ttyn, /dev/console）
  
  在 UNIX系统中，计算机显示器通常被称为控制台终端。它仿真了类型为Linux的一种终端，并且有一些设备特 殊文件与之相关联，你也可以登录到不同的虚拟终端上去，因而可以让系统同时有几个不同的会话期存在。只有系统或超级用户root可以向/dev/tty0进行写操作。

## NTP服务器搭建

> 第一种方法：安装NTPD服务

+ yum install ntp
+ systemctl enable ntpd
+ systemctl start ntpd
+ firewall-cmd --add-service=ntp
+ /etc/ntp.conf
  + restrict 192.168.1.0 [mask](https://so.csdn.net/so/search?q=mask&spm=1001.2101.3001.7020) 255.255.255.0 nomodify notrap
  + server 127.127.1.0
    fudge 127.127.1.0 stratum 1**

> 第二种方法：启用chrony服务

```
[root@ntp ~]# cat /etc/chrony.conf 

# Use public servers from the pool.ntp.org project.
# Please consider joining the pool (http://www.pool.ntp.org/join.html).
server 0.centos.pool.ntp.org iburst
server 1.centos.pool.ntp.org iburst
server 2.centos.pool.ntp.org iburst
server 3.centos.pool.ntp.org iburst

# Record the rate at which the system clock gains/losses time.
driftfile /var/lib/chrony/drift

# Allow the system clock to be stepped in the first three updates
# if its offset is larger than 1 second.
makestep 1.0 -1

# Enable kernel synchronization of the real-time clock (RTC).
rtcsync

# Enable hardware timestamping on all interfaces that support it.
#hwtimestamp *

# Increase the minimum number of selectable sources required to adjust
# the system clock.
#minsources 2

# Allow NTP client access from local network.
#allow 192.168.0.0/16
allow 0.0.0.0/0

# Serve time even if not synchronized to a time source.
local stratum 10

# Specify file containing keys for NTP authentication.
#keyfile /etc/chrony.keys

# Specify directory for log files.
logdir /var/log/chrony

# Select which information is logged.
#log measurements statistics tracking



[root@ntp ~]# chronyc sources -v
210 Number of sources = 4

.-- Source mode  '^' = server, '=' = peer, '#' = local clock.
/ .- Source state '*' = current synced, '+' = combined , '-' = not combined,
| /   '?' = unreachable, 'x' = time may be in error, '~' = time too variable.
||                                                 .- xxxx [ yyyy ] +/- zzzz
||      Reachability register (octal) -.           |  xxxx = adjusted offset,
||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
||                                \     |          |  zzzz = estimated error.
||                                 |    |           \
MS Name/IP address         Stratum Poll Reach LastRx Last sample               
===============================================================================
^? tock.ntp.infomaniak.ch        0   8     0     -     +0ns[   +0ns] +/-    0ns
^+ time.neu.edu.cn               1   6   377    46   -192us[ -192us] +/-   14ms
^? time.cloudflare.com           0   8     0     -     +0ns[   +0ns] +/-    0ns
^* time.neu.edu.cn               1   6   377    52   +203us[ +467us] +/-   14ms
```

## DNS服务器搭建

**DNS的分类**：

+ 主DNS服务器：就是一台存储着原始资料的DNS服务器。
+ 从DNS服务器：使用自动更新方式从主DNS服务器同步数据的DNS服务器。也成辅助DNS服务器。
+ 缓存服务器：不负责本地解析，采用递归方式转发客户机查询请求，并返回结果给客户机的DNS服务器。同时缓存查询回来的结果，也叫递归服务器。
+ 转发器：这台DNS发现非本机负责的查询请求时，不再向根域发起请求，而是直接转发给指定的一台或者多台服务器。自身并不缓存查询结果。

**以转发器为例**：

+ 安装bind
  
  + yum install bind bind-utils net-tools bash-completion
  + rpm -qa | grep bind
  + 安装完之后系统会多出一个named用户

+ 配置文件
  
  + /etc/named.conf
    
    + listen-on port 53 {any;};
    
    + allow-query  {any;};
    
    + forward only ;
      
      #first:先转发，转发器不响应，则自行迭代查询；only:只转发
      
      Forwarders {
      
      ​            8.8.8.8;
      
      ​            114,114,114,114;
      
      ​            };
      
      dnssec-enable no;
      
      dnssec-validation no; 

+ 启动服务
  
  + systemctl start named.service
    + systemctl status named.service
    + systemctl stop named.service
    + systemctl restart named.service
  + systemctl enable iptables.service 开机启动
  + netstat -an | grep :53

+ 防火墙放行
  
  + /etc/sysconfig/iptables
  + iptables -I INPUT -p tcp --dport 53 -j ACCEPT
  + iptables -I INPUT -p udp --dport 53 -j ACCEPT
  + service iptables save 
    + yum install iptables-services
  + systemctl stop/disable firewall.service 停止/禁止friewalld服务和自启动

+ 清除缓存
  
  + rndc flush

+ 保存缓存
  
  + rndc dumpdb
  + 路径 /var/named/data/cache_dump.db
  + 缓存文件在/etc/named.conf中定义

+ option选项
  
  + 涉及用户范围
    + 单个ip：10.0.2.10;
    + 网段：10.0.20.0/24;或者10.0.2.0.;
    + 多个ip：10.0.2.1;10.0.2.2;
    + None：不匹配所有
    + any：匹配所有
    + localhost：DNS主机
    + localnets：与DNS主机同网段
  + version：回答针对服务器版本的请求时的内容，默认为bind的真实版本。
  + directory：服务器的工作目录，配置文件均参考这个路径，默认为服务器的启动目录。
  + allow-query：设置哪个主机可进行查询，默认为any。
  + allow-query-cache：允许用户查询缓存，如无配置则依次继承allow-recursion、allow-query的设置，若无则默认default（localnets;localhost;）。
  + listen-on-v6：设置服务器监听ipv6请求的接口或端口，不设置则不监听v6请求。
  + recursion：设置服务器是否允许递归查询，默认为yes，如果是yes，并且一个DNS询问要求递归，那么服务器将会做所有能够回答查询请求的工作。若为off，并且服务器不知道答案，它将返回一个推荐响应。
  + dnssec-enable：设定BIND是否支持DNSSEC，该技术并不对数据进行加密，它只是验证您所访问的站点地址是否有效。是一种端到端的安全协议。默认为no。
  + max-ncache-ttl：设定BIND存储否定回答的最长时间。默认为10800，单位秒。最大可设为7天。
  + recursive-clients：BIND同时为用户执行递归查询的最大数量，默认为1000。
  + tcp-clients：服务器同时接受的TCP连接的最大数量，默认为100。
  + pid-file：用来保存BIND的进程号。默认值“/var/run/named.pid”。建议设置，方便kill等程序的使用。

+ bind9日志
  
  + 默认情况下，bind日志消息写到/var/log/messages文件，日志记录内容较少。
  
  + bind logging语法
    
    **建议将 cahnnel default_debug 改为null，否则named.run增长迅速。**
    
    loging {
    
    ​        channel xx {
    
    ​                file ;
    
    ​                syslog ;
    
    ​                null  ;
    
    ​                stderr. ;
    
    ​                severity ;
    
    ​                print-time yes/no ;
    
    ​                print-severity yes/no ;
    
    ​                print-category yes/no;
    
    ​        };
    
    ​        category xx {
    
    ​                ;
    
    ​        }
    
    };
  
  + 日志中有两个概念通道（channel）和类别（category）。
    
    + 通道（channel）
      + 通道指定应该向哪发送日志数据：是发给syslog，还是文件，或是named的标准错误输出，还是位存储桶。
      + severity是指定记录消息的级别（按照严重程度递减）
        + critical
        + error
        + warning
        + notice
        + info
        + debug
        + dynamic
      + print-time：日志中是否写入时间
      + print-severity：日志中是否写入消息级别
      + print-category：日志中是否写入日志类别
    + 类别（category）
      + 指定哪一种类别的数据使用哪个或者哪几个已经定义的通道。
      + default：匹配所有未明确指定的通道类别
      + general：包括所有未明确分类的bind消息
      + client：处理客户请求
      + config：配置文件分析和处理
      + database：与bind内部数据库有关，存储区数据和缓存记录
      + dnssec：处理dnssec签名响应
      + lame-servers：发现错误授权
      + network：网络操作
      + notify：异步区变动通知
      + queries：查询日志
      + resolver：名字解析，包括对来自解析器的递归查询的处理
      + security：认可/非认可的请求
      + update：动态更新事件
      + xfer-in：从远程名字服务器到本地名字服务器的区传送
      + xfer-out：从本地名字服务器到远程名字服务器的区传送

```sh
//本示例为设置转发服务器
// named.conf
//
//
// Provided by Red Hat bind package to configure the ISC BIND named(8) DNS
// server as a caching only nameserver (as a localhost DNS resolver only).
//
// See /usr/share/doc/bind*/sample/ for example named configuration files.
//
// See the BIND Administrator's Reference Manual (ARM) for details about the
// configuration located in /usr/share/doc/bind-{version}/Bv9ARM.html

options {
listen-on port 53 { any; };
listen-on-v6 port 53 { any; };
directory       "/var/named";
dump-file       "/var/named/data/cache_dump.db";
statistics-file "/var/named/data/named_stats.txt";
memstatistics-file "/var/named/data/named_mem_stats.txt";
recursing-file  "/var/named/data/named.recursing";
secroots-file   "/var/named/data/named.secroots";
allow-query     { any; };

//设置上游DNS服务器地址
forward only;
forwarders {8.8.8.8;};

/* 
- If you are building an AUTHORITATIVE DNS server, do NOT enable recursion.
- If you are building a RECURSIVE (caching) DNS server, you need to enable 
recursion. 
- If your recursive DNS server has a public IP address, you MUST enable access 
control to limit queries to your legitimate users. Failing to do so will
cause your server to become part of large scale DNS amplification 
attacks. Implementing BCP38 within your network would greatly
reduce such attack surface 
*/
recursion yes;

dnssec-enable no;
dnssec-validation no;

/* Path to ISC DLV key */
bindkeys-file "/etc/named.root.key";

managed-keys-directory "/var/named/dynamic";

pid-file "/run/named/named.pid";
session-keyfile "/run/named/session.key";
};

logging {
channel default_debug {
file "data/named.run";
severity dynamic;
};
};

zone "." IN {
type hint;
file "named.ca";
};

zone "swimfish.com" IN {
type master;
file "swimfish.com.zone";
};

include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";
```

## dig

+ 格式 
  
  dig [@global-server] [domain] [q-type] [q-class] {q-opt} {d-opt}
  
  + @global-server：默认/etc/resolv.conf定义的DNS，也可修改为其他。
  + domain：要查询的域名。
  + q-type：查询记录的类型，例如a、any、mx、ns、soa、hinfo、axfr、txt等，默认a。
  + q-class：查询的类别，相当于nslookup中的set class。默认值为in（internet）。
  + q-opt：查询选项，比如：-f file通过批处理文件解析多个地址；-p port指定查询端口（默认为53）。
  + d-opt：dig特有的选项。使用时要在前面加一个+号。
    + +vc：使用TCP协议查询
    + +time=##：设置超时时间
    + +trace：从根域开始跟踪查询结果

## nmap

+ icmp扫描
  
  + nmap -PE ip
    
     发送icmp echo、timestamp、netmask请求
  
  + nmap -PP ip
    
    进行icmp时间戳扫描
  
  + namp -PM ip
    
    进行icmp地址掩码扫描

+ tcp扫描
  
  + tcp syn扫描
    
    + tcp syn ping扫描
      
      nmap -PS ip
    
    + tcp syn 扫描
      
      **nmap -sS ip**
  
  + tcp ack扫描
    
    + tcp ack ping扫描
      
      nmap -PA ip
    
    + tcp ack扫描
      
      nmap -sA ip
  
  + tcp全连接扫描
    
    **nmap -sT ip**
  
  + tcp窗口扫描
    
    nmap -sW ip
  
  + tcp fin扫描
    
    nmap -sF ip
  
  + tcp Xmas树扫描
    
    nmap -sX ip
  
  + tcp null扫描
    
    nmap -sN ip

+ udp扫描
  
  + udp ping扫描
    
    nmap -PU ip
  
  + udp扫描
    
    nmap -sU ip

+ ip 扫描
  
  nmap -sO ip

+ 地址列表扫描
  
  nmap -iL file
  
  文件中可包含ip 10.0.2.1、子网 10.0.2.0/24

+ 路由跟踪
  
  nmap --traceroute ip
  
  类似traceroute工具，跟踪到目的的路径

## Port Knocking

> 端口敲门，只有敲击指定端口序列，才可开启防火墙访问所需服务，以kali系统添加端口敲门为例。

### 1. 安装knockd

```
#安装
apt-get install knockd

#服务开机运行
systemctl enable knockd.service 

#显示服务状态
systemctl status knockd.service 
```

### 2. 修改 /etc/default/knockd

```
# control if we start knockd at init or not
# 1 = start
# anything else = don't start
# PLEASE EDIT /etc/knockd.conf BEFORE ENABLING
START_KNOCKD=1

# command line options
KNOCKD_OPTS="-i eth1"
```

### 3. 修改 /etc/knockd.conf

```
[options]
#       UseSyslog
LogFile = /var/log/knock.log

[openSSH]
sequence    = 729,802,826,909
seq_timeout = 15
tcpflags    = syn
#       command     = /sbin/iptables -A INPUT -s %IP% -p tcp --dport 729 -j ACCEPT
#       command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 729 -j ACCEPT
#       command     = /sbin/iptables -I INPUT  -p tcp --dport 729 -j ACCEPT
start_command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 729 -j ACCEPT
cmd_timeout = 30
stop_command     = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 729 -j ACCEPT

[closeSSH]
sequence    = 909,826,802,729
#       seq_timeout = 15
#       command     = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 729 -j ACCEPT
command     = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 729 -j ACCEPT
#       command     = /sbin/iptables -D INPUT -p tcp --dport 729 -j ACCEPT
tcpflags    = syn

[openHTTPS]
sequence    = 12345,54321,24680,13579
seq_timeout = 5
command     = /usr/local/sbin/knock_add -i -c INPUT -p tcp -d 443 -f %IP%
tcpflags    = syn
```

### 4. 发送指定端口序列

```
#以nmap为例，-r指定按照指定序列发送
nmap -p 729,802,826,909 -T4 -A -v -r IP-ADDRESS
```

### 5. 添加默认规则

```
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -j REJECT  
```

### 6. 保存iptables内容（/etc/iptables/rules.v4）

```
iptables-save     

# Generated by iptables-save v1.8.10 (nf_tables) on Mon Mar 25 16:23:35 2024
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [5453:14694665]
-A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A INPUT -j REJECT --reject-with icmp-port-unreachable
COMMIT
# Completed on Mon Mar 25 16:23:35 2024
```

### 7. 载入iptables内容

```
iptables-restore < /etc/iptables/rules.v4
```

### 8. 开机生效iptables规则

```
systemctl enable netfilter-persistent
```

## CentOS安装图形界面

> 命令行界面安装图形界面，并设置默认启动图形界面。

+ 命令行运行级别：3
+ 图形界面运行级别：5

```shell
#安装X Window
yum groupinstall "X Window System"

#查看可选桌面组件
yum grouplist

#安装GNOME桌面
yum groupinstall "GNOME Desktop"

#查看当前运行级别
runlevel

#获取默认的启动界面模式
systemctl get-default

#图形界面到命令行界面，并且设置为开机启动。
systemctl isolate multi-user.target 
systemctl set-default multi-user.target

#命令行界面到图形界面，并且设置为开机启动。
systemctl isolate graphical.target
systemctl set-default graphical.target

#图形界面和命令行界面的切换
CTR+ALT+F2
```

## CentOS安装VirtualBox

> 示例为 centos 7.9  下在线安装 vbox 7.0.8

### 1.修改repo库

```
# 在/etc/yum.repo.d目录下创建virtualbox.repo文件
[root@centos7 yum.repos.d]# cat virtualbox.repo 
[virtualbox]
name=Oracle Linux / RHEL / CentOS-$releasever / $basearch - VirtualBox
baseurl=http://download.virtualbox.org/virtualbox/rpm/el/$releasever/$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://www.virtualbox.org/download/oracle_vbox_2016.asc

# 执行yum clean all 、yum makecache命令
[root@centos7 yum.repos.d]# yum clean all
[root@centos7 yum.repos.d]# yum makecache
```

### 2.安装VBox

```sh
#安装vbox
[root@centos7 yum.repos.d]# yum install VirtualBox-7.0.x86_64

#安装以后建议在图形界面下或通过X11使用
```

### 3.常见故障

+ 使用systemctl检查vboxdrv.service、vboxadd.service、vboxadd-service.service等相关服务是否正确启动，可能会因为缺少必要组件、内核版本造成，解决办法：
  
  + yum install gcc make perl
  
  + yum install kernel-devel
  
  + yum  update kernel

​        （这通常是新装机，安装镜像中的 kernel 版本比线上 repo 库中的 kernel-devel 低，因此安装 kernel-devel 时，安装了比当前运行内核版本高的 kernel-devel，为了一致，可以直接升级当前内核）

+ 无法选中“启用嵌套的VT-x / AMD-V”复选框
  
  ```
  $ vboxmanage list vms
  
  #　　样本输出：
  
  　　"CentOS 8 Server" {73997fc7-4ae2-42bf-a11d-fcbe00721e13}
  
  　　"Ubuntu 20.04 Server" {a7cab540-51c2-4110-b489-a4ad13b71f96}
  
  #　　如您所见，我在Virtualbox中创建了两个VM。
  
  #　　现在，我将使用命令为CentOS 8 VM启用嵌套功能：
  
  　　$ VBoxManage modifyvm "Ubuntu 20.04 Server" --nested-hw-virt on
  
  #　　另外，您可以使用vboxmanage命令小写：
  
  　　$ vboxmanage modifyvm "Ubuntu 20.04 Server" --nested-hw-virt on
  
  #　　此命令启用嵌套虚拟化，并将硬件虚拟化功能传递给虚拟机VM。
  ```

## CentOS安装VNC

> 示例为 centos 7.9  下在线安装 tigerVNC

### 1.服务安装

```
#安装VNC服务
[root@centos7 ~]# yum install -y tigervnc-server

#设置VNC密码(VNC密码非用户密码)
[root@centos7 ~]# vncpasswd 

#开启VNC服务（默认从端口1开始，逐渐增加）
[root@centos7 ~]# vncserver 

New 'centos7:2 (root)' desktop is centos7:2

Starting applications specified in /root/.vnc/xstartup
Log file is /root/.vnc/centos7:1.log

#查看监听端口
[root@centos7 ~]# netstat -tl
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
...   
tcp        0      0 0.0.0.0:5901            0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:5902            0.0.0.0:*               LISTEN     
...
tcp6       0      0 [::]:5901               [::]:*                  LISTEN     
tcp6       0      0 [::]:5902               [::]:*                  LISTEN     
...

#查看VNC端口开启情况
[root@centos7 ~]# vncserver -list

TigerVNC server sessions:

X DISPLAY #     PROCESS ID
:1              2839
:2              3573

#关闭VNC服务
[root@centos7 ~]# vncserver -kill :2
Killing Xvnc process ID 3573
```

### 2.防火墙开放

```
#增加vnc服务
[root@centos7 ~]# firewall-cmd --add-service=vnc-server  --permanent 
Warning: ALREADY_ENABLED: vnc-server
success

#防火墙规则生效
[root@centos7 ~]# firewall-cmd --reload 
success

#显示开放服务
[root@centos7 ~]# firewall-cmd --list-all
public (active)
target: default
icmp-block-inversion: no
interfaces: enp0s3 enp0s8
sources: 
services: dhcpv6-client vnc-server
...
```

### 3.设置为开机自启动服务

```
#复制生成配置文件
[root@centos7 ~]# cp /lib/systemd/system/vncserver@.service  etc/systemd/system/vncserver@:1.service

#编辑配置文件，将<USER>替换为root
[root@centos7 ~]# vim /etc/systemd/system/vncserver@:1.service

[Unit]
Description=Remote desktop service (VNC)
After=syslog.target network.target

[Service]
Type=simple

# Clean any existing files in /tmp/.X11-unix environment
ExecStartPre=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'
ExecStart=/usr/bin/vncserver_wrapper <USER> %i
ExecStop=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'

[Install]
WantedBy=multi-user.target

#重新加载配置文件
[root@centos7 ~]# systemctl daemon-reload 

#开启VNC服务
[root@centos7 ~]# systemctl start  vncserver@\:1.service 

#设置为开机启动
[root@centos7 ~]# systemctl enable  vncserver@\:1.service 
Created symlink from /etc/systemd/system/multi-user.target.wants/vncserver@:1.service to /etc/systemd/system/vncserver@:1.service.
```

## CentOS修改SSH默认端口

> 示例为 centos 7.9  下修改SSH端口，如从22修改为729。
> 
> （**注**：在所有配置修改完成前先不要注释掉原22端口）

### 1.修改SSHD配置文件

```
[root@amika-zhou ~]# cat /etc/ssh/sshd_config 
# If you want to change the port on a SELinux system, you have to tell
# SELinux about this change.
# semanage port -a -t ssh_port_t -p tcp #PORTNUMBER
#
#Port 22
port 729
```

### 2.修改防火墙

```
[root@amika-zhou ~]# firewall-cmd --add-port=729/tcp --permanent
success
[root@amika-zhou ~]# firewall-cmd --remove-service=ssh --permanent
success
[root@amika-zhou ~]# firewall-cmd --reload 
success
[root@amika-zhou ~]# firewall-cmd --list-all
public (active)
target: default
icmp-block-inversion: no
interfaces: eth0
sources: 
services: dhcpv6-client http
ports: 826/tcp 729/tcp
protocols: 
masquerade: no
forward-ports: 
source-ports: 
icmp-blocks: 
rich rules: 
```

### 3.修改SELinux

```
[root@amika-zhou ~]# sestatus
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Max kernel policy version:      31
[root@amika-zhou ~]# semanage port -a -t ssh_port_t -p tcp 729
[root@amika-zhou ~]# semanage port -l |grep ssh
ssh_port_t                     tcp      729, 22
[root@amika-zhou ~]# semanage port - -t ssh_port_t -p tcp 22
[root@amika-zhou ~]# semanage port -l |grep ssh
ssh_port_t                     tcp      729
```

注： 若没semanage命令   yum install policycoreutils-python

### 4.重启SSH和Firewall服务

```
[root@amika-zhou ~]# systemctl restart sshd.service 
[root@amika-zhou ~]# systemctl restart firewalld.service 
```

## python3编译安装

> 用于升级centos7的python2.7

### **1、进入系统，检查当前的 Python 版本。**

```text
python -V Python 2.7.5
```

### **2、下载 Python 软件包并进行解压。**

```text
wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz tar xvf Python-3.8.2.tgz mv Python-3.8.2 /usr/local/src/python3
```

### **3、安装编译所需的依赖项。**

```text
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc libffi-devel -y
```

### **4、进入解压后的 Python 文件夹，执行编译命令。**

```text
cd /usr/local/src/python3/ 
./configure --prefix=/usr/local/python3.8
make
make install (aptinstall)
```

### **5、安装完成后，验证 Python 3 是否安装成功。**

```text
python3 -V Python 3.8.2
```

### **6、查看 Python 的安装路径，并备份 Python 2.7 的可执行文件**

```text
whereis python mv /usr/bin/python /usr/bin/python2.7.bak
```

![img](https://pic3.zhimg.com/80/v2-92bc3395bdb1ff0dfc8fd499cd7da436_720w.webp)

### **7、修改 yum 配置文件**

将两个文件中的 /usr/bin/python 改为 /usr/bin/python2.7，完成后保存。

vi /usr/bin/yum vi /usr/libexec/urlgrabber-ext-down

![img](https://pic1.zhimg.com/80/v2-f5c2dc54d69abab71128a8af693bba18_720w.webp)

![img](https://pic2.zhimg.com/80/v2-fbfbc8491e4c3fb080b938bed7f6c501_720w.webp)

### **8、链接至 Python 3.8 的可执行文件。**

```text
ln -sf /usr/local/bin/python3.8 /usr/bin/python ln -sf /usr/local/bin/pip3.8 /usr/bin/pip
```

### **9、升级 pip 版本。**

```text
pip install --upgrade pip
```

### **10、完成后验证 Python 版本(记得-v是大写）。**

```text
python -V Python 3.8.2
```

## python3第三方库安装

> 主要是介绍离线安装方式

**Q：列出模块所有的依赖**

A：使用pipdeptree

```
pip install pipdeptree

[root@amika-zhou ~]# pipdeptree -p netmiko
netmiko==4.1.2
- ntc-templates [required: >=2.0.0, installed: 3.1.0]
- textfsm [required: >=1.1.0,<2.0.0, installed: 1.1.2]
- future [required: Any, installed: 0.18.3]
- six [required: Any, installed: 1.16.0]
- paramiko [required: >=2.7.2, installed: 3.3.1]
- bcrypt [required: >=3.2, installed: 4.0.1]
- cryptography [required: >=3.3, installed: 40.0.2]
- cffi [required: >=1.12, installed: 1.15.1]
- pycparser [required: Any, installed: 2.21]
- pynacl [required: >=1.5, installed: 1.5.0]
- cffi [required: >=1.4.1, installed: 1.15.1]
- pycparser [required: Any, installed: 2.21]
- pyserial [required: Any, installed: 3.5]
- pyyaml [required: >=5.3, installed: 6.0.1]
- scp [required: >=0.13.3, installed: 0.14.5]
- paramiko [required: Any, installed: 3.3.1]
- bcrypt [required: >=3.2, installed: 4.0.1]
- cryptography [required: >=3.3, installed: 40.0.2]
- cffi [required: >=1.12, installed: 1.15.1]
- pycparser [required: Any, installed: 2.21]
- pynacl [required: >=1.5, installed: 1.5.0]
- cffi [required: >=1.4.1, installed: 1.15.1]
- pycparser [required: Any, installed: 2.21]
- setuptools [required: >=38.4.0, installed: 59.6.0]
- tenacity [required: Any, installed: 8.2.2]
- textfsm [required: ==1.1.2, installed: 1.1.2]
- future [required: Any, installed: 0.18.3]
- six [required: Any, installed: 1.16.0]
```

**Q：安装部分三方库时出错 modulenotfounderror: No module named 'setuptools_rust'**

A：将setuptools更新一下

```
pip install -U pip setuptools
```

## openssl编译安装

> 很多软件必备，比如python，大多数要求1.1.1以上，该版本已停止维护，目前为3.x

**查看centos7默认的openssl版本**

```
[root@cs ~]# openssl version
OpenSSL 1.0.2k-fips  26 Jan 2017
[root@cs ~]# whereis openssl
openssl: /usr/bin/openssl /usr/lib64/openssl /usr/share/man/man1/openssl.1ssl.gz
```

**注意**，虽然openssl的最新版本已经到了3.x，但是亲测，centos7中安装Python解释器的话，最好的搭配是openssl1.1.1版本的。

**依赖下载**

```bash
yum update -y
yum install -y perl-IPC-Cmd
yum install -y openssl openssl-devel
yum install -y zlib zlib-devel openssl-devel sqlite-devel bzip2-devel libffi libffi-devel gcc gcc-c++
yum install -y wget
```

**先备份**

```bash
mv /usr/bin/openssl /usr/bin/openssl.bak
mv /usr/include/openssl /usr/include/openssl.bak
```

**openssl1.1.1tar包下载、解压、编译安装**

我从openssl官网：https://www.openssl.org/source/openssl-1.1.1w.tar.gz下载最新的1.1.1版本的tar包，此时叫做`openssl-1.1.1w.tar.gz`。

```bash
cd /opt
wget https://www.openssl.org/source/openssl-1.1.1w.tar.gz
tar -zxf openssl-1.1.1w.tar.gz
cd openssl-1.1.1w
./config -Wl,-rpath=/usr/lib64 --prefix=/usr/local/openssl --openssldir=/usr/local/openssl --libdir=/usr/lib64 && make -j 4 && make install
ln -s /usr/local/openssl/bin/openssl /usr/bin/openssl
```

**测试**

```bash
openssl version

[root@cs openssl-1.1.1w]# openssl version
OpenSSL 1.1.1w  11 Sep 2023
```

## Zsh-Powerlevel10k

> 将默认的bash替换为zsh，对终端界面进行美化

1.安装zsh

```
# 安装zsh
sudo yum install zsh git -y
（sudo apt install zsh -y）

# 查看系统当前使用的shell
echo $SHELL

# 设置默认zsh
chsh -s /bin/zsh
```

2.安装oh my zsh

```
# curl方法
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# wget方法
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# 国内镜像
sh -c "$(wget -O- https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"
```

3.安装 P10k

```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Gitee 镜像
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

4.在　`~/.zshrc` 中设置 `ZSH_THEME`

```
sed -i 's/ZSH_THEME.*/ZSH_THEME="powerlevel10k\/powerlevel10k"/g' .zshrc
# 添加
ZSH_THEME="powerlevel10k/powerlevel10k"
```

5.重启命令行

```
source .zshrc
```

6.设置 P10k

```
p10k configure

-  Character Set : Unicode [多图]
```

7.安装 zsh 插件

```
# 补全提示
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# 高亮
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# 在 ~/.zshrc 中添加：
plugins=(git zsh-autosuggestions zsh-syntax-highlighting pip)

#应用修改 
source ~/.zshrc 
```

## ishare2安装

> 用于获取模拟器的镜像文件

### 1.安装

+ 在线安装
  
  + ```
    wget -O /usr/sbin/ishare2 https://raw.githubusercontent.com/pnetlabrepo/ishare2/main/ishare2 > /dev/null 2>&1 && chmod +x /usr/sbin/ishare2 && ishare2
    ```
  
  + ```
    curl -o /usr/sbin/ishare2 https://raw.githubusercontent.com/pnetlabrepo/ishare2/main/ishare2 > /dev/null 2>&1 && chmod +x /usr/sbin/ishare2 && ishare2\
    ```

+ 手动安装
  
  + Download the latest version of ishare2 from the GitHub repository.
  + Copy the file to /usr/sbin/ishare2
  + Make the file executable using `chmod +x /usr/sbin/ishare2`
  + Run `ishare2` to start using it
  
  ```
  Note: You can install different versions of ishare2 browsing the releases page or tracking back to previous commits
  ```

### 2.命令格式

```linux
ishare2 [action] [param1] [param2]

action:
search      : Search for images by type
pull        : Download an image by type and number
installed   : Show installed images on server
labs        : Show labs on server and download images for those labs
mylabs      : Same as labs command but using a customized path to labs
relicense   : Generate a new iourc license for bin images
upgrade     : Retrieves a menu that allows users to upgrade ishare2 and PNETLab VM
changelog   : Show the latest changes made to ishare2
gui         : Web app to use ishare2 in browser
help        : Show useful information
test        : Test if ishare2 dependencies are reachable (GitHub, Google Spreadsheets)

param1:
type = all, bin, qemu, dynamips, docker or name

param2:
number = This number can be obtained using ishare2 search <type>
```

### 3.示例

### 3.1 Search for images by type or name

ishare2 search

```linux
# ishare2 search all
# ishare2 search bin
# ishare2 search qemu
# ishare2 search dynamips
```

ishare2 search

Examples:

```linux
# ishare2 search vios
# ishare2 search win-
# ishare2 search winserver
# ishare2 search kali
# ishare2 search mikro
# ishare2 search forti
# ishare2 search nxos
# ishare2 search vmx
# ishare2 search esxi
# ishare2 search palo
# ishare2 search Licensed
You can search for images by name or by type. If you search by name, you will get all images that match the name you entered. If you search by type, you will get all images of that type
```

### 3.2 Pull images by image number

```linux
# ishare2 pull bin <number>
# ishare2 pull qemu <number>
# ishare2 pull dynamips <number>
```

The image number can be obtained using `ishare2 search <type>` command.

Pull all images at once

```linux
# ishare2 pull bin all
# ishare2 pull qemu all (Not available for qemu type due to its large size)
# ishare2 pull dynamips all
```

### 3.3 Show installed images on server

```linux
# ishare2 installed all
# ishare2 installed bin
# ishare2 installed qemu
# ishare2 installed dynamips
# ishare2 installed docker
```

### 3.4 Download all images needed for a lab (Default path)

ishare2 can automatically download all images needed for a lab. This feature is available for .unl labs usually downloaded from [PNetLab Store](https://user.pnetlab.com/store/labs/view) or other sources.

```linux
# ishare2 labs
# ishare2 labs <number>
# ishare2 labs all
Not available for every lab because some of them are encrypted by lab authors and cannot be read by ishare2
```

### 3.5 Download all images needed for a lab (Customized path)

```linux
# ishare2 mylabs <path>
# ishare2 mylabs <path> <number>
# ishare2 mylabs <path> all
```

### 3.6 ishare2 GUI

```linux
# ishare2 gui install

# ishare2 gui start
# ishare2 gui stop
# ishare2 gui restart
```

### 3.7 Extras

```linux
# ishare2 relicense
# ishare2 upgrade
# ishare2 changelog
# ishare2 help
# ishare2 test
```

# 读书笔记

## 恶意网络环境下的Linux防御之道

### 1 基本安全原则

1.1 最小特权原则

+ 完成特定工作所需最小特权。
+ 控制根（root）访问、sudo提级、shell使用等。

1.2 深度防御

+ 不依赖于任何一种防御手段进行保护。
+ 建立层次分明的防御体系。

1.3 保持简单

+ 复杂性是安全之大敌。
+ 系统越复杂，人们就越难理解系统如何工作以及如何相互配合，也就越难保证其安全。
+ 复杂系统最终会压垮试图保护它的人。

1.4 区隔化

+ 背后的思想是：不要把所有鸡蛋放到一个篮子里。
+ 假定攻击者已侵入系统某一部分，应尽可能限制其攻击造成的破坏。
+ 服务：结合虚拟化技术，将每项服务隔离到自己的服务器上，避免其中一项服务遭攻击，影响基础设施的其他部分。
+ 数据：所有数据不要存在同一数据库中，重要文件不要存在单个服务器上。
+ 网络：不要将所有服务放在同一子网，通过网络限制来限定一项服务被攻破时所能做的事。
+ 应用：不要将所有帐户都设置相同的密码（包括用户名）。

### 2 基本密码安全

密码是最基本的身份验证方法之一，现在仍是用户证明自己身份的主要方式。

2.1 密码长度

+ 限制密码长度的目的是增加暴力攻击者可能需要猜测的次数。
+ 破解6位字符密码需要5分钟，8位需要2.5天，12位需要3026年。
+ 使用常用单词做为密码，在使用字典攻击时可能会减少破解时间。

2.2 密码复杂度

+ 通过增加额外字符，增加密码组合总数。
+ 12位全小写密码组合在数量级上仍优于8位最高复杂度密码的组合。

2.3 密码轮换

+ 操作麻烦
+ 策略效果不佳
+ 因为记忆的原因，可能会让人选择弱密码或者有规律的密码。

2.4 密码重用

+ 为减少记忆负担，会在不同的应用和场景选择使用相同的密码或者相同规律的密码。

2.5 密码策略

+ 建议简单原则，取消复杂度要求，密码至少12位。
+ 为便于记忆，选择密码短语。

2.6 密码管理器

+ 保留几个记住的强密码。
+ 其他的用密码管理器生成随机字符密码。

### 3.安全最佳实践

3.1 安全补丁

+ 提高安全性，最重要也是最简单的措施之一。

3.2 共享账户和账户维护

+ 共享账户本身是一种非常糟糕的做法，无论是shell、服务、web账户。
+ 共享账户使审计变得困难。
+ 账号生命周期内应做好其维护工作，如加入、离开、权限、流程等。

3.3 加密

+ 选择加密保存数据（特别是密码、秘钥之类）

+ 现在硬件条件下，因加密而增加的CPU负载很小。

## 网络基本知识

### 1 计算机网络基础知识回顾

### 1.1 网络

+ 层
+ 协议

### 1.2 数据包交换方式

+ 电路交换
  
  + 建立连接
  + 传输数据
  + 拆除电路

+ 报文交换
  
  分组交换的前身，不把报文拆分，因此传输时间比分组交换长。

+ 分组交换
  
  属于存储转发机制，将报文分解为分组，然后传输，到达目的端，对分组排序后组成报文。
  
  + 虚电路技术
    
    依次发送分组
  
  + 数据技术
    
    直接发送分组

### 1.3 计算机网络分类

+ 按覆盖范围
  + 局域网
  + 城域网
  + 广域网
+ 按使用者权限
  + 公用网
  + 专用网
+ 按拓扑结构
  + 总线型
  + 星状
  + 环状
  + 树状
  + 网状
+ 按交换方式
  + 电路交换网络
  + 报文交换网络
  + 分组交换网络

### 1.4 网络性能指标

+ 速率
  
  指一秒传输多少比特，叫比特率，也叫数据率。
  
  + bit/s，bps
  + kb/s，kbps
  + Mb/s，Mbps
  + Gb/s，Gbps

+ 带宽
  
  + 带宽表示网络传输数据的能力，即单位时间内从发送到接收端最高数据传输速率。单位与速度单位相同。
  + 香农定理可知，线路的频率、带宽越高，其所传输的最高速率也越高。
  + 木桶效应可知，发送端的接口速率、传输线路速率、接收端接收速率中的最小值，为最高的数据率（比特率）。

+ 吞吐量
  
  单位时间通过某个网络接口的实际数据量，它的值是所有数据率的和。

+ 时延
  
  + 指数据（报文、分组、比特等）从网络一端到达另外一端所消耗的时间，也称延迟、迟延。
  + 有发送时延、传输时延、排队时延、处理时延。

+ 往返时间
  
  从发送端发送数据开始，到发送端接收到接收端发来的确认分组截止，总共消耗的时间。

+ 利用率
  
  + 线路利用率
    
    某条线路被占用时间的百分比。
  
  + 网络利用率
    
    网络中所有线路利用率的加权平均。利用率增加的时候，时延会增加。一般超过50%，建议扩容或增加带宽。

+ 丢包率
  
  一定时间内，传输中丢失的分组和总分组数量的比例。
  
  无拥塞时，路径丢包率0，轻度拥塞1%-4%，严重5%-15%。
  
  + 接口丢包率
  + 节点丢包率
  + 链路丢包率
  + 路径丢包率
  + 网络丢包率

### 1.5 计算机网络体系架构

+ 开放系统互联参考模型 OSI/RM
  
  + 应用层
  + 表示层
  + 会话层
  + 传输层
  + 网络层
  + 数据链路层
  + 物理层
  
  理想模型，复杂，不适合商业化，输给了TCP/IP协议簇。

+ 传输控制协议/网际协议 TCP/IP
  
  + 应用层
    
    + HTTP
    + FTP
    + Telnet
    + NFS
    + DNS
    + SMTP,POP
    + SNMP
    + RIP,OSPF
    + ......
  
  + 传输层
    
    + TCP
      
      传输控制协议，面向连接，可靠协议。
    
    + UDP
      
      用户数据报协议，无连接，不可靠协议。
  
  + 网络层
    
    + IP
      
      提供IP的服务，是一种无连接的不可靠协议。
    
    + ICMP
      
      网际控制报文协议，在设备间传输控制消息的协议，对用户数据传输起着重要作用。
    
    + ARP
      
      地址解析协议，将IP地址映射为MAC地址。
    
    + RARP
      
      逆向地址解析协议，用于将MAC地址映射为IP地址。
  
  + 网络接口层
  
  ### 1.6 数据包中的flag标志
  
  | 缩写  | 全写   | 意义         |
  | --- | ---- | ---------- |
  | F   | FIN  | 结束会话       |
  | S   | SYN  | 开始会话       |
  | R   | RST  | 复位，中断连接    |
  | P   | PUSH | 推送，立即发送数据包 |
  | A   | ACK  | 应答         |
  | U   | URG  | 紧急         |
  | E   | ECE  | 显示拥塞提醒回应   |
  | W   | CWR  | 拥塞窗口减少     |

## 麒麟V10

国产Linux版本：

+ 银河麒麟 KylinOS
+ 优麒麟 Ubuntu Kylin
+ 中标麒麟 Neo Kylin
+ 深度 Deepin
+ 起点 StartOS

国产芯片：

+ 飞腾
+ 龙芯
+ 申威
+ 兆芯
+ 海光
+ 鲲鹏

## 网络相关

### 生成树

#### 一、BPDU数据报文

> 网桥协议数据单元(BPDU,Bridge Protocol Data Unit)生成树协议是一种桥嵌套协议，在IEEE 802.1d规范里定义，可以用来消除桥回路。它的工作原理是这样的：生成树协议定义了一个数据包，叫做桥协议数据单元BPDU（Bridge Protocol Data Unit）。

网桥用BPDU来相互通信，并用BPDU的相关机能来动态选择根桥和备份桥。但是因为从中心桥到任何网段只有一个路径存在，所以桥回路被消除。
在一个生成树环境里，桥不会立即开始转发功能，它们必须首先选择一个桥为根桥，然后建立一个指定路径。在一个网络里边拥有最低桥ID的将变成一个根桥，全部的生成树网络里面只有一个根桥。

**作用：**

+ 消除环路：通过阻塞冗余链路消除网络中可能存在的网络通信环路；
+ 当前活动的路径发生故障时，激活冗余备份链路，恢复网络连通性。

#### 二、BPDU报文类型：

1. **配置BPDU报文**  (Configuration BPDU)

> 负责建立和维护STP拓扑。
> 
> ***STP:***
> 
> + *没有选举根桥前，所有设备都会发送配置BPDU，选举根桥后只有根桥会发送配置BPDU*
> + *其它非根桥设备在RP端口收到根桥发送过来的配置BPDU后，才会触发向所有指定端口复制一份此配置BPDU，然后发送出去，不会主动发*
> + *非根网桥指定端口只有在接收到次优配置BPDU时，才会主动发送最优BPDU。*
> 
> ***RSTP:***
> 
> + *没有选举根桥前，所有设备都会发送配置BPDU在选举出根桥后即拓扑稳定后，*
> + *无论非根桥是否从RP端口收到根桥发来的配置BPDU，都会按照Hello Timer规定的时间在所有指定端口发送关于根的配置BPDU（除非根端口的BPDU老化或者收到更优的BPDU报文）*

配置BPDU包含了桥ID、路径开销和端口ID等参数。STP协议通过在交换机之间传递配置BPDU来选举根交换机，以及确定每个交换机端口的角色和状态。**在初始化过程中，每个桥都主动发送配置BPDU**。在**网络拓扑稳定以后，只有根桥主动发送配置BPDU**，其他交换机在收到上游传来的配置BPDU后，才会发送自己的配置BPDU。

在配置BPDU报文中，BPDU类型(BPDU Type)的值被设置为**0x00**，主要作用如下所述。

+ 用于选举根桥及端口角色。

+ 通过定期发送(每两秒发送一次)配置BPDU报文维护端口状态。

+ 用于确认接收到的TCN BPDU报文。

+ 用于选举根桥及端口角色。 
2. **TCN BPDU报文**  (Topology Change Notification BPDU)

> 负责传达拓扑的变更。
> 
> 在交换网络中，交换机依赖MAC地址表转发数据，缺省情况下MAC表项的老化时间是300s，如果生成树拓扑发生改变，交换机的转发路径也会改变，当MAC地址表未及时老化将导致数据转发发生错误，因此需要及时更新MAC地址表项此时就可以通过发送TCN BPDU报文来将MAC地址表项的老化时间缩短为15s，达到及时更新MAC地址表项的目的。

TCN BPDU报文中BPDU类型(BPDU Type)的值被设置为**0x80**，其作用是通告网络中拓扑发生了改变。
STP在以下3种情况下会发送TCN BPDU报文：

+ 端口从转发状态过渡到阻塞状态(Blocking)或者禁用状态。
+ 非根桥从一个指定端口收到 TCN BPDU报文后会从自己的根端口向根交换机转发。
+ 端口进入到转发状态并且桥设备已经存在一个指定端口。

（STP发送TCN BPDU的条件最早认为任何端口进入到Forwarding状态或者进入到Disable状态时，认为拓扑发生变化，后来STP对拓扑变化的定义做了优化当DP端口进入到Forwarading状态（建议将连接终端设备的DP端口设置为边缘端口进行优化）RP失效或者RP进入Forwarding状态根桥的DP失效直接发送TC BPDU（非根桥DP端口失效不认为拓扑发生变化））

#### 三、BPDU报文格式

##### STP/RSTP报文格式

1. Protocol Identifier：
2. Protocol Version Identifier:
   + 0：STP 802.1d 传统生成树
   + 2：RSTP 802.1w 快速生成树
   + 3：MSTP 802.1s 多生成树
3. BPDU Type:
   + Configuration BPDU（0x00）
   + Topology Change Notification BPDU（0x80）
4. BPDU Flag:
5. Root Identifier:
6. Root Path Cost:
7. Bridge Indentifier:
8. Port Indentifier:
9. Message Age：消息寿命，STP每经过一台交换机该值+1，本质上就是到根桥的跳数。
10. Max Age：最大寿命，一段时间没有收到根桥消息，达到该值，代表根桥故障。默认20S。
11. Hello Time：BPDU的发送间隔，默认2S
12. Forward Delay：监听、学习状态停留的时间，默认15S

<img title="" src="stp.png" alt="img" style="zoom:66%;">

##### MSTP报文格式：

<img title="" src="mstp.png" alt="img" style="zoom:66%;">

<img title="" src="mstp-1.png" alt="img" style="zoom:66%;">

#### 四、STP选举

选举原则：

------

+ 同一个二层网络，根桥设备只有一个。
+ 非根桥设备只有一个根端口，根桥设备只有指定端口。
+ 每条链路上只有一个指定端口。
+ 非根端口、非指定端口都称为阻塞端口。

比较规则：

------

+ RootID：优先级（默认32768）+MAC（交换机背板MAC）

+ Cost路径开销：接口带宽反比计算，802.1d中10Mbps为100，100Mbps为19，1000Mbps为4，10000Mbps为2

+ BridgeID：本交换机的ID标识

+ 包含交换机优先级和交换机MAC

+ 优先级：0-65535，缺省32768，必须是4096倍数，越小越好

+ MAC：交换机端口MAC中最小值作比较，越小越好

+ portID：优先级（默认128）+端口号

+ 优先级：0-255，缺省128，必须是16的倍数

+ 端口编号：越小越好

选举过程：

------

1. 选举根桥

每个交换机都假设自己是根，相互发送BPDU报文，根据规则选举根桥。

+ 比较桥优先级，越小越优

+ 比较MAC地址，越小越优

<img title="" src="stp-gqxj.png" alt="img" style="zoom:66%;">

2. 非根交换机选举根端口

每个交换机根据接收到的根桥BPDU中的开销（最优路径）选举根端口，交换机接收累加开销，转发不累加开销。

+ 比较端口收到的BPDU报文中Root ID最小的，为根端口（同一根桥，Root ID是一致的）
+ 比较路径开销，此开销为端口收到的最小路径开销，越小越优
+ 比较对端的BID，选优先级高的比较对端的PID，选择优先级高的
+ 比较本端口的PID，选择优先级高的

<img title="" src="stp-gdkxj.png" alt="img" style="zoom:66%;">

3. 每条线路选举指定端口

每条链路根据比较规则来选出指定端口，每条链路必须有指定端口。

+ 比较路径开销，此开销指的是端口发送出去的根路径开销，越小越优先（Eth端口开销默认为20000）
+ 比较本端的BID，选优先级高的
+ 比较本段的PID，选择优先级高的

<img title="" src="stp-zddkxj.png" alt="img" style="zoom:66%;">

4. 阻塞非根、非指定端口

除了根端口，指定端口，其他的为阻塞端口。

<img title="" src="stp-zsdkxj.png" alt="img" style="zoom:66%;">

​        **注：值越小优先级越高**

端口角色：

------

1. RP：根端口。每个非根网桥上有且只有一个，选举到达根网桥上路径开销值最小的成为根端口。
2. DP：指定端口。根网桥上每个端口都是指定端口，非根网桥上需要转发数据的端口也是指定端口。
3. AP：预备端口。该接口状态为blocking状态，只收BPDU,不发BPDU。

端口状态描述：

------

1. Disabled (禁用状态)：不转发BPDU报文，也不转发用户流量，不参与生成树计算；
+ 端口为SHUTDOWN
2. Blocking (阻塞状态) ：仅接收并处理BPDU，不转发用户流量，不学习MAC地址表；
+ 端口启用STP，还没选为根端口或指定端口；
+ 端口为AP；
3. Listening (侦听状态) ：接收并且发送BPDU，不接收也不转发用户流量，不学习MAC地址表，确定端口角色，将进行选举动作；
4. Learning (学习状态)：接收并且发送BPDU，不接收也不转发用户流量，学习MAC地址表；
5. Forwarding (转发状态)：接收并且发送BPDU，转发数据帧，学习MAC地址表，参与生成树计算。

> 注：端口由Blocking过渡到Forwarding有50S延时。
> 
> ​            Blocking到Listening有20S 老化时间
> 
> ​            Listening到Learning 有15S过渡时间（为了选举）
> 
> ​            Learning到Forwarding有 15S过渡时间（为了学习MAC地址）
> 
> STP从开启到转发，至少30s，最大50s。

端口开销标准

------

<img title="" src="stp-dkkx.png" alt="img" style="zoom:66%;">
