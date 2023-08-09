import logging
from logging.handlers import TimedRotatingFileHandler
from config import Config

format_dict = {
    1:
    logging.Formatter(
        '%(asctime)s-%(name)s-%(levelname)s:%(message)s-[%(filename)s-->%(funcName)s-->line:%(lineno)d]'
    ),
    2:
    logging.Formatter(
        '%(asctime)s-%(levelname)s:%(message)s-[%(filename)s-->%(funcName)s-->line:%(lineno)d]'
    ),
    3:
    logging.Formatter(
        '%(asctime)s-%(levelname)s:%(message)s-[%(filename)s-->%(funcName)s-->line:%(lineno)d]'
    ),
    4:
    logging.Formatter(
        '%(asctime)s-%(levelname)s:%(message)s-[%(filename)s-->%(funcName)s-->line:%(lineno)d]'
    ),
    5:
    logging.Formatter(
        '%(asctime)s-%(levelname)s:%(message)s-[%(filename)s-->%(funcName)s-->line:%(lineno)d]'
    )
}


# 指定保存日志的文件路径，日志级别，以及调用文件将日志存入到指定的文件中
class Logger():

    def __init__(self, logger, loglevel=1):
        logFileName = Config.logFileName
        logFileDir = Config.logFileDir
        logFilePath = logFileDir + logFileName
        
        self.logger = logging.getLogger(logger)  # 创建一个logger，参数为空则返回rootlogger
        self.logger.setLevel(Config.LoggerLogLever)  #甚至logger日志等级
        
        # 创建一个handler，用于写入日志文件
        filehandler = TimedRotatingFileHandler(filename=logFilePath,
                                                when='D',
                                                interval=1,
                                                backupCount=10,
                                                encoding='utf-8')
        filehandler.setLevel(Config.FileLogLever)

        # 再创建一个handler，用于输出到控制台
        streamhandler = logging.StreamHandler()
        streamhandler.setLevel(Config.ConsoleLogLever)

        # 定义handler的输出格式
        formatter = format_dict[int(loglevel)]
        filehandler.setFormatter(formatter)
        streamhandler.setFormatter(formatter)

         # 给logger添加handler
        self.logger.addHandler(filehandler)
        self.logger.addHandler(streamhandler)

    def getlog(self):
        return self.logger


# if __name__ == '__main__':
#   # 调用方式
#   logger = Logger(logger='sparrow',loglevel=1).getlog()  # 每个不同功能（函数）调用的时候，logger的名字不能重复
#   logger.info('hello, China!')
#   logger.info('hello, China!')
#   logger.info('hello, China!')