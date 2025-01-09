# ubuntu 自定义开机画面

## 1 启动过程

### 1.1 UEFI固件加载：

- 在系统启动时，UEFI固件首先加载，并显示制造商的Logo（如“LEGION”），这在启动过程中称为“splash screen”。
- 这张图片是嵌入在UEFI固件中的，用户通常无法直接修改或访问它，除非通过特殊的固件更新工具。
- 更改UEFI启动时显示的Logo图片通常是非常复杂且风险较高的操作，一般来说，普通用户不建议尝试。

### 1.2 操作系统加载：

- 随后，操作系统（如Ubuntu）启动并接管显示输出。在这时，UEFI的Logo通常会被操作系统自己的启动画面所覆盖。
- 在Ubuntu中，启动画面通常由`Plymouth`工具显示，但在你的情况中，似乎没有使用`Plymouth`。

## 2 修改Plymouth启动画面

### 2.1 准备Plymouth主题

#### 2.1.1 查找和下载主题

    你可以从网上下载Plymouth主题，或者自己创建一个。

+ **下载主题**：访问 [gnome-look.org](https://www.gnome-look.org/) 等网站，查找适合你的Plymouth主题。
- **创建主题**：如果你希望创建自己的主题，可以参考现有主题的结构和文件格式进行修改。

#### 2.1.2 解压并安装主题

    将下载的主题解压到 `/usr/share/plymouth/themes/` 目录中。

```shell
sudo tar -xvf your_theme.tar.gz -C /usr/share/plymouth/themes/
```

### 2.2 设置Plymouth主题

#### 2.2.1 查看已安装主题

    使用以下命令查看系统中已安装的Plymouth主题：

```shell
sudo update-alternatives --display default.plymouth
```

#### 2.2.2 设置新主题

    将Plymouth主题设置为你下载或创建的主题：

+ **更新替换项**：注册新的主题到 `update-alternatives` 系统。
  
  ```shell
  sudo update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth /usr/share/plymouth/themes/your_theme/your_theme.plymouth 100
  ```

+ **选择默认主题**：设置默认的Plymouth主题。
  
  ```shell
  sudo update-alternatives --config default.plymouth
  ```

    你会看到类似如下的输出，选择你想使用的主题：

```shell
There are 3 choices for the alternative default.plymouth (providing /usr/share/plymouth/themes/default.plymouth).

Selection    Path                                                           Priority   Status
------------------------------------------------------------
  0            /usr/share/plymouth/themes/default.plymouth                    50        auto mode
  1            /usr/share/plymouth/themes/default.plymouth                    50        manual mode
  2            /usr/share/plymouth/themes/your_theme/your_theme.plymouth      100       manual mode
```

    输入对应的数字选择新主题，然后按回车。

### 2.3 更新Plymouth配置

    执行以下命令来更新Plymouth配置：

```shell
sudo update-initramfs -u
```

### 2.4 重启系统

    最后，重启系统以查看效果：

```shell
sudo reboot
```

### 2.5 手动修改和自定义主题

    如果你希望进一步自定义主题，可以手动编辑Plymouth主题文件。以下是Plymouth主题文件的结构和一些关键配置项：

#### 2.5.1 主题文件结构

    一个Plymouth主题通常包含以下文件：

- **`your_theme.plymouth`**：主题配置文件，定义了主题的基本信息和资源文件。
- **`your_theme.script`**：脚本文件，定义了启动时的动画和图形元素。
- **`images/` 目录**：包含启动画面的图片资源。

#### 2.5.2 编辑主题配置文件

+ **打开配置文件**：

    编辑主题的主配置文件，例如 `/usr/share/plymouth/themes/your_theme/your_theme.plymouth`：

```shell
sudo nano /usr/share/plymouth/themes/your_theme/your_theme.plymouth
```

+ **修改配置项**：

    配置文件的内容类似如下：

```shell
[Plymouth Theme]
Name=Your Theme
Description=Custom Plymouth Theme
ModuleName=script

[script]
ImageDir=/usr/share/plymouth/themes/your_theme/images
ScriptFile=/usr/share/plymouth/themes/your_theme/your_theme.script
```

    你可以修改 `Name` 和 `Description` 来定制主题的信息。

#### 2.5.3 编辑脚本文件

+ **打开脚本文件**：

    编辑主题的脚本文件，例如 `/usr/share/plymouth/themes/your_theme/your_theme.script`：

```shell
sudo nano /usr/share/plymouth/themes/your_theme/your_theme.script
```

+ **自定义动画和图形**：

    你可以在脚本文件中定义动画效果和图形元素。示例脚本可能如下：

```shell
// Load and show image
Image img = Image("background.png");
img.SetPosition(PLYMOUTH_CENTER_ON_PARENT, PLYMOUTH_CENTER_ON_PARENT);
my_sprite = Sprite();
my_sprite.SetImage(img);

// Create progress bar
progress_bar = ProgressBar();
progress_bar.SetPosition(0, GetY(resolved->terminal_mode) - 20);
progress_bar.SetSize(GetX(resolved->terminal_mode), 20);
progress_bar.SetBackgroundColor(0.0, 0.0, 0.0);
```

## 3 解决常见问题

### 3.1 无法显示新主题

    如果你无法看到新主题，检查以下内容：

- 确认主题路径正确，图片资源和脚本文件存在。
- 确保更新了`initramfs`，并重启系统。

### 3.2 主题配置出错

    如果主题配置文件有错误，系统可能会回退到默认主题。检查配置文件的语法和路径是否正确。

## 4 参考执行脚本

+ 编辑好新的logo文件

+ 执行chlog脚本
  
  ```shell
  % vim chlog
  
  #!/bin/zsh
  
  echo " ===================================="
  echo "| 本脚本执行系统启动、关机logo的修改 |"
  echo " ====================================\n"
  
  if (( $# != 1 ))  {
  	echo '未指定正确的logo文件！'
  } elif { sudo cp $1 /usr/share/plymouth/ubuntu-logo.png && sudo cp $1 /usr/share/plymouth/themes/spinner/watermark.png && sudo update-initramfs -u } { 
  	echo '\nLogo修改完成，重启生效。'
  
  } else {
  	echo '\n脚本未正确执行，请检查' } 
  
  
  % ./chlogo tt2.png
  本脚本执行系统启动、关机logo的修改
  
  update-initramfs: Generating /boot/initrd.img-6.8.0-51-generic
  I: The initramfs will attempt to resume from /dev/nvme0n1p3
  I: (UUID=ba5d0c66-6c23-481c-a73f-435e6a902010)
  I: Set the RESUME variable to override this.
  Logo修改完成，重启生效。
  ```

--- 

# ubuntu 向应用和DOCK中添加图标

## 1 安装位置

    一般在/opt/下

## 2 执行链接

    在/usr/bin下创建应用执行文件的软链接

```shell
ln -s 原文件 链接文件
```

## 3 修改配置文件

    为保证应用能在“显示应用”中找到，并且后期能添加到DOCK，需要在/usr/share/applications下添加.desktop配置文件

```shell
[Desktop Entry]
Version=1.0
Name=世界那么大，我要去溜达...
Comment=An easy way to you want to
Keywords=Q;security;free;network;
Categories=GNOME;GTK;Settings;Security;X-GNOME-Settings-Panel;X-GNOME-SystemSettings;X-Unity-Settings-Panel;X-XFCE-SettingsDialog;X-XFCE-SystemSettings;
Exec=Q
Icon=phone.svg
Terminal=false
Type=Application
X-GNOME-Settings-Panel=Q
X-Unity-Settings-Panel=Q
X-Ubuntu-Gettext-Domain=Q
```

    主要修改“Name”和“Exec”。

    注销重新登录生效。

--- 

# Ubuntu 配置 sudo 时不需要输入密码

> 此方法在 Ubuntu 24.04 中测试通过，其他 Linux 版本仅供参考。

    sudo 相关的配置位于 `/etc/sudoers` 文件内。但这个文件不建议直接编辑，而是使用以下命令：

```shell
sudo visudo
```

该命令会打开默认的编辑器编辑 `/etc/sudoers` 文件，并在保存时自动检查文件格式并设置到正确的文件权限。

进入编辑状态后，在文件最后面（划重点：一定是在文件最后面）添加以下内容：

```shell
swimfish ALL=(ALL) NOPASSWD: ALL
```

    解释一下：`swimfish` 是我的登录用户名，根据需要改成自己的用户名即可。`NOPASSWD` 表示不需要输入密码，后面的 ALL 表示所有命令。

    也就是说，`swimfish` 用户在执行 `所有的` sudo 命令时均不需要输入密码。如果要设置指定命令无需输入密码，只需要把最后面的 `ALL` 替换为具体命令即可。

    如果要针对用户组设置规则，只需在组名前添加 `%` 即可，如（swimfish 为用户组的名字）：

```shell
%swimfish ALL=(ALL) NOPASSWD: ALL
```

> 重点：之前查了很多文档各种尝试均未生效，最后得知自己添加的内容 **一定** 要放到**文件最后**，否则是不生效的。

> Tips: `/etc/sudoers` 文件最后面有一行 `#includedir /etc/sudoers.d`，也可以把注释取消掉，并把自己的规则写到 `/etc/sudoers.d` 目录中，文件名任意。
