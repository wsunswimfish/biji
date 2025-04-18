以**Ubuntu系统启动过程为主线**，结合**Plymouth 启动画面主题配置**进行详细说明，辅以实战配置实例，确保**结构清晰、逻辑严谨、易于理解和实践**。

---

## 一、Ubuntu 启动流程概述（与启动画面关系）

Ubuntu 的启动流程大致如下：

| 阶段               | 主要组件             | 显示内容              | 是否与 Plymouth 相关    |
| ---------------- | ---------------- | ----------------- | ------------------ |
| 1. BIOS/UEFI 启动  | BIOS/UEFI        | 厂商 Logo / 引导选择    | 否                  |
| 2. Bootloader 加载 | GRUB             | Grub 菜单 / 引导内核    | 否                  |
| 3. 内核加载          | Linux Kernel     | Kernel 启动日志       | 否（除非 quiet 参数）     |
| 4. 初始化阶段         | initramfs + init | **Plymouth 动画界面** | ✅ 是                |
| 5. 系统初始化         | systemd          | 登录界面前服务初始化        | ✅ 是（若未禁用 plymouth） |
| 6. 登录界面          | GDM/lightdm      | 图形界面登录            | 否                  |

Plymouth **作用于内核加载后、图形界面启动前**这一阶段，主要目的是隐藏启动日志，显示统一、美观的启动动画界面。

---

## 二、Plymouth 主题基础

### 1. Plymouh 的作用

- 在系统启动时，展示启动动画（splash screen）。

- 遮蔽启动日志，提升用户体验。

### 2. 主题结构

每个 Plymouth 主题位于：

```
/usr/share/plymouth/themes/<主题名>/
```

典型文件结构：

```
my-theme/
├── my-theme.plymouth        # 主题定义文件（必须）
├── my-theme.script          # 脚本逻辑（脚本主题才有）
├── background.png           # 背景图像
├── logo.png                 # logo 图像
└── *.so                     # 图形模块（如使用插件）
```

`.plymouth` 是主入口配置文件，定义如下内容：

```ini
[Plymouth Theme]
Name=My Theme
Description=A sample plymouth theme
ModuleName=script

[script]
ImageDir=/usr/share/plymouth/themes/my-theme
ScriptFile=/usr/share/plymouth/themes/my-theme/my-theme.script
```

---

## 三、系统启动参数与 Plymouth 的关系

### 1. GRUB 启动参数

Plymouth 是否启用、显示动画由以下 GRUB 启动参数控制：

```bash
quiet splash
```

- `quiet`：隐藏内核启动日志

- `splash`：启用 Plymouth

**配置位置**： `/etc/default/grub`：

```bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```

修改后更新 GRUB：

```bash
sudo update-grub
```

---

## 四、实战：安装并应用一个新主题

### 示例主题：`spinfinity`

1. **安装主题包**

```bash
sudo apt install plymouth-themes
```

2. **查看可用主题**

```bash
sudo plymouth-set-default-theme --list
```

3. **设置新主题**

```bash
sudo plymouth-set-default-theme spinfinity
sudo update-initramfs -u
```

说明：

- `plymouth-set-default-theme`：修改默认主题

- `update-initramfs -u`：重新生成 initramfs，把主题打包进去
4. **重启系统验证**

```bash
sudo reboot
```

---

## 五、自定义一个简单主题（脚本类）

### 1. 创建主题目录

```bash
sudo mkdir /usr/share/plymouth/themes/mytheme
```

### 2. 编写 `mytheme.plymouth`

```ini
[Plymouth Theme]
Name=My Theme
Description=Simple script-based theme
ModuleName=script

[script]
ImageDir=/usr/share/plymouth/themes/mytheme
ScriptFile=/usr/share/plymouth/themes/mytheme/mytheme.script
```

### 3. 编写脚本 `mytheme.script`

```javascript
// 简单绘制一个 logo 和加载动画
logo = Image("logo.png");
screen_width = Window.GetWidth();
screen_height = Window.GetHeight();
logo_x = (screen_width - logo.GetWidth()) / 2;
logo_y = (screen_height - logo.GetHeight()) / 2 - 50;

Window.SetBackgroundTopColor(0.1, 0.1, 0.1); // 背景色
Window.SetBackgroundBottomColor(0.1, 0.1, 0.1);

logo.Show(logo_x, logo_y);

throbber = Sprite();
throbber.SetPosition(screen_width/2, screen_height/2 + 40);
throbber.SetImage("spinner.png");
throbber.StartRotation(5); // 旋转动画
```

### 4. 设置主题并打包

```bash
sudo plymouth-set-default-theme mytheme
sudo update-initramfs -u
```

---

## 六、调试和测试

### 模拟 Plymouth 启动（无需重启）：

```bash
sudo plymouthd ; sudo plymouth --show-splash ; sleep 5 ; sudo plymouth --quit
```

---

## 七、主题类型说明（高级）

