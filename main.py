import requests
from recipe_part1 import recipes # huge file
from bs4 import BeautifulSoup

# currentCounter = 28424;
#
idCounter = 0
parse_recipe_file = open("updated_recipe.py", "w")
parse_recipe_file.write("updated_recipe= [\n")


# grab the data
for recipe in recipes:
    print("Checking " + str(recipe["id"]) + "/28424")

    def find_nth(haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start + len(needle))
            n -= 1
        return int(start)


    def parse_recipe_url():
        # print(recipe["recipe_url"])
        recipe_url = recipe["recipe_url"]
        # find the location of whatever we are looking for
        # print(find_nth(recipe["recipe_url"],"http://", 2))

        indexOfSecondHttp = find_nth(recipe["recipe_url"], "http://", 2)
        parsed_url = recipe_url[indexOfSecondHttp:]
        #print(parsed_url)
        return parsed_url

    def get_webiste_soup(website_url):
        website_page = requests.get(website_url)
        website_soup = BeautifulSoup(website_page.content, 'html.parser')
        return website_soup
    def parse_recipe_title(website_soup):
        searching_for_title = str(website_soup.find('title'))
        parsed_recipe_title = searching_for_title[7:(len(searching_for_title) - 8)]
        return parsed_recipe_title


    # def parse_recipe_description(website_soup):
    #     #print("inside parse r d")
    #     searching_for_description = website_soup.find_all('meta')
    #     # print(searching_for_description)
    #     found_potiental_description = " "
    #     # print(len(searching_for_title))
    #     for meta_description in searching_for_description:
    #         current_meta = str(meta_description)
    #         searching_string = "og:description"
    #         index = find_nth(current_meta, searching_string, 1)
    #         if len(current_meta) < 30000 and index != -1:
    #             # print("start{")
    #             # print("\t" + current_meta)
    #             # print(str(index) + "}end")
    #             found_potiental_description = current_meta
    #             break
    #     # print(found_potiental_description)
    #     i = find_nth(found_potiental_description, "\"", 1) + 1
    #     n = find_nth(found_potiental_description, "\"", 2)
    #     parsed_recipe_description = found_potiental_description[i:n]
    #
    #     if "\n" in parsed_recipe_description:
    #         parsed_recipe_description = parsed_recipe_description.replace('\n', ' ')
    #     return parsed_recipe_description


    parsed_recipe_url = parse_recipe_url()
    # List of iv we want to keep
    # parsed_recipe_title
    # parsed_recipe_description

    try:
        website_soup = get_webiste_soup(parsed_recipe_url)
    except:
        website_soup = " "
    # we need to check if soup is a certain lenght if its too short than we hit an error page and not process item
    #print(website_soup)
    if len(str(website_soup)) > 3000:
        #searching_for_title = str(website_soup.find('title'))
        # & bc thats how long title is to take out the attr at the index 0 and end
        parsed_recipe_title = parse_recipe_title(website_soup)

            #searching_for_title[7:(len(searching_for_title)-8)]
        #print("[title]:" + parsed_recipe_title)
        # print(searching_for_title)
        # print(len(searching_for_title))
        # Look for Title attrible to set as title

        # parsed_recipe_description = parse_recipe_description(website_soup)
        #print("[desc]:" + parsed_recipe_description)
        if len(parsed_recipe_title) > 5:
            # lets print this shit!
            parse_recipe_file.write("\t{\n")
            parse_recipe_file.write("\t\t\"id\" : ")
            parse_recipe_file.write("\"" + str(idCounter) + "\"")
            parse_recipe_file.write(",\n")
            idCounter = idCounter + 1

            parse_recipe_file.write("\t\t\"recipe_url\" : ")
            parse_recipe_file.write("\"" + parsed_recipe_url + "\"")
            parse_recipe_file.write(",\n")

            parse_recipe_file.write("\t\t\"title\" : ")
            parse_recipe_file.write("\"" + parsed_recipe_title + "\"")
            parse_recipe_file.write(",\n")

            # parse_recipe_file.write("\t\t\"description\" : ")
            # parse_recipe_file.write("\"" + parsed_recipe_description + "\"")
            # parse_recipe_file.write(",\n")

            parse_recipe_file.write("\t\t\"tags\" : ")
            parse_recipe_file.write("\"" + recipe["tags"] + "\"")
            parse_recipe_file.write("\n")
            parse_recipe_file.write("\t},\n")

