from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"_3O0U0u"})
container = containers[0]

# price = container.findAll("div", {"class": "col col-5-12_2o7WAb"})
# print(price[0].text)

print(container.div.img["alt"])
ratings = container.findAll("div", {"class": "niH0FQ"})

print(ratings[0].text)

filename = "products.csv"
f = open(filename, "w")

headers = "Product_Name, Pricing, Rating\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("div", {"class":"col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "niH0FQ"})
    rating = rating_container[0].text

    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs." + rm_rupee[1]

    split_price = add_rs_price.split("E")
    final_price = split_price[0]

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    print(product_name.replace(",","|") + "," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",","|") + "," + final_price + "," + final_rating + "\n")

f.close()
