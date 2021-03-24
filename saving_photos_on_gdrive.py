from typing import io
import os
import io
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from PIL import Image

import requests
from recipes_small import recipes_small # huge file
from bs4 import BeautifulSoup
import urllib.request
from PIL.ExifTags import TAGS
from urllib.request import Request, urlopen

def get_webiste_soup(website_url):
    website_page = requests.get(website_url)
    website_soup = BeautifulSoup(website_page.content, 'html.parser')
    return website_soup

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return int(start)
# # Below code does the authentication
# # part of the code
# gauth = GoogleAuth()
#
# # Creates local webserver and auto
# # handles authentication.
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)

# replace the value of this variable
# with the absolute path of the directory
path = "/Users/Melody/PycharmProjects/random/recipe_photos"

recipe_photo_gFolder_ID = '1QlhjF80adCI8OUibS84VkH9Fxdlu9Ovn'
# currentUrl = 'http://thecookiewriter.com/oreos-cookies-and-cream-ice-cream/'
# #website_soup = get_webiste_soup('http://www.notquitenigella.com/2016/05/22/roasted-vegetable-salad/')
# #website_soup = get_webiste_soup('https://www.thatskinnychickcanbake.com/turtle-poke-cake/')
# website_soup = get_webiste_soup(currentUrl)
# website_soup_head = website_soup.find('head')

def count_tags_in_soup(website_soup_head):
    count = 0
    for tag in website_soup_head:
        count = count + 1
    return count

def getImageURL(webpageUrl):
    currentUrl = webpageUrl
    website_soup = get_webiste_soup(currentUrl)
    website_soup_head = website_soup.find('head')
    count_tags = count_tags_in_soup(website_soup_head)
    # print("[count tags] " + str(count_tags))
    # count_num_of_tag_element = 0;
    for tag in website_soup_head:
        tag_type = str(type(tag))
        tag_index = find_nth(tag_type, "bs4.element.Tag", 1)
        # print(tag_index)

        # Checks to see if the tag is in the code
        if tag_index >= 0:
            # print(str(count_num_of_tag_element) + " : ")
            # count_num_of_tag_element = count_num_of_tag_element + 1
            # print(type(tag))
            # print(tag)
            meta_soup = tag.find_all('meta')
            meta_index = find_nth(str(meta_soup), "meta", 1)
            # print("meta index: " + str(meta_index))

            if count_tags > 25:
                # print(type(tag))
                # print(tag.attrs)
                image_content_index = find_nth(str(tag.attrs), "og:image", 1)
                # twitter_content_index = find_nth(str(meta_content.attrs), "twitter:image", 1)
                # image_content_index = find_nth(str(meta_content.attrs), "og:image")
                if image_content_index >= 0 and (len(tag.attrs['content']) > 7):
                    # print(tag.attrs['content'])
                    image_not_found = 0
                    return tag.attrs['content']

                # Checks to see which tag has the meta tag
                # for meta_tag in meta_soup:
            else:
                if meta_index >= 0:
                    # print(str(count_num_of_tag_element-1) + " : ")
                    # print(tag)
                    # print("meta soup lenth : " + str(len(meta_soup)))
                    # print("[metasoup]" + str(meta_soup))
                    image_not_found = 1
                    for meta_tag in meta_soup:
                        # print("[meta tag]" + str(meta_tag))
                        # print(type(meta_tag))
                        # print(meta_tag)
                        # if meta_index >= 0:
                        # Checks to see if the meta has content
                        if bool(image_not_found):
                            if len(meta_tag) > 1:
                                meta_tag_content = meta_tag.find_all('meta')
                                meta_tag_content_index = find_nth(str(meta_tag_content), "meta", 1)

                                if meta_tag_content_index >= 0:
                                    # print(len(meta_tag_content))

                                    for meta_content in meta_tag_content:
                                        # print(type(meta_content))

                                        tag_index = find_nth(str(type(meta_content)), "bs4.element.Tag", 1)
                                        if tag_index >= 0:
                                            # for content in meta_content:
                                            # print(type(meta_content))
                                            # print(meta_content)

                                            image_content_index = find_nth(str(meta_content.attrs), "og:image", 1)
                                            # twitter_content_index = find_nth(str(meta_content.attrs), "twitter:image", 1)
                                            # image_content_index = find_nth(str(meta_content.attrs), "og:image")
                                            if image_content_index >= 0 and (len(meta_content.attrs['content']) > 7):
                                                # print("meta attrs: " + meta_content.attrs['content'])
                                                image_url = meta_content.attrs['content']

                                                image_not_found = 0
                                                return image_url

