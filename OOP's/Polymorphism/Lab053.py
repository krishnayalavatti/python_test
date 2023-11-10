class Browser:
    def __init__(self, browser):
        self.browser = browser

    def openBrowser(self, browser='chrome'):
        print("write the code to open the browser " + browser)


b = Browser("Chrome")
b.openBrowser()
