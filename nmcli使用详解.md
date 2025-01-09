# nmcli工具详解

## 1. nmcli 安装

**nmcli实用工具是由NetworkManager包提供，有关详情，请参阅NetworkManager（8）**

```bash
~]$ yum install -y NetworkManager
```

> 在CentOS 7中，默认已安装。
> 
> 其他系统中，例如RaspBerry中为 apt install network-manager

------

## 2. nmcli 基本选项

| 选项  | 作用                                   |
| --- | ------------------------------------ |
| -t  | 简洁输出，会将多余的空格删除，                      |
| -p  | 人性化输出，输出很漂亮                          |
| -n  | 优化输出，有两个选项tabular(不推荐)和multiline(默认) |
| -c  | 颜色开关，控制颜色输出(默认启用)                    |
| -f  | 过滤字段，all为过滤所有字段，common打印出可过滤的字段      |
| -g  | 过滤字段，适用于脚本，以:分隔                      |
| -w  | 超时时间                                 |

------

## 3. general 常规选项

命令格式：`nmcli general {status|hostname|permissions|logging}`
命令描述：使用此命令可以显示网络管理器状态和权限，你可以获取和更改系统主机名，以及网络管理器日志记录级别和域。

### 3.1 status

显示网络管理器的整体状态。

```bash
[root@www ~]# nmcli general status
STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN    
connected  full          enabled  enabled  enabled  enabled 
```

### 3.2 hostname

获取主机名或该更主机名，在没有给定参数的情况下，打印配置的主机名，当指定了参数，它将被移交给NetworkManager，以设置为新的系统主机名。

```bash
[root@www ~]# nmcli general hostname
www.keepdown.cn
[root@www ~]# nmcli general hostname myself
[root@www ~]# nmcli general hostname
myself
```

### 3.3 permissions

显示当前用户对网络管理器可允许的操作权限。 如启用和禁用网络、更改WI-FI和WWAN状态、修改连接等。

```bash
[root@www ~]# nmcli general permissions 
PERMISSION                                                 VALUE 
org.freedesktop.NetworkManager.enable-disable-network      yes   
org.freedesktop.NetworkManager.enable-disable-wifi         yes   
org.freedesktop.NetworkManager.enable-disable-wwan         yes   
org.freedesktop.NetworkManager.enable-disable-wimax        yes   
org.freedesktop.NetworkManager.sleep-wake                  yes   
org.freedesktop.NetworkManager.network-control             yes   
org.freedesktop.NetworkManager.wifi.share.protected        yes   
org.freedesktop.NetworkManager.wifi.share.open             yes   
org.freedesktop.NetworkManager.settings.modify.system      yes   
org.freedesktop.NetworkManager.settings.modify.own         yes   
org.freedesktop.NetworkManager.settings.modify.hostname    yes   
org.freedesktop.NetworkManager.settings.modify.global-dns  yes   
org.freedesktop.NetworkManager.reload                      yes   
org.freedesktop.NetworkManager.checkpoint-rollback         yes   
org.freedesktop.NetworkManager.enable-disable-statistics   yes
```

### 3.4 loggin

获取和更改网络管理器日志记录级别和域，没有任何参数当前日志记录级别和域显示。为了更改日志记录状态, 请提供级别和域参数,有关可用级别和域值, 参阅**NetworkManager.conf(5)**

```bash
[root@www ~]# nmcli general logging
LEVEL  DOMAINS             
INFO   PLATFORM,RFKILL,ETHER,WIFI,BT,MB,DHCP4,DHCP6,PPP,IP4,IP6,AUTOIP4,DNS,VPN,SHARING,SUPPLICANT,AGENTS,SETTINGS,SUSPEND,CORE,DEVICE,OLPC,INFINIBAND,FIREWALL,ADSL,BOND,VLAN,BRIDGE,TEAM,CONCHECK,DCB,DISPATCH,AUDIT,SYSTEMD,PROXY
```

------

## 4. networking 网络控制

