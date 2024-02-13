"""
This program reads from movie.xml file and uses elementTree
to read the data from the xml file. 
Referred: https://docs.python.org/2/library/xml.etree.elementtree.html
https://blog.finxter.com/parsing-xml-files-in-python-a-simple-guide/
https://www.programiz.com/python-programming/set
"""

import xml.etree.ElementTree as ET


# Read in movie.xml and get the root node
tree = ET.parse("movie.xml")
root = tree.getroot()

favorite_count = 0  # Initialise favorite_count to 0
non_favorite_count = 0  # Initialise non_favourite_count to 0
unique_child_tag_set = set() # Create a set object to store unique child tags

# Iterate through movie elements
for movie in root.iter("movie"):

    # Get all child tags for element movie and add it to set to hold
    # only unique tags and avoid repetitions    
    for child in movie:
        unique_child_tag_set.add(child.tag)

    # Get all the description element of movie and display the
    # list of all descriptions
    descriptions = list(movie.find("description").itertext())
    print(f"Movie Descriptions: {descriptions}")

    # Get the favorite element and if True increase favorite_count
    # else increase non_favorite_count and display them both
    favorite = movie.get("favorite")
    if favorite.lower() == "true":
        favorite_count += 1
    else:
        non_favorite_count += 1

print("\nChild tags of element movie: ")
for tag in unique_child_tag_set:
    print(tag)

print(f"\nNumber of Favorite movies: {favorite_count}")
print(f"\nNumber of Non Favorite movies: {non_favorite_count}")