| 模块名       | 描述             |
| --------- | -------------- |
| `script`  | 最常见，基于脚本控制动画   |
| `details` | 显示文本日志（无动画）    |
| `text`    | 简单文本显示（低图形能力时） |
| `fade-in` | 渐显 Logo        |
| `spinner` | 默认旋转圆圈动画       |

---

## 八、总结：关键配置参数与影响关系表

| 配置项 / 参数                     | 位置                    | 影响            |
| ---------------------------- | --------------------- | ------------- |
| `quiet splash`               | GRUB 启动参数             | 是否启用 Plymouth |
| `.plymouth` 文件               | 主题定义目录                | 定义主题元信息       |
| `.script` 文件                 | `ModuleName=script` 时 | 控制动画逻辑        |
| `update-initramfs`           | 系统命令                  | 更新启动加载内容      |
| `plymouth-set-default-theme` | 系统命令                  | 修改默认主题        |

---

如果你想进一步制作**更复杂的动画效果、集成自定义字体、交互式元素**，可以继续深入研究 **Plymouth Scripting API**。





提供一个高级动画主题脚本示例，帮助更深入理解 `Plymouth Script` 的能力，还可以作为构建自定义启动界面的范例。

---

## ✅ 高级动画主题脚本示例

下面是一个基于 **多层图像 + 动态旋转 + 渐变背景 + 动画节奏控制** 的完整脚本，模拟“启动波动环”效果。

### 🔧 1. `mytheme.plymouth` 配置

```ini
[Plymouth Theme]
Name=Advanced Animated Theme
Description=A theme with logo, background, and animated ring
ModuleName=script

[script]
ImageDir=/usr/share/plymouth/themes/mytheme
ScriptFile=/usr/share/plymouth/themes/mytheme/mytheme.script
```

---

### 🎬 2. `mytheme.script` 逻辑解释 + 实现

```javascript
// 获取屏幕尺寸
screen_width = Window.GetWidth();
screen_height = Window.GetHeight();

// 设置背景颜色渐变（深蓝到黑）
Window.SetBackgroundTopColor(0.0, 0.1, 0.2);     // 顶部颜色
Window.SetBackgroundBottomColor(0.0, 0.0, 0.0);  // 底部颜色

// 加载 Logo 图像（静态）
logo = Image("logo.png");
logo_x = (screen_width - logo.GetWidth()) / 2;
logo_y = (screen_height - logo.GetHeight()) / 2 - 50;
logo.Show(logo_x, logo_y);

// 加载动画环图像（旋转）
ring = Image("ring.png");  // 透明背景，中心为旋转轴
ring_sprite = Sprite();
ring_sprite.SetImage(ring);
ring_sprite.SetPosition((screen_width - ring.GetWidth())/2,
                        (screen_height - ring.GetHeight())/2 + 40);

// 加载点状脉冲图像（循环渐显）
pulse = Image("pulse.png");
pulse_sprite = Sprite();
pulse_sprite.SetImage(pulse);
pulse_sprite.SetPosition((screen_width - pulse.GetWidth())/2,
                         (screen_height - pulse.GetHeight())/2 + 120);

// 设置动画帧率
plymouth.SetUpdateInterval(0.033);  // 每秒约30帧

// 动画循环控制变量
angle = 0;
alpha = 0.0;
fade_dir = 1;

// 注册动画函数
fun update_callback() {
    // 旋转动画
    angle += 4;
    if (angle >= 360) {
        angle = 0;
    }
    ring_sprite.SetRotation(angle);

    // 脉冲透明度循环（0.0 ↔ 1.0）
    alpha += fade_dir * 0.05;
    if (alpha >= 1.0) {
        alpha = 1.0;
        fade_dir = -1;
    } else if (alpha <= 0.0) {
        alpha = 0.0;
        fade_dir = 1;
    }
    pulse_sprite.SetOpacity(alpha);
}

// 绑定动画刷新
plymouth.SetUpdateFunction(update_callback);
```

---

### 🖼️ 图像建议与设计

| 图像文件名       | 说明                               |
| ----------- | -------------------------------- |
| `logo.png`  | 居中主 Logo，透明背景（例如企业或 Ubuntu logo） |
| `ring.png`  | 中空环形图像，中心旋转（512x512 透明）          |
| `pulse.png` | 发光点、阴影、发散效果图，用于模拟节奏感             |

确保图像分辨率为 **PNG 格式** 且带透明通道，可通过 [GIMP](https://www.gimp.org/) 或 Photoshop 编辑。

---

### 🚀 部署流程总结

1. 放置主题文件到目录：

```bash
sudo mkdir /usr/share/plymouth/themes/mytheme
sudo cp *.png mytheme.plymouth mytheme.script /usr/share/plymouth/themes/mytheme/
```

2. 设置主题：

```bash
sudo plymouth-set-default-theme mytheme
sudo update-initramfs -u
```

3. 重启测试或模拟：

```bash
sudo reboot
# 或快速测试：
sudo plymouthd ; sudo plymouth --show-splash ; sleep 5 ; sudo plymouth --quit
```

---
