# -*- coding: utf-8 -*-

from knitter import executer
from demoprj import conf, testcase

#http://chromedriver.storage.googleapis.com/index.html
executer.run(conf.ChromeDemo, testcase.testcase1)