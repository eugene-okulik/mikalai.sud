###

создание папки с данными о тестировании для allure
pytest -v --alluredir=allure-result

###

отчет allure
allure serve allure-result/

###

сгенерить отчет, сам создат папку и все туда засунет
allure generate
###

запустить локально отчет(в браузере) из папки allure-report(создастся при выполнении allure generate)
allure serve

###






###

отчет allure
allure serve allure-results/

###

создание папки с репортами
allure generate -c allure-results/ -o allure-reports

##
