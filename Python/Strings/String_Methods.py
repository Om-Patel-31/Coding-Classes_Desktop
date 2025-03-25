print("Activity-1")
poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)
poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

print()
print("Activity-2")
line_one = "The sky has given over"
list_one_words = []
words = line_one.split()
list_one_words.append(words)
print(list_one_words)

print()
print("Activity-3")
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
author_names = authors.split(',')


author_last_names = []

for author in author_names:
   author_last_names.append(author.split()[-1])

print("Author names:",author_names)
print("Author Lastnames:",author_last_names)

print()
print("Activity-4")
spring_storm_text = \
"""The sky has given over
its bitterness.
Out of the dark change
all day long
rain falls and falls
as if it would never end.
Still the snow keeps
its hold on the ground.
But water, water
from a thousand runnels!
It collects swiftly,
dappled with black
cuts a way for itself
through green ice in the gutters.
Drop after drop it falls
from the withered grass-stems
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

print()
print("Activity-5")
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on",
"stones"]
reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

print()
print("Activity-6")
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = ' '.join(winter_trees_lines)
print(winter_trees_full)

print()
print("Activity-7")
love_maybe_lines = ['Always ', ' in the middle of our bloodiest battles ', 'you lay down your arms', ' like flowering mines ','\n',' to conquer me home. ']
love_maybe_lines_stripped = []
for line in love_maybe_lines:
   love_maybe_lines_stripped.append(line.strip())
   love_maybe_full  = '\n'.join(love_maybe_lines_stripped)
   print(love_maybe_full)

print()
print("Activity-8")
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary
career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a
mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina.
Jean Tomer is most well known for his first book Cane, which vividly portrays the life
of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
print(toomer_bio_fixed)

print()
print("Activity-9")
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)

print()
print("Activity-10")
def poem_title_card(poet, title):
   print('The poem "{}" is written by {}.'.format(title, poet))

poem_title_card("Walt Whitman", "I Hear America Singing")

print()
print("Activity-11")
def poem_description(publishing_date, author, title, original_work):
   poem_desc = "The poem {} by {} was originally published in {} in {}.".format(title, author, original_work, publishing_date)
   return poem_desc

my_beard_description = print(poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends"))

print()
print("Activity-12")
highlighted_poems = "Afterimages:Audre Lorde:1997, The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925, Georgia Dusk:Jean Toomer:1923, Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr.Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
# print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(',')

for highlighted_poem in highlighted_poems:
   highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)