# BigLearnReport

#### 1. 介绍
​		青年大学习（爬虫+数据处理+自动发送未完成名单到学院各个班群）

#### 2. 主要功能
- 对青年大学习的学习情况做收集与汇总，做到自动读取，自动处理，自动发布
- 爬虫 
    - 通过selenium获取cookie
    - 通过requests批量爬取数据
- 消息通知，配合mirai框架向各个班群发送QQ信息
- 服务器api
  - 可通过内置api查询程序信息与系统状态

#### 3. 基本模块

- Core
  - main.py - 程序执行的入口
- Config
  - config.ini - 填写基本配置信息
  - settings.py - 对config.ini中数据进行读取与初始化
- Logger
  - logger - 输出日志信息到控制台、日志文件与Server模块
- Message
  - message - 消息传递接口，可通过QQ机器人与邮箱发送信息
- Scheduler
  - scheduler - 定时执行模块，在config.ini 中开启并设置后，定时执行/Core/main.py中代码
- Server
  - handler - 包含主要的HTTP请求处理与api
  - server - 用于配置并启动服务器线程
- Static
  - web网页查看日志
  - Restful api提供项目信息接口

#### 4. 运行环境

- [Python 3](https://www.python.org/)

#### 5. 安装教程

1. ```shell
   git clone https://gitee.com/louisyoung1/tiny-server.git
   ```

2. ```sh
   cd tiny-server
   ```

#### 6. 使用说明

1. 修改/Core/main.py中代码，修改为你要运行的代码

2. 按注释要求编辑/Config/config.ini文件中配置项

3. 确保你此时在/tiny-server目录下，并运行

   ```sh
   python3 runserver
   ```

#### 7. 目录结构

```shell
.
├── Config
│   ├── config.ini
│   └── settings.py
├── Core
│   └── core.py
├── Logger
│   ├── Log_Files
│   │   └── TinyServer.log
│   └── logger.py
├── Message
│   └── message.py
├── Scheduler
│   ├── scheduler.py
│   └── tools.py
├── Server
│   ├── handler.py
│   └── server.py
├── Static
│   ├── 404.html
│   ├── change.html
│   ├── css
│   ├── favicon.ico
│   ├── images
│   ├── index.html
│   ├── js
│   └── log.html
└── runserver.py
```



#### 8. 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
