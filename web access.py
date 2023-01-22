import webbrowser
import time

browser = webbrowser.get(using='windows-default')

print("Hi! Welcome to the web access")
time.sleep(2)
print("Time for doing some shopping")
time.sleep(2)

while True:
    print("We have so many website like Amazon, Flipkart, SnapDeal, Ebay, BigBasket and BigBazaar")
    time.sleep(2)
    shopping = input("Type your website name here from the above list or type leave: ")
    case = shopping.lower()
    if case == "amazon":
        browser.open_new("https://www.amazon.in/")
    if case == "flipkart":
        browser.open_new("https://www.flipkart.com/")
    if case == "snapdeal":
        browser.open_new("https://www.snapdeal.com/")
    if case == "ebay":
        browser.open_new("https://www.ebay.com/")
    if case == "bigbasket":
        browser.open_new("https://www.bigbasket.com/")
    if case == "bigbazaar":
        browser.open_new("https://shop.bigbazaar.com/")
    if case == "leave":
        print("OK! Bye. Do come next time")
        break