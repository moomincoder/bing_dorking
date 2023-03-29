import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_dorks", help="The file that is a list of dorks that you want to use")
parser.add_argument("input_file", help="The file of targets")
args = parser.parse_args()

file2 = open(args.input_file, 'r')
count2 = 0

output_file = open("output.txt", "a")
saved_searches = open("saved.txt", "a")

print("        _            _            _           _       ")
print("      /\ \         /\ \         /\ \        /\_\      ")
print("     /  \ \____   /  \ \       /  \ \      / / /  _   ")
print("    / /\ \_____\ / /\ \ \     / /\ \ \    / / /  /\_\ ")
print("   / / /\/___  // / /\ \ \   / / /\ \_\  / / /__/ / / ")
print("  / / /   / / // / /  \ \_\ / / /_/ / / / /\_____/ /  ") 
print(" / / /   / / // / /   / / // / /__\/ / / /\_______/   ")
print("/ / /   / / // / /   / / // / /_____/ / / /\ \ \      ")
print("\ \ \__/ / // / /___/ / // / /\ \ \  / / /  \ \ \     ")
print(" \ \___\/ // / /____\/ // / /  \ \ \/ / /    \ \ \    ")
print("  \/_____/ \/_________/ \/_/    \_\/\/_/      \_\_\   ")

while True:
    count2 += 1

    file1 = open(args.input_dorks, 'r')
    # Get next line from file
    line2 = file2.readline()
 
    # if line is empty
    # end of file is reached
    if not line2:
        break
    target = line2.strip()

    count = 0
    list_of_dorks_list = []
    while True:
        count += 1
    
        # Get next line from file
        line = file1.readline()
    
        # if line is empty
        # end of file is reached
        if not line:
            break
        list_of_dorks_list.append(line.strip())
        dork = line.strip()
        new_string = dork.replace("target", target)
        # print(new_string)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }

        params = {
            'q': new_string,
        }

        response = requests.get('https://www.bing.com/search', params=params, headers=headers)
        # print(response)
        # print(response.content)
        print(new_string)
        string_to_write = str(response.content) + '\n'
        output_file.write(string_to_write)
        found = ("There are no results for site" in string_to_write)
        if found == True:
            saved_searches.write(new_string + '\n')

# The objective of this program is to be able to pass in a url, and have this program use a variety of dorks for different search engines to try and find any possible information leaks

# once the lines are read in the the word "Target" needs to be replaced with whatever the targets name is, for instance "target" ==> "redox.com"

# This works
# curl --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" https://www.bing.com/search?q=test%20test


# This works fine
# curl https://www.bing.com/search?q=test%20test