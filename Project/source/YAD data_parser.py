import operator
from operator import itemgetter

def match(str):
	if str.find("Chinese") >= 0 :
		return "Chinese"
	elif str.find("Italian") >= 0 :
		return "Italian"
	elif str.find("Korean") >= 0 :
		return "Korean"
	elif str.find("American") >= 0 or str.find("Burgers") >= 0 :
		return "American"
	elif str.find("Japanese") >= 0 :
		return "Japanese"
	elif str.find("Indian") >= 0 :
		return "Indian"
	else :
		return "other"

data = []

if __name__ == "__main__":
	with open('business.json') as f:
		index = 0
		for lines in f:
			index += 1
			#if index == 40:
				#print lines.strip().split("\":")
			business_id = lines.strip().split("\":")[1].strip().split("\"")[1]
			school = lines.strip().split("\":")[3].strip().split("\"")[1]
			category = lines.strip().split("\":")[5].strip().split("[\"")[1].strip().split("\"]")[0]
			photo_url = lines.strip().split("\":")[6].strip().split("\"")[1]
			review_count = lines.strip().split("\":")[8].strip().split(" ")[0].strip().split(",")[0]
			name = lines.strip().split("\":")[9].strip().split("\"")[1]
			url =  lines.strip().split("\":")[11].strip().split("\"")[1]
			stars =  lines.strip().split("\":")[14].strip().split(" ")[0].strip().split(",")[0]

			if match(category) != "other":
				data.append((school,match(category),business_id,photo_url,review_count,name,url,stars))
			#print match(category)
			#print business_id
			#print school
			#print category
			#print photo_url
			#print review_count
			#print name
			#print url
			#print stars

				#print lines.strip().split("\":")[5].strip().split("[\"")[1].strip().split("\"]")[0]
		data.sort(key=itemgetter(0,1))

		print len(data)

	file = open("yelp-business-treemap.json", "w")

	file.write("{\n")
	file.write("\"name\": \"YAD Business\",\n")
	file.write("\"children\": [\n")

	index = 0

	for lines in data:

		if index == 0:
	# School
			file.write("{\n")
			file.write("\"name\": "+"\""+data[0][0]+"\""+",\n")
			file.write("\"children\": [\n")
	# Style
			file.write("{\n")
			file.write("\"name\": "+"\""+data[0][1]+"\""+",\n")
			file.write("\"children\": [\n")

		elif data[index][0] != data[index-1][0] and index != len(data)-1:
			file.write("]\n")
			file.write("}\n")
			file.write("]\n")
			file.write("},")
	# School
			file.write("{\n")
			file.write("\"name\": "+"\""+data[index][0]+"\""+",\n")
			file.write("\"children\": [\n")
	# Style
			file.write("{\n")
			file.write("\"name\": "+"\""+data[index][1]+"\""+",\n")
			file.write("\"children\": [\n")

		elif data[index][1] != data[index-1][1]:
			file.write("]\n")
			file.write("},\n")
			file.write("{\n")
			file.write("\"name\": "+"\""+data[index][1]+"\""+",\n")
			file.write("\"children\": [\n")
###########################################################

	# Restaurant


		if index != 0 and data[index][1] == data[index-1][1] and data[index][0] == data[index-1][0] :
			file.write(",\n")
		file.write("{")
		file.write("\"name\": "+"\""+data[index][5]+"\""+",")
		file.write("\"review_count\": "+"\""+data[index][4]+"\""+",")
		file.write("\"photo_url\": "+"\""+data[index][3]+"\""+",")
		file.write("\"star\": "+"\""+data[index][7]+"\"")
		file.write("}")
		index += 1


		if index == len(data):
			file.write("]\n")
			file.write("}\n")
			file.write("]\n")
			file.write("}]\n")
			file.write("}")


