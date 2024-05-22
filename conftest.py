from pytest import fixture
from selenium import webdriver as selwebdriver
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.safari.options import Options as safariOptions
from selenium.webdriver.safari.service import Service as safariService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import configparser

def pytest_addoption(parser):
    parser.addoption(
        '--seleniumhub', action='store', default=None, help='the cmd option to define the ip address of selenium hub to connect to'
    )
    # parser.addoption(
    #     '--html', action='store', default='reports/latest-automation-report-Edge.html', help='the cmd option to generate the html report'
    # )

# @fixture(scope='session', autouse=True)
# def browser(request):

#     browserType = str.lower(request.config.getoption('--browser'))

#     if browserType == 'edge':
#         options = edgeOptions()
#         options.add_argument('--headless')
#         options.add_argument('--guest')
#         # print(request.config.getoption('--html'))
#         driver = selwebdriver.Edge(service=edgeService(EdgeChromiumDriverManager().install()), options=options)
#     elif browser == 'safari':
#         driver = selwebdriver.Safari(service=safariService())
#     else:
#         driver = selwebdriver.Edge(service=edgeService(EdgeChromiumDriverManager().install()))

#     driver.maximize_window()
#     driver.implicitly_wait(30)

#     yield driver

#     driver.quit()

# @fixture(scope='session')
# def testConfigReader():
#     config = configparser.ConfigParser()
#     config.read('config/ini_config.ini')

#     yield config

# def pytest_generate_tests(metafunc):
            
#     temp_xlsName = str.split(metafunc.function.__qualname__, '.')[0]
#     xlsName = str.split(temp_xlsName, '_')[1] + '.xlsx'
#     sheetName = str.split(metafunc.function.__name__, '_')[1]
#     xlsFullFilePath = 'testdata' + '/' + str.split(metafunc.module.__name__, '_')[1] + '/' + xlsName

#     if os.path.exists(xlsFullFilePath):
        
#         workbook = load_workbook(xlsFullFilePath, read_only=True)

#         if sheetName in workbook.sheetnames:

#             workbook.close()
#             df = pd.read_excel(xlsFullFilePath, sheet_name=sheetName, header=0)
#             # df = pd.read_excel('testdata/pandas/SampleWithPandas.xlsx', sheet_name='pandasdemo1', header=0)
#             dl = df.to_dict(orient='records')

#             metafunc.parametrize('testdata', dl, scope="class")