命令格式：`nmcli networking {on|off|connectivity}`
命令描述：查询网络管理器网络状态，开启和关闭网络
选项：

- **on**: 禁用所有接口

- **off**: 开启所有接口

- connectivity
  
  : 获取网络状态，可选参数
  
  ```
  checl
  ```
  
  告诉网络管理器重新检查连接性，否则显示最近已知的状态。而无需重新检查。（可能的状态如下所示）
  
  - **none**: 主机为连接到任何网络
  - **portal**: 无法到达完整的互联网
  - **limited**: 主机已连接到网络，但无法访问互联网
  - **full**: 主机连接到网络，并具有完全访问
  - **unknown**: 无法找到连接状态

```bash
[root@www ~]# nmcli networking connectivity
full
[root@www ~]# nmcli networking connectivity check
full
```

------

## 5. radio 无线传输控制

命令格式：`nmcli radio {all|wifi|wwan}`
显示无线开关状态，或启用和禁用开关

```bash
[root@www ~]# nmcli radio all
WIFI-HW  WIFI     WWAN-HW  WWAN    
enabled  enabled  enabled  enabled 
[root@www ~]# nmcli radio all off
[root@www ~]# nmcli radio all
WIFI-HW  WIFI      WWAN-HW  WWAN     
enabled  disabled  enabled  disabled 
[root@www ~]# nmcli radio wifi on
[root@www ~]# nmcli radio wwan on
[root@www ~]# nmcli radio all
WIFI-HW  WIFI     WWAN-HW  WWAN    
enabled  enabled  enabled  enabled
```

------

## 6. monitor 活动监视器

活动监视器（ACTIVITY MONITOR）

观察网络管理器活动。监视连接的变化状态、设备或连接配置文件。

另请参阅 `nmcli connection monitor` 和`nmcli device monitor`某些设备或连接中的更改。

------

## 7. connection 连接管理

命令格式：`nmcli connection {show|up|down|modify|add|edit|clone|delete|monitor|reload|load|import|export}`
这是主要使用的一个功能。

### 7.1 show

show有两种用法，分别是：

**1. 列出活动的连接，或进行排序（+-为升降序）**

```bash
# 查看所有连接状态
[root@www ~]# nmcli connection show
# 等同于nmcli connection show --order +active
[root@www ~]# nmcli connection show --active
# 以活动的连接进行排序
[root@www ~]# nmcli connection show --order +active
# 将所有连接以名称排序
[root@www ~]# nmcli connection show --order +name
# 将所有连接以类型排序(倒序)
[root@www ~]# nmcli connection show --order -type
```

**2. 查看指定连接的详细信息**

```bash
[root@www ~]# nmcli connection show eth0
# 省略......
```

### 7.2 up

激活连接，提供连接名称或uuid进行激活，若未提供，则可以使用ifname指定设备名进行激活。

```bash
# 以连接名进行激活
[root@www ~]# nmcli connection up eth0
# 以uuid进行激活
[root@www ~]# nmcli connection up 5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03
# 以设备接口名进行激活
[root@www ~]# nmcli connection up ifname eth0
```

### 7.3 down

停用连接，提供连接名或uuid进行停用，若未提供，则可以使用ifname指定设备名进行激活。

```bash
# 以连接名进行激活
[root@www ~]# nmcli connection down eth0
# 以uuid进行激活
[root@www ~]# nmcli connection down 5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03
# 以设备接口名进行激活
[root@www ~]# nmcli connection down ifname eth0
```

### 7.4 modify

这些属性可以用`nmcli connection show eth0`进行获取，然后可以修改、添加或删除属性，若要设置属性，只需指定属性名称后跟值，空值将删除属性值，同一属性添加多个值使用`+`。同一属性删除指定值用`-`加索引。

**添加多个ip**

