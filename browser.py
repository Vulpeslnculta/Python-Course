import webbrowser

# webbrowser.open_new('https://www.python.org/')


# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep="; ", end=" ")
chrome = webbrowser.get(using='chrome')
chrome.open('https://www.python.org/')
