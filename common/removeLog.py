import os
import time
import datetime
from common.handleLog import Logger
import traceback
from config import Config

'''
处理日志文件
 删除超过设定的保留天数的文件
'''

removeLoglogger = Logger(loglevel=1, logger='removeOutDateLog').getlog()


# 计算到今天的天数差值
def getDaysToNow(dateStr):
    current_ime = time.localtime(time.time())
    compare_time = time.strptime(dateStr, "%Y-%m-%d")
    last_time = datetime.datetime(compare_time[0], compare_time[1],
                                  compare_time[2])
    now_time = datetime.datetime(current_ime[0], current_ime[1],
                                 current_ime[2])
    diff_day = (now_time - last_time).days
    return diff_day


# 删除超过设定期限的日志文件
def removeOutDateLogs():
    filePath = Config.logFileDir
    holdDays = Config.logFilesHoldDays
    allLogFiles = os.listdir(filePath)
    try:
        for logFile in allLogFiles:
            logFilePath = filePath + logFile

            time_local = time.localtime(os.path.getctime(logFilePath))
            time_Ymd = time.strftime("%Y-%m-%d", time_local)
            logFileExists = getDaysToNow(time_Ymd) + 1

            if isinstance(holdDays, int) and holdDays > 0:
                if os.path.exists(filePath):
                    if logFileExists > holdDays:
                        os.remove(logFilePath)
                        removeLoglogger.info('日志文件【%s】创建已超过【%d】天，已被删除' %
                                             (logFile, holdDays))
                    else:
                        removeLoglogger.info('日志文件【%s】创建不足【%d】天，不需要删除' %
                                             (logFile, holdDays))
                else:
                    removeLoglogger.info('日志文件【%s】不存在，删除失败！' % (logFile))
            else:
                removeLoglogger.info('日志文件保留天数【%s】设置异常，请检查！' % (str(holdDays)))
    except Exception:
        removeLoglogger.error(traceback.format_exc())


# if __name__ == '__main__':
#     removeOutDateLogs()