```bash
# 添加三个
[root@www ~]# nmcli connection modify eth0 +ipv4.addresses 192.168.100.102/24
[root@www ~]# nmcli connection modify eth0 +ipv4.addresses 192.168.100.103/24
[root@www ~]# nmcli connection modify eth0 +ipv4.addresses 192.168.100.104/24
# 查看
[root@www ~]# nmcli -f IP4 connection show eth0
IP4.ADDRESS[1]:                         192.168.100.101/24
IP4.GATEWAY:                            192.168.100.100
IP4.DNS[1]:                             8.8.8.8
# 启用配置
[root@www ~]# nmcli connection up eth0
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/18)
# 再次查看
[root@www ~]# nmcli -f IP4 connection show eth0
IP4.ADDRESS[1]:                         192.168.100.101/24
IP4.ADDRESS[2]:                         192.168.100.102/24
IP4.ADDRESS[3]:                         192.168.100.103/24
IP4.ADDRESS[4]:                         192.168.100.104/24
IP4.GATEWAY:                            192.168.100.100
IP4.DNS[1]:                             8.8.8.8
```

**删除指定ip**

```bash
[root@www ~]# nmcli -f IP4 connection show eth0
IP4.ADDRESS[1]:                         192.168.100.101/24
IP4.ADDRESS[2]:                         192.168.100.102/24
IP4.ADDRESS[3]:                         192.168.100.103/24
IP4.ADDRESS[4]:                         192.168.100.104/24
IP4.GATEWAY:                            192.168.100.100
IP4.DNS[1]:                             8.8.8.8
# 删除索当前索引为2的地址
[root@www ~]# nmcli connection modify eth0 -ipv4.addresses 2
# 查看
[root@www ~]# nmcli -f IP4 connection show eth0
IP4.ADDRESS[1]:                         192.168.100.101/24
IP4.ADDRESS[2]:                         192.168.100.102/24
IP4.ADDRESS[3]:                         192.168.100.103/24
IP4.ADDRESS[4]:                         192.168.100.104/24
IP4.GATEWAY:                            192.168.100.100
IP4.DNS[1]:                             8.8.8.8
# 再次激活
[root@www ~]# nmcli connection up eth0
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/19)
# 查看
[root@www ~]# nmcli -f IP4 connection show eth0
IP4.ADDRESS[1]:                         192.168.100.101/24
IP4.ADDRESS[2]:                         192.168.100.102/24
IP4.GATEWAY:                            192.168.100.100
IP4.DNS[1]:                             8.8.8.8
```

### 7.5 add

这是创建一个新的连接，需要指定新创建连接的属性，语法与modify相同。

```bash
[root@www ~]# nmcli con add con-name eth1 type ethernet  autoconnect yes ifname eth0
# con-name     连接名称
# type              连接类型
# autoconnect 是否自动连接
# ifname          连接到的设备名称


% nmcli con add type wifi ssid YDBG con-name tt ifname wlp0s20f3 ip4 192.168.104.6/22 gw4 192.168.104.1  
```

更多的类型或方法可以使用`nmcli connection add help`查看。

### 7.6 clone

克隆连接，克隆一个存在的连接，除了连接名称和uuid是新生成的，其他都是一样的。

```bash
[root@www ~]# nmcli connection clone eth0 eth0_1
```

### 7.7 delete

删除连接，这将删除一个连接。

```bash
[root@www ~]# nmcli connection delete eth0_1
```

### 7.8 load

从磁盘加载/重新加载一个或多个连接文件，例如你手动创建了一个`/etc/sysconfig/network-scripts/ifcfg-ethx`连接文件，你可以将其加载到网络管理器，以便管理。

```bash
[root@www ~]# echo -e "TYPE=Ethernet\nNAME=ethx" > /etc/sysconfig/network-scripts/ifcfg-ethx
[root@www ~]# nmcli connection show
NAME  UUID                                  TYPE            DEVICE 
eth0  5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03  802-3-ethernet  eth0 
[root@www ~]# nmcli connection load /etc/sysconfig/network-scripts/ifcfg-ethx 
[root@www ~]# nmcli connection show
NAME  UUID                                  TYPE            DEVICE 
eth0  5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03  802-3-ethernet  eth0   
ethx  d45d97fb-8530-60e2-2d15-d92c0df8b0fc  802-3-ethernet  --
```

