from bs4 import BeautifulSoup

with open("D:/Grinding/scrappingPythonLearning/01/Home.html", "r") as f:
    content = f.read()

    soup = BeautifulSoup(content, "lxml")

    # print(soup.prettify())

    tags = soup.find("h5")

    all_tags = soup.find_all("h5")

    for tag in all_tags:
        text_Only = tag.text

    
    course_cards = soup.find_all("div", class_="card")

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        