parse_recipe_file.write("]")




        # if index >= 0:
        #     print("start{")
        #     print("\t" + current_meta)
        #     print("}end")
        #     found_potiental_description = current_meta
        #     break;

    # while is_not_description_found:
    #     for meta_description in searching_for_description:
    #         #print(meta_description)
    #         searching_string = "og:description"
    #         index = find_nth(str(meta_description), searching_string, 1)
    #
    #         if index >= 0:
    #             print("found index {")
    #             print(str(meta_description))
    #             print("} end")
    #             is_not_description_found = False;
    #             found_potiental_description = str(meta_description)
    #             print(type(found_potiental_description))
    #             print(len(found_potiental_description))
    #             break;
    #     #     end of if search_string
    #     # end for loop for meta_description
    # # end of while loop
    # print("outside loop")
    #print(found_potiental_description)
    #print(len(found_potiental_description))
    #<meta content="This roasted vegetable salad using the best of Autumn's produce is simple but very effective. First golden beetroots are sweet roasted along with their nutritious leaves and green beans. This is then paired with a smoked paprika rolled feta cheese that lends a fantastic depth of flavour to this simple salad." property="og:description"/>

    #i = find_nth(found_potiental_description, "\"", 1)
    #n = find_nth(found_potiental_description, "\"", 2)
    #print(type(i))

    #searching_for_title[7:(len(searching_for_title) - 8)]
    #found_potiental_description[1, 5]
    #print(parsed_recipe_description)














    # title
    # author ?
# check to see if the link is valid
# if valid then add to the list





# # print(website_soup.prettify())
# website_recipe_file = open("recipes-part2.json", "w")
# website_recipe_file.write("[\n")
# #12830
# for x in range(837, 838):
#
#     website_url = 'https://web.archive.org/web/20200218191910/http://www.tastespotting.com/browse/' + str(x)
#     website_page = requests.get(website_url)
#     website_soup = BeautifulSoup(website_page.content, 'html.parser')
#
#
#
#     # used so we can figure out when the end of the list is
#     recipe_test = website_soup.find_all('div', 'trendspotted-item')
#     recipe_card_count = len(recipe_test)
#
#
#
#     for recipe_card in website_soup.find_all('div', 'trendspotted-item'):
#         # recipe_card_count = recipe_card_count - 1
#         website_recipe_file.write("\t{\n")
#
#         # adding a title for ease
#         website_recipe_file.write("\t\t\"id\" : ")
#         website_recipe_file.write("\"" + str(currentCounter) + "\"")
#         currentCounter = currentCounter + 1;
#         website_recipe_file.write(",\n")
#
#         recipe_text = str(recipe_card.find('h3'))
#         print("recipe #" + str(currentCounter))
#         print(recipe_text)
#
#
#         # locating where the first link is at for
#         # the recipe URL
#         i = 34
#         try:
#             target_index = recipe_text.index("target")
#         except:
#             target_index = recipe_text.index("<img")
#         n = target_index - 2
#         recipe_url = recipe_text[i:n]
#         try:
#             target_index = recipe_url.index("&amp")
#         except:
#             target_index = len(recipe_url) - 1
#         recipe_url = recipe_url[:target_index]
#         website_recipe_file.write("\t\t\"recipe_url\" : ")
#         website_recipe_file.write("\"" + recipe_url + "\"")
#         website_recipe_file.write(",\n")
#         #print(recipe_url)
#
#
#         # locating search words
#         end_of_tags_words = recipe_text.index(" height")
#         start_of_tags_Words = recipe_text.index("alt=")
#         i = start_of_tags_Words + 5
#         n = end_of_tags_words - 1
#         snippet = recipe_text[i:]
#         quote_index = snippet.index("\"")
#         tag_words = snippet[:quote_index]
#         website_recipe_file.write("\t\t\"tags\" : ")
#         website_recipe_file.write("\"" + tag_words + "\"")
#         website_recipe_file.write("\n")
#
#         # locating image location
#         # start_of_image = recipe_text.index("src")
#         # end_of_image = recipe_text.index("width")
#         # i = start_of_image + 5
#         # n = end_of_image - 2
#         # snippet = recipe_text[i:]
#         # quote_index = snippet.index("\"")
#         # image_url = snippet[:quote_index]
#         # website_recipe_file.write("\t\t\"image_url\" : ")
#         # website_recipe_file.write("\"" + image_url + "\"")
#         # website_recipe_file.write("\n")
#         # if(recipe_card_count == 0) :
#         #     website_recipe_file.write("\t}\n")
#         # else :
#         website_recipe_file.write("\t},\n")
#
# website_recipe_file.write("]")