### 7.9 monitor

监视连接配置文件活动。每当指定的连接更改时, 此命令都会打印一行。要监视的连接由其名称、UUID 或 D 总线路径标识。如果 ID 不明确, 则可以使用关键字 id、uuid 或路径。有关 ID 指定关键字的说明, 请参阅上面的连接显示。

监视所有连接配置文件, 以防指定无。当所有监视的连接消失时, 该命令将终止。如果要监视连接创建, 请考虑使用带有 nmcli 监视器命令的全局监视器。

```bash
[root@www ~]# nmcli connection monitor eth0
```

------

## 8. device 设备管理

命令格式：`nmcli device {status|show|set|connect|reapply|modify|disconnect|delete|monitor|wifi|lldp}`
显示和管理设备接口。该选项有很多功能，例如连接wifi，创建热点，扫描无线，邻近发现等，下面仅列出常用选项。详细功能可使用`nmcli device help`查看。

### 8.1 status

打印设备状态，如果没有将命令指定给`nmcli device`，则这是默认操作。

```bash
[root@www ~]# nmcli device status
DEVICE  TYPE      STATE      CONNECTION 
eth0    ethernet  connected  eth0       
lo      loopback  unmanaged  --         
[root@www ~]# nmcli device
DEVICE  TYPE      STATE      CONNECTION 
eth0    ethernet  connected  eth0       
lo      loopback  unmanaged  --
```

### 8.2 show

显示所有设备接口的详细信息。

```bash
# 不指定设备接口名称，则显示所有接口的信息
[root@www ~]# nmcli device show eth0
GENERAL.DEVICE:                         eth0
GENERAL.TYPE:                           ethernet
GENERAL.HWADDR:                         00:0C:29:99:9A:A1
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
GENERAL.CONNECTION:                     eth0
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConnection/9
WIRED-PROPERTIES.CARRIER:               on
IP4.ADDRESS[1]:                         192.168.100.101/24
IP4.ADDRESS[2]:                         192.168.100.102/24
IP4.GATEWAY:                            192.168.100.100
IP4.DNS[1]:                             8.8.8.8
```

### 8.3 set

设置设备属性

```bash
[root@www ~]# nmcli device set ifname eth0 autoconnect yes
```

### 8.4 connect

连接设备。提供一个设备接口，网络管理器将尝试找到一个合适的连接, 将被激活。它还将考虑未设置为自动连接的连接。(默认超时为90s)

```bash
[root@www ~]# nmcli dev connect eth0
Device 'eth0' successfully activated with '5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03'.
```

### 8.5 reapply

使用上次应用后对当前活动连接所做的更改来更新设备。

```bash
[root@www ~]# nmcli device reapply eth0
Connection successfully reapplied to device 'eth0'.
```

### 8.6 modify

修改设备上处于活动的设备，但该修改只是临时的，并不会写入文件。（语法与 nmcli connection modify 相同）

```bash
[root@www ~]# nmcli device modify eth0 +ipv4.addresses 192.168.100.103/24
Connection successfully reapplied to device 'eth0'.
[root@www ~]# nmcli dev show eth0
[root@www ~]# nmcli device modify eth0 -ipv4.addresses 1
Connection successfully reapplied to device 'eth0'.
```

### 8.7 disconnect

断开当前连接的设备，防止自动连接。但注意，断开意味着设备停止！但可用 connect 进行连接

```bash
[root@www ~]# nmcli device disconnect eth0
```

### 8.8 delete

删除设备，该命令从系统中删除接口。请注意, 这仅适用于诸如bonds, bridges, teams等软件设备。命令无法删除硬件设备 (如以太网)。超时时间为10秒

```bash
[root@www ~]# nmcli device delete bonds
```

### 8.9 monitor

监视设备活动。每当指定的设备更改状态时, 此命令都会打印一行。

监视所有设备以防未指定接口。当所有指定的设备消失时, 监视器将终止。如果要监视设备添加, 请考虑使用带有 nmcli 监视器命令的全局监视器。