def makeSmallerImage(imageUrl, image_title):
    # response = requests.get(imageUrl)
    # image_bytes = io.BytesIO(response.content)
    try :
        source = Image.open(urllib.request.urlopen(imageUrl))
        # source = Image.open(imageUrl + "/test_photo.png")
    except:
        req = Request(imageUrl, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        source = Image.open(io.BytesIO(webpage))


    source.thumbnail(size=(300, 300))
    source.save('recipe_photos/'+ image_title +'.png')


    # w, h = (source.width // 2 + 1), (source.height // 2)
    #
    # # This will show our canvas. The top one allows
    # # us to get what we want with no canvas
    # # w,h = source.width, source.height
    #
    # target = Image.new('RGB', (w, h), 'rosybrown')
    #
    # target_x = 0
    # for source_x in range(0, source.width, 2):
    #     target_y = 0
    #     for source_y in range(0, source.height, 2):
    #         pixel = source.getpixel((source_x, source_y))
    #         target.putpixel((target_x, target_y), pixel)
    #         target_y += 1
    #     target_x += 1
    #
    # target.save('recipe_photos/'+ image_title +'.png')
    # makeSmallerImageFromSmallerImage(imageUrl)


# def makeSmallerImageFromSmallerImage(imageUrl):
#     # source = Image.open(requests.get(imageUrl, stream=True).raw)
#     source = Image.open(imageUrl + "/test_photo-smaller.png")
#
#     w, h = (source.width // 2 + 1), (source.height // 2)
#
#     # This will show our canvas. The top one allows
#     # us to get what we want with no canvas
#     # w,h = source.width, source.height
#
#     target = Image.new('RGB', (w, h), 'rosybrown')
#
#     target_x = 0
#     for source_x in range(0, source.width, 2):
#         target_y = 0
#         for source_y in range(0, source.height, 2):
#             pixel = source.getpixel((source_x, source_y))
#             target.putpixel((target_x, target_y), pixel)
#             target_y += 1
#         target_x += 1
#
#     target.save(imageUrl + '/test_photo-smaller.png')

# count_tags = count_tags_in_soup(website_soup_head)

for recipe in recipes_small:
    image_title = recipe['id']
    current_url = recipe['recipe_url']
    # print(current_url)
    print(getImageURL(current_url))
    imageUrl = getImageURL(current_url)
    makeSmallerImage(imageUrl, image_title)


# makeSmallerImage(path, 'title')
# makeSmallerImage('https://images.notquitenigella.com/images/autumn-roasted-salad/ll.jpg', 'title')
# req = Request('https://tikkido.com/sites/default/files/onigiri-emoji-HERO.jpg', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# # source = Image.open(urllib.request.urlopen('https://tikkido.com/sites/default/files/onigiri-emoji-HERO.jpg'))
# print(type(webpage))
# image = Image.open(io.BytesIO(webpage))
# print(type(image))
# source = Image.open(webpage, 'rb')
# source.thumbnail(size=(300,300))
# source.save('3.png')
# response = requests.get(imageUrl)
# image_bytes = io.BytesIO(response.content)
#
#
# img = PIL.Image.open(image_bytes)
#
# img.show()
# makeSmallerImageFromSmallerImage(path)
# count_num_of_tag_element = 0;
# for tag in website_soup_head:
#     tag_type = str(type(tag))
#     tag_index = find_nth(tag_type, "bs4.element.Tag", 1)
#     # print(tag_index)
#
#     # Checks to see if the tag is in the code
#     if tag_index >= 0:
#         # print(str(count_num_of_tag_element) + " : ")
#         # count_num_of_tag_element = count_num_of_tag_element + 1
#         # print(type(tag))
#         # print(tag)
#         meta_soup = tag.find_all('meta')
#         meta_index = find_nth(str(meta_soup), "meta", 1)
#         # print("meta index: " + str(meta_index))
#
#         if count_tags > 14:
#             # print(type(tag))
#             # print(tag.attrs)
#             image_content_index = find_nth(str(tag.attrs), "og:image", 1)
#             # twitter_content_index = find_nth(str(meta_content.attrs), "twitter:image", 1)
#             # image_content_index = find_nth(str(meta_content.attrs), "og:image")
#             if image_content_index >= 0 and (len(tag.attrs['content']) > 7):
#                 print(tag.attrs['content'])
#
#                 image_not_found = 0
#             # Checks to see which tag has the meta tag
#             # for meta_tag in meta_soup:
#         else:
#             if meta_index >= 0:
#                 # print(str(count_num_of_tag_element-1) + " : ")
#                 # print(tag)
#                 # print("meta soup lenth : " + str(len(meta_soup)))
#                 # print("[metasoup]" + str(meta_soup))
#                 image_not_found = 1
#                 for meta_tag in meta_soup:
#                     # print("[meta tag]" + str(meta_tag))
#                     # print(type(meta_tag))
#                     # print(meta_tag)
#                 # if meta_index >= 0:
#                     # Checks to see if the meta has content
#                     if bool(image_not_found):
#                         if len(meta_tag) > 1:
#                             meta_tag_content = meta_tag.find_all('meta')
#                             meta_tag_content_index = find_nth(str(meta_tag_content), "meta", 1)
#
#                             if meta_tag_content_index >= 0:
#                                 # print(len(meta_tag_content))
#
#                                 for meta_content in meta_tag_content:
#                                     # print(type(meta_content))
#
#                                     tag_index = find_nth(str(type(meta_content)), "bs4.element.Tag", 1)
#                                     if tag_index >= 0:
#                                         # for content in meta_content:
#                                         # print(type(meta_content))
#                                         # print(meta_content)
#
#
#                                         image_content_index = find_nth(str(meta_content.attrs), "og:image", 1)
#                                         # twitter_content_index = find_nth(str(meta_content.attrs), "twitter:image", 1)
#                                         #image_content_index = find_nth(str(meta_content.attrs), "og:image")
#                                         if image_content_index >=0 and (len(meta_content.attrs['content']) > 7):
#                                             print(meta_content.attrs['content'])
#
#                                             image_not_found = 0

                                        # print(content_index)
                                    # if content_index >= 0:
                                    #     print(content.attrs)

                    # print("[" + str(meta_tag) + "]" + str(len(meta_tag)))
        # if image_index >= 0:
        #     print("tweet img found: " + str(image_index))
        #     print(tag.attrs)
        #     print(tag)
        # print("I'm a tag")




# sys.exit()
# iterating thought all the files/folder
# of the desired directory
# for x in os.listdir(path):
#
#
#     # upload photo to gdrive specified folder
#     f = drive.CreateFile({'title': x, 'parents': [{'id': recipe_photo_gFolder_ID}]})
#     f.SetContentFile(os.path.join(path, x))
#     f.Upload()

    # Due to a known bug in pydrive if we
    # don't empty the variable used to
    # upload the files to Google Drive the
    # file stays open in memory and causes a
    # memory leak, therefore preventing its
    # deletion
#     f = None