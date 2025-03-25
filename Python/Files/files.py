import csv
import json

print("Activity-1")
with open('welcome.txt') as text_file:
    text_data = text_file.read()
print(text_data)
print()

print("Activity-2")
with open('how_many_lines.txt') as lines_doc:
        for lines in lines_doc:
              print(lines)
print()

print("Activity-3")
with open('just_the_first.txt') as first_line_doc:
      first_line = first_line_doc.readline()
      print(first_line)
print()

print("Activity-4")
with open('bad_bands.txt', 'w') as bad_band_docs:
    bad_band_docs.write("BTS")
print()

print("Activity-5")
with open('cool_dogs.txt', 'a') as cool_dogs_file:
      cool_dogs_file.write("Air Buddy\n")
print()

print("Activity-6")
with open('fun_file.txt') as close_this_file:
    setup = close_this_file.readline()
    punchline = close_this_file.readline()
    print(setup)
print() 

print("Activity-7")
with open('logger.csv') as log_csv_file:
     log_csv_data = log_csv_file.read()
     print(log_csv_data)
print()

print("Activity-8")
with open('cool_csv.csv') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        # print(row)
        if "Cool Fact" in row:
            print(row['Cool Fact'])
print()

print("Activity-9")
with open("books.csv") as books_csv:
     books_reader = csv.DictReader(books_csv, delimiter="@")
     isbn_list=[]
     for row in books_reader:
          isbn_list.append(row['ISBN'])
     print(isbn_list)
print()

print("Activity-10")
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time':
'13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021,
'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address':
'172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time':
'23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit':
1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address':
'104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time':
'18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

with open('logger.csv', mode='w') as logger_csv:
     log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
     log_writer.writeheader()
     for log_entry in access_log:
          log_writer.writerow(log_entry)
print()

print("Activity-11")
with open('message.json') as message_json:
     message = json.load(message_json)
     print(message['text'])
print()

print("Activity-12")
data_payload = [
{'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
'follow up': 'But enough talk!'}
]

with open('data.json', 'w') as data_json:
     json.dump(data_payload, data_json)