```bash
[root@www ~]# nmcli device monitor eth0
```

------

## 9. nmcli 返回状态码

mcli 如果成功退出状态值为0，如果发生错误则返回大于0的值。

- **0**: 成功-指示操作已成功
- **1**: 位置或指定的错误
- **2**: 无效的用户输入，错误的nmcli调用
- **3**: 超时了（请参阅 --wait 选项）
- **4**: 连接激活失败
- **5**: 连接停用失败
- **6**: 断开设备失败
- **7**: 连接删除失败
- **8**: 网络管理器没有运行
- **10**: 连接、设备或接入点不存在
- **65**: 当使用 --complete-args 选项，文件名应遵循。

https://www.cnblogs.com/liuhedong/

# Linux性能监控工具

| 工具        | 介绍                                     |
| --------- | -------------------------------------- |
| dbench    | 文件系统加载基准测试工具                           |
| filebench | 基于模型的文件系统工作负载生成器                       |
| fio       | I/O基准测试和压力/硬件验证工具                      |
| fs_mark   | 基准同步/异步文件创建                            |
| iperf     | TCP/UDP带宽性能的测量工具                       |
| nuttcp    | 确定初始TCP或UDP网络层吞吐量                      |
| siege     | HTTP回归测试和基准测试实用程序                      |
| sockperf  | 用于测试延迟和吞吐量的网络基准测试实用程序（网络套接字API的延迟和吞吐量） |
| stress    | 将给定子系统置于指定负载下的工具                       |
| sysbench  | 系统性能指标                                 |
| wbox      | 用于测试Web服务器和Web应用程序的HTTP性能的命令行工具        |
| ttcp      | 使用TCP/IP对内存进行内存性能测量的工具                 |
| qperf     | 测量网络套接字和RDMA性能（网络测试）                   |
| top       | 动态显示系统进程的指标                            |
| ps        | 获取一组选定活动进程的快照                          |
| vmstat    | 虚拟内存统计，内存、分页、块输入/输出。终端和CPU活动的及时报告      |
| sar       | 系统活动报告器，                               |
| perf      | 使用硬件性能计数器和内核跟踪点来跟踪其他命令和应用程序对系统的影响。     |
| tuned     | 根据配置控制系统的资源                            |

# 常用命令或技巧

## 1.CentOS系统日志

* 存放位置
  
  * /var/log

* 相关日志
  
  * 系统引导日志：/var/log/boot.log
  * 核心启动日志：/var/log/messages
  * 系统日志：一般在/var/log下
    * /var/run/utmp 记录现在登录的用户
    * /var/log/lastlog 记录每个用户最后的登录信息
    * /var/log/btmp 记录错误的登录尝试
    * /var/log/auth.log 需要身份确认的操作

* 日志级别
  
  | 编码  | 优先级     | 严重性                      |
  | --- | ------- | ------------------------ |
  | 7   | debug1  | 对开发人员调试应用有用，操作过程中无用。     |
  | 6   | info    | 正常的操作信息，可以手机报告、监测吞吐量等。   |
  | 5   | notice  | 注意，正常且重要的东西。             |
  | 4   | warning | 警告，如果不及时处理，将会发生错误。       |
  | 3   | err     | 错误，阻止某个模块或程序的功能不能正常使用。   |
  | 2   | crit    | 关键错误，已经影响整个系统或者软件不能正常工作。 |
  | 1   | alert   | 警报，需要立即修改。               |
  | 0   | emerg   | 紧急，内核崩溃等严重信息。            |

* 日志查看工具 
  
  * journalctl
    * journalctl：不带参数显示所有信息（从旧到新）。
    * journalctl -r：反序，从新到旧。
    * journalctl -f：显示最新日志条目，实时输出。
    * journalctl -n：（--lines）指定输出的行数
    * journalctl --since 指定时间 --until 指定时间
    * journalctl -u 服务名称：查看指定服务的日志。
    * journalctl -k：查看系统核心日志。
    * ​

## 