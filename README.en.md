# BigLearnReport

#### 1. Description
​		Youth Learning (spider + data processing + automatic sending of the unfinished list to each class group of the college)

#### 2. Key Feature
- Collect and summarize the learning situation of young people in large learning, so as to automatically read, process and publish
- the spider
    - Get the cookie through Selenium
    - Crawl data from batch requests
- Message notification, send QQ messages to each group in cooperation with Mirai framework
- Server API
    - Program information and system status can be queried through the built-in API

#### 3. Basic Modules

- Core
- main. py - Entry to program execution
- Config
  - config.ini - Fill in the basic configuration information
  - settings.py - Read and initialize data in config.ini
- Logger
- logger - Outputs log messages to the console, log file, and Server module
- Message
- message - Message passing interface, can send messages through QQ robot and mailbox
- Scheduler
  - Scheduler - Scheduled execution of the /Core/main.py module. Once opened and set in config.ini, the /Core/main.py module is scheduled to be executed
- Server
- Handler - Contains the main HTTP request handling and API
- server - Used to configure and start the server thread
- Static
- Web page view log
- RESTful APIs provide an interface to project information

#### 4. Operation Environment

- [Python 3](https://www.python.org/)

#### 5. Installation Tutorial

1. ```shell
   git clone https://gitee.com/louisyoung1/tiny-server.git
   ```

2. ```sh
   cd tiny-server
   ```


#### 6. Usage

1. Change the code in /Core/main.py to the code you want to run

2. Edit the configuration items in /Config/config.ini file according to the comment requirements

3. Create the Log_Files/ directory in the Logger/ directory and the file name you specified in your configuration
   ```sh
   mkdir Logger/Log_Files
   touch Logger/Log_Files/TinyServer.log
   ```

4. Make sure you are in /tiny-server and enter

   ```sh
   python3 runserver
   ```

#### 7. Directory Structure

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

#### 8. Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request
