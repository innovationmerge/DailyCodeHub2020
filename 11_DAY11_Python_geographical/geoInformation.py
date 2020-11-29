# iNNovationMerge

#  Python program to extract geographical information from Raw text

# pip install geograpy3==0.1.2

import geograpy
text = "Bangalore(Bengaluru), is the capital of the Indian state of Karnataka. It has a population of about 10 million and a metropolitan population of about 8.52 million, making it the third most popular city and fifth most populous urban agglomeration in India."


def getGeoGraphy(text):
    places = geograpy.get_place_context(text=text)
    return places.countries,places.regions,places.cities
print(getGeoGraphy(text))

# (['Bengaluru', 'Bangalore', 'British Indian Ocean Territory', 'Karnataka', 'India'], ['Indian', 'Bengaluru', 'Bangalore', 'Karnataka', 'India'], ['Bangalore'])