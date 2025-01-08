# 1 Git 工作流

![](https://www.runoob.com/wp-content/uploads/2015/02/git-process.png)



# 2 Git 工作区、暂存区、本地仓库、远程仓库关系

![](https://www.runoob.com/wp-content/uploads/2015/02/1352126739_7909.jpg)



<img src="https://www.runoob.com/wp-content/uploads/2015/02/git-command.jpg" title="" alt="" width="655">



**说明：**

- workspace：工作区
- staging area：暂存区/缓存区
- local repository：版本库或本地仓库
- remote repository：远程仓库



# 3 Git基本操作

## 3.1 创建仓库

| 命令        | 说明                  |
| --------- | ------------------- |
| git init  | 初始化仓库               |
| git clone | 拷贝一份远程仓库，也就是下载一个项目。 |

## 3.2 修改与提交

| 命令             | 说明                   |
| -------------- | -------------------- |
| git add        | 添加文件到暂存区             |
| git status     | 查看仓库当前的状态，显示有变更的文件。  |
| git diff       | 比较文件的不同，即暂存区和工作区的差异。 |
| git difftool   | 使用外部差异工具查看和比较文件的更改。  |
| git range-diff | 比较两个提交范围之间的差异。       |
| git commit     | 提交暂存区到本地仓库。          |
| git reset      | 回退版本。                |
| git rm         | 将文件从暂存区和工作区中删除。      |
| git mv         | 移动或重命名工作区文件。         |
| git notes      | 添加注释。                |
| git checkout   | 分支切换。                |
| git switch     | 更清晰地切换分支。            |
| git restore    | 恢复或撤销文件的更改。          |
| git show       | 显示 Git 对象的详细信息。      |

## 3.3 提交日志

| 命令               | 说明                                  |
| ---------------- | ----------------------------------- |
| git log          | 查看历史提交记录                            |
| git blame <file> | 以列表形式查看指定文件的历史修改记录                  |
| git shortlog     | 生成简洁的提交日志摘要                         |
| git describe     | 生成一个可读的字符串，该字符串基于 Git 的标签系统来描述当前的提交 |

## 3.4 远程操作

| 命令            | 说明               |
| ------------- | ---------------- |
| git remote    | 远程仓库操作           |
| git fetch     | 从远程获取代码库         |
| git pull      | 下载远程代码并合并        |
| git push      | 上传远程代码并合并        |
| git submodule | 管理包含其他 Git 仓库的项目 |

# 4 Git文件状态

    Git 的文件状态分为三种：工作目录（Working Directory）、暂存区（Staging Area）、本地仓库（Local Repository）。

## 4.1 工作目录（Working Directory）

    工作目录是你在本地计算机上看到的项目文件。它是你实际操作文件的地方，包括查看、编辑、删除和创建文件。所有对文件的更改首先发生在工作目录中。

    在工作目录中的文件可能有以下几种状态：

- **未跟踪（Untracked）**：新创建的文件，未被 Git 记录。
- **已修改（Modified）**：已被 Git 跟踪的文件发生了更改，但这些更改还没有被提交到 Git 记录中。

## 4.2 暂存区（Staging Area）

    暂存区，也称为索引（Index），是一个临时存储区域，用于保存即将提交到本地仓库的更改。你可以选择性地将工作目录中的更改添加到暂存区中，这样你可以一次提交多个文件的更改，而不必提交所有文件的更改。

- 使用 `git add <filename>` 命令将文件从工作目录添加到暂存区。
- 使用 `git add .` 命令将当前目录下的所有更改添加到暂存区。

## 4.3 本地仓库（Local Repository）

    本地仓库是一个隐藏在 `.git` 目录中的数据库，用于存储项目的所有提交历史记录。每次你提交更改时，Git 会将暂存区中的内容保存到本地仓库中。

+ 使用 `git commit -m "commit message"` 命令将暂存区中的更改提交到本地仓库。

## 4.4 文件状态的转换流程

+ **未跟踪（Untracked）**：
  新创建的文件最初是未跟踪的。它们存在于工作目录中，但没有被 Git 跟踪。

+ **已跟踪（Tracked）**：
  通过 `git add` 命令将未跟踪的文件添加到暂存区后，文件变为已跟踪状态。

+ **已修改（Modified）**：
  对已跟踪的文件进行更改后，这些更改会显示为已修改状态，但这些更改还未添加到暂存区。

+ **已暂存（Staged）**：
  使用 `git add` 命令将修改过的文件添加到暂存区后，文件进入已暂存状态，等待提交。

+ **已提交（Committed）**：
  使用 `git commit` 命令将暂存区的更改提交到本地仓库后，这些更改被记录下来，文件状态返回为已跟踪状态。

# 5 远程仓库  (Github)



<img title="" src="https://www.runoob.com/wp-content/uploads/2015/03/Git-push-command.jpeg" alt="" width="635">

## 5.1 前期准备

+ **生成 SSH Key**
  
      由于你的本地 Git 仓库和 GitHub 仓库之间的传输是通过SSH加密的，所以我们需要配置验证信息，使用以下命令生成 SSH Key：
  
  ``` 
  ssh-keygen -t rsa -C "youremail@example.com"
  ```
  
      后面的 **your_email@youremail.com** 改为你在 Github 上注册的邮箱，之后会要求确认路径和输入密码，我们这使用默认的一路回车就行。
  
      成功的话会在 **~/** 下生成 **.ssh** 文件夹，进去，打开 **<mark>id_rsa.pub</mark>**，复制里面的 **key**。

+ **github配置** 
  
  进入 Account => Settings（账户配置），左边选择 **SSH and GPG keys**，然后点击 **New SSH key** 按钮，title 设置标题，可以随便填，粘贴在你电脑上生成的 key。

+ **github创建仓库**
  
  登录后点击" New repository "，创建新的仓库。

## 5.2 添加远程库 （本地标识）

```
git remote add [shortname] [url]
```

+ shortname ：对应远程仓库的本地标识名，例如，biji、origin

+ url ：git@github.com:wsunswimfish/biji.git

## 5.3 查看远程仓库（本地标识）

查看当前配置有哪些远程仓库，执行时加上 -v 参数，可以看到每个别名的实际链接地址。

```
$ git remote
origin
$ git remote -v
origin    git@github.com:wsunswimfish/biji.git (fetch)
origin    git@github.com:wsunswimfish/biji.git (push)
```

## 5.4 提交到Github

将本地仓库信息推送到远程仓库

```
git push -u biji master
```

## 5.5 提取远程仓库

+ 从远程仓库下载新分支与数据
  
  ```
  git fetch
  ```

+ 从远端仓库提取数据并尝试合并到当前分支
  
  ```
  git merge
  ```

## 5.6 删除远程仓库（本地标识）

```
git remote rm [别名]
```

# 6 连接问题

ssh 访问 gitHub 出错如下：

```
$ ssh -T git@github.com
The authenticity of host 'github.com (140.82.118.4)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? 
Host key verification failed.
```

解决办法：（将GitHub添加到信任主机列表后，可以成功访问）

```
$ ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

$ ssh -T git@github.com
Warning: Permanently added the RSA host key for IP address '140.82.118.4' to the list of known hosts.
Hi earthnorth! You've successfully authenticated, but GitHub does not provide shell access.
```




